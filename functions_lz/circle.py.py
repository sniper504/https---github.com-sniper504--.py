def square(radius):
    s=3.14*float(radius)**2
    return(s)

def length(radius):
    l=2*3.14*int(radius)
    return(l)

print("введите радиус")
radius=input()

result=square(radius)
print("площадь круга")
print(result)

result=length(radius)
print("длина окружности")
print(result)