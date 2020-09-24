FROM rabbitmq:latest

# RUN rabbitmqctl set_permissions -p tochka rmq_user ".*" ".*" ".*"

COPY ./rabbitmq.conf /etc/rabbitmq/rabbitmq.conf.1
RUN cat /etc/rabbitmq/rabbitmq.conf.1 >> /etc/rabbitmq.conf && rm /etc/rabbitmq/rabbitmq.conf.1
