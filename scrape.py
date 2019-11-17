import os
import requests
from bs4 import BeautifulSoup
import json

# scrape information from the website
def getinformation(url):
    # decide what URL to create
    if 'af' in  url:
        eventUrl = 'https://www.wegottickets.com/event/'+url
    else:
        eventUrl = 'https://www.wegottickets.com/'+url
    # get website data
    source = requests.get(eventUrl)
    webData = BeautifulSoup(source.text,'html.parser')
    event ={}
    information = webData.find('div',class_="left full-width-mobile event-information event-width")
    # if a title is found  add page contents to events dict
    if information.h1.text:
        event['artists_playing'] = information.h1.text.strip()
        if information.find('a',attrs={'title':True}):
            event['venue'] = information.find('a',attrs={'title':True}).text.strip()
        else:
            event['venue'] = information.find('span',class_='secondaryInformation').next_sibling.strip()
        venue_details = information.find_all('td')
        city = venue_details[1].a.text.strip().split(":")
        event['city'] = city[0]
        event['date'] = venue_details[3].text.strip()
        event['time'] = venue_details[5].text.strip()
        event['age'] = venue_details[7].text.strip()
        pricefound = webData.find('div',class_="price").strong.text.strip()
        event['price'] = pricefound[1:]
    return event

# write json
def write_json(event):
    print(os.getcwd())
    f = open(os.path.join(os.getcwd(),"eventsjson.json"), "w")
    f.write(event)
    f.close()
    print("JSON file eventsjson.js written to : "+os.getcwd())

# extract URLS from the website
def extract_urls(website):
    source = requests.get(website)
    webData = BeautifulSoup(source.text,'html.parser')
    list = webData.findAll('a',attrs={'title':True})
    listOfUrls =set()
    events = []
    for link in list:
        newlink = str(link['href'])
        if "event" in newlink:
            listOfUrls.add(newlink)
    # convert list into a set then a List to remove duplicates
    sortedurls =[]
    for se in listOfUrls:
        events.append(getinformation(se))
    return events

# start web scraping
def scrape_web():
    # url for for web site to scrap
    url = "http://www.wegotickets.com/searchresults/all"
    events = extract_urls(url)
    print(events)
    # convert into JSON and save to event.json file:
    write_json(json.dumps(events))
