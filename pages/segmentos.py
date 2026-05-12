from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

import time

def click_accordion(driver, column, row):
    selector = (
    "body > main > section > "
    "section.rs-py-0.rs-px-5.rs-flex.rs-gap-y-6."
    "lg\\:rs-gap-x-5.xl\\:rs-gap-x-10."
    "rs-w-full.rs-max-w-\\[1170px\\] > "
    f"div:nth-child({column}) > "
    f"div:nth-child({row}) > "
    "button > svg"
    )

    try:
        element = driver.find_element(By.CSS_SELECTOR, selector)
        element.click()
        return True
    except:
        print('!!! Accordion not found !!!')
        return False
    
def get_category_name(driver, column, row):
    selector = (
    "body > main > section > "
    "section.rs-py-0.rs-px-5.rs-flex.rs-gap-y-6.lg\:rs-gap-x-5.xl\:rs-gap-x-10.rs-w-full.rs-max-w-\[1170px\] > "
    f"div:nth-child({column}) > div:nth-child({row}) > "
    "button > div > div.rs-flex.rs-flex-col.rs-items-start.rs-text-raGray15 > div > span"
    )

    try:
        element = driver.find_element(By.CSS_SELECTOR, selector)
        return element.text
    except:
        print('!!! Category name not found !!!')
        return None



def scrape_segments(driver, wait):
    driver.get("https://www.reclameaqui.com.br/segmentos/")
    time.sleep(5)

    column = 1
    row = 1
    while True:
        # Get category name
        print(f"\n Column: {column} - Row: {row}")
        print(get_category_name(driver, column, row))


        # Open accordion
        result = click_accordion(driver, column, row)

        if not result:
            column += 1
            row = 1
            continue

        row +=1

        time.sleep(2)

    

    
