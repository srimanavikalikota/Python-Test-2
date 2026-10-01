s=input("Enter the first value (s): ")
v=input("Enter the second value (v): ")

print(f"Type of x before swap:{type(s)}")

t=s
s=v
v=t
print("After swapping:")
print("s=",s)
print("v=",v)