# import boto3
# import pandas as pd

# # # Specify the AWS region where your DynamoDB table is located
# aws_region = 'us-east-1'  # e.g., 'us-east-1'

# # # Initialize DynamoDB client or resource with the specified region
# dynamodb = boto3.resource('dynamodb', region_name=aws_region)

# # Define table name and primary key
# # table_name = 'evaporimeter'
# # primary_key = 'timestamp'  # Assuming timestamp is the primary key

# # Query DynamoDB table
# # table = dynamodb.Table(table_name)
# # response = table.scan()

# # # Convert response items to DataFrame
# # items = response['Items']
# # df = pd.DataFrame(items)

# # # Optional: Convert timestamp to datetime format
# # df['timestamp'] = pd.to_datetime(df['timestamp'])

# # # Display the DataFrame
# # print(df.head())

# table = dynamodb.Table('evaporimeter')
# response = table.get_item(
    
# )
# print (response)

import boto3
import pandas as pd

aws_region = 'us-east-1'
aws_access_key_id = '' # Add your access key
aws_secret_access_key = '' # Add your secret key

# Initialize DynamoDB client
dynamodb = boto3.resource('dynamodb', region_name=aws_region, aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)
table_name = 'evaporimeter'
# Retrieve DynamoDB table
table = dynamodb.Table(table_name)
# Perform a scan operation to retrieve all items in the table
response = table.scan()

# Extract items from the response
items = response['Items']
df = pd.DataFrame(items)
# Loop through all items and print them
print("Retrieved data from DynamoDB:")
# print(df)
val= pd.DataFrame(df)
val["timestamp"] = pd.to_datetime(val["timestamp"])
val = val.sort_values('timestamp', ascending=False)
latest_item = val.iloc[[0]]
print(latest_item)
json_data = latest_item.to_json(orient='records')

# Write the JSON data to a file
with open('data.json', 'w') as f:
    f.write(json_data)