FROM tomcat:latest
USER root
RUN apt-get update
RUN apt-get install python3-pip -y
RUN pip install mysql-connector-python
RUN pip install behave
RUN pip install allure-behave
RUN pip install requests

RUN	apt-get install -y wget
RUN	apt-get install -y tar

ENV JAVA_VERSION 1.8.0

RUN apt-get install -y openjdk-8-jre

ENV JAVA_HOME /usr/lib/jvm/java

ENV MAVEN_VERSION_MAJOR 3
ENV MAVEN_VERSION_MINOR 5.2

RUN wget https://dlcdn.apache.org/maven/maven-3/3.9.1/binaries/apache-maven-3.9.1-bin.tar.gz
RUN tar xzvf apache-maven-3.9.1-bin.tar.gz
RUN mv apache-maven-${MAVEN_VERSION_MAJOR}.${MAVEN_VERSION_MINOR}  /usr/local/apache-maven
ENV M2_HOME=/usr/local/apache-maven
ENV M2=$M2_HOME/bin
ENV PATH=$M2:$PATH

CMD  java -version && mvn -version
