#Created on March 9, 2020
#Seth Daetwiler
#--------------#

#import request module for scraping
import requests
#import twilio
from twilio.rest import Client
#import html from lxml for html parsing
from lxml import html

page = requests.get("http://www.whatcomcounty.us/3329/Novel-Coronavirus-COVID-19")

htmlTree = html.fromstring(page.content)
pending = int(htmlTree.xpath('.//li[text()[contains(.,"PUI")]]/strong/text()')[0])
confirmed = int(htmlTree.xpath('.//li[text()[contains(.,"Confirmed")]]/strong/text()')[0])
negative = int(htmlTree.xpath('.//li[text()[contains(.,"Negative")]]/strong/text()')[0])


print(pending, confirmed, negative)
#establish connection to Twilio
client = Client("ACcab4f9d48297c67f7ca504496a4f4cc2","b786b0cebb8516a90574dc9e7cb9dd4a")
#compose message and format body
client.messages.create(to="+12533706279", from_="+12565308360", body="---------- \nPending: " + str(pending) + "\nConfirmed: " + str(confirmed) + "\nNegative: " + str(negative))

exit()