input_data=open("input.txt","r")
a=input_data.read()
b=25
a=str(int(a)*(a))+str(b)
output_data=open("output.txt","w")
output_data.write(a)
input_data.close()
output_data.close()