input_data=open("input.txt","r")
a=input_data.read()
if int(a) > 0 :
    for i in range(1,int(a)+1):
        k=k+i
elif int(a) < 0:
    for i in range(int(a),2):
        k=k+i
else :
   k=1
output_data=open("output.txt","w")
output_data.write(str(a))
input_data.close()
output_data.close()