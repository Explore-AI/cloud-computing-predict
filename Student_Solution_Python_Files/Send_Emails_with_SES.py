"""
    This function is used to send emails via Amazon SES.
    
    Author: Explore Data Science Academy.
    
    Description: The contents of this file should be added to a AWS 
                 Lambda function created as part of the EDSA 
                 Cloud-Computing Predict. For further guidance around 
                 this process, see the README instruction file which
                 sits at the root of this repo.
"""

import boto3    # Python AWS SDK

# Sample text that you would like to email to your recipient address from your sender address
    
Text = '# Insert your sample email here

# Set the email reply variable equal to the Text variable

email_reply =   f'{Text}' 

# SES Functionality


# Replace sender@example.com with your "From" address.
# This address must be verified with Amazon SES.

SENDER = 'sender@example.com'

# Replace recipient@example.com with a "To" address. If your account 
# is still in the sandbox, this address must be verified.

RECIPIENT =  f"{recipient@example.com}" 


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
        
        
    
