FROM python:3.8

RUN mkdir -p /usr/app/
WORKDIR /usr/app

RUN pip install --upgrade pip 
COPY ./requirements.txt .
RUN pip install -r requirements.txt 
RUN pip install gunicorn

COPY . . 

# Running python application
CMD gunicorn run:app --bind 0.0.0.0:3000 --reload