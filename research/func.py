import requests
from bs4 import BeautifulSoup
import logging

log = logging.getLogger('log')

host = 'https://www.free-work.com'
url = "https://www.free-work.com/fr/tech-it/jobs"

headers = {'user-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:105.0) Gecko/20100101 Firefox/105.0'}

def freework(q):
    session = requests.Session()
    params = {'query' : q}
    res = session.get(url, params=params)
    return res


def response(q):
    res = freework(q)
    if res.ok:
        log.debug("\nUrl....... : " + res.url)
        log.debug("Status_code : " + str(res.status_code))
        log.debug('--'*20)

        soup = BeautifulSoup(res.text, 'html.parser')
        title = soup.find('title')

        # la box principal 
        content = soup.find_all('div', class_="cursor-pointer")
        return content

    return None



def data(q):

    element = []
    content = response(q)

    if content != None:

        for box in content:
            data_json = {}
        
            h = box.find('div', class_="h-full")
            h_a = h.find('a')
            details = h.find('div', class_="gap-2")
            boite_name = details.find('div', class_="w-full")
            publish_date = details.find('div', class_="text-sm").find('time')
            span = h.find_all('span')

            link = h_a['href']
            desc = h.find('div', class_="line-clamp-3")
            contract_with_title = h_a.text.strip().replace('\n' , ',').split(',')
            data_json['contrat'] = contract_with_title[0]
            data_json['entreprise'] = boite_name.text.strip()

            if len(span) == 1:
                data_json['lieu'] = span[0].text
            if len(span) == 2:
                data_json['lieu'] = span[1].text
            if len(span) == 3:
                data_json['lieu'] = span[2].text
                data_json['dure'] = span[0].text
            data_json['publish'] = publish_date.text
            

            try:
                exist = span[2]
                data_json['salaire'] = span[1].text
            except:
                pass
            data_json['intitule'] = contract_with_title[2].strip()
            data_json['desc'] = desc.text
            data_json['link'] = host+link
            element.append(data_json)
        return element