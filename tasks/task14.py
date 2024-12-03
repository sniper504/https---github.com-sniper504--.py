input_data=open("input.txt","r")
data =input_data.read()
output_data=open("output.txt","a")
data = data.split() 
a=int(data[0])
b=int(data[1])
while a!=0 or  b!=0:
 if a>b: a=a%b
else: b=b%a
if a==0:
    nod=b
else: 
    nod=a
nok=(data[0]*data[1])/nod
output_data.write(str(nok))
input_data.close()
output_data.close()