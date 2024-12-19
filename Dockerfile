FROM python:3.9.13

ENV PYTHONDONTWRITEBYTECODE=1  
ENV PYTHONUNBUFFERED=1        

RUN apt-get update -y && \
    apt-get install -y && \
    apt-get install -y --no-install-recommends netcat && \
    apt-get clean

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /opt/src

COPY ./src .

EXPOSE 8000
