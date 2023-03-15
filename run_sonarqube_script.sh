#!/bin/bash

java -jar /root/.sonar/sonar-scanner-4.7.0.2747-macosx/lib/sonar-scanner-cli-4.7.0.2747.jar  -Dsonar.projectKey=UEL_Thesis   -Dsonar.sources=./backend-flask/   -Dsonar.host.url=http://192.168.168.115:9000
