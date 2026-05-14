import argparse

import pages.empresa as empresa
import pages.categoria as categoria
import pages.segmentos as segmentos

import browser


def main():
    parser = argparse.ArgumentParser(description="Crawler CLI") 

    parser.add_argument("segmentos", required=True,
                        help="Scrape /segmentos for subcategory links")
    parser.add_argument("categories", required=True,
                        help="Scrape all categories for company links")

    args = parser.parse_args()

    try:
        if args.segmentos:
            segmentos.scrape_segments()
        elif args.categories:
            categoria.scrape_categories()
            
        
    finally:
        input("\nPress ENTER to close...")

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