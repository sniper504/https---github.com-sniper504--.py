input_data=open("input.txt","r")
k=input_data.read()
a=9
b=(a-int(k))

c=str(k)+str(a)+str(b)
output_data=open("output.txt","w")
output_data.write(c)