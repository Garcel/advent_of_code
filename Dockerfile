FROM python:3.10.0-alpine3.14
ARG UID=1000
ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY requirements.txt /code/
RUN python3 -m pip install -r requirements.txt --no-cache-dir

# Add a new user non root user
RUN adduser docker_user -u ${UID} --disabled-password

# Change to non-root privilege
USER docker_user

COPY . /code/
