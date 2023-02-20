# Week 0 — Billing and Architecture

I created an AWS account for the bootcamp as my current previous account was over one year and i wanted to leverage the 12 month free tier you get with a new account. 

One of my first tasks after creating this account was to obviously login to the root account and created an IAM user. I then assigned the IAM user admin provileges to enable me administer my the AWS account without the root account. Just before logging out of the root account, i had to "activate" access to billing information for the root account.

I then proceeded to log in as the new IAM user and created a billing alarm using Cloudwatch. While creating the alarm, i had to create an SNS topic to be used in delivering CloudWatch Notifications to my email via SNS.

I also created a budget of $5, and a notification setting that'll be triggerred if my actual usage is close to and hits the budgetted amount.

