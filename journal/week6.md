# Week 6 — Deploying Containers






I was able to successfully push our frontend React app and the backend container images to ECR, each one having its own repository. ECR provides ability to store container images for easy deployment to services that run containers. ECR provides the advantage of not having any restriction on the number of pulls that can be made within a time period. ECRs free tier allows 500MB per month to store container images.

To run the containers on ECS we had to create a cluster (a container for grouping related services), one service each for our backend and frontend workloads and container definitions within the services to define the config for the containers to be run. Although, i had previously worked with ECS, i still didnt fully get the difference between a services and a task on ECS. Andrew's instructional content helped me undertand it much better.

We also created custom domains for our application. In our architecture diagram, we planned to use Route 53 as the DNS provider for our app domains, so i created a DNS Hosted Zone on Route 53 and pointed my domain to the Route 53 NameServers from my domain registrar to enable DNS requests for my domain to be handled by Route 53. My own domain is app.cruddur.com for the frontend app and api.cruddur.com for the backend app. 

We also had to create certificates on ACM to enable Transport Layer Security. The certificate was applied on an Application Elastic Load Balancer we created. On the ELB, we created listener rules to point traffic with host header api.cruddur.com to the backend target group and other traffic to the frontend.


I was also able to follow Adrew's instructional content to fix messaging in production.

The issue was as a result of a CORS error. We were able to fix it by specifying the domains for CORS to allow content from.

<img width="1909" alt="image" src="https://user-images.githubusercontent.com/112012120/234297198-6dabfb91-6d90-41c4-90d6-53926fd64ba8.png">

On the code side of things, it was really interesting because we wrote BASH and Ruby scripts. The bash scripts in my repo /bin path allow us to automatically perform certain repititive tasks such as login to ECR, push images to ECR, deploy a new image to ECS and the likes. It provided me with a much needed experience into BASH scripting. I was also able to create some BASH scripts of mine to start up and stop my DB for convenience. 
