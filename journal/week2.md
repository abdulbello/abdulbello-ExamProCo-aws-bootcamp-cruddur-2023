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


I'm currently trying to add custom attributes to my span for the Honeycomb intrumentation. I have add
