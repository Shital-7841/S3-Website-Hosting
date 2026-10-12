\# Automated Static Website Hosting Using AWS SDK



\## 1. Project Overview



This project demonstrates how to host a static website on Amazon S3 and automatically upload website files using Python and the AWS SDK for Python (Boto3).



The website contains a welcome message and an interactive button. Amazon S3 provides static website hosting without requiring an EC2 server.



\## 2. Objectives



\- Host a static website using Amazon S3.

\- Automate file uploads using Python and Boto3.

\- Access the website through an S3 website endpoint.

\- Demonstrate a simple cloud hosting workflow.



\## 3. AWS Services Used



\- \*\*Amazon S3:\*\* Stores website files and hosts the static website.

\- \*\*AWS IAM:\*\* Manages permissions for accessing AWS resources.

\- \*\*AWS SDK for Python (Boto3):\*\* Uploads website files to S3.



\## 4. Technologies Used



\- Python

\- Boto3

\- HTML

\- JavaScript

\- AWS CLI

\- Git and GitHub



\## 5. Project Structure



```text

S3-Website-Hosting/

├── website/

│   └── index.html

├── screenshots/

├── upload\_website.py

└── README.md

```



\## 6. Live Website



\[Open the live website](http://s3-website-shital-959590.s3-website.ap-south-1.amazonaws.com)



\*\*Note:\*\* The S3 website endpoint uses HTTP. This is suitable for this demonstration, but do not enter sensitive information on the public site.



\## 7. Setup Instructions



\### Prerequisites



\- Python installed

\- AWS CLI installed

\- An AWS account with appropriate S3 permissions

\- Boto3 installed



\### Install Boto3



```bash

pip install boto3

```



\### Configure AWS CLI



```bash

aws configure

```



Configure your AWS credentials securely and set the region to `ap-south-1`.



\### Upload Website Files



Run this command from the project folder:



```bash

python upload\_website.py s3-website-shital-959590

```



The script uploads the files from the `website` directory to the specified S3 bucket.



\## 8. Screenshots



The following screenshots document the project. Open the screenshots folder in this repository to view the uploaded images.



1\. \[Working Website](screenshots/01-working-website.png)

2\. \[S3 Hosting Settings](screenshots/02-s3-hosting-settings.png)

3\. \[Uploaded S3 File](screenshots/03-s3-uploaded-file.png)

4\. \[GitHub Repository](screenshots/04-github-repository.png)

5\. \[Successful Git Push](screenshots/05-git-push-success.png)



\## 9. Results



\- Successfully hosted the website on Amazon S3.

\- Successfully uploaded the website file using Python and Boto3.

\- Verified the website in a browser.

\- Uploaded the project source code to GitHub.



\## 10. Security Considerations



\- Never upload AWS access keys, secret keys, passwords, or other sensitive information to GitHub.

\- Use appropriate IAM permissions.

\- Public access is enabled for this demonstration website. Do not store private files in the public bucket.



\## 11. GitHub Repository



\[View the source code on GitHub](https://github.com/Shital-7841/S3-Website-Hosting)



\## 12. Conclusion



This project demonstrates basic cloud computing concepts, Amazon S3 static website hosting, Python automation with Boto3, and version control using GitHub.

