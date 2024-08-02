import requests
from bs4 import BeautifulSoup

url = "https://feeds.npr.org/510318/podcast.xml"

resp = requests.get(url)

soup = BeautifulSoup(resp.content, features="xml")

# print(soup.prettify())

items = soup.find_all('item')

news_items = [] #array

for item in items:
    # print(item)
    news_item = {} #dictionary
    news_item['title'] = item.title.text
    desc_text = item.description.text
    index_of_service_text = desc_text.find("<em")
    desc_text_minus_service_text = ""
    if index_of_service_text == 0:
        desc_text_minus_service_text = desc_text[desc_text.find("<br/><br/>")+10:]
    else:
        desc_text_minus_service_text = desc_text[:desc_text.find("<br/><br/><em>"):]

    desc_text_stripped_of_sponsor_message_choices = desc_text_minus_service_text[:desc_text_minus_service_text.find("Learn more about")]
    news_item['description'] = desc_text_stripped_of_sponsor_message_choices
    news_item['podcasturl'] = item.enclosure.get('url')
    news_items.append(news_item)    

def newsItems():
    return news_items[0:5]
