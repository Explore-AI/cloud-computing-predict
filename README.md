# Cloud Computing Predict

#### EXPLORE Data Science Academy Cloud Computing Predict
## Overview

In this predict you will make use of Python and AWS to create an intelligent data science portfolio website. At a high-level, the website will be hosted in a serverless manner on AWS; showcasing your amazing data science, machine learning and AI projects. 

<p align="center">
  <img src="https://github.com/Explore-AI/Pictures/blob/master/ezgif.com-gif-maker.gif?raw=true"/>
</p>

This predict will not only teach you the valuable skill of setting up and consuming AWS services to host a website, but it will also teach you how to use these services in creating an intelligent NLP service. This NLP solution will allow you to automatically populate and send intelligent emails to interested parties based on the messages they send to you through the website. For example, if a potential recruiter sees a particular portfolio project on your website that interests them and contacts you regarding the said project, it is possible to set up your NLP bot to pick up what the tone and key phrases are in the recruiter's message. Some smart programming techniques can then be used to automatically send a response. 

<p align="center">
  <img src="https://raw.githubusercontent.com/Explore-AI/Pictures/master/serverless_predict_process.PNG"/>
    <br>
    <em>Figure 1: Cloud Computing Predict System Overview</em>
</p>


In **Figure 1** the solutions architecture of this predict is depicted. Below follows a brief description of each module in the system:

>- [x] **[GitHub Template Repo:](https://github.com/)** A dedicated EXPLORE template repo which houses all the content and instructions for the student to complete the Predict. 
>
>- [x] **[AWS Lambda:](https://aws.amazon.com/lambda/)** A serverless compute instance responsible for multiple processing steps:
>      - Stores the enquiry details within an AWS DynamoDB instance for later retrieval.
>      - Forwards the enquiry contents to AWS Comprehend to help formulate an intelligent response to the site visitor.
>      - Provides logic to formulate an intelligent response based on AWS Comprehend output.
>      - Upon successful completion of these tasks, invokes AWS SES to send emails to the website enquirer and an automated marking email address hosted by EDSA.
>      
>- [x] **[AWS Amplify:](https://aws.amazon.com/amplify/)** Responsible for serving the static web content hosted in GitHub which becomes the basis of the student web page.
>
>- [x] **[Amazon DynamoDb:](https://aws.amazon.com/dynamodb/)** A NoSQL database responsible for storing enquiry details from individuals visiting the student webpage.
>
>- [x] **[Anazon SES:](https://aws.amazon.com/ses/)** A code-driven email service responsible for returning an intelligent response to webpage visitors based upon their enquiries.
>
>- [x] **[AWS API Gateway:](https://aws.amazon.com/api-gateway/)** AWS service responsible for receiving enquiry details via an API call from the student webpage, and for passing these on to the internal lambda function.
>
>- [x] **[AWS Comprehend:](https://aws.amazon.com/comprehend/)** An intelligent NLP  service capable of characterising sentiment and extracting key-phrases from the ingested text. Used to detect topics within the received webpage enquiries.

## Predict Instructions

The completion of the predict involves nine distinct steps which follow on from one another sequentially. This means that you have to completely finish a particular step before you can move on to the next one.


Brief description of each step in the 9-step predict process:

  1. In the first step you will create a private fork of the EDSA Cloud-Computing template repo that stores all of the code needed to host your static website. 
    
  2. This step is all about customising the static website to suit your needs. You will use the provided bootstrap template and general guides to modify the look and contents of the website to fit your preferences. 
    
  3. In the third step you will use AWS Amplify to serve your modified website. We provide the initial steps to begin this process, and then leave the remainder of the task as an exercise for you to understand and complete. 
  
  4. This step involves the creation of an AWS DynamoDB NoSQL database. This database will be used to store website data as and when visitors send an enquiry. 
    
  5. Here you will create an IAM role that will give your AWS Lambda function (created in step 6) the required permissions to interact with AWS Comprehend, AWS SES, AWS DynamoDB and AWS API Gateway.
    
  6. In this step things get interesting. We set up the AWS Lambda function, Pandas and Numpy ARN layers and, AWS API Gateway trigger:
    
      - **The AWS Lambda Function** will be used to:
        - Write data to Amazon DynamoDB;
        - Generate intelligent email responses with Amazon Comprehend, and
        - Send emails with Amazon SES.

      - **Pandas and Numpy ARN:**
        - AWS Lambda runs Python on a Linux operating system. This means if we want to use popular libraries such as Pandas and Numpy in our lambda function, we need to configure our Linux environment accordingly. We can do this by adding layers to our lambda function. In the case of Pandas and Numpy, we will be adding the respective layers for each library to our Linux environment.

      - **The AWS API Gateway trigger** configures a publicly accessible HTTP API which listens for POST requests from the webpage. When a request is received, its content is parsed and used to invoke the connected lambda function.   
    
  7. In step seven you will need to configure the Lambda function created previously to write incoming data from the website to the DynamoDB database created in step four.
    
  8. This step involves the configuration of the AWS SES service so that your pipeline can send emails automatically with the help of a Lambda function.
    
  9. In this final step you will be required to complete the NLP portion of the predict with the use of AWS Comprehend and by defining additional program logic. At a high level, AWS Comprehend will be used to extract sentiment and key phrases from a message sent from your static website. Using programming logic, you will then define several helper methods and functions which will enable the population of an automated response if the extracted key phrases and sentiment align to specific operating conditions. 
  
### 1) Fork the Provided Template Repository

We have already set up a repository with all the requisite files and instructions that you need to successfully complete this predict. The template repo that you need to fork can be found [here](). If you have any trouble forking a repo, you might find [this link](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/duplicating-a-repository) helpful.


### 2) Modify the Portfolio Webpage Template

Step two in the process is where you will create your website and add your relevant data science and machine learning portfolio projects. For this step we will provide you with a baseline template which you can change as you please. 

Below follows a brief description of the files in the bootstrap template:

| Folder           | File Name                | Description      |
| ---------------- | ----------------         | ---------------- |
| Assets/mail    | contact_me.js            | Contains all the code required to send the data from the filled website form through the defined endpoint to the AWS Lambda function    |
| Assets/mail    | jqBootstrapValidation.js | This JavaScript file is used to check if the data entered in the form on the website is in the correct format. If the data is in the expected format and the endpoint is in place the message will be sent. If not, an error message will be displayed prompting the user to input the correct information.    |
| Assets/img     | n/a                      | This folder contains all the images used within the website.                    |
| css            | style.css                | Here the CSS file is kept that controls the style i.e. look and feel of your website    |
| js             | scripts.js               | Other content    |
| N/A            | index.html               | The index.html is used to define your static web page. This is the file that you will mostly be working with when creating your website.      |



**Steps to modify the provided bootstrap template to make the static website your own:**

  I. Open the `index.html` file with an editor of your choice i.e. Pycharm, Brackets, VS Code, etc. and customise the website according to your preference. You can find some general guidance of what to change by reading the code comments we have placed for you. Here is an example comment that you can expect to find in the `index.html` file:  
 
```html
  <!-- ========= CUSTOMISE SECTION =========== -->
  <!-- This comment instructs you what to change and how to change it -->
  <!-- ======================================= --> 
```

| :zap: WARNING :zap:                                                                                     |
| :--------------------                                                                                   |
| While you are free to modify many aspects of the webpage, you should **NOT** alter its functioning. Do not add/remove any fields from the form section, nor modify the variable names captured by the contact_me.js script  | 
 
 II. Once you've modified the bootstrap template according to your preference, you can move to the next step. Here you will get your hands dirty serving the static website with the help of AWS Amplify :)
 
 

 
### 3) Serve Static Web Page on AWS Amplify

To serve the static website, you will make use of the AWS Amplify service. As mentioned before, AWS Amplify simplifies the process of web development by providing a serverless framework which removes the need to worry about a running webserver or underlying hosting infrastructure. Below are the step-by-step instructions required to host your beautiful portfolio website:

  
  I. The first step is to log in to the AWS Management Console and navigate to the [AWS Amplify](https://aws.amazon.com/amplify/) service. 
  
| :information_source: NOTE :information_source:                                                                                                    |
| :--------------------                                                                                                                             |
| *Take note of which AWS region you have selected for the AWS Amplify service. When spinning up new AWS services from here on out, it is advised that all of your services reside in the same region*|
  
  II. Once you have located AWS Amplify in the console, select `Get Started`.

<p align="center">
  
<img src="https://raw.githubusercontent.com/Explore-AI/Pictures/master/Amp-1.PNG" style="width:500px;" />
  <br>
  <em>Figure 2: Get started with AWS Amplify</em>
  
</p>
  
  III. Select `Get Started` on the `Host Your Web App` menu:
  
  <p align="center">
  
  <img src="https://raw.githubusercontent.com/Explore-AI/Pictures/master/Amp-2.PNG" style="width:350px;"/>
    <br>
    <em>Figure 3: Host your web app</em>
  
  </p>
  
  
  IV. Next, you need to connect your GitHub repo created in section 1, containing the bootstrap template, with AWS Amplify. 
   
  <p align="center">
  
  <img src="https://raw.githubusercontent.com/Explore-AI/Pictures/master/Amp-3.PNG" style="width:500px;"/>
    <br>
    <em>Figure 4: Connect GitHub repo</em>
  
  </p>

  Note that if you have not already done so, you will be required to `authorise` GitHub to be able to access your public and private repositories. Upon successful authorisation (depicted in figure 5), leave all the settings as their defaults and click `'next'`.
  
  <p align="center">
  
  <img src="https://raw.githubusercontent.com/Explore-AI/Pictures/master/Amp-4.PNG" style="width:500px;"/>
    <br>
    <em>Figure 5: Authorise GitHub</em>
  
  </p>

  V. Finally, initiate the hosting of your webpage by clicking on `'deploy'` on the following screen. 
  
| :information_source: NOTE :information_source:                                                                                                    |
| :--------------------                                                                                                                             |
| By this point in the process your modified website should be up and running through the AWS Amplify service with a sample domain name: `branch_name.reference_number.amplifyapp.com`. You can view an example of the fully functioning website deployed with AWS Amplify [here](https://main.dajjrrhheaglb.amplifyapp.com/)|
  

### 4) Create DynamoDb Database


Within the proposed system, a database is required that will store all the data sent from the serverless hosted website. For this predict, you will be using the AWS DynamoDB NoSQL database for this purpose. The following steps will help you set this service up within the AWS: 


  I. Navigate to the AWS DynamoDb service via the AWS Management Console
  
  
  II. On the DynamoDB `Dashboard` select `Create Table`.

  <p align="center">
  <img src="https://raw.githubusercontent.com/Explore-AI/Pictures/master/db-1.PNG" style="width:550px;"/>
    <br>
    <em>Figure 6: Create a DynamoDB table</em>
  </p>
  
  III. Give your table a relevant name, for example, `my-portfolio-data-table`
  
  IV. In the `Primary Key` field insert `ResponsesID` and set the type to number.
  
  <p align="center">
  <img src="https://raw.githubusercontent.com/Explore-AI/Pictures/master/db-2.PNG" style="width:550px;"/>
    <br>
    <em>Figure 7: Create a DynamoDB table</em>
  </p>  
  
  V. Click on `Create`.
  
  VI. Select the table you just created from the side panel,  and under the `Items` tab,  click on `Create Item`.
  
  <p align="center">
  <img src="https://raw.githubusercontent.com/Explore-AI/Pictures/master/db-3.PNG" style="width:750px;"/>
    <br>
    <em>Figure 8: Add new items and their data types to created table</em>
  </p>  
  
  VII. Set an initial index by entering the number 100 in the `ResponsesID` field. (Note that this field represents a unique primary key that will be generated within the Lambda function upon its execution)
  
  VIII. Click on the `+` icon and select `insert - number`. Name this item `Cell`. Enter `0123456789` in the Value field.
  
  IX. Click on the `+` icon and select `insert - string`. Name this item `Email`. Enter `student@explore-ai.net` in the Value field.
  
  X. Click on the `+` icon and select `insert - string`. Name this item `Message`. Enter `Empty Message` in the Value field.

  XI. Click on the `+` icon and select `insert - string`. Name this item `Name`. Enter `Student` in the value field.
  
  <p align="center">
  <img src="https://raw.githubusercontent.com/Explore-AI/Pictures/master/db-4.PNG" style="width:1000px;"/>
    <br>
    <em>Figure 9: Final populated table after following steps VIII - XI.</em>
  </p>   
  
  XII. Store the table entry by clicking on `Save`.
  
  XIII. Select the created table and navigate to the `Overview` tab.
  
  XIV. Scroll down and note your Amazon Resource Name (ARN)	for the created table. *Save this for later use in the IAM policy creation steps*.
  
### 5) Create the Lambda IAM Role and Attach the Required Policies

  
An IAM role is needed to give the system's Lambda function access to relevant AWS services. In total you need to create four policies for this IAM Role:

 | **Policy** | **Description** |
 |------------|-------------|
 |**AWS Comprehend Policy** | Allows the Lambda function to call AWS Comprehend in order calculate a sentiment score and extract key phrases from received text entered on the website. |
 |**AWS SES Policy** | Allows the Lambda function to invoke the AWS SES service in order to send automated responses via email. |
 |**AWS Basic Lambda Execution Policy** | Grants the Lambda function permission to access AWS services and resources. |
 |**AWS DynamoDB Policy** | Gives the Lambda function write permissions in order to store data from the website to a designated (existing) AWS DynamoDB table. |


The following steps can be followed to create an IAM Role for the Lambda function, and to attach each requisite policy to it  
  
  I. Navigate to the IAM service in the AWS Management Console and on the `Roles` tab select `Create Role`
  
  II. From there select `Lambda` under the common use cases. Next click on the `Next Permission` button.

  
- AWS Comprehend, SES and Basic Lambda Execution IAM Policy:

  
      - In the search box type in `ComprehendFullAccess` and check the select box. 
      

      - In the search box type in `AmazonSESFullAccess` and check the select box.
      

      - In the search box type in `AWSLambdaBasicExecutionRole` and check the select box.
      
     
      -  Once you have attached the three above mentioned policies you can click on `Attach policy`.
      

- AWS DynamoDb IAM Policy:     

   
      - On the `Roles` tab navigate to the IAM role created in the step above.
      

      - Select the role and click on `Add inline policy`.
      
      
      - Select `Choose a service` and in the search box type `DynamoDb` 
      
      
      - Under `Actions` check the `Write` checkbox.
      
      
      - Under `Resources/table` select `Add ARN`
      
      
      - Within the `Specify ARN for table` text box, insert the ARN noted in step 4.
      
      
      - Click `add`, click review policy
      
      
      - Give the inline policy a relevant name and select `Create policy`
      
  <p align="center">
  <img src="https://raw.githubusercontent.com/Explore-AI/Pictures/master/iam-4.PNG" style="width:1000px;"/>
    <br>
    <em>Figure 10: AWS DynamoDB IAM Role</em>
  </p>  
      
    
  
### 6) Set-up the Initial AWS Lambda Function and the AWS API Gateway Trigger
  
In this step you will set up the AWS API Gateway and the AWS Lambda function. This will be a three-part process.

#### Part 1: Lambda Initialisation

Part 1 involves creating the AWS Lambda Function with a Python 3.7 runtime. You will also attach the IAM role created within step 5 to govern the lambda function's access control.
  
  I. Navigate to the AWS Lambda service via the AWS Management Console.
  
  II. Once there, under functions, click `Create function`.
  
  III. Select `Author from scratch` and give your function a relevant name (e.g. model-solution-cloud-computing-predict).
  
  <p align="center">
  <img src="https://raw.githubusercontent.com/Explore-AI/Pictures/master/lam-1.PNG" style="width:550px;"/>
    <br>
    <em>Figure 11: Created lambda function</em>
  </p>  
  
  IV. Under `runtime` select `Python 3.7`.
  
  V. Under `Change default execution role` select `Use an existing role`.
  
  VI. Select the IAM role created in step 5.
  
  VII. Click `Create function`.
  
#### Part 2: Layer Addition

The objective of part 2 is to add two layers to the generated lambda function - one Pandas layer and one Numpy layer. You need to add these layers so that the Pandas and Numpy libraries can be used in the building of your solution i.e. the Python code telling the lambdas function what to do.
 
  I. Under `layers` click add layer.
  
  II. Select `Specify an ARN`.
  
  III. Get the correct Numpy and Pandas layers for your region and Python version from [this table](https://github.com/keithrozario/Klayers/blob/master/deployments/python3.7/arns/eu-west-1.csv)
  
  <p align="center">
  <img src="https://raw.githubusercontent.com/Explore-AI/Pictures/master/lam-4.PNG" />
    <br>
    <em>Figure 12: Numpy and Pandas layers in lambda function</em>
  </p> 
  

#### Part 3: API Gateway Creation

The final part within step 6 is to create an AWS API Gateway endpoint and to set this as your lambda's function trigger. At a high level, this gateway is responsible for interfacing between your deployed website (running from AWS Amplify) and the lambda function you have created - invoking the lambda when the gateway receives an API call (HTTP POST request sent by the webpage) and passing through its data payload to the function. This process sets off a chain of programmatic events which ultimately will generate and send your intelligent email automatically.   

From your lambda function overview, do the following: 

  I. Select `add trigger`.
  
  II. Under `Trigger configuration`, select `API Gateway`.
  
  III. Under `API Type` select `HTTP API`.
  
  IV. Under `Security` select `open`.
  
  V. Under `Additional Settings` check the `CORS` checkbox.
  
  VI. Click add.
  
  <p align="center">
  <img src="https://raw.githubusercontent.com/Explore-AI/Pictures/master/lam-2.png" style="width:501px;"/>
    <br>
    <em>Figure 13: Properties of the created API Gateway</em>
  </p> 


  VII. Copy the `API endpoint` address under the configured trigger.
  
  VIII. Navigate to the `contact_me.js` file in your GitHub repo created in step 1, and replace the default API URL string with the one copied in the previous step.
  
  <p align="center">
  <img src="https://raw.githubusercontent.com/Explore-AI/Pictures/master/lam-3.PNG" style="width:500px;"/>
    <br>
    <em>Figure 14: Configuring the AWS API Gateway URL within the `contact_me.js` endpoint.</em>
  </p> 
  
  IX. Commit the changes to your remote repo and wait for the branch to be redeployed by AWS Amplify.
  

| :information_source: NOTE :information_source:                                                                                                    |
| :--------------------                                                                                                                             |
| By this point in the process your website should enable you to fill out the form with the appropriate information and, upon submission, you should receive the `Your message has been sent` notification. |
  

### 7) AWS Lambda Function for Writing to DynamoDB

You are now at a point in the predict where you can start building the actual lambda functionality. Initially you will start off with the simple task of using the AWS Lambda + API Gateway to write the data coming from the website form to the previously created DynamoDB database. If needed, you can familiarise yourself with the overall process as represented within **figure 1**.

  <p align="center">
  <img src="https://raw.githubusercontent.com/Explore-AI/Pictures/master/cloud-computing-predict-dynamodb.gif" />
    <br>
    <em>Figure 15: Lambda writing data from the website to DynamoDB</em>
  </p> 


*Below follows the code required to get the desired output from the lambda function. Make sure this code is sitting in the `lambda_function.py` file under the main directory within the browser-based AWS Lambda IDE (the main directory will typically have the same name as your created lambda function).*


```python
import boto3    # Python AWS SDK
import json     # Used for handling API-based data
import base64   # Needed to decode the incoming POST data
import random.randint   # Used to generate DynamoDB key values

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
    # Create a random variable that can take a value between 1 and 1 000 000 000. This variable will be used as our key value i.e the ResponsesID
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

In this step you will setup AWS Simple Email Service (SES), to programmatically send emails when required. This is a two-part process: 

 - The first part entails the verification of email addresses for the sending and receiving of messages generated by SES. 
 - The second part sees you configure the lambda function (i.e. `lambda_function.py`) to send emails to specified addresses when triggered by a POST request being received by the API gateway.      
   
#### Part 1: Verify your Email with Amazon SES:

When using Amazon SES for the first time, all accounts start out in sandbox mode. This is to prevent new accounts from abusing the service and sending out spam emails. In sandbox mode the following restrictions apply:

 - You can only send mail to verified email addresses and domains, or to the [Amazon SES mailbox simulator](https://docs.aws.amazon.com/ses/latest/DeveloperGuide/send-email-simulator.html).

 - You can only send mail from verified email addresses and domains.

 - You can send a maximum of 200 messages per 24-hour period.

 - You can send a maximum of 1 message per second.
    
   
When your account is promoted out of the sandbox, you can send emails to any recipient, regardless of whether the recipient's address or domain is verified. However, you still have to verify all identities that you use as "From", "Source", "Sender", or "Return-Path" addresses.


| :information_source: NOTE :information_source:                                                                                                         |
| :--------------------                                                                                                                                  |
| You do not have to move your account out of Sandbox Mode complete the predict. However, for interest, to move out of sandbox mode you can follow [these](https://docs.aws.amazon.com/ses/latest/DeveloperGuide/request-production-access.html) instructions. |


The following steps will guide you in verifying your sender and recipient email addresses on the AWS SES console.

  I. Navigate to the AWS SES console with the AWS Management Console.
    
  II. On the AWS SES console select `Email Addresses`.
    
  III. Click on `Verify a New Email Address`
    
  <p align="center">
  <img src="https://raw.githubusercontent.com/Explore-AI/Pictures/master/ses-1.PNG" />
    <br>
    <em>Figure 16: Verify email with AWS SES</em>
  </p> 
  
  IV. In the textbox type the email address which you would like to use as your sender email address and click `Verify This Email Address`.
    
   <p align="center">
  <img src="https://raw.githubusercontent.com/Explore-AI/Pictures/master/ses-2.PNG" />
    <br>
    <em>Figure 17: Verify sender email with AWS SES</em>
  </p> 
  
  V. Go to your inbox and click on the link to verify your sender email address.
    
   <p align="center">
  <img src="https://raw.githubusercontent.com/Explore-AI/Pictures/master/ses-3.PNG" />
    <br>
    <em>Figure 18: Verified sender email address </em>
  </p>     
    
    
  VI. Repeat steps 1-5 for your recipient email address.
    
   
#### Part 2: Python Code that Sends an Email Via AWS SES:

Below is the code required to set up the email functionality with your AWS Lambda function. At this point, the process is:

  - Form is filled out on the website and posted to the API Gateway endpoint.
    
  - The data passes through the AWS API Gateway and triggers the AWS Lambda function.
    
  - The sender information is decoded.
    
  - The lambda function writes the data to the AWS DynamoDB database.
    
  - A sample message is populated.
    
  - The email address of the sender, found in the decoded information, is used as as recipient email address.
    
  - The sample message is sent from your verified email address to the verified recipient address via AWS SES.


The following Python script implements the above steps which are performed within the lambda function: 

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

    # Replace student@explore-ai.net below with your "From" address.
    # This address must be verified with Amazon SES.
    SENDER = 'student@explore-ai.net'
    
    # Use the form data to populate the recipient address. 
    # Note that If your account is still in the sandbox, 
    # the recipient address must be verified.
    RECIPIENT =  f"{dec_dict['email']}" 
    
    
    # The subject line for the email.
    SUBJECT = "Data Science Portfolio Project Website"
    
    # The email body for recipients with non-HTML email clients
    BODY_TEXT = (email_reply)

    # The character encoding for the email.
    CHARSET = "UTF-8"
    
    # Create a new SES resource.
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

In this final step you will be building out the predict's NLP functionality with the help of AWS Comprehend. The NLP functionality will enable you to extract the overwhelming sentiment (categorical variable) from a message,  as well as a list of key phrases as determined by AWS comprehend. With the sentiment information and a list of key phrases, you can build in intelligent, automated email responses into your AWS Lambda function. To help you thoroughly understand this section, we provide a three-part breakdown wherein we describe each key element involved in the formation of an intelligent response. 

The first part is the process description; where we go through the logic of how to use AWS comprehend to extract sentiment and key phrases. The second part covers the helper functions utilised; where we describe the two helper methods and the lambda function required to orchestrate an intelligent automated response. The final part is an end-to-end example; where we simulate what should be achieved once the entire AWS Lambda/AWS Comprehend/AWS SES integration is built.

#### Part 1: Process Description

At a high-level, the entire intelligent response process can be described as follow:

  1. The form is filled out on the website and sent. This form contains the following sender data:
     - `name`
     - `cellphone number`
     - `email address`, and
     - `message`.
  
  2. The data passes through the AWS API Gateway and triggers the AWS Lambda function.
  
  3. The sender data is decoded.
  
  4. The `message` is used in AWS Comprehend to extract the message sentiment and a dictionary of key phrases.
  
  5. A custom helper function finds the score and value of the most likely sentiment present in the message.
  
  6. Another helper function is used to convert the list of key phrases, generated by AWS Comprehend, to a numpy array. This array contains individual words present within the key phrase dictionary. This helper function also performs a lookup - producing a set of key phrases which match a custom list of keywords we wish to detect and reply to.  
  
  7. Having extracted the above data from the received message, the following email logic can be applied:
        
```python

if message_sentiment == 'Desired_Sentiment':
    
    if (AWS_Comprehend_Extracted_Words == Provided_List_of_Words):
        
        generate some personalised response based on message content
        
    else:
        
        generate some generic response based on message content
        
```

#### Part 2: Helper Function Descriptions


In this section we provide an overview of the helper functions required to send the intelligent, automated email responses. 

**Function 1 - `find_max_sentiment(Comprehend_Sentiment_Output):`**

This function extracts and returns the highest probable sentiment from a given message.
  - Input argument:
    - Comprehend_Sentiment_Output: Sentiment dictionary generated by AWS Comprehend.
  - Outputs:
    - overall_sentiment: A string representing the most probable sentiment within the message. 
    - sentiment_score: The value of the highest probable sentiment present in the message.


```python

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

    overall_sentiment = Comprehend_Sentiment_Output['Sentiment']

    print(sentiment_score, overall_sentiment)
    
    return overall_sentiment, sentiment_score

```           
**Function 2 - `key_phrase_finder(list_of_important_phrases, list_of_extracted_phrases):`**

This function attempts to find a match between the words in a key phrases dictionary produced by AWS Comprehend to a provided custom list of words. The result of the search is returned as a boolean variable.
  - Input arguments:     
    - list_of_important_phrases: A string-based list of words representing topics to be detected i.e. `['CV', 'data', 'science']`
    - list_of_extracted_phrases: An AWS Comprehend key phrases dictionary. 
  - Outputs: 
    - listing: An empty list to append the individual words present in the AWS Comprehend key phrases dictionary.
    - phrase_checker: A boolean variable representing the whether a match is discovered between the function's input lists.
            
```python

def key_phrase_finder(list_of_important_phrases, list_of_extracted_phrases):

    listing = []
    phrase_checker = None

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
    
        phrase_checker = True
        
    else:
        
        phrase_checker = False
    
    return listing, phrase_checker
```
    
**Function 3 - `email_response(name, email_address, critical_phrase_list, sentiment_list, sentiment_scores, list_of_extracted_phrases, AWS_Comprehend_Sentiment_Dump):`**
    
This function takes in the parsed information from the sender i.e. `name`, `email_address`, the `sentiment` and the `key phrases` output from AWS Comprehend, and a `list of critical phrases`, and uses the logic described in the 'Process Description' section to populate a email. 

  - Input arguments:     
    - name: The name of the requester.
    - email_address: The email address of the requester.
    - critical_phrase_list: A list of words that you want to match to the words in the AWS key phrases dictionary.
    - sentiment_list: A list of possible sentiments that a message could contain i.e. ['Positive', 'Negative', 'Neutral', 'Mixed'].
    - sentiment_scores: The sentiment score attached to each of the listed sentiments in the `sentiment_list` as determined by AWS Comprehend.
    - list_of_extracted_phrases: A list of the individual words present in the key phrases dictionary.
    - AWS_Comprehend_Sentiment_Dump: The sentiment summary dictionary as populated by AWS Comprehend.
  - Outputs: 
    - Text: The intelligently populated email response based on the contents of the sender's message.

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
    Phrase_Matcher_Article = key_phrase_finder(critical_phrase_list,  list_of_extracted_phrases)
    Matched_Phrases_Article = Phrase_Matcher_Article[0]
    Matched_Phrases_Checker_Article = Phrase_Matcher_Article[1]
    
    # Check for project phrases
    Phrase_Matcher_Project = key_phrase_finder(['github', 'git', 'Git', 'GitHub', 'projects', 'portfolio', 'Portfolio'],  list_of_extracted_phrases)
    Matched_Phrases_Project = Phrase_Matcher_Project[0]
    Matched_Phrases_Checker_Project = Phrase_Matcher_Project[1]
    
    # Check for C.V phrases
    Phrase_Matcher_CV = key_phrase_finder(['C.V', 'resume', 'Curriculum Vitae', 'Resume', 'CV'],  list_of_extracted_phrases)
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
        # CV, Article, Project
        if  ((Matched_Phrases_Checker_CV == True) & (Matched_Phrases_Checker_Article == True) & (Matched_Phrases_Checker_Project == True)):
            mytuple = (Greetings_text, CV_text, Article_Text, Project_Text, Farewell_Text)
            Text = "\n \n".join(mytuple)
            
        # CV, Project
        elif ((Matched_Phrases_Checker_CV == True) & (Matched_Phrases_Checker_Article == False) & (Matched_Phrases_Checker_Project == True)):
            mytuple = (Greetings_text, CV_text, Project_Text, Farewell_Text)
            Text = "\n \n".join(mytuple)
            
        # CV
        elif ((Matched_Phrases_Checker_CV == True) & (Matched_Phrases_Checker_Article == False) & (Matched_Phrases_Checker_Project == False)):
            mytuple = (Greetings_text, CV_text, Farewell_Text)
            Text = "\n \n".join(mytuple)
            
        # Article
        elif ((Matched_Phrases_Checker_CV == False) & (Matched_Phrases_Checker_Article == True) & (Matched_Phrases_Checker_Project == False)):
            mytuple = (Greetings_text, Article_Text, Farewell_Text)
            Text = "\n \n".join(mytuple)       
        # None    
        elif ((Matched_Phrases_Checker_CV == False) & (Matched_Phrases_Checker_Article == False) & (Matched_Phrases_Checker_Project == False)):
            mytuple = (Greetings_text, Farewell_Text)
            Text = "\n \n".join(mytuple)   
            
        # Project
        elif ((Matched_Phrases_Checker_CV == False) & (Matched_Phrases_Checker_Article == False) & (Matched_Phrases_Checker_Project == True)):
            mytuple = (Greetings_text, Project_Text ,Farewell_Text)
            Text = "\n \n".join(mytuple) 

        # CV, Article
        elif  ((Matched_Phrases_Checker_CV == True) & (Matched_Phrases_Checker_Article == True) & (Matched_Phrases_Checker_Project == False)):
            mytuple = (Greetings_text, CV_text, Article_Text, Farewell_Text)
            Text = "\n \n".join(mytuple)
        
        # Project, Article 
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

#### Part 3: End-to-end Example

In this section we will review a basic example of how an email response is generated with the full solution architecture.

Let's say you someone visiting your deployed webpage posts the following sample message using the form:

> Hi Explore Data Science Student,
>
> I love your website and your portfolio projects. I also had a look at your GitHub page and I am quite impressed with the quality of your work.
>
> Your medium articles also captured my attention.
>
> Could you please forward me your CV so that I can present you for a potential job at one of my clients. It is for a six month contract and I feel that your experience and skills match the job specifications perfectly.
>
> Thank you so much for your time.
> 
> Kind regards,
> 
> Joanne Liebenberg
> 
> Senior HR Manager, Real Analytics Resources

Running this message through our AWS Comprehend service produces [these](https://github.com/Vincent-EDSA/cloud-computing-predict/blob/main/Model_Solution_Python_Files/Example_AWS_Comprehend_Key_Phrases_Output.txt) key phrases and [this](https://github.com/Vincent-EDSA/cloud-computing-predict/blob/main/Model_Solution_Python_Files/Example_AWS_Comprehend_Sentiment_Output.txt) sentiment classification output.

From this output it can be seen that AWS Comprehend picked up that the message has a positive sentiment, and that it contains key phrases such as: 'your portfolio projects', 'your GitHub page', 'Your medium articles', 'a potential job', etc. We can therefore set up some logic along with our helper functions to build out our responses.

To define this logic, we start by providing some sample `string` replies that we can add to our email response if certain supplied words match the words in our AWS Comprehend key phrases dictionary. These sample replies can take the following form:

**1. Sample reply if a CV related word is matched**
    CV_text = 'I see that you mentioned my C.V in your message. I am happy to forward you my C.V in response. If you have any other questions or C.V related queries please do get in touch. '

**2. Sample reply if a portfolio project related word is matched**
    Project_Text = 'The projects I listed on my site only include those not running in production. I have several other projects that might interest you.'

**3. Sample reply if a Medium article related word is matched**
    Article_Text = 'In your message you mentioned my blog posts and data science articles. I have several other articles published in academic journals. Please do let me know if you are interested - I am happy to forward them to you.'
  
**4. Sample reply if the detected sentiment is negative**  
    Negative_Text = 'I see that you are unhappy in your response. Can we please set up a session to discuss why you are not happy, be it with the website, my personal projects or anything else. \n\nLooking forward to our discussion. \n\nKind Regards, \n\nMy Name'
 
**5. Sample reply if the detected sentiment is neutral** 
    Neutral_Text = 'Thank you for your email. Let me know if you need any additional information.\n\nKind Regards, \n\nMyName'
    
**6. Sample farewell reply** 
    Farewell_Text = 'Again, Thank you for your email.\n\nIf there is anything else I can assist you with please let me know and I will set up a meeting for us to meet in person.\n\nKind Regards, \n\nMyName'
    
    
With sample replies now defined, we can use conditional logic and string manipulation techniques to *build* up a response.

For instance, we define a `Phrase_Matcher_Project` variable that makes use of the `key_phrase_finder` function and passes a list of words that might be project related, for example `['github', 'git', 'Git', 'GitHub', 'projects', 'portfolio', 'Portfolio']`. 

If any of these words now match the extracted keywords in the Comprehend dictionary, the value of the `Phrase_Matcher_Project` variable will be `True`. We can then use an `if function` and string manipulation to add a greeting, the project text and the farewell text to an `email_reply` variable. In the example we've presented, this `email_reply` variable will take on the following form:

> Good day Joanne Liebenberg,
>
> The projects I listed on my site only include those not running in production. I have several other projects that might interest you.
> 
> Again, thank you for your email.
>
> If there is anything else I can assist you with please let me know and I will set up a meeting for us to meet in person.
>
> Kind Regards, 
>
> MyName

Remember that in the example additional keywords were present such as: `CV`, `projects`, `articles`, etc. We could therefore set up a CV, Project and Article phrase checker and use the same logic as discussed above to generate an intelligent automated response. The `email_response` variable would then take on the following value for the full example:

> Good day Joanne Liebenberg,
> 
> I see that you mentioned my C.V in your message. I am happy to forward you my C.V in response. If you have any other questions or C.V related queries please do get in touch. 
> 
> In your message you mentioned my blog posts and data science articles. I have several other articles published in academic journals. Please do let me know if you are interested - I am happy to forward them to you
> 
> The projects I listed on my site only include those not running in production. I have several other projects that might interest you.
> 
> Again, thank you for your email.
>
> If there is anything else I can assist you with please let me know and I will set up a meeting for us to meet in person.
>
> Kind Regards, 
>
> MyName
   
| :information_source: NOTE :information_source:                                                                                                         |
| :--------------------                                                                                                                                  |
| The lambda function for the full solution can be found [here](https://github.com/Vincent-EDSA/cloud-computing-predict/blob/main/Model_Solution_Python_Files/Aggregated_Lambda_Function.py) |


## Conclusion

If you followed the nine-step process described above correctly, you should now have a fully functioning portfolio website capable of sending intelligent email responses in an automated way. Congrats! 

Following the conclusion of this predict, you are free (and we encourage you) to tweak various aspects of the project to personalise it even further. Here are just a few ideas you can try:

    - Set up more logic that will cater for a wider array of email responses. 
    - Use a different [Bootstrap](https://getbootstrap.com/) template and see if you can reproduce the results of the project.
    - Integrate more AWS services. For example, see if you can integrate AWS QuickSight to visualize the data in your AWS DynamoDB NoSQL database. Alternatively, you could try to use the [AWS Lex](https://aws.amazon.com/lex/) service to place a chatbot on your profile page, adding another layer of intelligent interaction to engage potential clients.  
