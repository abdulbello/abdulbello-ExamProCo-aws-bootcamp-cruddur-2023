#!/bin/bash

java -jar /sonar-scanner-4.7.0.2747-macosx/lib/sonar-scanner-cli-4.7.0.2747.jar  -Dsonar.projectKey=UEL_Thesis   -Dsonar.sources=./backend-flask/   -Dsonar.host.url=http://172.20.10.3:9000
