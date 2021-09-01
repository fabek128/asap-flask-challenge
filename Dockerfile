FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y python3-pip python-dev build-essential libpq-dev python3-venv python3-virtualenv
COPY . .
RUN pip install -r requirements.txt
RUN virtualenv venv
RUN . venv/bin/activate
RUN python manage.py db init
EXPOSE 5000
CMD [ "make",  "run"]