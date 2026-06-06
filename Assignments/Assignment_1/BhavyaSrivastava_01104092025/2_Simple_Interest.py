# 2- Find Simple Interest 

principal = float(input("Enter Principal Amount: "))
rate = float(input("Enter Rate of Interest: "))
time = float(input("Enter Time (years): "))

simple_interest = (principal * rate * time) / 100
print("Simple Interest =", simple_interest)