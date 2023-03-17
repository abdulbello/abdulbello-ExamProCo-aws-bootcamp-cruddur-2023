# Week 2 — Distributed Tracing

Its week 3!!, its exciting and the work continues!!!


So this week, we would be working on distributed tracing. Which is a way to implement observability into your project. Distributed tracing enables us view telemetry (metrics, logs and traces) data across all our services (backend, frontend).


While instrumenting our app to send telemetry to Honeycomb, we encountered the Pip dependency management issue.- where pip does not auto-update the requirements.txt file with packages installed with the "pip" command. I decided to read up on the issue and discovered the new way of handling dependencies for python is with Pipenv. It handles the pip dependency issue quite well and additionally helps create a virtual environment. Pipenv creates a pipfile and pipfile.lock file where it stores packages (dependencies) and their version numbers automatically in the pipfile.lock file. This helps reduce potential application crash issues when the project is installed on a different machine or when the pipenv install --deploy command is run. The pipenv install --deploy command is what helps install the exact dependencies specified in the pipfile and pipfile.lock files.

I have decided to move to Pipenv for dependency management on this project. I had to modify my backend-app Dockerfiles to reflect these changes. See Dockerfile content: 

<img width="728" alt="image" src="https://user-images.githubusercontent.com/112012120/224047306-8c433c41-35a5-4e49-ac1a-bc335cf01939.png">


I watched Chirag and Ashish's videos which were informative, especially Chirag's video on observability across different products. Chirag showed the agents used by different AWS observability related services; such as Cloudwatch agent which allows sending logs and metrics to cloudwatch. I look forward to instrumenting the Cruddur app with xray and viewing the data on xray just like we did on Honeycomb.io, Which i really liked the simplicity of it.

I was able to instrument the Cruddur app with open telemetry, Honeycomb and AWS xray, to push the data to Honeycomb and AWS xray by following the live class and Andrew's supplementary videos.

<img width="1438" alt="image" src="https://user-images.githubusercontent.com/112012120/224734008-b389dbc5-b7f5-453f-8e71-a51b648f7b07.png">



<img width="1440" alt="image" src="https://user-images.githubusercontent.com/112012120/224734276-b1b75a69-312c-4901-8ce3-1e228dba466b.png">


As part of the homework STRETCH assignements, I have just added a custom attribute to my span for the Honeycomb instrumentation. I was able to add a custome attribute (app.handle) which shows the handle for the user in that span.

See below image as proof.

<img width="1440" alt="image" src="https://user-images.githubusercontent.com/112012120/224765050-5dd8794d-dfdc-4383-a859-efbe74cbc5fc.png">


I was also able to implement observability with rollbar as well as subsegments on xray as seen below. It is interestiing implementing observability as this is my first time really. We only use Azure app insights and i've always wondered how they get such depth of information from an execuing application. :

![image](https://user-images.githubusercontent.com/112012120/225931010-22f19d67-d678-4bfe-9fa9-3b75f25d4d16.png)



![image](https://user-images.githubusercontent.com/112012120/225933048-20a2224a-2019-43dc-914f-b96e4fff46cd.png)



