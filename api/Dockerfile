FROM python:3.10-slim-bullseye

# Path: /app
RUN mkdir /app
WORKDIR /app

# Path: /app/requirements.txt
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

# Path: /app
COPY . /app

CMD [ "python", "./api.py" ]
