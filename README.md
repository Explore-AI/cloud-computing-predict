# Cloud Computing Predict

#### EXPLORE Data Science Academy Cloud Computing Predict
## Overview

In this predict you will make use of Python and AWS to create an intelligent data science portfolio website. At a high-level, the website will be hosted in a serverless manner on AWS; showcasing your amazing data science, machine learning and AI projects. 

<p align="center">
  <img src="https://github.com/Explore-AI/Pictures/blob/master/ezgif.com-gif-maker.gif?raw=true"/>
</p>

This predict will not only teach you the valuable skill of setting up and consuming AWS services to host a website, but it will also teach you how to use these services in creating an intelligent Natural Language Processing (NLP) service. This NLP solution will allow you to automatically populate and send intelligent emails to interested parties based on the messages they send to you through the website. For example, if a potential recruiter sees a particular portfolio project on your website that interests them and contacts you regarding the said project, it is possible to set up your NLP component to pick up what the tone and key phrases are in the recruiter's message. Some smart programming techniques can then be used to automatically send a response. 

<p align="center">
  <img src="https://raw.githubusercontent.com/Explore-AI/Pictures/master/serverless_predict_process.PNG"/>
    <br>
    <em>Figure 1: Cloud Computing Predict System Overview</em>
</p>


In **Figure 1** the solutions architecture of this predict is depicted. Below follows a brief description of each module in the system:

>- [x] **[GitHub Template Repo:](https://github.com/)** This dedicated EXPLORE template repo which houses all the content and instructions for a student to complete the Predict. 
>
>- [x] **[AWS Lambda:](https://aws.amazon.com/lambda/)** A serverless compute instance responsible for multiple processing steps:
>      - Stores the enquiry details within an AWS DynamoDB instance for later retrieval.
>      - Forwards the enquiry contents to AWS Comprehend to help formulate an intelligent response to the site visitor.
>      - Provides logic to formulate an intelligent response based on AWS Comprehend output.
>      - Upon successful completion of these tasks, invokes AWS SES to send emails to the website enquirer and an automated marking email address hosted by EDSA.
>      
>- [x] **[AWS Amplify:](https://aws.amazon.com/amplify/)** Responsible for serving the static web content hosted in GitHub which becomes the basis of the student web page.
>
>- [x] **[Amazon DynamoDB:](https://aws.amazon.com/dynamodb/)** A NoSQL database responsible for storing enquiry details from individuals visiting the student webpage.
>
>- [x] **[Anazon SES:](https://aws.amazon.com/ses/)** A code-driven email service responsible for returning an intelligent response to webpage visitors based upon their enquiries.
>
>- [x] **[AWS API Gateway:](https://aws.amazon.com/api-gateway/)** AWS service responsible for receiving enquiry details via an API call from the student webpage, and for passing these on to the internal lambda function.
>
>- [x] **[AWS Comprehend:](https://aws.amazon.com/comprehend/)** An intelligent NLP  service capable of characterising sentiment and extracting key-phrases from the ingested text. Used to detect topics within the received webpage enquiries.

## Predict Instructions

The completion of the predict involves nine distinct steps which follow on from one another sequentially. This means that you have to completely finish a particular step before you can move on to the next one.


Brief description of each step in the 9-step predict process:

  [Step 1:](#1_section_id) In the first step you will create a **private** fork of this repo (EDSA Cloud-Computing template repo) that stores all of the code needed to host your static website. 
    
  [Step 2:](#2_section_id) This step is all about customising the static website to suit your needs. You will use the provided bootstrap template and general guides to modify the look and contents of the website to fit your preferences. 
    
  [Step 3:](#3_section_id) In the third step you will use AWS Amplify to serve your modified website. We provide the initial steps to begin this process, and then leave the remainder of the task as an exercise for you to understand and complete. 
  
  [Step 4:](#4_section_id) This step involves the creation of an AWS DynamoDB NoSQL database. This database will be used to store website data as and when visitors send an enquiry. 
    
  [Step 5:](#5_section_id) Here you will create an IAM role that will give your AWS Lambda function (created in step 6) the required permissions to interact with AWS Comprehend, AWS SES, AWS DynamoDB and AWS API Gateway.
    
  [Step 6:](#6_section_id) In this step things get interesting. We set up the AWS Lambda function, a Numpy ARN layer, and an AWS API Gateway trigger:
    
   - **The AWS Lambda Function** will be used to:
        - Write data to Amazon DynamoDB;
        - Generate intelligent email responses with Amazon Comprehend, and
        - Send emails with Amazon SES.

   - **Numpy ARN:**
        - AWS Lambda runs Python on a Linux operating system. This means if you want to use popular libraries such as Numpy in your lambda function, you need to configure your Linux environment accordingly. You can do this by adding layers to your lambda function. In the case of Numpy, you will be adding the relevant layer to your Linux environment.

   - **The AWS API Gateway trigger** configures a publicly accessible HTTP API which listens for POST requests from the webpage. When a request is received, its content is parsed and used to invoke the connected lambda function.   
    
  [Step 7:](#7_section_id) In step seven you will need to configure the Lambda function created previously to write incoming data from the website to the DynamoDB database created in step four.
    
  [Step 8:](#8_section_id) This step involves the configuration of the AWS SES service so that your pipeline can send emails automatically with the help of a Lambda function.
    
  [Step 9:](#9_section_id) In this final step you will be required to complete the NLP portion of the predict with the use of AWS Comprehend and by defining additional program logic. At a high level, AWS Comprehend will be used to extract sentiment and key phrases from a message sent from your static website. Using programming logic, you will then define several helper methods and functions which will enable the population of an automated response if the extracted key phrases and sentiment align to specific operating conditions. 

---
### 1) Fork the Template Repository <a id='1_section_id'></a>
---

This repository acts as a resource containing all the requisite files and instructions that you need to successfully complete this predict. To continue development and before you can move on to the following steps, you need to create a private fork of this repo using your own GitHub profile.

If you have any trouble forking the repo, you might find [this link](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/duplicating-a-repository) helpful.

| :zap: WARNING :zap:                                                                                     |
| :--------------------                                                                                   |
| This predict represents an individual project. As such when forking this repo, you need to ensure that it is hosted *privately* within your GitHub account, free from collaboration form your peers or access from the public.| 

---
### 2) Modify the Portfolio Webpage Template <a id='2_section_id'></a>
---

Step two in the process is where you will create your website and add your relevant data science and machine learning portfolio projects. For this step we will provide you with a baseline template which you can change freely in certain areas. 

Below follows a brief description of the files in the bootstrap template:

| Folder           | File Name                | Description      |
| ---------------- | ----------------         | ---------------- |
| Assets/mail    | contact_me.js            | Contains all the code required to send data from the filled website form through the defined endpoint to the AWS Lambda function    |
| Assets/mail    | jqBootstrapValidation.js | This JavaScript file is used to check if data entered in the contact form on the website is in the correct format. If the data is in the expected format, the script will attempt to send this to a specified URL endpoint. If the data is in an incorrect format, an error message will be displayed prompting the user to input the correct information.    |
| Assets/img     | n/a                      | This folder contains all the images used within the website.                    |
| css            | style.css                | This CSS (Cascading Style Sheets) file is responsible for controlling the style i.e. look and feel of the website    |
| js             | scripts.js               | Various scripts to increase the responsiveness and utility of the website.    |
| Project root            | index.html               | This file defines your static web page, and will be worked on when personalising the website to meet your preferences.   |

| :triangular_flag_on_post: PREDICT TASK :triangular_flag_on_post:                                                                                      |
| :--------------------                                                                                   |
| In this section of the predict you are tasked with **modifying the static website template so that it represents your unique blend of technical skills**. Below you will find some helpful tips that might come handy during this website design/modification journey.  | 

**Steps to modify the provided bootstrap template to make the static website your own:**

  I. Open the `index.html` file with an editor of your choice i.e. Pycharm, Brackets, VS Code, etc. and customise the website according to your preference. You can find some general guidance of what to change by reading the code comments we have placed for you. Here is an example comment that you can expect to find in the `index.html` file:  
 
```html
  <!-- ========= CUSTOMISE SECTION =========== -->
  <!-- This comment instructs you on what to change and how to change it -->
  <!-- ======================================= --> 
```

| :zap: WARNING :zap:                                                                                     |
| :--------------------                                                                                   |
| While you are free to modify many aspects of the webpage, you should **NOT** alter its functioning. Do not add/remove any fields from the form section, nor modify the variable names captured by the `contact_me.js` script  | 
 
 II. Once you've modified the bootstrap template according to your preference, you can move to the next step. Here you will get your hands dirty serving the static website with the help of AWS Amplify :)
 

---  
### 3) Serve Static Web Page on AWS Amplify <a id='3_section_id'></a>
---

To serve your static website, you will make use of the AWS Amplify service. As mentioned before, AWS Amplify simplifies the process of web development by providing a serverless framework which removes the need to worry about a running webserver or underlying hosting infrastructure.


| :triangular_flag_on_post: PREDICT TASK :triangular_flag_on_post:                                                                                      |
| :--------------------                                                                                   |
| In this section of the predict you again get the chance to showcase your cloud computing skills. You are tasked with using AWS Amplify to serve your modified website in a serverless manner. 

Here it is important to **serve your website with AWS Amplify via your GitHub repository**. That way, when you make any changes to the files sitting in the `deployed` branch, AWS Amplify will automatically pick up the branch changes and re-deploy your website. | 

  
| :information_source: NOTE :information_source:                                                                                                    |
| :--------------------                                                                                                                             |
| By this point in the process your modified website should be running through the AWS Amplify service with a sample domain name: `branch_name.reference_number.amplifyapp.com`. You can view an example of the fully functioning website deployed with AWS Amplify [here](https://main.dajjrrhheaglb.amplifyapp.com/)|


---
### 4) Create DynamoDb Database <a id='4_section_id'></a>
---

  
Within the proposed system, a database is required that will store all the data sent from the serverless hosted website. For this predict, you will be using the AWS DynamoDB NoSQL database for this purpose. 

The data sent from the website will have the following schema:

> | Variable Name    | Variable Data Type | VariableDescription |
> | ---------------- | ----------------   |  ----------------   |
> | Name             | String             |  Name of the person filling out the form on the website                   |
> |                  |                    |                     |
> | Email Address    | String             |  Email address of the person filling out the form on the website          |
> |                  |                    |                     |
> | Phone Number     | Integer            |  Phone number of the person filling out the form on the website           |
> |                  |                    |                     |
> | Message          | String             |  Message to you from the person filling out the website form              |
> |                  |                    |                     |


We will create an additional parameter called `ResponsesID`.

> | Variable Name    | Variable Data Type | VariableDescription |
> | ---------------- | ----------------   |  ----------------   |
> | ResponsesID      | Integer            | Primary key used to identify reponse instance      |

The following steps will help you set this service up within the AWS ecosystem:
  
  I. Navigate to the AWS DynamoDb service via the AWS Management Console
  
  II. On the DynamoDB `Dashboard` select `Create Table`.

  <p align="center">
  <img src="https://raw.githubusercontent.com/Explore-AI/Pictures/master/db-1.PNG" style="width:550px;"/>
    <br>
    <em>Figure 2: Create a DynamoDB table</em>
  </p>
  
  III. Give your table a relevant name, for example, `my-portfolio-data-table`. Store this name for use in later stages of the predict.
  
  IV. In the `Primary Key` field insert `ResponsesID` and set the type to number.
  
  <p align="center">
  <img src="https://raw.githubusercontent.com/Explore-AI/Pictures/master/db-2.PNG" style="width:550px;"/>
    <br>
    <em>Figure 3: Create a DynamoDB table</em>
  </p>  
  
  V. Click on `Create`.
  
  VI. Select the table you just created from the side panel,  and under the `Items` tab,  click on `Create Item`.
  
  <p align="center">
  <img src="https://raw.githubusercontent.com/Explore-AI/Pictures/master/db-3.PNG" style="width:750px;"/>
    <br>
    <em>Figure 4: Add new items and their data types to created table</em>
  </p>  
  
  VII. Set an initial index by entering the number '100' in the `ResponsesID` field. (Note that this field represents a unique primary key that will be generated within the Lambda function upon its execution)
  
  VIII. Click on the `+` icon and select `insert - number`. Name this item `Cell`. Enter `0123456789` in the Value field.
  
  IX. Click on the `+` icon and select `insert - string`. Name this item `Email`. Enter `student@explore-ai.net` in the Value field.
  
  X. Click on the `+` icon and select `insert - string`. Name this item `Message`. Enter `Empty Message` in the Value field.

  XI. Click on the `+` icon and select `insert - string`. Name this item `Name`. Enter `Student` in the value field.
  
  <p align="center">
  <img src="https://raw.githubusercontent.com/Explore-AI/Pictures/master/db-4.PNG" style="width:1000px;"/>
    <br>
    <em>Figure 5: Final populated table after following steps VIII - XI.</em>
  </p>   
  
  XII. Store the table entry by clicking on `Save`.
  
  XIII. Select the created table and navigate to the `Overview` tab.
  
  XIV. Scroll down and note your Amazon Resource Name (ARN)	for the created table. *Save this for later use in the IAM policy creation steps*.
  
--- 
### 5) Create an IAM Role <a id='5_section_id'></a>
---

In step 5 you once again get the chance to show off your cloud computing skills. This predict involves using *a lot* of AWS services, and as such we need a comprehensive IAM Role that will adequately govern the access and authority of the AWS Lambda function. In this predict you will make use of the following services:

    - AWS Lambda
    
    - AWS API Gateway
    
    - AWS Comprehend
    
    - AWS SES
    
    - AWS DynamoDB
   
  
You therefore need an IAM role to give the Lambda function the required access to the various services that we will be using in this predict. In total, you need to create four policies for this IAM Role:

 | **Policy** | **Description** |
 |------------|-------------|
 |**AWS Comprehend Policy** | Allows the Lambda function to call AWS Comprehend in order calculate a sentiment score and extract key phrases from received text entered on the website. |
 |**AWS SES Policy** | Allows the Lambda function to invoke the AWS SES service in order to send automated responses via email. |
 |**AWS Basic Lambda Execution Policy** | Grants the Lambda function permission to access AWS services and resources. |
 |**AWS DynamoDB Policy** | Gives the Lambda function write permissions in order to store data from the website to a designated (existing) AWS DynamoDB table. |

| :triangular_flag_on_post: PREDICT TASK :triangular_flag_on_post:                                                                                      |
| :--------------------                                                                                   |
| You are tasked with **using the AWS IAM service to set up the necessary policies as described above**. It is important to remember that the DynamoDB policy will be of type inline, and that you will need to use the specific DynamoDB table ARN associated with the table you created in [Step 4](#4_section_id) to appropriately set up this policy.| 


---
### 6) Set-up the Initial AWS Lambda Function and the AWS API Gateway Trigger <a id='6_section_id'></a>
---
  
In this step you will set up the AWS API Gateway and the initial AWS Lambda function. This will be a three-part process:

| :triangular_flag_on_post: PREDICT TASK :triangular_flag_on_post:                                                                                      |
| :--------------------                                                                                   |
| Below is a brief description of the required three part process. You are, however, tasked with executing the three parts and little-to-no additional guidance will be give here. This is because, setting up an AWS Lambdas function is a key outcome of this course and should be something you are very familiar with by this time.| 


#### Part 1: Lambda Initialisation

Part 1 involves creating the AWS Lambda Function with a Python 3.7 runtime. You will also attach the IAM role created within step 5 to govern the lambda function's access control.
  
  
#### Part 2: Layer Addition

In part 2, the objective is to add an ARN  layer to the generated lambda function - one for Numpy. You need to add this layer so that you may use the Numpy library building your solution i.e. the Python code telling the lambdas function what to do. Remember these layers are `region` and `runtime` specific. Find your relevant ARN [here](https://github.com/keithrozario/Klayers).
 
#### Part 3: API Gateway Creation

The final part within step 6 is to create the AWS API Gateway and set this endpoint as your lambda's function trigger. At a high level, this gateway is responsible for interfacing between your deployed website (running from AWS Amplify) and the lambda function you have created - invoking the lambda when the gateway receives an API call (HTTP POST request sent by the webpage) and passing through its data payload to the function. This process sets off a chain of programmatic events which ultimately will generate and send your intelligent email automatically.

Your API should have the following characteristics: 
 - **API Type**: HTTP.
 - **Supported Method**: POST.
 - **Utilised Authorization**: None.
 - **[Cross-origin resource sharing (CORS)](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS)**: Enabled.
 - **Detailed billing**: Disabled.

Once you have created the API Gateway, you should replace the URL of the endpoint in your `contact_me.js` file to your specific endpoint URL. The following steps might help you in your endeavour. 

 
  I. Note the `API endpoint` address under the configured trigger.
  
  II. Use this API and navigate to the `contact_me.js` file in your GitHub repo created in step 1.
  
  <p align="center">
  <img src="https://raw.githubusercontent.com/Explore-AI/Pictures/master/lam-3.PNG" style="width:500px;"/>
    <br>
    <em>Figure 6: Created API Gateway</em>
  </p> 
  
  III. Replace the existing API URL with your API endpoint.
  
  IV. Commit the changes and wait for the branch to be redeployed by AWS Amplify.
  
  
| :information_source: NOTE :information_source:                                                                                                    |
| :--------------------                                                                                                                             |
| By this point in the process your website should enable you to fill out the form with the appropriate information and, upon submission, you should receive the `Your message has been sent` notification. |
  
---
### 7) AWS Lambda Function for Writing to DynamoDB <a id='7_section_id'></a>
---

You are now at a point in the predict where you can start building the actual lambda functionality. Initially you will start off with the simple task of using the AWS Lambda + API Gateway to write the data coming from the website form to the previously created DynamoDB database. If needed, you can familiarise yourself with the overall process as represented within **figure 1**.

  <p align="center">
  <img src="https://raw.githubusercontent.com/Explore-AI/Pictures/master/cloud-computing-predict-dynamodb.gif" />
    <br>
    <em>Figure 7: Lambda writing data from the website to DynamoDB</em>
  </p> 


| :triangular_flag_on_post: PREDICT TASK :triangular_flag_on_post:                                                                                      |
| :--------------------                                                                                   |
| **Set up the lambda function to write the website POST data to DynamoDB**. To get the functionality displayed in figure 7, you will need to use Python to tell your AWS Lambda function what to do and how to do it. Luckily we have some stater code for you. You can use the code found [here](student_solution_files/basic_lambda_data_decoding.py) to read and decode the incoming data from the website. Then, using the boilerplate code found [here](student_solution_files/write_data_to_dynamodb.py) as starting point, you can enable your lambda function to write to DynamoDB.| 

---
### 8) AWS Lambda Function for Sending an Email with AWS SES <a id='8_section_id'></a>
---

In this step you will setup AWS Simple Email Service (SES), to programmatically send emails when required. This is a two-part process: 

 - The first part entails the verification of email addresses for the sending and receiving of messages generated by SES. 
 
 - The second part sees you configure your growing lambda function to send emails to specified addresses when triggered by a POST request being received by the API gateway.
   
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

| :triangular_flag_on_post: PREDICT TASK :triangular_flag_on_post:                                                                                      |
| :--------------------                                                                                   |
| There are two predict-related tasks for this step. The first of these is the **verification of sender and recipient email addresses**. Here you will need to add `edsa.predicts@explore-ai.net` as a recipient address within SES. This email account forms part of our predict assessment process and will be used at a later stage for predict marking. Note that when requesting verification for this email address, *it may take up to 24 hours for confirmation to be given*. In addition to the explore email address, **you need to configure a sender and a recipient address respectively for your testing purposes**.| 

#### Part 2: Programmatically send an email via Amazon SES:

Having registered the necessary email addresses, you are now ready to invoke AWS SES within your lambda function to automate the sending of email messages. 

| :triangular_flag_on_post: PREDICT TASK :triangular_flag_on_post:                                                                                      |
| :--------------------                                                                                   |
| At this point we want you to once again show us your great cloud computing and python skills. The **second task involves sending a sample email to your recipient address from your sender address, using AWS SES**. Here we provide some basic guidance in the form of [this](student_solution_files/send_emails_with_ses.py) this template, which your are required to complete and to add to your lambda function in order to help you accomplish your end goal.| 

---
### 9) AWS Lambda Function for Using Amazon Comprehend <a id='9_section_id'></a>
---

In this final step you will be building out the predict's NLP functionality with the help of AWS Comprehend. The NLP functionality will enable you to extract the overwhelming sentiment (categorical variable) from a message, as well as a list of its key phrases as determined by AWS comprehend. With the sentiment information and a list of key phrases, you can build in intelligent, automated email responses into your AWS Lambda function. To help you thoroughly understand this section, we provide a three-part breakdown wherein we describe each key element involved in the formation of an intelligent response. 

The **first part** is the process description; where we go through the logic of how to use AWS comprehend to extract sentiment and key phrases. The **second part** covers the helper functions utilised; where we describe two helper functions and the main lambda function required to orchestrate an intelligent automated response. The third and **final part** is an end-to-end example; where we simulate what should be achieved once the entire AWS Lambda/AWS Comprehend/AWS SES integration is built.

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
  - The function implementation can be found [here](student_solution_files/find_maximum_sentiment.py)
   
**Function 2 - `key_phrase_finder(list_of_important_phrases, list_of_extracted_phrases):`**

This function attempts to find a match between the words in a key phrases dictionary produced by AWS Comprehend to a provided custom list of words. The result of the search is returned as a boolean variable.
  - Input arguments:     
    - list_of_important_phrases: A string-based list of words representing topics to be detected i.e. `['CV', 'data', 'science']`
    - list_of_extracted_phrases: An AWS Comprehend key phrases dictionary. 
  - Outputs: 
    - listing: An empty list to append the individual words present in the AWS Comprehend key phrases dictionary.
    - phrase_checker: A boolean variable representing the whether a match is discovered between the function's input lists.
  - The function implementation can be found [here](student_solution_files/find_key_phrases.py)
            
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
  - - The function implementation can be found [here](student_solution_files/email_responses.py)

The email_response method works as follow:

  1. You supply a list of words which correspond to topics which you'd like to extract/filter for within an incoming website enquiry.
  2. The supplied list of words are matched with words extracted from the AWS Comprehend key phrases dictionary. 
  3. A `boolean` response is given for each match detected across various configured keyword categories.
  4. Given the match, or potentially multiple matches, you can set up logic to start building an email response sequentially.

| :triangular_flag_on_post: PREDICT TASK :triangular_flag_on_post:                                                                                      |
| :--------------------                                                                                   |
| The final task of the predict requires you to use the provided functions and the boilerplate AWS Comprehend/AWS Lambda code found [here](student_solution_files/aggregated_lambda_function.py) to build out the full functionality of the automated predict pipeline.| 
      

# End-to-end Example

In this section we will review a basic example of how an email response is generated with the full solution architecture.

Let's say someone visiting your deployed webpage posts the following sample message using the form:

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
> Charlotte Regression
> 
> Senior HR Manager, Real Analytics Resources

Running this message through our AWS Comprehend service produces [these](student_solution_files/Example_AWS_Comprehend_Key_Phrases_Output.txt) key phrases and [this](student_solution_files/Example_AWS_Comprehend_Sentiment_Output.txt) sentiment classification output.

From this output it can be seen that AWS Comprehend picked up that the message has a positive sentiment, and that it contains key phrases such as: 'your portfolio projects', 'your GitHub page', 'Your medium articles', 'a potential job', etc. We can therefore set up some logic along with our helper functions to build out our responses.

To define this logic, we start by providing some sample `string` replies that we can add to our email response if certain supplied words match the words in our AWS Comprehend key phrases dictionary. These sample replies can take the following form:

**1. Sample reply if a CV related word is matched**:

```
CV_Text = 'I see that you mentioned my C.V in your message. I am happy to forward you my C.V in response. If you have any other questions or C.V related queries please do get in touch. '
```

**2. Sample reply if a portfolio project related word is matched**

```
Project_Text = 'The projects I listed on my site only include those not running in production. I have several other projects that might interest you.'
```
**3. Sample reply if a Medium article related word is matched**

```    
Article_Text = 'In your message you mentioned my blog posts and data science articles. I have several other articles published in academic journals. Please do let me know if you are interested - I am happy to forward them to you.'
```
**4. Sample reply if the detected sentiment is negative**  

```
Negative_Text = 'I see that you are unhappy in your response. Can we please set up a session to discuss why you are not happy, be it with the website, my personal projects or anything else. \n\nLooking forward to our discussion. \n\nKind Regards, \n\nMy Name'
```

**5. Sample reply if the detected sentiment is neutral** 

```
Neutral_Text = 'Thank you for your email. Let me know if you need any additional information.\n\nKind Regards, \n\nMyName'
```

**6. Sample farewell reply** 
    
```    
Farewell_Text = 'Again, Thank you for your email.\n\nIf there is anything else I can assist you with please let me know and I will set up a meeting for us to meet in person.\n\nKind Regards, \n\nMyName'
```    
    
With sample replies now defined, we can use conditional logic and string manipulation techniques to *build* up a response.

For instance, we define a `Phrase_Matcher_Project` variable that makes use of the `key_phrase_finder` function and passes a list of words that might be project related, for example `['github', 'git', 'Git', 'GitHub', 'projects', 'portfolio', 'Portfolio']`. 

If any of these words now match the extracted keywords in the Comprehend dictionary, the value of the `Phrase_Matcher_Project` variable will be `True`. We can then use conditional logic and string manipulation to add a greeting, the project text and the farewell text to an `email_reply` variable. In the example we've presented, this `email_reply` variable will take on the following form:

> Good day Charlotte Regression,
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

> Good day Charlotte Regression,
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
| The boilerplate lambda function for the full solution can be found [here](student_solution_files/aggregated_lambda_function.py) |

## Predict Assessment

| :triangular_flag_on_post: PREDICT TASK :triangular_flag_on_post:                                                                                      |
| :--------------------                                                                                   |
| Please ensure that all the below information is submitted in order to be fairly marked on your performance in completing this Predict.| 

Once completed, your predict solution will be marked at a time indicated within the Predict Overview Slides and as communicated on Athena. To facilitate this assessment, please submit the following details via the Predict Submission tab on Athena using [this](student_solution_files/predict_detail_submission_template.csv) simple template: 
 - Your **Name and Surname**; 
 - The **Website URL** of your deployed project as recorded in [Step 3](#3_section_id) of this guide, and 
 - Your **AWS API Gateway URL** as recorded in part 3 of [Step 6](#6_section_id). 

Please also ensure that you have verified the `edsa.predicts@explore-ai.net` email address via AWS SES as instructed in step 8, part 1. 

Note that while you are free to personalise many aspects of this predict, for assessment purposes you will only be awarded marks for its functionality. As such, please make every effort to ensure that your completed predict solution is able to replicate the functioning specified throughout the above instruction steps.  

## Conclusion

If you followed the nine-step process described above correctly, you should now have a fully functioning portfolio website capable of sending intelligent email responses in an automated way. Congrats! 

Following the conclusion of this predict and its assessment, you are free (and we encourage you) to tweak various aspects of the project to personalise it even further. Here are just a few ideas you can try:

   - Set up more logic that will cater for a wider array of email responses. 
   - Use a different [Bootstrap](https://getbootstrap.com/) template and see if you can reproduce the results of the project.
   - Integrate more AWS services. For example, see if you can integrate AWS QuickSight to visualize the data in your AWS DynamoDB NoSQL database. Alternatively, you could try to use the [AWS Lex](https://aws.amazon.com/lex/) service to place a chatbot on your profile page, adding another layer of intelligent interaction to engage potential clients.

<p align="center">
  <img src="assets/img/digital_skills_logo.png" width=800px/>
</p>
