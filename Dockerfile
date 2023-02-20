FROM python:3.11
COPY ./test_task_fib/ /app/
COPY requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

ENTRYPOINT celery -A test_task_fib.fib_worker worker --loglevel=INFO
