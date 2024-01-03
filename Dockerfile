FROM locustio/locust
# Switch to root user for installations
USER root
# Install system utilities
RUN apt-get update && apt-get install -y psmisc procps
COPY requirements.txt /opt/requirements.txt
RUN pip3 install -r /opt/requirements.txt