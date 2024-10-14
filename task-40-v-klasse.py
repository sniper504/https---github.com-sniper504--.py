input_data=open("input.txt","r")
data =input_data.read()
output_data=open("output.txt","w")
data=data.split()
n=int(data[0])
a=2**n
output_data.write(str(a))
input_data.close()
output_data.close()