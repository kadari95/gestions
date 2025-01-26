from python:3
ENV PYTHONBUFFERD 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN mkdir /app

WORKDIR /app

COPY  . /app/

RUN python -m venv /env

RUN  python -m pip install --upgrade pip

COPY requirement.txt /app/

RUN pip install -r requirement.txt 
