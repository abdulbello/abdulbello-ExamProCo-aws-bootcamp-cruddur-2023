FROM 611672787239.dkr.ecr.us-east-1.amazonaws.com/cruddur-python:3.10-slim-buster

WORKDIR /backend-flask

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
#ENV PIPENV_VENV_IN_PROJECT=1

#RUN /bin/bash

COPY . .

#RUN pip3 install pipenv

#RUN pipenv install --system --deploy --ignore-pipfile

#RUN pipenv sync

#RUN chmod +x cmd_script.sh

EXPOSE ${PORT}

#HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 CMD curl -f "https://4567-$GITPOD_WORKSPACE_ID.$GITPOD_WORKSPACE_CLUSTER_HOST" || exit 1

CMD [ "python3", "-m" ,"-u", "flask", "run", "--host=0.0.0.0", "--port=4567", "--debug"]

#CMD /bin/bash ./cmd_script.sh
