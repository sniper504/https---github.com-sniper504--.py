input_data=open("input.txt","r")
data =input_data.read()
output_data=open("output.txt","a")
data = data.split() 
a=data[0]
b=data[1]
c=data[2]
d=data[3]
for x in range(-100,100):
    if a*(x**3)+b*(x**2)+c*x+d==0:
            output_data.write(str(x)+' ')
output_data=open("output.txt","a")
input_data.close()
output_data.close()