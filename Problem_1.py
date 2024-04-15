
Given a list of length M, you need to print and find sum of the elements of list 

Input Format :

Line 1 : An int M 
Line 2 : M int elements of list seperated by ';'

Output Format:

Addition 

Constraints :
1 <= M <= 10^6

"""
m=[]
M=int(input("enter number of elements"))
l=input("enter M elemnts:" )
num=''
total_sum=0
m.append(l)
for ele in m:
    if ele==';':
        m.remove(ele)
for i in l:
    if i==';':
        total_sum+=int(num)
        num=''
    else:
        num+=i
total_sum+=int(num)
print(total_sum)
