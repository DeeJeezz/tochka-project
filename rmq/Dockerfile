FROM rabbitmq:latest

RUN mkdir /var/log/rmq

COPY ./rabbitmq.conf /etc/rabbitmq/rabbitmq.conf.1
RUN cat /etc/rabbitmq/rabbitmq.conf.1 >> /etc/rabbitmq.conf && rm /etc/rabbitmq/rabbitmq.conf.1
