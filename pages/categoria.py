from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By 
from selenium.webdriver.support import expected_conditions as EC
from browser import setup_driver
from utils import read_dicts_from_csv, save_dicts_to_csv

import time

def check_if_company_listing_last_page_achieved(driver, wait):
    # Checks if max page in company listing is achieved
    # If last page, return False
    element = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#pagination-segment"))
    )
    # Get element text
    pagination_text = element.text
    current_page = pagination_text.split()[0]
    last_page = pagination_text.split()[-1]

    if current_page == last_page:
        return False
    else:
        return True
    

def get_company_hyperlinks_in_page(driver, wait):
    # Gets all companys urls in category page
    links_elements = wait.until(
        EC.presence_of_all_elements_located(
          (By.CSS_SELECTOR, "[id^='segmentos_botao_ver_empresa_'] .rs-line-clamp-3")
        )
    )
    # extract hrefs from obtained elements
    companies = {el.get_attribute("text") for el in links_elements}
    links = [el.get_attribute("href") for el in links_elements]
    
    return dict(zip(companies, links))


def iterate_category_company_listing(driver, wait, category_url):
    # Gets all company urls in category page
    # Company listing starts at "Melhores" tab at (child=2) 
    # css=.rs-bg-transparent:nth-child(2)
    companies_urls = 
    # Go to category url
    driver.get(category_url)
    # Iterate over tab childs
    for tab in [2, 1, 3]:

        if tab != 2:
            # Click on next child
            tab_element = wait.until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, ".rs-bg-transparent:nth-child(" + str(tab) + ")")
                )
            )
        # Set not final page as True
        not_final_page = True
        # Iterate over pages (dynamic display)
        while not_final_page:
            companies_urls.update(get_company_hyperlinks_in_page(driver, wait))

            # Check if final_page is achieved, if not, click in next page button
            not_final_page = check_if_company_listing_last_page_achieved(driver, wait)
            if not_final_page:
                # Locate and click on next page button
                next_button = wait.until(
                    EC.element_to_be_clickable((By.ID, "pagination-segment-next-1"))
                )
                next_button.click()

    return companies_urls


def scrape_categories():
    # Scrape all saved categories for their company listings
    lines_dicts = read_dicts_from_csv('segmentos.csv')
    results = []

    for x in lines_dicts:
        driver = setup_driver()
        wait = WebDriverWait(driver, 30)
        time.sleep(5)

        driver.get(x['href'])
        companies_urls = iterate_category_company_listing(driver, wait, x['href'])


