import requests
import logging

# create logger
logger = logging.getLogger("cloud-functions")
logger.setLevel(logging.INFO)


api_url = 'https://hacker-news.firebaseio.com/v0/'
top_stories_url = api_url + 'topstories.json'
item_url = api_url + 'item/{}.json'

def get_data_engineer_stories(top_stories):
    data_engineer_stories = []

    for story_id in top_stories:
        r = requests.get(item_url.format(story_id))
        if r.status_code == 200:
            story = r.json()
            if 'data engineer' in story['title'].lower():
                data_engineer_stories.append(story)
        else:
            logger.error(f"Error code: [{r.status_code}]")


    return data_engineer_stories


if __name__ == "__main__":
    top_stories = requests.get(top_stories_url).json()
    data_engineer_stories = get_data_engineer_stories(top_stories)




