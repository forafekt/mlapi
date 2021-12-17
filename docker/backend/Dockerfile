FROM ubuntu:20.04
RUN apt-get update
RUN apt-get install python3 -y
RUN apt-get install python3-pip -y
RUN apt-get install vim -y
RUN apt-get install -y build-essential libssl-dev libffi-dev python3-dev python3-venv

# set environment variables
ENV DISABLE_COLLECTSTATIC=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV DEBUG=1

ENV PORT=$PORT
EXPOSE $PORT

# Set container working directory
WORKDIR /home/forafekt/apps

ENV VIRTUAL_ENV=/home/forafekt/apps/ml-venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN . $VIRTUAL_ENV/bin/activate
RUN chmod 777 -R $VIRTUAL_ENV

COPY requirements.txt .

RUN python3 --version
RUN python3 -m pip install -U --force-reinstall pip
RUN python3 -m pip install --upgrade wheel
RUN pip install -r requirements.txt
RUN pip install gunicorn
RUN pip install tzdata

ADD ./src /home/forafekt/apps/src
ADD ./docker /home/forafekt/apps/docker
ADD ./research /home/forafekt/apps/research

RUN mkdir -p /home/forafekt/apps/src/staticfiles
RUN mkdir -p /home/forafekt/apps/src/static




