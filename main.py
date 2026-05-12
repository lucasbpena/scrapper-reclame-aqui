import argparse

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pages.empresa as empresa
import pages.categoria as categoria

import browser
import pages.segmentos as segmentos

def run_company_listing(driver, wait, category):
    max_page = empresa.get_complaints_listing_number_of_pages(driver, wait)
    results = empresa.iterate_pages(driver, wait, company, max_page)
    print(results)


def run_complaint_listing(driver, wait, company):
    driver.get(url)
    links = driver.find_elements(By.CSS_SELECTOR, "a[href*='/reclamacao/']")
    for l in links:
        print(l.get_attribute("href"))


def main():
    parser = argparse.ArgumentParser(description="Crawler CLI") 

    parser.add_argument("--mode", choices=["segmentos",], required=True,
                        help="Routine to run")

    parser.add_argument("--url", help="URL to crawl")
    parser.add_argument("--company", help="Company name")

    args = parser.parse_args()

    driver = browser.setup_driver()
    wait = WebDriverWait(driver, 30)

    try:
        if args.mode == "segmentos":
            segmentos.scrape_segments(driver, wait)
            
            



    finally:
        input("\nPress ENTER to close...")
        driver.quit()


if __name__ == "__main__":
    main()


'''            if not args.company:
                raise ValueError("You must provide --company")
            run_listing(driver, wait, args.company)

        elif args.mode == "single":
            if not args.url:
                raise ValueError("You must provide --url")
            run_single_page(driver, wait, args.url)
'''