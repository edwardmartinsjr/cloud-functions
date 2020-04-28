import requests
import logging
from mailjet_rest import Client
import os

# create logger
logger = logging.getLogger("cloud-functions")
logger.setLevel(logging.INFO)

api_key = os.environ['MAILJET_API_KEY']
api_secret = os.environ['MAILJET_API_SECRET']

mailjet = Client(auth=(api_key, api_secret), version='v3.1')

api_url = 'https://hacker-news.firebaseio.com/v0/'
top_stories_url = api_url + 'topstories.json'
item_url = api_url + 'item/{}.json'

def get_data_engineer_stories(top_stories):
    data_engineer_stories = []

    for story_id in top_stories:
        r = requests.get(item_url.format(story_id))
        if r.status_code == 200:
            story = r.json()
            if 'data' in story['title'].lower():
                data_engineer_stories.append(story)
        else:
            logger.error(f"Error code: [{r.status_code}]")


    return data_engineer_stories

def get_top_stories(top_stories_url):
    top_stories = []

    try:
        r = requests.get(top_stories_url)
        
        if r.status_code == 200:
            top_stories = r.json()
        else:
            logger.error(f"Error code: [{r.status_code}]")
        
        return top_stories
    except BaseException as err:
        logger.error(f"Error [{err}]")
        raise SystemExit()

def scan_hacker_news(request):    
    top_stories = get_top_stories(top_stories_url)
    data_engineer_stories = get_data_engineer_stories(top_stories)

    data = {
        'Messages': [
            {
                "From": {
                    "Email": "edwardmartinsjr@gmail.com",
                    "Name": "Edward Martins"
                    },
                    "To": [
                        {
                            "Email": "edwardmartinsjr@gmail.com",
                            "Name": "Edward Martins"
                            }
                            ],
                            "Subject": "Hacker News - Data Engineer Stories",
                            "TextPart": "Hacker News - Data Engineer Stories",
                            "HTMLPart": "<h3>Dear Edward!</h3><br />This is the top Data Engineer Stories: <br /> {}".format(data_engineer_stories),
                            "CustomID": "AppGettingStartedTest"
                            }
                            ]
                            }

    try:
        if data_engineer_stories:        
            r = mailjet.send.create(data=data)
            if r.status_code == 200:
                logger.info("E-mail sent.")
            else:
                logger.error(f"Error code: [{r.status_code}]")
    except BaseException as err:
        logger.error(f"Error [{err}]")
        raise SystemExit()

if __name__ == "__main__":
    scan_hacker_news("")




