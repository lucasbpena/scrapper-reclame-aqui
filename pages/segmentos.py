from selenium import webdriver
from selenium.webdriver.common.by import By
from utils import save_dicts_to_csv
import time

from browser import setup_driver

URL = "https://www.reclameaqui.com.br/segmentos/"

def click_accordion(driver, column, row):
    # Clicks category accordion (open/close)
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

    except Exception as e:
        print(f"!!! Accordion not found !!! {e}")

        return False


def get_category_name(driver, column, row):
    # Get category name based on column and row
    selector = (
        "body > main > section > "
        "section.rs-py-0.rs-px-5.rs-flex.rs-gap-y-6."
        "lg\\:rs-gap-x-5.xl\\:rs-gap-x-10."
        "rs-w-full.rs-max-w-\\[1170px\\] > "
        f"div:nth-child({column}) > "
        f"div:nth-child({row}) > "
        "button > div > div.rs-flex.rs-flex-col."
        "rs-items-start.rs-text-raGray15 > div > span"
    )

    try:
        element = driver.find_element(By.CSS_SELECTOR, selector)

        return element.text

    except Exception as e:
        print(f'!!! Category name not found !!! {e}')

        return None


def get_subcategories(driver):
    # Get all subcategories and their links in opened accordion
    elements = driver.find_elements(
        By.CSS_SELECTOR,
        '[id$="-acordeon"] > div > a'
    )

    result = []

    for el in elements:
        text = el.text.strip()
        href = el.get_attribute("href")

        result.append({
            "subcategory": text,
            "href": href
        })

    return result


def scrape_segments():
    # Scrape all segments
    all_results = []

    # 3 columns
    for column in range(1, 4):

        print(f"\n========== COLUMN {column} ==========")

        # Restart browser every column
        driver = setup_driver()
        driver.get(URL)
        time.sleep(5)

        row = 1

        while True:

            print(f"\nColumn: {column} - Row: {row}")

            category_name = get_category_name(driver, column, row)

            if not category_name:
                print("No more rows in this column.")
                break

            print(category_name)

            # Open accordion
            opened = click_accordion(driver, column, row)

            if not opened:
                break

            time.sleep(2)

            # Get links
            subcategories = get_subcategories(driver)

            for item in subcategories:
                item["category"] = category_name

            all_results.extend(subcategories)

            # Close accordion
            click_accordion(driver, column, row)

            time.sleep(1)

            row += 1

        driver.quit()

    save_dicts_to_csv(all_results, "segments.csv")
    print(f"\nSaved {len(all_results)} subcategories to data/segments.csv")