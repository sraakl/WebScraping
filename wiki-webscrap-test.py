# coding: utf-8
from bs4 import BeautifulSoup
tree = BeautifulSoup(page.content
import requests
page = requests.get('https://de.wikipedia.org/wiki/Richard_Hall_(Boxer)')
tree = BeautifulSoup(page.content, 'html.parser')
tree.select("#Vorlage-Infobox-Boxer")
tree.select("#Vorlage-Infobox-Boxer tr")
tree.select("#Vorlage-Infobox-Boxer")[0]
tree.select("#Vorlage-Infobox-Boxer")[0].select("tr")
tree.select("#Vorlage-Infobox-Boxer")[0].select("tr")[-5:-1]
tree.select("#Vorlage-Infobox-Boxer")[0].select("tr")[-5:-1][0]
tree.select("#Vorlage-Infobox-Boxer")[0].select("tr")[-5:-1][0].select
tree.select("#Vorlage-Infobox-Boxer")[0].select("tr")[-5:-1][0].select("th")[0]
tree.select("#Vorlage-Infobox-Boxer")[0].select("tr")[-5:-1][0].select("th")[0].text
tree.select("#Vorlage-Infobox-Boxer")[0].select("tr")[-5:-1][0].select("td")[0].text[:-1]
