FROM python:3.8
LABEL Name=manage-cars Version=0.0.1
WORKDIR /app
RUN pip3 install -r requirements.txt
EXPOSE 8000
