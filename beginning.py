from lxml import html
import requests
#electron web framework

page = requests.get('http://econpy.pythonanywhere.com/ex/001.html')
tree = html.fromstring(page.content)

#This will create a list of buyers:
buyers = tree.xpath('//div[@title="buyer-name"]/text()')
#This will create a list of prices
prices = tree.xpath('//span[@class="item-price"]/text()')

buyers_dict = dict(zip(buyers,prices))

for name, value in buyers_dict.items():

    print(f"Buyer {name} has Price: {value}")
