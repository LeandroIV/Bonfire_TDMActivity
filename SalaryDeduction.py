class SalaryCalculator:
    """Class to compute salary deductions and net salary."""

    # Constants for deductions
    SSS_CONTRIBUTION = 1200  
    PHILHEALTH_RATE = 0.05  
    PAGIBIG_CONTRIBUTION = 100
    FIXED_TAX = 1875  

    def __init__(self, gross_salary):
        """Initialize with gross salary."""
        if not isinstance(gross_salary, (int, float)) or gross_salary <= 0:
            raise ValueError("Gross salary must be a positive number.")
        
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


def get_valid_salary():
    """Prompt user for a valid salary input."""
    while True:
        try:
            salary_input = input("Enter your monthly salary: ").strip()
            salary = float(salary_input)
            if salary <= 0:
                raise ValueError("Salary must be a positive number.")
            return salary
        except ValueError as error:
            print(f"Invalid input: {error}. Please enter a valid positive number.")


def main():
    """Main function to get user input and calculate salary deductions."""
    monthly_salary = get_valid_salary()
    salary_calculator = SalaryCalculator(monthly_salary)
    salary_calculator.compute_deductions()
    salary_calculator.display_breakdown()


if __name__ == "__main__":
    main()