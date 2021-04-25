FROM ubuntu:16.04


RUN apt-get update -y && \
    apt-get install -y python-pip python-dev && \
    apt-get install -y python3-pip 

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

ENTRYPOINT [ "/bin/bash" ]

CMD [ "start.sh" ]

ENTRYPOINT [ "python" ]

CMD [ "test.py" ]
