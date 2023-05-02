# Week 6 — Deploying Containers






I was able to successfully push our frontend React app and the backend container images to ECR, each one having its own repository. ECR provides ability to store container images for easy deployment to services that run containers. ECR provides the advantage of not having any restriction on the number of pulls that can be made within a time period. ECRs free tier allows 500MB per month to store container images.

To run the containers on ECS we had to create a cluster (a container for grouping related services), one service each for our backend and frontend workloads and container definitions within the services to define the config for the containers to be run. Although, i had previously worked with ECS, i still didnt fully get the difference between a services and a task on ECS. Andrew's instructional content helped me undertand it much better.

We also created custom domains for our application. In our architecture diagram, we planned to use Route 53 as the DNS provider for our app domains, so i created a DNS Hosted Zone on Route 53 and pointed my domain to the Route 53 NameServers from my domain registrar to enable DNS requests for my domain to be handled by Route 53. My own domain is app.cruddur.com for the frontend app and api.cruddur.com for the backend app. 

We also had to create certificates on ACM to enable Transport Layer Security. The certificate was applied on an Application Elastic Load Balancer we created. On the ELB, we created rules to point traffic on port 4567 to the api backend target group and traffic to port  


also  ECS, behind a loadbalancer.

#discuss a bit more

<img width="733" alt="image" src="https://user-images.githubusercontent.com/112012120/233143302-d6a6ad97-6cee-47a8-adb1-a3aba138993b.png">


I was also able to follow Adrew's instructional content to fix messaging in production.

The issue was as a result of 

<img width="1909" alt="image" src="https://user-images.githubusercontent.com/112012120/234297198-6dabfb91-6d90-41c4-90d6-53926fd64ba8.png">

