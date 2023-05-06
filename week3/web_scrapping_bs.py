from bs4 import BeautifulSoup
import requests

request_page = requests.get('https://www.bnr.ro/files/xml/nbrfxrates2021r.htm')
print(request_page)
link = BeautifulSoup(request_page.text, 'html.parsel')
dataset, header_list = [], []
main = link.find_all('div', attrs = {'id' : 'contentDiv'})
for obj in main:
    if len(obj.find_all('table')) >0:
        data_table = obj.find_all('table')
        for table_index in obj.find_all('table'):
            if len(table_index.find_all('tr'))>0:
                header_list = [table_trs.get_text() for table_trs in table_index.find_all('th')]

                break

        break
print(header_list)