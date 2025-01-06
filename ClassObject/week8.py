#Lamda function

# sum = lambda num1,num2 :num1+num2
# print(sum(5,6))

# # list comprehensive
# lis = [1,2,3,4,5,6]
# result = [val*2 for val in lis]
# print(result)


#map() function

# def AddNum(num):
#     return num+5

# numbers = [1,2,3,4,5]
# result = map(AddNum,numbers)
# print(list(result))

#reduce() function

# import functools

# # Define a list of numbers
# numbers = [1, 2, 3, 4]

# # Use reduce to compute the product of list elements
# product = functools.reduce(lambda x, y: x * y, numbers)
# print("Product of list elements:", product)


#filter() function

# def is_even(n):
#     return n % 2 == 0

# # Define a list of numbers
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# # Use filter to filter out even numbers
# even_numbers = filter(is_even, numbers)
# print("Even numbers:", list(even_numbers))