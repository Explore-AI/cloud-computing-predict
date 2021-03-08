# Cloud Computing Predict

#### EXPLORE Data Science Academy Cloud Computing Predict


## Overview

In this predict you will be making use of Python and AWS to create an intelligent data science portfolio website. At a high-level, the website will be hosted in a serverless manner on AWS, showcasing your amazing data science, machine learning and AI projects. 

<p align="center">
  <img src="https://github.com/Explore-AI/Pictures/blob/master/ezgif.com-gif-maker.gif?raw=true"/>
</p>

This predict will not only teach you the valuable skill of setting up and consuming AWS services to host a website, but it will also teach you how to use these services in creating an intelligent NLP service. This NLP solution will allow you to automatically populate and send intelligent emails to interested parties based on the messages they send to you through the website. For example, if a potential recruiter sees a particular portfolio project on your website that interests them and contacts you regarding the said project, it is possible to set up your NLP bot to pick up what the tone and key phrases are in the recruiter's message. Some smart programming techniques can then be used to automatically send a response. 

In **Figure 1** the solutions architecture of this predict is depicted. Below follows a brief description of each element in the process:

>- [x] **[GitHub:](https://github.com/)** A dedicated private/public repo forked from an EXPLORE template repo which houses all the content and instructions for the student to complete the Predict.
>
>- [x] **[AWS Lambda:](https://aws.amazon.com/lambda/)** A serverless compute instance responsible for multiple processing steps:
>      - Stores the enquiry details within an AWS DynamoDB instance for later retrieval.
>      - Forwards the enquiry contents to AWS Comprehend to help formulate an intelligent response to the site visitor.
>      - Upon successful completion of these tasks, sends a confirmation signal to an EDSA Lambda for automated marking.
>      
>- [x] **[AWS Amplify:](https://aws.amazon.com/amplify/)** Responsible for serving the static web content hosted in GitHub which becomes the basis of the student web page.
>
>- [x] **[Amazon DynamoDb:](https://aws.amazon.com/dynamodb/)** A NoSQL database responsible for storing enquiry details from individuals visiting the student webpage.
>
>- [x] **[Anazon SES:](https://aws.amazon.com/ses/)** An automatable email service responsible for returning an intelligent response to webpage visitors based upon their enquiries.
>
>- [x] **[AWS API Gateway:](https://aws.amazon.com/api-gateway/)** AWS service responsible for receiving enquiry details via an API call from the student webpage, and for passing these on to the internal lambda function.
>
>- [x] **[AWS Comprehend:](https://aws.amazon.com/comprehend/)** An intelligent NLP  service capable of characterising sentiment and extracting key-phrases from the ingested text. Used to detect topics within the received webpage enquiries.


<p align="center">
  <img src="https://raw.githubusercontent.com/Explore-AI/Pictures/master/serverless_predict_process.PNG"/>
    <br>
    <em>Figure 1: Cloud Computing Predict System Overview</em>
  
</p>


## Predict Instructions

This predict is broken down into 9 sequential steps meaning you have to completely finish a particular step before you can move on to the next one.


Brief description of each step in the 9-step predict process:

    1. In the first step we will setup a private repository on GitHub that will store all the code needed for a static website.
    
    2. This step is all about building your static website. Here, we provide you with a bootstrap template and some general guides but how you would like your website to look and feel is all up to you. You are free to modify, chop and change your website to represent what you would like it to represent.
    
    3. In the third step we will be serving your created website with the help of AWS Amplify. We will provide you with the initial steps to get you started but the rest is left to you to figure out how to get this up and running.
    
    4. Here we will be creating an AWS DynamoDB NoSQL database. This database will be used to store website data as and when visitors populate and send the form. 
    
    5. Step five is where we will be creating an IAM role that will give your AWS Lambda function the required access to AWS Comprehend, AWS SES, AWS DynamoDB and AWS API Gateway.
    
    6. This step is where things get interesting. Here we will be setting up the AWS Lambda function, Pandas and Numpy ARN layers and AWS API Gateway trigger:
    
        - **The AWS Lambda Function** will be used to:
        
                - write data to Amazon DynamoDB,
                - generate intelligent email responses with Amazon Coprehend, and
                - send emails with Amazon SES.
        
        - **The AWS API Gateway triggre** can be seen as a module that sits on top of the AWS Amplify hosted static website. This gateway tells the website request data where to go and the Lambda trigger does something with the data passing though the gateway.
    
    7. In step seven we will be configuring the Lambda function we created in step six to write the incoming data from the website to our DynamoDB database which we created in step four.
    
    8. This step is where we configure the AWS SES service so that we can send and receive emails automatically with the help of our Lambda function.
    
    9. Here we will dive into the NLP portion of the predict with the help of AWS Comprehend. At a high level, AWS Comprehend will be used to extract sentiment and key phrases from the message sent from your static website. Using logic we will then populate an automated response if the extracted key phrases and sentiment matches a specified sentiment and targeted list of key phrases. Also in this step, we will be going through all the helper methods required to send an intelligent and automated email response and we will provide a step by step example of how the email logic is set up.
    


### 1) Create a New Repo On GitHub

The main objective of this step is to create a new repository on GitHub. This repo will be used to store all your website code.



Below are the detailed steps required to create a new private repo:

  I. In the upper-right corner of any page, use the `+` drop-down menu, and select New repository.
  
  <p align="center">
  
  <img src="https://raw.githubusercontent.com/Explore-AI/Pictures/master/git_1.PNG"/>
    <br>
    <em>Figure 2: Create a new repository</em>
  
  </p>

  
  II. Type a short, memorable name for your repository. For example, "Test-Repo".

  
  <p align="center">
  
  <img src="https://raw.githubusercontent.com/Explore-AI/Pictures/master/git_2.PNG"/>
    <br>
    <em>Figure 3: Name your repository</em>
  
  </p>
  
  III. Choose repository visibility, select Initialize this repository with a README and select create repository.
  
  <p align="center">
  
  <img src="https://raw.githubusercontent.com/Explore-AI/Pictures/master/git_3.PNG"/>
    <br>
    <em>Figure 4: Create your repository</em>
  
  </p>
  

  

### 2) Download and Modify the Portfolio Webpage Template

Step two in the process is where you will create your website and add your relevant data science and machine learning portfolio projects. For this step we will provide you with a baseline template which you can change as you please. 

Below follows a brief description of the files in the bootstrap template:

| Folder           | File Name                | Description      |
| ---------------- | ----------------         | ---------------- |
| ./Assets/mail    | contact_me.js            | Contains all the code required to send the data from the filled website form through the defined endpoint to the AWS Lambda function    |
| ./Assets/mail    | jqBootstrapValidation.js | This JavaScript file is used to check if the data entered in the form on the website is in the correct format. If the data is in the expected format and the endpoint is in place the message will be sent if not, an error message will be displayes prompting the user to input the correct information.    |
| ./Assets/img     | n/a                      | This folder contains all the images that you would like to use in your website.                    |
| ./css            | style.css                | Here the CSS file is kept that controls the style i.e. look and feel of your website    |
| ./js             | scripts.js               | Other content    |
| ./               | index.html               | The index.html is used to define your static web page. This is the file that you will mostly be working with when creating your website.      |



**Steps to download and modify the provided bootstrap template to make the static website your own:**

  I. Download the bootstrap template found [here](https://drive.google.com/drive/folders/18bAsAtIm6Ip15cqB3qEDMVvLiovEyF9u)
  
  II. Add the bootstrap template to your newly created GitHub account.
  
  <p align="center">
  
  <img src="https://github.com/Explore-AI/Pictures/blob/master/git_4.PNG"/>
    <br>
    <em>Figure 5: Add the static website files to your GitHub repo</em>
  
  </p>
  
  
  III. Open the `index.html` file with an editor of your choice i.e. Pycharm, Brackets, VS Code, etc. and customise the website according to your preference. You can find some general guidance of what to change by reading the code comments. Here is an example comment that you can expect to find in the `index.html` file:  
 
 ``` <! -- This comment instructs you what to change and how to change it --> ```
 
 IV. As soon as you have modified the bootstrap template according to your liking and you are happy, you can move to the next step. Here we will get our hands dirty with the serving of your static website with the help of AWS Amplify :)
 
 

 
### 3) Serve Static Web Page on AWS Amplify

To serve our static website we will be making use of the AWS Amplify service. As mentioned before, AWS Amplify simplifies the process of web development by handling the deployment infrastructure side of things. Below is the step by step instructions required to host your beautiful portfolio website.



  
  I. The first step is to log in to the AWS Management Console and navigate to the [AWS Amplify](https://aws.amazon.com/amplify/) service. 
  
*Please note which region you have selected for the AWS Amplify service. When spinning up new AWS services from here on out, it is advised that all of your services should sit in the same region as the chosen AWS Amplify region.*
  
  II. Once you have located AWS Amplify you should select `Get Started`.

<p align="center">
  
<img src="https://raw.githubusercontent.com/Explore-AI/Pictures/master/Amp-1.PNG" style="width:500px;" />
  <br>
  <em>Figure 6: Get started with AWS Amplify</em>
  
</p>
  
  III. The next step is to select `Get Started` on the `Host Your Web App` menu
  
  <p align="center">
  
  <img src="https://raw.githubusercontent.com/Explore-AI/Pictures/master/Amp-2.PNG" style="width:350px;"/>
    <br>
    <em>Figure 7: Host your web app</em>
  
  </p>
  
  
  IV. Next, you need to connect your GitHub repo created in section 1, containing the bootstrap template, with AWS Amplify.
   
  <p align="center">
  
  <img src="https://raw.githubusercontent.com/Explore-AI/Pictures/master/Amp-3.PNG" style="width:500px;"/>
    <br>
    <em>Figure 8: Connect GitHub repo</em>
  
  </p>
    
  V. You are now required to `authorise` GitHub to be able to access your public and private repositories. Leave all the settings default and click `next` and `deploy` your solution.
  
  <p align="center">
  
  <img src="https://raw.githubusercontent.com/Explore-AI/Pictures/master/Amp-4.PNG" style="width:500px;"/>
    <br>
    <em>Figure 9: Autorise GitHub</em>
  
  </p>
  

  
**NOTE: By this point in the process your modified website should be up and running through the AWS Amplify service with a sample domain name branch_name.reference_number.amplifyapp.com.**

**You can view an example of the fully functioning website deployed with AWS Amplify [here](https://main.dajjrrhheaglb.amplifyapp.com/)**


### 4) Create DynamoDb Database

  
We need a database that will store all the data sent from the serverless hosted website. For this predict we will be using the AWS DynamoDB NoSQL database for this purpose.


  
  I. Navigate to the AWS DynamoDb service via the AWS Management Console
  
  
  II. On the DynamoDB `Dashboard` select `Create Table`.

  <p align="center">
  <img src="https://raw.githubusercontent.com/Explore-AI/Pictures/master/db-1.PNG" style="width:550px;"/>
    <br>
    <em>Figure 10: Create a DynamoDB table</em>
  </p>
  
  III. Give your table a relevant name, for example, `my-portfolio-data-table`
  
  IV. In the `Primary Key` field insert `ResponsesID` and set the type to number.
  
  <p align="center">
  <img src="https://raw.githubusercontent.com/Explore-AI/Pictures/master/db-2.PNG" style="width:550px;"/>
    <br>
    <em>Figure 10: Create a DynamoDB table</em>
  </p>  
  
  V. Click on `Create`.
  
  VI. Select the table just created and under `Items` click on `Create Item`.
  
  <p align="center">
  <img src="https://raw.githubusercontent.com/Explore-AI/Pictures/master/db-3.PNG" style="width:750px;"/>
    <br>
    <em>Figure 11: Add new items and their data types to created table</em>
  </p>  
  
  VII. Enter 100 in the `ResponsesID` field. (this is a unique number that we will generate with the Lambda function)
  
  VIII. Click on the `plus` icon and select `insert - number`. Name this item `Cell`. Enter `0123456789` in the Value field.
  
  IX. Click on the `plus` icon and select `insert - string`. Name this item `Email`. Enter `vincent@explore-ai.net` in the Value field.
  
  X. Click on the `plus` icon and select `insert - string`. Name this item `Message`. Enter `Empty Message` in the Value field.

  XI. Click on the `plus` icon and select `insert - string`. Name this item `Name`. Enter `Vincent` in the value field.
  
  <p align="center">
  <img src="https://raw.githubusercontent.com/Explore-AI/Pictures/master/db-4.PNG" style="width:1000px;"/>
    <br>
    <em>Figure 12: Final populated table</em>
  </p>   
  
  XII. Click on save.
  
  XIII. Select the created table and navigate to the `Overview` tab.
  
  XIV. Scroll down and note your Amazon Resource Name (ARN)	for the created table. Save this for later use in the IAM policy creation steps.
  

  

### 5) Create an IAM Policy

  
We need an IAM policy to give the Lambda function the required access to the various services that we will be using in this predict. In total we need to create 4 policies for this IAM Role:

    1. AWS Comprehend Policy: Give the Lambda function access to AWS Comprehend to parse the message from the website form to AWS Comprehend to allow AWS Comprehend to calculate a message sentiment score and extract key phrases from the message.
    
    2. AWS SES Policy: Give the Lambda function access to AWS SES to allow us to send automated responses via email.
    
    3. AWS Basic Lambda Execution Policy: Grants the Lambda function permission to access AWS services and resources.
    
    4. AWS DynamoDB Policy: Give the Lambda function access to write data from the website to a designated (existing) AWS DynamoDB table.


  
  I. Navigate to the IAM service in the AWS Management Console and on the `Roles` tab select `Create Role`
  
  II. From there select `Lambda` under the common use cases. Next click on the `Next Permission` button.
  
  
- AWS Comprehend IAM Role:

  
      - In the search box type in `ComprehendFullAccess`, check the select box and click `Next: Tags`. 

      - Leave the `Next: Tags` page as is and click `Next: Review`.
      
      - Give your role an easy to remember name and click create role.
      
  <p align="center">
  <img src="https://raw.githubusercontent.com/Explore-AI/Pictures/master/iam-1.PNG" style="width:550px;"/>
    <br>
    <em>Figure 13: AWS Comprehend IAM Role</em>
  </p>   
      
      
- AWS SES IAM Role:

  
      - On the `Roles` tab navigate to the IAM role created in the step above.

      - Select the role and click on `Attach Policy`.
      
      - In the search box type in `AmazonSESFullAccess`, check the select box and click `Attach Policy`.
      
  <p align="center">
  <img src="https://raw.githubusercontent.com/Explore-AI/Pictures/master/iam-2.PNG" style="width:550px;"/>
    <br>
    <em>Figure 14: AWS SES IAM Role</em>
  </p>  
      
      
- AWS Basic Lambda Execution IAM Role:     

   
      - On the `Roles` tab navigate to the IAM role created in the step above.

      - Select the role and click on `Attach Policy`.
      
      - In the search box type in `AWSLambdaBasicExecutionRole`, check the select box and click `Attach Policy`.

  <p align="center">
  <img src="https://raw.githubusercontent.com/Explore-AI/Pictures/master/iam-3.PNG" style="width:550px;"/>
    <br>
    <em>Figure 15: AWS Basic Lambda IAM Role</em>
  </p>      
  
- AWS DynamoDb IAM Role:     

   
      - On the `Roles` tab navigate to the IAM role created in the step above.
      

      - Select the role and click on `Add inline policy`.
      
      
      - Select `Choose a service` and in the search box type `DynamoDb` 
      
      
      - Under `Actions` check the `Write` checkbox.
      
      
      - Under `Resources/table` select `Add ARN`
      
      
      - Under `Region` select the `any` checkbox.
      
      
      - Under the `Table name` insert the ARN noted in 4.
      
      
      - Click `add`, click review policy
      
      
      - Give the inline policy a relevant name and select `Create policy`
      
  <p align="center">
  <img src="https://raw.githubusercontent.com/Explore-AI/Pictures/master/iam-4.PNG" style="width:1000px;"/>
    <br>
    <em>Figure 16: AWS DynamoDB IAM Role</em>
  </p>  
      
    
  
### 6) Set-up the Initial AWS Lambda Function and the AWS API Gateway Trigger
  
In this step we will be setting up the AWS API Gateway and the AWS Lambda function. This will be a three step process.

    

**Step 1**

Step one will be focused on creating the AWS Lambda Function with a Python 3.7 runtime. For access control we would like to use the IAM role created previously to govern the lambda function.
  
  I. Navigate to the AWS Lambda service via the AWS Management Console.
  
  II. Once there, under functions, click `Create function`.
  
  III. Select `Author from scratch` and give your function a relevant name (e.g. model-solution-cloud-computing-predict).
  
  <p align="center">
  <img src="https://raw.githubusercontent.com/Explore-AI/Pictures/master/lam-1.PNG" style="width:550px;"/>
    <br>
    <em>Figure 17: Created lambda function</em>
  </p>  
  
  IV. Under `runtime` select `Python 3.7`
  
  V. Under `Change default execution role` select `Use an existing role`.
  
  VI. Select the IAM role created in step 5.
  
  VII. Click `Create function`.
  
**Step 2**

In step two the objective is to add two layers to the generated lambda function - one Pandas layer and one Numpy layer. We need to add these layers so that we may use the Pandas and Numpy libraries building our solution i.e. the Python code telling the lambdas function what to do.
 
  I. Under `layers` click add layer.
  
  II. Select `Specify an ARN`.
  
  III. Get the correct Numpy and Pandas layers for your region and Python version from [here](https://github.com/keithrozario/Klayers/blob/master/deployments/python3.7/arns/eu-west-1.csv)
  
  <p align="center">
  <img src="https://raw.githubusercontent.com/Explore-AI/Pictures/master/lam-4.PNG" />
    <br>
    <em>Figure 18: Numpy and Pandas layers in lambda function</em>
  </p> 
  

**Step 3**

The final step is to create the AWS API Gateway and set this endpoint as our lambdas function trigger. At a high level what this means is that, if the endpoint is hit i.e. the AWS API Gateway, our AWS Lambdas function will be invoked and the code will be executed setting off the chain of events that will generate and send the intelligent email automatically. 

 
  I. Select `add trigger`.
  
  II. Under `Trigger configuration` select `API Gateway`.
  
  III. Under `API Type` select `HTTP API`.
  
  IV. Under `Security` select `open`.
  
  V. Under `Additional Settings` check the `CORS` checkbox.
  
  VI. Click add.
  
  <p align="center">
  <img src="https://raw.githubusercontent.com/Explore-AI/Pictures/master/lam-2.PNG" style="width:500px;"/>
    <br>
    <em>Figure 19: Created API Gateway</em>
  </p> 
  
  VII. Note the `API endpoint` address under the configured trigger.
  
  VIII. Use this API and navigate to the `contact_me.js` file in your GitHub repo created in step 1.
  
  <p align="center">
  <img src="https://raw.githubusercontent.com/Explore-AI/Pictures/master/lam-3.PNG" style="width:500px;"/>
    <br>
    <em>Figure 18: Created API Gateway</em>
  </p> 
  
  IX. Replace the existing API URL with your API endpoint.
  
  X. Commit the changes and wait for the branch to be redeployed by AWS Amplify.
  
  
**NOTE: By this point in the process your website should enable you to fill out the form with the appropriate information and upon submission, you should receive the notification `Your message has been sent`**
  

### 7) AWS Lambda Function for Writing to DynamoDB

We are now at a point in the predict where we can start building the actual lambda functionality. We start off with the simplest task. That is, using the AWS Lambda/AWS API Gateway orchestration to write the data coming from the website form to our created DynamoDB database. If you need to familiarise yourself with the overall process, please refer back to **figure 1**.

  <p align="center">
  <img src="https://raw.githubusercontent.com/Explore-AI/Pictures/master/cloud-computing-predict-dynamodb.gif" />
    <br>
    <em>Figure 20: Lambda writing data from the website to DynamoDB</em>
  </p> 


*Below follows the code required to get the desired output from the lambda function. Make sure this code is sitting in the `lambda_function.py` file under the main directory (the main directory will typically have the same name as your created lambda function).*


```python
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
    }
    
    # Write to dynamodb
    
    # Create a random variable that can take a value between 1 and 1000000000. This variable will be used as our key value i.e the ResponsesID
    
    rid = randint(1, 1_000_000_000)
    
    # Instantiate the DynamoDB service with the help of the boto3 library
    
    dynamodb = boto3.resource('dynamodb')
    
    # Instantiate the table. Remember pass the name of the DynamoDB table created in step 4

    table = dynamodb.Table('Email-Responses')
    
    # Write the responses to the table using the put_item method.
    
    response = table.put_item(Item={'ResponsesID':rid,
                                    'Name':dec_dict['name'],
                                    'Email':dec_dict['email'] ,
                                    'Cell':dec_dict['phone'] ,
                                    'Message':dec_dict['message']
    })
    
    return df

```


### 8) AWS Lambda Function for Sending an Email with AWS SES

In this step we will be setting up AWS Simple Email Service or AWS SES for short, to automatically send emails. This is a two step process. The first step will be to verify your email address on the AWS SES console and the second step will be to setup the lambda function python file i.e. `lambda_function.py` in such a way that when the AWS API Gateway is hit, the lambda function will automatically send an email to the email address specified by the person that filled out the form on your static hosted website.
   
**Step 1 Verify your email with Amazon SES:**

When using Amazon SES for the first time, all accounts start out in sandbox mode. This is to prevent new accounts to abuse the service and send out spam emails. In sandbox mode the following restrictions apply:

    - You can only send mail to verified email addresses and domains, or to the [Amazon SES mailbox simulator](https://docs.aws.amazon.com/ses/latest/DeveloperGuide/send-email-simulator.html).
   
    - You can only send mail from verified email addresses and domains.
   
    - You can send a maximum of 200 messages per 24-hour period.
   
    - You can send a maximum of 1 message per second.
    
   
When your account is out of the sandbox, you can send email to any recipient, regardless of whether the recipient's address or domain is verified. However, you still have to verify all identities that you use as "From", "Source", "Sender", or "Return-Path" addresses.

*Note: To move out of sandbox mode you can follow [these](https://docs.aws.amazon.com/ses/latest/DeveloperGuide/request-production-access.html) instructions.*


The following steps will guide you in verifying your sender and recipient email addresses on the AWS SES console.

    1) Navigate to the AWS SES console with the AWS Management Console.
    
    2) On the AWS SES console select `Email Addresses`.
    
    3) Click on `Verify a New Email Address`
    
  <p align="center">
  <img src="https://raw.githubusercontent.com/Explore-AI/Pictures/master/ses-1.PNG" />
    <br>
    <em>Figure 21: Verify email with AWS SES</em>
  </p> 
  
    4) In the textbox type the email address wich you would like to use as your sender email address and click `Verify This Email Address`.
    
    
   <p align="center">
  <img src="https://raw.githubusercontent.com/Explore-AI/Pictures/master/ses-2.PNG" />
    <br>
    <em>Figure 22: Verify sender email with AWS SES</em>
  </p> 
  
    5) Go to your inbox and click on the link to verify your sender email address.
    
   <p align="center">
  <img src="https://raw.githubusercontent.com/Explore-AI/Pictures/master/ses-3.PNG" />
    <br>
    <em>Figure 23: Verified sender email address </em>
  </p>     
    
    
    6) Repeat steps 1-5 for your recipient email address.
    
   
**Step 2 Python code that sends an email via AWS SES:**

Below is the code required to set up the email functionality with your AWS Lambda function. At this point the process is:

    - Form is filled out on the website and sent.
    
    - The data passes through the AWS API Gateway and triggers the AWS Lambda function.
    
    - The sender information is decoded.
    
    - The lambda function writes the data to the AWS DynamoDB database.
    
    - A sample message is populated.
    
    - The email address of the sender, found in the decoded information, is used as as recipient email address.
    
    - The sample message is sent from your verified email address to the verified recipient address via AWS SES.
    


```python
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

```


### 9) AWS Lambda Function for Using Amazon Comprehend

In this step we will be building our NLP functionality with the help of AWS Comprehend. The NLP functionality will enable us to extract the overwhelming sentiment from a message as well as a list of key phrases as determined by AWS comprehend. With the sentiment information and a list of key phrases we can then build in intelligent, automated email responses in our AWS Lambda function. To thoroughly understand this section we provided a three step breakdown where we describe each key element. The first is the process description where we go through the logic of how to use AWS comprehend to extract sentiment and key phrases. The second is the methods description where we describe the two helper methods and the lambda function required to orchestrate an intelligent automated response. The final is end-to-end example where we simulate what we would like to achieve once the entire AWS Lambda/AWS Comprehend/AWS SES integration is built.

**Process Description**

At a high-level the entire process can be described as follow:

        1. The form is filled out on the website and sent. This form contains the following sender data: `name`, `cellphone number`, `email address`, and `message`.
        
        2. The data passes through the AWS API Gateway and triggers the AWS Lambda function.
        
        3. The sender data is decoded.
        
        4. The `message` is used in AWS Comprehend to extract the message sentiment and a dictionary of key phrases.
        
        5. A custom helper function finds the score and value of the most likely sentiment present in the message.
        
        6. Another helper function is used to convert the list of key phrases, generated by AWS Comprehend, to a numpy array. The difference here is that the numpy array does not contain the key phrases as elements but rather the individual words present in the key phrases dictionary.
        
        7. The helper function described in point 6 also matches the list of extracted key phrases with a provided list of phrases/words. 
        
        8. We can then set up email logic with an if condition as follow:
        
```python

if message_sentiment == 'Desired_Sentiment':
    
    if (AWS_Comprehend_Extracted_Words == Provided_List_of_Words):
        
        generate some personalised response based on message content
        
    else:
        
        generate some generic response based on message content
        
```


**Methods Description**

In this sub-section we will be going over the helper methods required to send intelligent, automated email responses.

    Method 1 - find_max_sentiment(Comprehend_Sentiment_Output):
    
    This method extracts and return the highest probable sentiment from a given message.
    
            - Comprehend_Sentiment_Output: The sentiment dictionary generated by AWS Comprehend.
            
            - sentiment_score: The value of the highest probable sentiment present in a given message.
            
```python
import boto3    # Python AWS SDK
import json     # Used for handling API-based data.
import base64   # Needed to decode the incoming POST data
from random import randint # Create response id
from botocore.exceptions import ClientError # Catch errors on client side
import pandas as pd # Create Dataframe
import numpy as np # Array manipulation

# Find overwhelming sentiment in article

def find_max_sentiment(Comprehend_Sentiment_Output):
    
    sentiment_score = 0

    if Comprehend_Sentiment_Output['Sentiment'] == 'POSITIVE':

        sentiment_score = Comprehend_Sentiment_Output['SentimentScore']['Positive']

    elif Comprehend_Sentiment_Output['Sentiment'] == 'NEGATIVE':

        sentiment_score = Comprehend_Sentiment_Output['SentimentScore']['Negative']

    elif Comprehend_Sentiment_Output['Sentiment'] == 'NEUTRAL':

        sentiment_score = Comprehend_Sentiment_Output['SentimentScore']['Neutral']

    else:

        sentiment_score = Comprehend_Sentiment_Output['SentimentScore']['Mixed']

    print(sentiment_score, Comprehend_Sentiment_Output['Sentiment'])
    
    return Comprehend_Sentiment_Output['Sentiment'], sentiment_score

 ```           
    Method 2- key_phrase_finder_2(list_of_important_phrases, list_of_extracted_phrases):
    
    This method matches the words in the key phrases dictionary, from AWS Comprehend, to a provided list of words and return True if there is a match and false otherwise
    
            - list_of_important_phrases: this variable takes a list of words i.e. ['CV', 'data', 'science']
            
            - list_of_extracted_phrases: this variable comes in the form of the AWS Comprehend key phrases dictionary
            
            - listing: empty list to append the individual words present in the AWS Comprehend key phrases dictionary
            
            - PhraseChecker: boolean variable which takes on the value of true if there is a matched word in the provided list and the list of words present in the AWS Comprehend key phrases dictionary
            
            
```python
def key_phrase_finder_2(list_of_important_phrases, list_of_extracted_phrases):

    listing = []
    PhraseChecker = None

    res = str(list_of_extracted_phrases).split()

    for important_word in list_of_important_phrases:

        names = res
        names2 = [word for word in names if important_word in word]

        isnot_empty = np.array(names2).size > 0
        
        if isnot_empty == True:

            listing = np.append(listing, names2)
            
        else:
            
            listing = listing
            
    if np.array(listing).size > 0:
    
        PhraseChecker = True
        
    else:
        
        PhraseChecker = False
    
    return listing, PhraseChecker


```
    
    Method 3 - email_response(name, email_address, critical_phrase_list, sentiment_list, sentiment_scores, list_of_extracted_phrases, AWS_Comprehend_Sentiment_Dump) :
    
    This method takes in the information from the sender i.e. name, email_address, the sentiment and the sentiment and key phrases output from comprehend, and a list of critical phrases and uses the logic described in the Process Description section to populate a email. 
    
    The email_response method works as follow:
    
    1. You supply a list of words.

    2. The supplied list of words are matched with words extracted from the AWS Comprehend key phrases dictionary. 

    3. If there is a match, the function returns `True` and if not it returns `False`.

    4. Given the match, or potentially multiple matches, you can set up logic to start building an email response sequentially.
      
```python

def email_response(name, email_address, critical_phrase_list, sentiment_list, sentiment_scores, list_of_extracted_phrases, AWS_Comprehend_Sentiment_Dump):
    
    # Check for the sentiment of the message and find dominant sentiment score
    
    Sentiment_finder = find_max_sentiment(AWS_Comprehend_Sentiment_Dump)
    
    overwhelming_sentiment = Sentiment_finder[0]
    
    overwhelming_sentiment_score = Sentiment_finder[1]
    
    # Check for article critical phrases
    
    Phrase_Matcher_Article = key_phrase_finder_2(critical_phrase_list,  list_of_extracted_phrases)
    
    Matched_Phrases_Article = Phrase_Matcher_Article[0]
     
    Matched_Phrases_Checker_Article = Phrase_Matcher_Article[1]
    
    # Check for project phrases
    
    Phrase_Matcher_Project = key_phrase_finder_2(['github', 'git', 'Git', 'GitHub', 'projects', 'portfolio', 'Portfolio'],  list_of_extracted_phrases)
    
    Matched_Phrases_Project = Phrase_Matcher_Project[0]
     
    Matched_Phrases_Checker_Project = Phrase_Matcher_Project[1]
    
    # Check for C.V phrases
    
    Phrase_Matcher_CV = key_phrase_finder_2(['C.V', 'resume', 'Curriculum Vitae', 'Resume', 'CV'],  list_of_extracted_phrases)
    
    Matched_Phrases_CV = Phrase_Matcher_CV[0]
     
    Matched_Phrases_Checker_CV = Phrase_Matcher_CV[1]
    
    # Generate standard responses
    
    Greetings_text = f'Good day {name},'

    CV_text = 'I see that you mentioned my C.V in your message. I am happy to forward you my C.V in response. If you have any other questions or C.V related queries please do get in touch. '
 
    Project_Text = 'The projects I listed on my site only include the ones not running in production. I have several other projects that might interest you.'
    
    Article_Text = 'In your message you mentioned my blog posts and data science articles. I have several other articles published in academic journals. Please do let me know if you are interested - I am happy to forward them to you'
  
    Negative_Text = 'I see that you are unhappy in your response. Can we please set up a session to discuss why you are not happy, be it with the website, my personal projects or anything else. \n\nLooking forward to our discussion. \n\nKind Regards, \n\nMy Name'
 
    Neutral_Text = 'Thank you for your email. Let me know if you need any additional information.\n\nKind Regards, \n\nMyName'
    
    Farewell_Text = 'Thank you for your email.\n\nIf there is anything else I can assist you with please let me know and I will set up a meeting for us to meet in person.\n\nKind Regards, \n\nMyName'
    
    # Email Logic
    
    # Positive Response
    
    if overwhelming_sentiment == 'POSITIVE':
    
        if  ((Matched_Phrases_Checker_CV == True) & (Matched_Phrases_Checker_Article == True) & (Matched_Phrases_Checker_Project == True)):
            
            mytuple = (Greetings_text, CV_text, Article_Text, Project_Text, Farewell_Text)
            
            Text = "\n \n".join(mytuple)
            
        elif ((Matched_Phrases_Checker_CV == True) & (Matched_Phrases_Checker_Article == False) & (Matched_Phrases_Checker_Project == True)):
            
            mytuple = (Greetings_text, CV_text, Project_Text, Farewell_Text)
            
            Text = "\n \n".join(mytuple)
            
        elif ((Matched_Phrases_Checker_CV == True) & (Matched_Phrases_Checker_Article == False) & (Matched_Phrases_Checker_Project == False)):
            
            mytuple = (Greetings_text, CV_text, Farewell_Text)
            
            Text = "\n \n".join(mytuple)
            
        elif ((Matched_Phrases_Checker_CV == False) & (Matched_Phrases_Checker_Article == True) & (Matched_Phrases_Checker_Project == False)):
            
            mytuple = (Greetings_text, Article_Text, Farewell_Text)
            
            Text = "\n \n".join(mytuple)       
            
        elif ((Matched_Phrases_Checker_CV == False) & (Matched_Phrases_Checker_Article == False) & (Matched_Phrases_Checker_Project == False)):
            
            mytuple = (Greetings_text, Farewell_Text)
            
            Text = "\n \n".join(mytuple)   
            
        elif ((Matched_Phrases_Checker_CV == False) & (Matched_Phrases_Checker_Article == False) & (Matched_Phrases_Checker_Project == True)):
            
            mytuple = (Greetings_text, Project_Text ,Farewell_Text)
            
            Text = "\n \n".join(mytuple)   
            
        elif  ((Matched_Phrases_Checker_CV == True) & (Matched_Phrases_Checker_Article == True) & (Matched_Phrases_Checker_Project == False)):
            
            mytuple = (Greetings_text, CV_text, Article_Text, Farewell_Text)
            
            Text = "\n \n".join(mytuple)
            
        else:
            
            mytuple = (Greetings_text, Project_Text, Article_Text, Farewell_Text)
            
            Text = "\n \n".join(mytuple)
            
    elif overwhelming_sentiment == 'NEGATIVE':

            mytuple = (Greetings_text, Negative_Text)
            
            Text = "\n \n".join(mytuple)
            
    else:


            mytuple = (Greetings_text, Neutral_Text)
            
            Text = "\n \n".join(mytuple)
    
    
    return Text
    
```

**End-to-end Example**

In this section we will be going over a basic example of how an email response is generated with the full solutions architecture.


Lets say we have the following sample message:

> Hi Explore Data Science Student,
>
> I love your website and your portfolio projects. I also had a look at your GitHub page and I am quite impressed with the quality of your work.
>
> Your medium articles also captured my attention.
>
> Could you please forward me your CV so that I can present you for a potential job at one of my clients. It is for a six week contract and I feel that your experience and skills match the job specifications perfectly.
>
> Thank you so much for your time.
> 
> Kind regards,
> 
> Joanne Liebenberg
> 
> Senior HR Manager, Real Analytics Resources

Running this message through our AWS Comprehend service produces [this](https://github.com/Vincent-EDSA/cloud-computing-predict/blob/main/Model_Solution_Python_Files/Example_AWS_Comprehend_Key_Phrases_Output.txt) key phrases output and [this](https://github.com/Vincent-EDSA/cloud-computing-predict/blob/main/Model_Solution_Python_Files/Example_AWS_Comprehend_Sentiment_Output.txt) sentiment output.

From this we can see that our NLP solution picked up that we have a positive sentiment in the message and that the message contains key phrases such as: 'your portfolio projects', 'your GitHub page', 'Your medium articles', 'a potential job', etc.

We can therefore set up some logic to start to build an automated intelligent response with our helper functions.

We firstly start by providing some sample `string` replies that we can add to our email response if certain supplied words match the words in our AWS Comprehend key phrases dictionary. These sample replies can take the following form:

**1. A reply if we match CV related words**

    CV_text = 'I see that you mentioned my C.V in your message. I am happy to forward you my C.V in response. If you have any other questions or C.V related queries please do get in touch. '

**2. A reply if we match portfolio project related words**

    Project_Text = 'The projects I listed on my site only include the ones not running in production. I have several other projects that might interest you.'

**3. A reply if we match Medium article related words**

    Article_Text = 'In your message you mentioned my blog posts and data science articles. I have several other articles published in academic journals. Please do let me know if you are interested - I am happy to forward them to you'
  
    
**4. A reply if we our sentiment is negative**  

    Negative_Text = 'I see that you are unhappy in your response. Can we please set up a session to discuss why you are not happy, be it with the website, my personal projects or anything else. \n\nLooking forward to our discussion. \n\nKind Regards, \n\nMy Name'
 
**5. A reply if we our sentiment is neutral** 
 
    Neutral_Text = 'Thank you for your email. Let me know if you need any additional information.\n\nKind Regards, \n\nMyName'
    
**6. A farewell reply** 

    Farewell_Text = 'Again, Thank you for your email.\n\nIf there is anyting else I can assist you with please let me know and I will set up a meeting for us to meet in person.\n\nKind Regards, \n\nMyName'
    
    
With our sample replies now defined we can use `if conditions` and `string manipulation` techniques to *build* a response.

For instance we define a `Phrase_Matcher_Project`  variable that makes use of the `key_phrase_finder_2` method and pass a list of words that might be project related, for example ['github', 'git', 'Git', 'GitHub', 'projects', 'portfolio', 'Portfolio']. 

If any of these words now match the extracted key words in the Comprehend dictionary the value of the `Phrase_Matcher_Project` variable will be `True`. We can then use an `if function` and string manipulation to add a greetings text, the project text and the farewell text to an `email_reply` variable. This `email_reply` variable will take the following value for this explained case:

> Good day Joanne Liebenberg,
>
> The projects I listed on my site only include the ones not running in production. I have several other projects that might interest you.
> 
> Again, thank you for your email.
>
> If there is anyting else I can assist you with please let me know and I will set up a meeting for us to meet in person.
>
> Kind Regards, 
>
> MyName

Moving away from the toy case, remember we had key phrases that included the words: `CV`, `projects`, `articles`, etc. We can therefore set up a CV, Project and Article phrase checker and use the same logic as discussed above to generate an intelligent automated response. Our `email_response` variable will therefore take the following value for the full example:

> Good day Joanne Liebenberg,
> 
> I see that you mentioned my C.V in your message. I am happy to forward you my C.V in response. If you have any other questions or C.V related queries please do get in touch. 
> 
> In your message you mentioned my blog posts and data science articles. I have several other articles published in academic journals. Please do let me know if you are interested - I am happy to forward them to you
> 
> The projects I listed on my site only include the ones not running in production. I have several other projects that might interest you.
> 
> Again, thank you for your email.
>
> If there is anyting else I can assist you with please let me know and I will set up a meeting for us to meet in person.
>
> Kind Regards, 
>
> MyName
   
**Note: The lambda function that makes all of this possible can be viewed [here](https://github.com/Vincent-EDSA/cloud-computing-predict/blob/main/Model_Solution_Python_Files/Aggregated_Lambda_Function.py)**


## Conclusion

If you followed the 9 step process described in this predict correctly you should now have a fully functioning portfolio project website capable of sending intelligent email responses in an automated way. Now that you have the full working product you are free to tweak various aspects of the project to personalise it even further. You can try to:

    - Set up more logic that will cater for a wider array of email responses. 
    
    - Use a different bootstrapping template and see if you can reproduce the results.
    
    - Integrate more AWS service, for example see if you can integrate AWS QuickSight to visualise the data in your AWS DynamoDB NoSQL database.
