input_data=open("input.txt","r")
data =input_data.read()
output_data=open("output.txt","w")
data=data.split()
a=int(data[0])
b=0
while a != 0:    
    if a%2==1:
        b+=1
    a=a//2
output_data.write(str(b))
input_data.close()
output_data.close()