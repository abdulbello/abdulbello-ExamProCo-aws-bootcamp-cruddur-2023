#!/bin/bash
/root/.sonar/sonar-scanner-4.7.0.2747-macosx/lib java -jar sonar-scanner-cli-4.7.0.2747.jar  -Dsonar.projectKey=UEL_Thesis   -Dsonar.sources=.   -Dsonar.host.url=http://192.168.168.115:9000
