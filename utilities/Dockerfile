FROM tomcat:latest
USER root
RUN apt-get update
RUN apt-get install python3-pip -y
RUN pip install mysql-connector-python
RUN pip install behave
RUN pip install allure-behave
RUN pip install requests

