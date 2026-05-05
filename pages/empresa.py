from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def get_complaints_listing_max_page(driver, wait):
    # Get max pagination number for clompaints in company page
    element = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".sc-fAGzit"))
    )
    # Get element text and return max page number
    text_value = element.text

    return int(text_value.split()[-1])


def get_complaints_hyperlinks_in_page(driver, wait):
    # espera os links aparecerem
    links_elements = wait.until(
        EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, ".sc-1oekl5r-0 .sc-1oekl5r-2")
        )
    )

    # extrair os hrefs
    links = [el.get_attribute("href") for el in links_elements]

    print(links)

def iterate_company_complaints_listing(driver, wait, company_name, max_page):
    # Iterate over all pages for getting complaints hyperlinks
    complaints_urls = []

    for i in range(1, max_page + 1):
        # Get next page URL
        driver.get(f'https://www.reclameaqui.com.br/empresa/{company_name}/lista-reclamacoes/?pagina={i}')
        # Extend obtained complaints URLs
        complaints_urls.extend(get_complaints_listing_max_page(driver, wait))

    return complaints_urls


