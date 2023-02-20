from celery import Celery

worker = Celery('fib_worker', broker='amqp://admin:pass@localhost:5672', backend='rpc://')

@worker.task(name='fibonacci_task')
def fibonacci(n, memo={}):
  if n <= 0:
    return 0
  elif n == 1:
    return 1
  elif n in memo:
    return memo[n]
  else:
    memo[n] = fibonacci(n-1) + fibonacci(n-2)
    return memo[n]