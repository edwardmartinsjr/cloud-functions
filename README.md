# Cloud Functions

[![CircleCI](https://circleci.com/gh/edwardmartinsjr/cloud-functions/tree/master.svg?style=shield)](https://circleci.com/gh/edwardmartinsjr/cloud-functions/tree/master)

1. This program is a single .py file.

2. This program is written in python 3.7, using only python’s built-in libraries.

3. This program contains a main() method that:
	
    a. Get the top stories from the hacker news API;
	
    b. Iterate over the every story;

    c. If any of their titles match "Data Engineer":
	
    - Send an e-mail with the links

4. Test:
```
python test_main.py -v
```

5. Run:
```
python main.py
```

6. Deploy:
```
gcloud functions deploy cloud-functions \
--runtime python37 \
--trigger-http
```

7. Scheduler:
```
gcloud scheduler jobs create http email_job cloud-functions \
--scheduler="0 0 * * *" \
--uri=https://us-central1-project.my-bigquery-project-270416/cloud-functions

```

8. Scheduler job lists:
```
gcloud scheduler jobs list

```

