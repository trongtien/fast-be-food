ARG PYTHON_VERSION=3.10.4-slim-buster

FROM python:${PYTHON_VERSION} as python
RUN pip install --upgrade pip


WORKDIR /code

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

RUN apt-get update && apt-get install --no-install-recommends -y \
  build-essential \
  libpq-dev
  
COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir -r /code/requirements.txt

COPY ./src /code/src

CMD ["uvicorn", "src.main:app", "--host", "localhost", "--port", "3337", "--reload"]

EXPOSE 9000