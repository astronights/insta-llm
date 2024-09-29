import os
import time

import json
from ast import literal_eval

import pandas as pd

import requests
import google.generativeai as genai

API_KEY = ''

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash') 

prompt = '''  
You are a social media marketing expert working for a Boutique specializing in Indian ethnic wear.\
You are an expert in generating marketing material such as Instagram captions for products that are sold on Instagram.\

Please generate an interesting instagram caption for this image. The caption can have upto 1000 characters, so try to
The caption should contain multiple paragraphs. The first paragraph should be a captivating one liner about the product. The next paragraphs should contain more details like descriptions.
If you have to use the word kurta, please use kurti instead, as this is for women's fashion.

The caption should be programmed to boost engagement and discovery of this account with the Instagram algorithm.
The output should be returned as a parseable JSON with a key for options. The options key should contain a list of 5 captions without any hashtags.
Please have a variety of captions, with some options without emojis and some using emojis suitable for social media.
Another key should be the list of hashtags (each with the # symbol). Do not generic Instagram hashtags.
'''

def upload_and_check_media(media_paths):
    gen_files = []
    
    for file_path in media_paths:
        gen_file = genai.upload_file(path=file_path)
        
        while gen_file.state.name == "PROCESSING":
            print(f"Processing {file_path}, waiting for completion...", end='')
            time.sleep(2)
            gen_file = genai.get_file(gen_file.name)
        
        if gen_file.state.name == "FAILED":
            raise ValueError(f"File processing failed for {file_path}")
        
        gen_files.append(gen_file)
    
    return gen_files

def download_media(url, filename):
    response = requests.get(url)
    with open(filename, 'wb') as f:
        f.write(response.content)
    return filename

data = None

with open('./posts.json', 'r') as f:
    data = json.load(f)

print(f'Posts: {len(data)}')

old_ids = pd.read_csv('./llm_results.csv', dtype={'id': object})['id'].values.tolist()
print(f'Already done: {len(old_ids)}')

c = 0
start = time.time()
out = []

# print(old_ids)
remainders = [x for x in data if str(x['id']) not in old_ids]
print(f'Remaining: {len(remainders)}')

for item in remainders:
    row = {'id': str(item['id']), 'caption': item.get('caption'), 'type': item['media_type'],
           'timestamp': item['timestamp'], 'permalink': item['permalink']}
    
    if row['id'] in old_ids:
        continue
    
    medias = []
    if row['type']=='IMAGE':
        image_url = item['media_url']
        temp_image = download_media(image_url, f"temp_{row['id']}.jpg")
        medias.append(temp_image)

    elif row['type']=='VIDEO':
        video_url = item['media_url']
        temp_video = download_media(video_url, f"temp_{row['id']}.mp4")
        medias.append(temp_video)

    elif row['type'] == 'CAROUSEL_ALBUM':
        for media in item['children']['data']:
            media_url = media['media_url']
            if media['media_type'] == 'IMAGE':
                temp_image = download_media(media_url, f"temp_{media['id']}_carousel.jpg")
                medias.append(temp_image)
            elif media['media_type'] == 'VIDEO':
                temp_video = download_media(media_url, f"temp_{media['id']}_carousel.mp4")
                medias.append(temp_video)

    gen_files = upload_and_check_media(medias)
    response = model.generate_content([prompt] + gen_files).text

    res_dict = literal_eval(response.lstrip('```json').rstrip('```'))

    for i in range(1, 6):
        row[f'llm_caption_{i}'] = res_dict['options'][i-1]
    row['hashtags'] = res_dict['hashtags']
    out.append(row)

    for f in medias:
        os.remove(f)

    c += 1
    if c == len(remainders) or c % 5 == 0:
        print(f'Time: {(time.time() - start):.2f}s: {c}')

        df = pd.DataFrame(out)
        df.to_csv('./llm_results.csv', mode='a', index=False, header=False)
        out = []
        start = time.time()

with open('./captions.json', 'w') as f:
    json.dump(out, f)