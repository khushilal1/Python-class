# #lambda function
# # sybntax: lambda arguments :expression

# x=lambda a:a+4#lamnda funtion
# # y=x(2)
# # print(y)
# print(x(5))


# y=lambda a,b,c:a+b*c
# print(y(2,34,5)) 

#lamda inside ither function
def my_function(n):
    return lambda a:a*n

double=my_function(2)
a=double(4)
print(a)