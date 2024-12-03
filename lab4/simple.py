input_data=open("input.txt","r")
data =input_data.read()
print ("Введите число ")
a=int(input())
k=0
if a %2 ==0:
        k=k+1
        if k==0:
            print("Y")
else:
        print("N") 
output_data=open("output.txt","w")
input_data.close()
output_data.close()