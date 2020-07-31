# fool.com
# zacks.com
# marketwatch.com
# seekingalpha.com
# cnbc.com
# thestreet.com
# barrons.com
# finance.yahoo.com
# investing.com
# nasdaq.com

# A simple scraper that scrapes article links with a desired keyword
# Only scrapes Investopedia for now

from urllib.request import urlopen
from bs4 import BeautifulSoup as soup

# Investopedia

def get_Investopedia(keyword):
    keyword = keyword.lower()
    urlTrading = "https://www.investopedia.com/markets-news-4427704"
    urlMarket = "https://www.investopedia.com/trading-news-4689736"
    urlCompany = "https://www.investopedia.com/company-news-4427705"

    company_page = urlopen(urlCompany)
    market_page = urlopen(urlMarket)
    trading_page = urlopen(urlTrading)

    page_html = company_page.read() + market_page.read() + trading_page.read()
    page_soup = soup(page_html, 'html.parser')
    page_articles = page_soup.findAll('a', {'class': 'comp card mntl-card card'}, )
    company_page.close()
    market_page.close()
    company_page.close()
    links = []
    result = []
    for item in page_articles:
        links.append(item.get('href'))
    for index, link in enumerate(links):
        if keyword in links[index]:
            result.append(link)
    return result
    

def main():
    search_loop = True
    while search_loop:
        keyword_input = input('Enter string keyword to search for on the website:')
        result = get_Investopedia(keyword_input)
        for item in result:
            print(item)
        search_input = input('Enter y/n to continue searching. . .')
        search_input.lower()
        if search_input == 'n':
            search_loop = False
            break
        elif search_input != 'y':
            raise Exception('Input must be y/n')


main()
