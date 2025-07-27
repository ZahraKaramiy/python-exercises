import time

def timer(f):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = f(*args, **kwargs)
        end_time = time.time()
        
        execution_time = end_time - start_time
        print(f"Returned value: {result}")
        print(f"Execution time: {execution_time:.6f} seconds")
        return result
    return wrapper 
    
    
@timer
def generator_list(n):
    my_list = []
    for i in range(1, n+1):
        my_list.append(i)
    return my_list
        

generator_list(10)