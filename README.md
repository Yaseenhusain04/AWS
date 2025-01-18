Add Two Numbers Function
Overview
This AWS Lambda function takes two numbers as input and returns their sum. It is designed to be triggered via an API Gateway or directly through AWS Lambda. The function validates the input and handles errors gracefully.
Setup Instructions
Create an AWS Lambda Function: Go to the AWS Lambda console and create a new function.
Set Environment Variables: If you are using the S3 upload function, set the environment variable S3_BUCKET_NAME to your desired S3 bucket name.
Deploy the Function: Copy the code provided below into the Lambda function code editor.

Store Document in S3 Function
Overview
This AWS Lambda function uploads a document or PDF file to a specified S3 bucket. It accepts the file content and filename as input and handles errors during the upload process.
Setup Instructions
Create an S3 Bucket: Create an S3 bucket in the AWS Management Console.
Set Environment Variables: In the Lambda function configuration, set the environment variable S3_BUCKET_NAME to the name of your S3 bucket.
Deploy the Function: Copy the code provided below into the Lambda function code editor.

Testing the Functions
For the Add Two Numbers Function, you can test it by invoking it with an event object like:
{
    "num1": 10,
    "num2": 20
}
For the Store Document in S3 Function, you can test it with:
{
    "file_content": "This is a test document content.",
    "file_name": "test_document.txt"
}
