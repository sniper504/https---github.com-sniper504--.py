input_data=open("input.txt","r")
output_data=open("output.txt","w")
data=input_data.read()
N=int(input('введите число'))#длина ряда
list=[]
list.append(N)
a=1
b=1
a=b = 1
for i in range(2, N):
    a, b = b, a + b
    print(b, end=' ')
input_data.close()
output_data.close()