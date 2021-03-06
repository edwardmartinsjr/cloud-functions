import requests
import logging

# Create logger
logger = logging.getLogger("cloud-functions")
logger.setLevel(logging.INFO)

# Set hacker-news urls
api_url = "https://hacker-news.firebaseio.com/v0/"
top_stories_url = api_url + "topstories.json"
item_url = api_url + "item/{}.json"

def get_data_engineer_stories(top_stories):
    data_engineer_stories = []

    for story_id in top_stories:
        r = requests.get(item_url.format(story_id))
        if r.status_code == 200:
            story = r.json()
            # Search for 'data' term on each title
            if "data" in story["title"].lower():
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
        logger.error(f"Exception: [{err}]")
        raise SystemExit()

def store_data(data_engineer_stories, client, table):
    try:
        if data_engineer_stories:
            for row in data_engineer_stories:
                rows_to_insert = [{
                    "id":row["id"],
                    "by":row["by"],
                    "score":row["score"],
                    "time":row["time"],
                    "title":row["title"],
                    "type":row["type"],
                    "url":row["url"]}]
                # Make an API request.
                r = client.insert_rows(table, rows_to_insert)
                if r.status_code == 200:
                    return True
                else:
                    logger.error(f"Error code: [{r.status_code}], {r.error}")
        return False
    except BaseException as err:
        logger.error(f"Exception: [{err}]")
        raise SystemExit()

# GCP Function
def scan_hacker_news(request):
    from google.cloud import bigquery

    # Construct a BigQuery client object.
    client = bigquery.Client()

    # Prepares a reference to the dataset
    dataset_ref = client.dataset("hacker_news")
    table_ref = dataset_ref.table("stories")
    table = client.get_table(table_ref)
 
    top_stories = get_top_stories(top_stories_url)
    data_engineer_stories = get_data_engineer_stories(top_stories)
    store_data(data_engineer_stories, client, table)

if __name__ == "__main__":
    scan_hacker_news("")
    