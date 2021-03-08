"""
    Lambda function that decodes data from your portfolio website and sends a populated sample email to a requester with Amazon SES. 

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
    
    df = {
        'statusCode': 200,
        'body': json.dumps(f"Name: {dec_dict['name']}, Email: {dec_dict['email']}, Cell: {dec_dict['phone']}, Message: {dec_dict['message']}")
    }
    
    # This is the sample text that we will be sending to the requester. We will later see how we can use NLP to create automated intelligent responses.  
    
    Text = 'This is a sample email'
        
    # Set the email reply variable equal to the Text variable
        
    email_reply =   f'{Text}' 
    
    # SES Functionality
    

    # Replace sender@example.com with your "From" address.
    # This address must be verified with Amazon SES.
    
    SENDER = 'vincent@explore-ai.net'
    
    # Replace recipient@example.com with a "To" address. If your account 
    # is still in the sandbox, this address must be verified.
    
    RECIPIENT =  f"{dec_dict['email']}" 
    
    
    # The subject line for the email.
    
    SUBJECT = "Data Science Portfolio Project Website"
    
    # The email body for recipients with non-HTML email clients
    
    BODY_TEXT = (email_reply)

    # The character encoding for the email.
    
    CHARSET = "UTF-8"
    
    # Create a new SES resource and specify a region.
    # client = boto3.client('ses',region_name=AWS_REGION)
    
    client = boto3.client('ses')
    
    # Try to send the email.
    
    try:
        #Provide the contents of the email.
        
        response = client.send_email(
            Destination={
                'ToAddresses': [
                    RECIPIENT,
                ],
            },
            Message={
                'Body': {

                    'Text': {
                        'Charset': CHARSET,
                        'Data': BODY_TEXT,
                    },
                },
                'Subject': {
                    'Charset': CHARSET,
                    'Data': SUBJECT,
                },
            },
            Source=SENDER,
          
        )
    # Display an error if something goes wrong.	
    
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        print("Email sent! Message ID:"),
        print(response['MessageId'])
        
        
    
    return df, email_reply
