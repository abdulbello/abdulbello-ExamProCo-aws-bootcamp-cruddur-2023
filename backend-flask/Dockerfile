FROM python:3.10-slim-buster

WORKDIR /backend-flask

#COPY requirements.txt requirements.txt
#RUN pip3 install -r requirements.txt
#ENV PIPENV_VENV_IN_PROJECT=1


#RUN /bin/bash

COPY . .

RUN pip3 install pipenv

RUN pipenv install --system --deploy --ignore-pipfile

#RUN pipenv sync

RUN chmod +x cmd_script.sh

ENV FLASK_ENV=development

EXPOSE ${PORT}

HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 CMD curl -f http://localhost/api/activities/notifications || exit 1

#CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=4567"]

CMD /bin/bash ./cmd_script.sh
