from decimal import Decimal as dec

input_data=open("input.txt","r")
n=input_data.read()
E=dec('2.7182818284590452353602875')
c=str(round(E,int(n)))
output_data=open("output.txt","w")
output_data.write(c)
input_data.close()
output_data.close()