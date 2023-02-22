# Week 0 — Billing and Architecture

I created an AWS account for the bootcamp as my current previous account was over one year and i wanted to leverage the 12 month free tier you get with a new account. I also watched the Youtube videos from Chirag and Ashish.

I really enjoyed both videos as they reminded me some basic stuff i might have forgotten about AWS, as i have experience working with production systems on AWS prior to the bootcamp. I liked Ashish's presentation on AWS Organisations and SCP as i had not used both features prior to the bootcamp.

One of my first tasks after creating this account was to obviously login to the root account and created an IAM user. I then assigned the IAM user admin provileges to enable me administer my the AWS account without the root account. Just before logging out of the root account, i had to "activate" access to billing information for the root account.

I then proceeded to log in as the new IAM user and created a billing alarm using Cloudwatch. While creating the alarm, i had to create an SNS topic to be used in delivering CloudWatch Notifications to my email via SNS.

I also created a budget of $5, and a notification setting that'll be triggerred if my actual usage is close to and hits the budgetted amount.

Another requirement for week 0 was to use Cloud shell which i did. I was happy to know that you get 1GB free data storage with ther cloud shell to store settings and related documents in all regions.


I then watched Andrew Brown's architectural diagram guide on Youtube and created the required conceptual and logical architectural diagram for cruddur and the logical CI/CD pipeline architecture for it. The link to the diagrams is : https://lucid.app/lucidchart/7943683c-15e8-407d-a28d-23fb727d1d17/edit?invitationId=inv_737d9524-e316-4572-9a71-28403d758e49

<img width="1232" alt="image" src="https://user-images.githubusercontent.com/112012120/220642838-d61bd066-8d1b-4be7-a65e-e6993ebf48eb.png">


Finally, i genrated AWS access keys for the IAM user i created and created a named profile to use the access keys i generated to enable me make API calls programmatically from the CLI. I am interested in the fefatures that AWS CLI v2 have to offer interms of authenticating without directly storing access keys on your machine.

I look forward to week 1 of the bootcamp




