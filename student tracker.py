print("Student grade tracker: ")
print("Enter your Five subjects marks:")
e=int(input("English marks:"))
m=int(input("Maths marks:"))
s=int(input("Science marks:"))
ss=int(input("Social science marks:"))
l=int(input("Language marks:"))
total=e+m++s+ss+l
avg=total/5
if(avg<=30):
    print("Bad, need to improve")
elif(avg>=30 and avg<=60):
    print("Good marks!")
else:
    print("Excellent ! keep it up ")
    
    
