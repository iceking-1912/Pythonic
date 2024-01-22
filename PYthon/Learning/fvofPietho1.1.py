
print('Hi Himanshu')
import random
def my_es_pie(n):
    num_c=0
    num_t=0
    for _ in range(n):
        x= random.uniform(0,1)
        y= random.uniform(0,1)
        distance = x**2 + y*2
        if distance <= 1:
            num_c += 1
    return
    print(4 * num_c/num_t)

my_es_pie(50)

