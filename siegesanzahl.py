# coding: utf-8
from bs4 import BeautifulSoup
import requests
requests.get('https://de.wikipedia.org/wiki/Richard_Hall_(Boxer)')
tree = requests.get('https://de.wikipedia.org/wiki/Richard_Hall_(Boxer)')
tree = requests.get('https://de.wikipedia.org/wiki/Richard_Hall_(Boxer)')
help(tree)
tree = requests.get('https://de.wikipedia.org/wiki/Richard_Hall_(Boxer)').content
ass = BeautifulSoup(tree, 'html.parser')
ass.select("#Vorlage-Infobox-Boxer")[0].select("tr")[-5:-1][0].select("td")[0].text[:-1]
ass.select("#Vorlage-Infobox-Boxer")[0].select("tr")[-5:-1][0].select("td")[0].text[:-1]
ass.select("#Vorlage-Infobox-Boxer")[0].select("tr")[-5:-1]
ass.select("#Vorlage-Infobox-Boxer")[0]
ass.select("#Vorlage-Infobox-Boxer")[0].select("tr")
ass.select("#Vorlage-Infobox-Boxer")[0].select("tr")[11:15]
ass.select("#Vorlage-Infobox-Boxer")[0].select("tr")[11:14]
ass.select("#Vorlage-Infobox-Boxer")[0].select("tr")[11:14]
ass.select("#Vorlage-Infobox-Boxer")[0].select("tr")[11:14]
ass2 = ass.select("#Vorlage-Infobox-Boxer")[0].select("tr")[11:14]
ass2
ass2[0]
ass2[0].select("th")
ass2[0].select("th")
ass3 = ass2[0].select("th")
ass3[0]
ass3[0].text
ass3[0].text[0:-1]
ass3[0].text[-1]
ass3[0].text[:-1]
siege = ass3[0].text[:-1]
siege
ass.select("#Vorlage-Infobox-Boxer")[0].select("tr")[11:14]
ass2
ass2[0]
ass2[0].select("th")
ass2[0].select("td")
anzahl_siege = ass2[0].find("td")
anzahl_siege = ass2[0].find("td").text[:-1]
anzahl_siege
siege
anzahl_siege = int(ass2[0].find("td").text[:-1])
anzahl_siege
print(siege + ":" + str (anzahl_siege))
#get_ipython().run_line_magic('save', 'current_session ~0/')
