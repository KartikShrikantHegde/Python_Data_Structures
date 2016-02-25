# count, avg, sum in a list

K=[]
sum=0
count=0
while True:
    input=raw_input("Enter the number\n")
    if (input=='done'):
        break
    value=float(input)
    K.append(value)

for i in K:
    sum=sum+i
    count=count+1

print "Sum is :", sum
print "Average is :",sum/len(K)

