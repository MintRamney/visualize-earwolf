from urllib.request import urlopen
from bs4 import BeautifulSoup
from Earwolf import Guest
from collections import defaultdict
import csv

def parse_directory_page(url):
# Reads a single directory page for personal page URLs
    soup = BeautifulSoup(url.read(), "lxml")

    person_list_raw = soup.find_all('div', class_="single-human")
    person_list=[]

    for person in person_list_raw:
        person_list.append(Guest(person.span.getText(), person.a['href']))

    print(soup.a['href'])
    #print(person_list)
    return person_list


def find_hosted_shows(guest):
# Finds which shows a given person has hosted
    url = guest.url
    html = urlopen(url)
    soup = BeautifulSoup(html.read(), "lxml")
    try:
        hosted_shows_raw = soup.find('div', class_="hostedshows").find_all('h1', class_="showtitle")
    except:
        return []

    for show in hosted_shows_raw:
        guest.hosted_shows.append(get_showTitle(show.getText()))

    return guest.hosted_shows

def find_guested_shows(guest):
# Finds which shows a given person has been a guest on
    url = guest.url
    html = urlopen(url)
    soup = BeautifulSoup(html.read(), "lxml")

    try:
        guested_shows_raw = soup.find('div', class_="guestedshows").find_all('div', class_="ep-description")
    except:
        return {}

    for show in guested_shows_raw:
        text = get_showTitle(show.find('a').getText())
        if text not in guest.guested_shows:
            guest.guested_shows[text] = 1
        else:
            guest.guested_shows[text] += 1

    return guest.guested_shows

def get_showTitle(episode):
    for i, c in enumerate(episode):
        if (episode[i] == '#'):
            return episode[0:i-1]

    return episode
