from bs4 import BeautifulSoup
import requests

url = "https://www.hellowork.com/emploi/recherche.html"
params = {'k' : 'python', 'l':'montpellier'}
user_agent = {'user-agent' : 'Mozilla/5.0 (Linux; Android 11; Pixel 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.91 Mobile Safari/537.36'}

s = requests.Session()

def find_links(url, params):
    host = "https://www.hellowork.com"
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


def scrap(url, params):
    links = find_links(url, params)
    if links:
        for link in links:
            res = s.get(link, headers=user_agent)
            if res.ok:
                print(f"url : {res.url}")
                print(f"status : {res.status_code}")
                soup = BeautifulSoup(res.text, "html.parser")
                title = soup.find('title')
                print(f"Titre : {title}")
            break

scrap(url, params)