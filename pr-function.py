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
    return(c)

print('Введите выражение')
user_input = float(input())
number_element=len(user_input)
if '-' in user_input:
        number_list=user_input.split("-")
        result = float(number_list[0])
        for i in range(1,len(number_list)):
                number_list[i] = float(number_list[i])
                result = subtract(result,number_list[i])
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
print(result)


            