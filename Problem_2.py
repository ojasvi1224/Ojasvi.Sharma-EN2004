Problem: Knock Knock are you there?

Input Format:

1. Take M int input from the User 
2. Get M , seperated values from a user 
3. Enter a number 'N' you are looking for

Output Format:

1. Print index on console once Found or Print 'Better Luck Next Time' to the console


"""
M=int(input("Enter no. of elements:"))
m=[]
i=1
while i <= M:
  l=input("M Elements:")
  m.append(l)
  i=i+1
N=input("Enter number you're looking for:")
for index,ele in enumerate(m):
    if ele==N:
        print(index)
        break
    else:
        print('Better Luck Next Time')
