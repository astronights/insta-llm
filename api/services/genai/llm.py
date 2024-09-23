from .prompts import bio

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