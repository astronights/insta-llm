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

    file_data = request.files['media']
    keywords = request.form.get('keywords', '')

    filename = secure_filename(file_data.filename)
    file_path = os.path.join('api/services/data', filename)
    file_data.save(file_path)

    gen_file = genai.upload_file(path=file_path)
    llm_prompt = upload.format(keywords=keywords)

    response = model.generate_content([llm_prompt] + [gen_file]).text
    os.remove(file_path)

    texts = literal_eval(response.lstrip('```json').strip('```'))

    options = [t['headline'] + '\n\n' + t['description'] for t in texts['options']]
    hashtags = ' '.join(texts['hashtags'])

    return {'captions': options, 'hashtags': hashtags}