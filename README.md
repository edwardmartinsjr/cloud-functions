# Cloud Functions

[![CircleCI](https://circleci.com/gh/edwardmartinsjr/cloud-functions/tree/master.svg?style=shield)](https://circleci.com/gh/edwardmartinsjr/cloud-functions/tree/master)

1. This program is a single .py file.

2. This program is written in python 3.7, using only python’s built-in libraries.

3. This program contains a main() method that:
	
    a. Get the top stories from the hacker news API;
	
    b. Iterate over the every story;

    c. If any of their titles match "Data Engineer":
	
    - Send data to BigQuery

4. Install requirements:
```
pip install -r requirements.txt
```

5. Test:
```
python test_main.py -v
```

6. Run:
```
python main.py
```

7. Deploy:
```
gcloud functions deploy scan_hacker_news \
--runtime python37 \
--trigger-http
```

8. Scheduler:
```
gcloud scheduler jobs create http email_job \
--schedule="20 * * * *" \
--uri=https://us-central1-my-bigquery-project-270416.cloudfunctions.net/scan_hacker_news

```

9. Scheduler job lists:
```
gcloud scheduler jobs list

```

