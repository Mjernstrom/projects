import os
from urllib.request import urlopen, re
from bs4 import BeautifulSoup as soup 
import csv

def get_emails():
    url = 'http://mandevillehigh.stpsb.org/faculty.html'
    # Open, read, and parse the page
    url_page = urlopen(url)
    url_page_html = url_page.read()
    url_page_soup = soup(url_page_html, 'html.parser')
    url_page_emails = url_page_soup.findAll('td')
    # Open csv file in parent directory and append the emails to the list
    destination = os.path.join(os.getcwd(),'EmailList.csv')
    content_list = []
    for index, item in enumerate(url_page_emails):
        if index >= 107 and index <= 155:  
            item = str(item.get_text())
            if '.' in item: 
                item +='@stpsb.org'
                content_list.append(item)
        if index > 155:
            break;
    url_page.close()
    final_list = []
    # Convert list to list of lists
    for item in content_list:
        sub = item.split()
        final_list.append(sub)
    # Append to the first open cell in the csv file
    with open(destination, 'a') as file:
        writer = csv.writer(file,  lineterminator = '\n')
        for item in final_list:
            writer.writerow(item)


get_emails()
