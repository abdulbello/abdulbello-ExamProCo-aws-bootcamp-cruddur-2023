# Week 1 — App Containerization

Week 1 has just started and its a lot of knowledge gained already.. Thank you Andrew!!!

I followed the recording of Week1 - App containerization live class, and was able to create a docker file for the backend (flask) project. I also copied the dockerfile instructions into the docker file which builds the container image for the backedn application. I was able to install the required dependencies for the flask app by running "pip3 install -r requirements.txt". In addition i was able to set the required environment variables and run the application. The application endpoint /api/activities/home returns the following json output.

<img width="695" alt="image" src="https://user-images.githubusercontent.com/112012120/221838912-589dcd00-54dc-46ac-aac5-8811c37f85b3.png">


It was interesting to learn from James Spurin and Edith Puclla, the guest instructors about docker containers and how every command run in your docker file, essentially creates an image, and that the "CMD" instruction in your docker file is your container entry point. The entry point is run when the container actually starts up.

Andrew released additional post class content which i was able to follow in creating a backend notification endpoint and a frontend notification page for for the cruddur app. It was an interesting experience that has made me very interested in improving my knowledge of flask and Javascript.



As for the additional homework challenges, I was able to achieve the following:

Run the CMD command in docker file as an external script. This took a while to achieve as I had to go read docker documentation to understand the various methods of running the CMD command (shell and executable mode). I also needed to do some research on shell scripting. My CMD command: CMD /bin/bash ./cmd_script.sh


I created a docker hub account (free tier) and created 2 repositories for the backend and frontend application images. Afterwards, I was able to push both frontend and backend images to my docker hub repo. Repo: https://hub.docker.com/repositories/onivehu

As part of the homework challenges suggested by Andrew, i was able to learn about multi-stage builds which i think can be really useful to eliminate the need of maintaining multiple Dockerfiles and reducing complexity with using docker.
