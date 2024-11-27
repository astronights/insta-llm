from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

import time
import pyperclip
import pandas as pd

chrome_options = Options()

chrome_options.add_argument("--start-maximized")

webdriver_service = Service(
    '')

user_data_dir = r''
chrome_options.add_argument(f'user-data-dir={user_data_dir}')
chrome_options.add_argument('profile-directory=Default')

driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)

def navigate_to_post(post_url):
    driver.get(post_url)
    time.sleep(3)

def edit_caption(new_caption):
    buttons = driver.find_elements(By.XPATH, "//div[@role='button' and @tabindex='0']")
    menu_button = [butt for butt in buttons if 'more options' in butt.get_attribute('outerHTML').lower()][0]
    menu_button.click()
    time.sleep(2)

    buttons = driver.find_elements(By.XPATH, "//button")
    edit_button = [butt for butt in buttons if 'Edit' in butt.get_attribute('outerHTML')][0]
    edit_button.click()
    time.sleep(2)

    caption_area = driver.find_element(By.XPATH, "//div[@aria-label='Write a caption...']")
    caption_area.clear()

    pyperclip.copy(new_caption)

    caption_area.send_keys(Keys.CONTROL, 'v')
    time.sleep(2)

    buttons = driver.find_elements(By.XPATH, "//div[@role='button' and @tabindex='0']")
    done_button = [butt for butt in buttons if 'Done' in butt.get_attribute('outerHTML')][0]
    done_button.click()
    time.sleep(3)

df = pd.read_csv('updates.csv', dtype={'id': object})
old_ids = pd.read_csv('completed.csv', dtype={'id': object})
print(f'Total: {len(df)}, Completed: {len(old_ids)}')

df = df[~df.id.isin(old_ids['id'])]
print(f'Remaining Updates: {len(df)}')

c = 0
start = time.time()

for ix, row in df.iterrows():
    POST = row['permalink']
    CAPTION = row['caption']

    navigate_to_post(POST)
    edit_caption(CAPTION)

    row_df = df[df.id == row.id][['id', 'permalink']]
    row_df.to_csv('./completed.csv', mode='a', index=False, header=False)

    time.sleep(10)

    c += 1
    if c % 5 == 0:
        print(f'Processed: {c} {(time.time()-start):.2f}')
        start = time.time()

    if c == 20:
        break