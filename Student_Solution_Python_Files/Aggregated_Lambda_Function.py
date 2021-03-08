
"""
    This is the final AWS Lambda function skeleton. You can populate this skeleton with the relevant code as you work through the predict instructions sequentially.
    
    
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
from random import randint # Create response id
from botocore.exceptions import ClientError # Catch errors on client side
import pandas as pd # Create Dataframe
import numpy as np # Array manipulation

# Insert key phrases function


# Insert sentiment extraction function


# Insert email responses function

# Lambda function orchestrating the entire predict logic

def def lambda_handler(event, context):
    
    # Perform JSON data decoding 
    
    body_enc = event['body']
    dec_dict = json.loads(base64.b64decode(body_enc))
    
    # Create a dataframe from the decoded JSON dictionary 
    
    df = {
        'statusCode': 200,
        'body': json.dumps(f"Name: {dec_dict['name']}, Email: {dec_dict['email']}, Cell: {dec_dict['phone']}, Message: {dec_dict['message']}")


    # Insert code to write to dynamodb
    
    
    # Amazon Comprehend
    
    
    comprehend = boto3.client(service_name='comprehend')
    
    text = #Insert code to get the website message into this variable
    
    Sentiment = # Insert code to get the sentiment with AWS comprehend
    
    KeyPhrases = # Insert code to get the key phrases with AWS comprehend
    
    # Get list of phrases in numpy array
    
    phrase = []
    
    for i in range(0, len(KeyPhrases['KeyPhrases'])-1):
    
        phrase = np.append(phrase, KeyPhrases['KeyPhrases'][i]['Text'])


    # Use email_response function to generate an email response
        
        
    Text = email_response(name = # Insert the correct variable , 
                          email_address = d# Insert the correct variable, 
                          critical_phrase_list = ['Medium', 'article', 'publish', 'Towards Data Science', 'blog'], 
                          sentiment_list =  ['Positive', 'Negative', 'Neutral', 'Mixed'], 
                          sentiment_scores = Sentiment['SentimentScore'],
                          list_of_extracted_phrases = # Insert the correct variable,
                          AWS_Comprehend_Sentiment_Dump = Sentiment)
        
        
        
    email_reply =   f'{Text}' 
    
    # SES Functionality

    # Insert code to send an email, with AWS SES, with the above defined Text variable as body
    
    
    return df    
    




