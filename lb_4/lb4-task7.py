input_data=open("input.txt","r")
output_data=open("output.txt","w")
a=input_data.read()
if a > b and a > c:
    output_data.write(str(a))
elif b>=c and b>=a:
    output_data.write(str(b))
else:
    output_data.write(c)    
output_data.write(a)
input_data.close()
output_data.close()