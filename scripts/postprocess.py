import json
from ast import literal_eval

import numpy as np
import pandas as pd

emojis = None
with open('../api/static/emojis.json', 'r', encoding='utf-8') as f:
    emojis = json.load(f)

emojis = list(set([x for y in emojis.values() for x in y]))
print(f'Emojis: {len(emojis)}')

data = None
with open('./posts.json', 'r') as f:
    data = json.load(f)
print(f'Posts: {len(data)}')

df = pd.read_csv('llm_results.csv', dtype={'id': object})
print(f'LLM Responses: {df.shape}')

df = df[~df.id.str.contains('E')]

df['to_edit'] = np.where(df.caption.fillna('').str.contains(' '), 0, 1)
print(f'Edits: {df.to_edit.sum()}')

np.random.seed(42)
df['caption_ix'] = np.random.choice([1,2,3,4,5], size=len(df))
df['updated_caption'] = df.apply(lambda row: row[f'llm_caption_{row["caption_ix"]}'], axis=1)

np.random.seed(42)
df['emoji'] = np.random.choice(emojis+[''], size=len(df))

sizes = ['36', '38', '40', '42', '44', '46']

def random_sizes(row):
    n = np.random.randint(4, len(sizes))
    sampled_sizes = np.random.choice(sizes, n, replace=False)
    return ' | '.join(sorted(sampled_sizes))

df['sizes'] = df.apply(random_sizes, axis=1)

df['contact_text'] = df['emoji'] + ' Feel free to message me for pricing and for more details ' + df['emoji']
df['hashtag_text'] = df['hashtags'].apply(lambda items: ' '.join(literal_eval(items)))

df['final_caption'] = df['updated_caption'] + '\n\n' + 'Sizes available: ' + df['sizes'] + '\n' + df['contact_text'] + '\n\n' + df['hashtag_text']

df.to_csv('all_posts.csv', index=False)
df.loc[df.to_edit == 1, ['id', 'permalink', 'final_caption']].rename(columns={'final_caption': 'caption'}).to_csv('updates.csv', index=False)