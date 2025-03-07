# Bonfire_TDMActivity
Lab Activity for our Software Implementation and Management
Identified Technical Debt
Poor Naming Conventions

The function name compute_deductions is misleading since it prints results rather than returning them.
Variable names like sss, philhealth, pagibig, and tax could be clearer, e.g., sss_contribution, philhealth_contribution, etc.
Lack of Modular Functions

The function mixes calculation and output, making it harder to reuse.
Better structure would involve separate functions for computing deductions and displaying results.
Hardcoded Values Instead of Dynamic Inputs

sss = 1200, pagibig = 100, and tax = 1875 are fixed values. These should be configurable or computed dynamically.
Tax, in particular, is usually based on salary brackets, not a fixed value.
No Error Handling

No validation for user input (e.g., negative salary values or non-numeric input).
Potential runtime error if the user enters invalid data.
Code Duplication

salary = float(input("Enter your monthly salary: ")) is written outside the function, leading to poor function encapsulation.
Printing results within the function makes it hard to reuse elsewhere.