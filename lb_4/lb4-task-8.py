input_data=open("input.txt","r")
output_data=open("output.txt","w")
data=input_data.read()
data=data.split()
a=int(data[0])
b=int(data[1])
c=int(data[2])
if c==a*b:
    output_data.write("yes")
else:       
    output_data.write("no") 
output_data.write(c)
input_data.close()
output_data.close()