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
    page_articles = page_soup.findAll(
        'a', {'class': 'comp card mntl-card card'}, )
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
    result = get_Investopedia('earnings')
    for item in result:
        print(item)


main()
