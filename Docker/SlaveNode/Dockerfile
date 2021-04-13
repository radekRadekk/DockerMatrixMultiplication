FROM python:3.7-alpine
WORKDIR /SlaveNode

COPY ./SlaveNode /SlaveNode

RUN sleep 1;
CMD ["slave_main.py"]
ENTRYPOINT ["python3"]