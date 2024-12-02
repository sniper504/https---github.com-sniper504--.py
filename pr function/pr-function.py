import math
def multiply(a,b):
    c=float(a)*float(b)
    return(c)
def add(a,b):
    c=float(a)+float(b)
    return(c)
def subtract(a,b):
    c=float(a)-float(b)
    return(c)
def divide(a,b):
    c=float(a)/float(b)
    return(float(c))
def factorial(a):
    c=int(math.factorial(a))
    return(c)
def degree(a,b) :
       c=float(a) ^ float(b) 
print('Введите выражение')
user_input = input()
number_element=len(user_input)
if '-' in user_input:
        number_list=user_input.split("-")
        print(number_list)
        result = (number_list[0])
        for i in range(1,len(number_list)):
                number_list[i] = float(number_list[i])
                result =(subtract(result,number_list[i]))
elif '+' in user_input:
        number_list=user_input.split("+")
        result = number_list[0]
        for i in range(1,len(number_list)):
                number_list[i] = float(number_list[i])
                result = add(result,number_list[i])
elif '*' in user_input:
        number_list=user_input.split("*")
        result = number_list[0]
        for i in range(1,len(number_list)):
                number_list[i] = float(number_list[i])
                result = multiply(result,number_list[i])
elif '/' in user_input:
        number_list=user_input.split("/")
        result = number_list[0]
        for i in range(1,len(number_list)):
                number_list[i] = float(number_list[i])
                result = divide(result,number_list[i])
elif "!"  in user_input: 
        number_list=user_input.split("!")
        result = number_list[0]
        for i in range(0,len(number_list)):
            number_list[i] = float(number_list[i])
            result = factorial(float(number_list[i]))
elif "^"  in user_input: 
        number_list=user_input.split("^")
        result = number_list[0]
        for i in range(1,len(number_list)):
                number_list[i] = float(number_list[i])
                result = degree(result,number_list[i])                        
print(result)


            