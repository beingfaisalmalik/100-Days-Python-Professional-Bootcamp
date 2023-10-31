import time
current_time = time.time()


def speed_calc_decorator(function):
  def wrapper():
      function()
      print(f'{function.__name__} run  {time.time()-current_time}')
  return wrapper
    
@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i

@speed_calc_decorator
def slow_function():
    
    for i in range(100000000):
        i * i
    
fast_function()
slow_function()
