FROM spark:3.5.3

USER root

RUN mkdir -p /opt/spark/apps

COPY Spark-Test-1.0.jar /opt/spark/apps/

RUN chmod -R 755 /opt/spark/apps

USER spark