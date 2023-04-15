FROM python:3.10-alpine
EXPOSE 8000
WORKDIR /home/project/aswan

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV LANG C.UTF-8

# install dependencies
RUN apk update \
    && apk add \
    gcc python3-dev musl \
    musl-dev 
   

RUN pip install --upgrade pip
COPY requirements.txt /home/project/aswan/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt



# copy project
COPY . /home/project/aswan


