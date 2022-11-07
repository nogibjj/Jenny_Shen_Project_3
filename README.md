# IDS 706 Project 3
![AHR_LinkedInLogo350x350](https://user-images.githubusercontent.com/112578566/200218397-33ad188c-ae14-49d2-8156-3be13c720a00.png)

## Background, dataset and setups
Project 3 demonstrates how to use google bigquery with python by connecting bigquery to python and writing some simple queries to request for data results.

The dataset selected in this case is from the bigquery public data named "american_health_rankings".
<img width="1071" alt="Screen Shot 2022-11-06 at 10 17 41 PM" src="https://user-images.githubusercontent.com/112578566/200219300-ca677c29-7d75-4a74-a4dc-e9796c716ea0.png">

First, need to create a service account and create a key to authenticate and connect to the google cloud platform and services.
<img width="883" alt="Screen Shot 2022-11-06 at 10 20 40 PM" src="https://user-images.githubusercontent.com/112578566/200219633-1d1594ed-e13d-4dba-8537-967d53c234c7.png">

Then insert the key, project_ID to make connection
<img width="461" alt="Screen Shot 2022-11-06 at 10 22 08 PM" src="https://user-images.githubusercontent.com/112578566/200219798-2338dee7-ccb2-4f78-8ff2-36b103d913eb.png">

## Some interesting questions seeking for answers and respective queries to return the results
1. What's an overivew of the data?
<img width="596" alt="Screen Shot 2022-11-06 at 10 18 30 PM" src="https://user-images.githubusercontent.com/112578566/200219378-21751d77-b7a4-4e20-bed6-243e8650a151.png">

2. What's the top 10 states with the highest health ranking value by valuing people who are able-bodied?
<img width="335" alt="Screen Shot 2022-11-06 at 10 15 46 PM" src="https://user-images.githubusercontent.com/112578566/200219118-c305d243-7323-46a0-803a-1bf2bab6183f.png">

3. Which five states have the lowest health ranking value in 2019?
<img width="382" alt="Screen Shot 2022-11-06 at 10 16 03 PM" src="https://user-images.githubusercontent.com/112578566/200219152-f8b56f16-d03f-4876-abef-5bb0b136ca04.png">

## Install the client libraries

```
pip install --upgrade google-cloud-bigquery
```
