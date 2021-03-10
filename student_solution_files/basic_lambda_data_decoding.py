"""
    Initial AWS Lambda function is used to decode POST-request data received from the 
    student portfolio website.
    
    Author: Explore Data Science Academy.

    Note:
    ---------------------------------------------------------------------
    The contents of this file should be added to a AWS  Lambda function 
    created as part of the EDSA Cloud-Computing Predict. 
    For further guidance around this process, see the README instruction 
    file which sits at the root of this repo.
    ---------------------------------------------------------------------

"""

# Lambda dependencies
import boto3    # Python AWS SDK
import json     # Used for handling API-based data.
import base64   # Needed to decode the incoming POST data

def lambda_handler(event, context):
    
    # Perform JSON data decoding 
    body_enc = event['body']
    dec_dict = json.loads(base64.b64decode(body_enc))

    # Note that all of the POST data from our website form can now 
    # be accessed via the `dec_dict` dictionary object. 
    # For example, if we entered the name field as 'Student_name on the website' :
    # >>> dec_dict['name']
    # 'Student_name'
    
    # Create a response object to tell the website that the form data 
    # was successfully received. We use the contents of the decoded JSON dictionary
    # to create this response. As the predict progresses, we'll include 
    # more information about the AWS services we will invoke. 
    lambda_response = {
        'statusCode': 200, # <-- Tells the website that everything executed successfully.
        'body': json.dumps({
        'Name': dec_dict['name'],
        'Email': dec_dict['email'],
        'Cell': dec_dict['phone'], 
        'Message': dec_dict['message']
        })
    }

    return lambda_response
