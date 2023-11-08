print("YUSUF AND SONS")
print("Please fill in the required information correct")
p = float(input("What is your principal? "))
r = float(input("what is your interest rate? "))
n = int(input("Enter the number of times interest applies per time period? "))
t = float(input("Enter the number of time periods elapsed? "))


SI = p* (1 + r*t)

CI = p* (1 + r/n)**(n*t)

print(f'simple interest = {SI}, Compound interest = {CI}')
