def compute_deductions(gross_salary):
    """Calculate and display salary deductions and net salary."""

    # Constants for deductions
    SSS_CONTRIBUTION = 1200  
    PHILHEALTH_RATE = 0.05  
    PAGIBIG_CONTRIBUTION = 100
    FIXED_TAX = 1875  

    # Compute deductions
    philhealth_deduction = (gross_salary * PHILHEALTH_RATE) / 2
    total_deductions = SSS_CONTRIBUTION + philhealth_deduction + PAGIBIG_CONTRIBUTION + FIXED_TAX
    net_salary = gross_salary - total_deductions

    # Display breakdown of deductions
    print("\nSalary Breakdown")
    print("-" * 30)
    print(f"Gross Salary:       {gross_salary:,.2f}")
    print(f"SSS Deduction:      {SSS_CONTRIBUTION:,.2f}")
    print(f"PhilHealth Deduction: {philhealth_deduction:,.2f}")
    print(f"Pag-IBIG Deduction: {PAGIBIG_CONTRIBUTION:,.2f}")
    print(f"Tax Deduction:      {FIXED_TAX:,.2f}")
    print(f"Total Deductions:   {total_deductions:,.2f}")
    print(f"Net Salary:         {net_salary:,.2f}\n")

# Get user input and compute deductions
try:
    monthly_salary = float(input("Enter your monthly salary: "))
    if monthly_salary < 0:
        raise ValueError("Salary cannot be negative.")
    compute_deductions(monthly_salary)
except ValueError as error:
    print(f"Invalid input: {error}")
