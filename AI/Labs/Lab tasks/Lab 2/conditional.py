originalSalary = int(input("Enter your salary: "))
netSalary = originalSalary
if originalSalary>30000:
    netSalary = originalSalary - (originalSalary*0.07)
elif originalSalary>=20000:
    netSalary = originalSalary - (originalSalary*0.05)
elif originalSalary<20000:
    netSalary = originalSalary
print("Your final salary is",netSalary)