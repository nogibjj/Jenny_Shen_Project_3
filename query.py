import pandas as pd
from google.cloud import bigquery
from google.oauth2 import service_account
credentials = service_account.Credentials.from_service_account_file(
'/workspaces/Jenny_Shen_Project_3/delta-lore-367218-f07fe87ff70d.json')

# variables
project_id = 'delta-lore-367218'
bq_dataset = "roller_coaster"

# connections
client = bigquery.Client(credentials= credentials,project=project_id)
dateset_ref = client.dataset('bq_dataset')

# data overview
query = """
    SELECT *
    FROM `delta-lore-367218.demo3.roller_coaster`
    LIMIT 20
"""

query_job = client.query(query)  # Make an API request.
results = query_job.result()
output = results.to_dataframe()
# print(output)

# # find the top 10 states with the highest health ranking value by valuing people who are able-bodied
# query1 = """
#     SELECT state_name, value, lower_ci, upper_ci
#     FROM `bigquery-public-data.america_health_rankings.ahr`
#     WHERE measure_name = 'Able-Bodied'
#     ORDER BY value DESC
#     LIMIT 10
# """
# query_job1 = client.query(query1)  # Make an API request.
# results1 = query_job1.result()
# output1 = results1.to_dataframe()
# # print(output1)


# #find states with the lowest health ranking value in 2019
# query2 = """
#     SELECT measure_name, state_name, value, source_date
#     FROM `bigquery-public-data.america_health_rankings.ahr`
#     WHERE source_date = '2019'
#     ORDER BY value ASC
#     LIMIT 5
# """
# query_job2 = client.query(query2)  # Make an API request.
# results2 = query_job2.result()
# output2 = results2.to_dataframe()
# # print(output2)