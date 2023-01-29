from bs4 import BeautifulSoup
import requests

url = "https://www.hellowork.com/emploi/recherche.html"
user_agent = {'user-agent' : 'Mozilla/5.0 (Linux; Android 11; Pixel 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.91 Mobile Safari/537.36'}

s = requests.Session()

def find_links(lang, location):
    host = "https://www.hellowork.com"
    params = {'k' : lang, 'l':location}
    links = []

    res = s.get(url, headers=user_agent, params=params)
    if res.ok:
        soup = BeautifulSoup(res.text, "html.parser")
        content = soup.find('ul', class_="crushed")
        element_li = content.find_all('li', class_="!tw-mb-6")
        for element in element_li:
            div = element.find('div', class_='crushed')
            div2_1 = div.find('div', class_="offer--maininfo")
            info = div2_1.find("h3", class_="!tw-mb-0")
            # h3 = info.text
            a = info.find('a')['href']
            links.append(host+a)
    return links


def scrap(lang:str, location:str)->list:
    """return une liste de dictionnaire"""
    links = find_links(lang, location)
    data = []
    if links:
        for link in links:
            data_dict = {}
            res = s.get(link, headers=user_agent)
            if res.ok:
                soup = BeautifulSoup(res.text, "html.parser")
                section = soup.find('section', class_="campagne")
                h1 = section.find('h1', class_="tw-flex-col")
                span = h1.find('span', class_="!tw-text-4xlOld")

                data_dict["title"] = span.text

                li = section.find_all('li')
                city = li[0].find('span')
                contr = li[1].find('span')

                data_dict['city'] = city.text.strip()
                data_dict['contrat'] = contr.text.strip()

                main = soup.find('main')
                section1 = main.find('section')
                h2 = section1.find('h2')
                p = section1.find('p')
                date = section1.find('span', class_="retrait").find('span')

                data_dict["minititre"] = h2.text.strip()
                data_dict['detail'] = p.text.strip()
                data_dict['date'] = date.text

                data.append(data_dict)

    return data
