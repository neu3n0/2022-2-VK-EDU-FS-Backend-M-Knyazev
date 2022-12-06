FROM python:3.8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN mkdir "/web_django"
WORKDIR /web_django
RUN pip install --upgrade pip
COPY ./requirements.txt /web_django
RUN pip install -r requirements.txt
COPY . /web_django/