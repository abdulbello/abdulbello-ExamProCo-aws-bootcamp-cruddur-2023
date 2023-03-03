FROM python:3.10-slim-buster

WORKDIR /backend-flask

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

RUN /bin/bash

COPY . .

RUN chmod +x cmd_script.sh

ENV FLASK_ENV=development

EXPOSE ${PORT}

#CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=4567"]

CMD /bin/bash ./cmd_script.sh
