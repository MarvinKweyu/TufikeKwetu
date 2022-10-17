FROM python:3.9.6-alpine


# env variables
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# deps
RUN apk update 
RUN apk add postgresql-dev gcc musl-dev python3-dev libffi-dev openssl-dev


RUN pip install --upgrade pip

#Set the working directory in the Docker container
WORKDIR /code

#Copy the dependencies file to the working directory
COPY requirements.txt .

#Install the dependencies
RUN pip install -r requirements.txt

#Copy the Flask app code to the working directory
COPY src/ .

#Run the container
CMD [ "python", "./app.py" ]