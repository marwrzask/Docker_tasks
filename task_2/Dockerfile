FROM python:3.9-slim-buster

COPY . /app
WORKDIR /app

RUN pip install pytest

ARG RUN_TEST=true

RUN if [ ${RUN_TEST}=true ] ; then pytest ; fi


CMD ["python", "task_2.py"]