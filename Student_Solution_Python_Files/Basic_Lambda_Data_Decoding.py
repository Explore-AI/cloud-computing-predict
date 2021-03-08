"""
    This AWS Lambda function is used to decode the POST data from your website.
    
    Author: Explore Data Science Academy.
    
    Description: The contents of this file should be added to a AWS 
                 Lambda function created as part of the EDSA 
                 Cloud-Computing Predict. For further guidance around 
                 this process, see the README instruction file which
                 sits at the root of this repo.
"""


import boto3    # Python AWS SDK
import json     # Used for handling API-based data.
import base64   # Needed to decode the incoming POST data

def lambda_handler(event, context):
    
    # Perform JSON data decoding 
    
    body_enc = event['body']
    dec_dict = json.loads(base64.b64decode(body_enc))
    
    # Create a dataframe from the decoded JSON dictionary 
    
    df = {
        'statusCode': 200,
        'body': json.dumps(f"Name: {dec_dict['name']}, Email: {dec_dict['email']}, Cell: {dec_dict['phone']}, Message: {dec_dict['message']}")
    
    return df
