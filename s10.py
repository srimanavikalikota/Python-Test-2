p=int(input("Enter the principal amount:"))
r=int(input("Enter the rate:"))
t=int(input("Enter the time:"))

i=(p*r*t)/100
total_amount=p+i
print(f"simple interest:{i}")
print(f"total_amount:{total_amount}")

print(f"Type of principal:{type(p)}")
print(f"Type of interest:{type(i)}")
