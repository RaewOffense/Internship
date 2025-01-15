import sys

def generator_obj(max):
    count =1
    while count<=max:
        yield count
        count +=1
gen_obj = generator_obj(3)
print(next(gen_obj))
print(next(gen_obj))
print(next(gen_obj))

for number in generator_obj(3):
    print(number)

s