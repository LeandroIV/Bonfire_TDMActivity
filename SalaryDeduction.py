class SalaryCalculator:
    """Class to compute salary deductions and net salary."""

    # Constants for deductions
    SSS_CONTRIBUTION = 1200  
    PHILHEALTH_RATE = 0.05  
    PAGIBIG_CONTRIBUTION = 100
    FIXED_TAX = 1875  

    def __init__(self, gross_salary):
        """Initialize with gross salary."""
        self.gross_salary = gross_salary
        self.deductions = {}
        self.net_salary = 0

    def compute_deductions(self):
        """Calculate salary deductions."""
        self.deductions["SSS"] = self.SSS_CONTRIBUTION
        self.deductions["PhilHealth"] = (self.gross_salary * self.PHILHEALTH_RATE) / 2
        self.deductions["Pag-IBIG"] = self.PAGIBIG_CONTRIBUTION
        self.deductions["Tax"] = self.FIXED_TAX

        total_deductions = sum(self.deductions.values())
        self.net_salary = self.gross_salary - total_deductions

    def display_breakdown(self):
        """Display detailed salary breakdown with proper alignment."""
        print("\nSalary Breakdown")
        print("-" * 35)
        print(f"{'Gross Salary:':<25} {self.gross_salary:>10,.2f}")
        for name, amount in self.deductions.items():
            print(f"{name + ' Deduction:':<25} {amount:>10,.2f}")
        print(f"{'Total Deductions:':<25} {sum(self.deductions.values()):>10,.2f}")
        print(f"{'Net Salary:':<25} {self.net_salary:>10,.2f}\n")


def main():
    """Main function to get user input and calculate salary deductions."""
    try:
        monthly_salary = float(input("Enter your monthly salary: "))
        if monthly_salary < 0:
            raise ValueError("Salary cannot be negative.")

        # Create an instance of SalaryCalculator
        salary_calculator = SalaryCalculator(monthly_salary)
        salary_calculator.compute_deductions()
        salary_calculator.display_breakdown()

    except ValueError as error:
        print(f"Invalid input: {error}")


if __name__ == "__main__":
    main()
