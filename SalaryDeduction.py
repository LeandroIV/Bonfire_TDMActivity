def compute_deductions(salary):
sss = 1200
philhealth = (salary * 0.05) / 2
pagibig = 100
tax = 1875 # Assuming fixed value for simplicity

deductions = sss + philhealth + pagibig + tax
net_salary = salary - deductions

print("Gross Salary:", salary)
print("SSS Deduction:", sss)
print("PhilHealth Deduction:", philhealth)
print("Pag-IBIG Deduction:", pagibig)
print("Tax Deduction:", tax)
print("Total Deductions:", deductions)
print("Net Salary:", net_salary)

salary = float(input("Enter your monthly salary: "))
compute_deductions(salary)