from .prompts import bio, upload

from werkzeug.utils import secure_filename
from flask import Blueprint, request
import google.generativeai as genai
import os

genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel('gemini-1.5-flash') 

from ast import literal_eval
import os

llm = Blueprint('llm', __name__)

@llm.route('/bio', methods=['POST'])
def generate_bio():
    old_bio = request.form.get('bio')
    
    llm_prompt = bio.format(old_bio=old_bio)    
    options = model.generate_content(llm_prompt).text.lstrip('```json').strip('```')

    texts = [v['bio'] for v in literal_eval(options)]

    return {'bios': texts}

@llm.route('/upload', methods=['POST'])
def generate_upload():

    keywords = request.form.get('keywords', '')
    n_files = int(request.form.get('num_files', '0'))

    paths = []
    gen_files = []
    
    for i in range(n_files):
        file_data = request.files[f'media-{i}']
        filename = secure_filename(file_data.filename)
        file_path = os.path.join(os.environ['TMP_DIR'], filename)

        file_data.save(file_path)
        paths.append(file_path)

        gen_file = genai.upload_file(path=file_path)
        gen_files.append(gen_file)

    description = '\n' if len(keywords) == 0 else f'''\
    Here are a few keywords provided by the designer about this product: {keywords}. \n
    '''
    
    llm_prompt = upload.format(description=description)    

    response = model.generate_content([llm_prompt] + gen_files).text
    
    for fp in paths:
        os.remove(fp)   

    texts = literal_eval(response.lstrip('```json').strip('```'))
    hashtags = ' '.join(texts['hashtags'])

    return {'captions': texts['options'], 'hashtags': hashtags}