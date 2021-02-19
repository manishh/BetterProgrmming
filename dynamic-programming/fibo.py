from timeit import default_timer as timer
from datetime import timedelta

fibo_cache = [0]*200

def recursive_fibonacci(num):
    if num in (0, 1):
        return num

    return recursive_fibonacci(num-1) + recursive_fibonacci(num-2)


def dynamic_fibonacci(num):
    if num in (0, 1):
        return num
    elif 0 != fibo_cache[num]:
        return fibo_cache[num]

    fibo_cache[num] = dynamic_fibonacci(num-1) + dynamic_fibonacci(num-2)
    return fibo_cache[num]


if __name__ == '__main__':

    fibo_num = 45  # change as needed
    start = timer()
    print(f"Dynamic fibonacci answer = {dynamic_fibonacci(fibo_num)}")
    dyna_end = timer()
    print(f"Time for Dynamic = {timedelta(seconds=dyna_end-start)}")
    print(f"Recursive fibonacci answer = {recursive_fibonacci(fibo_num)}")
    rec_end = timer()
    print(f"Time for Recursive = {timedelta(seconds=rec_end-start)}")




