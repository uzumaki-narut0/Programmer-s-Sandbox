#base image
FROM ubuntu:16.04

RUN echo "deb http://archive.ubuntu.com/ubuntu trusty main universe" > /etc/apt/sources.list
RUN apt-get update

RUN apt-get install -y gcc
RUN apt-get install -y python
RUN apt-get install -y ruby
RUN apt-get install -y php5-cli
RUN apt-get install -y npm
RUN apt-get install -y nodejs

# Install any needed packages specified in requirements.txt
#RUN pip install -r -y requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80


# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

#CMD ["python", "server.py"]