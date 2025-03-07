# Bonfire_TDMActivity
Lab Activity for our Software Implementation and Management

# Identified Technical Debt & Improvements

## 1. Poor Naming Conventions  
- **Issue:** The function name `compute_deductions` was misleading as it printed results instead of returning them.  
- **Fix:** Renamed functions and variables to accurately describe their purpose.  
  - Example: `sss` → `sss_contribution`, `pagibig` → `pagibig_contribution`, etc.  

## 2. Lack of Modular Functions  
- **Issue:** Salary calculation and printing were combined in a single function.  
- **Fix:** Separated logic into individual functions:  
  - `compute_deductions()` – Calculates deductions  
  - `display_breakdown()` – Displays results  

## 3. Hardcoded Values Instead of Dynamic Inputs  
- **Issue:** Deductions like SSS (₱1200), Pag-IBIG (₱100), and Tax (₱1875) were hardcoded.  
- **Fix:**  
  - Replaced fixed values with constants.  
  - Implemented dynamic tax computation instead of using a fixed tax value.

## 4. No Error Handling  
- **Issue:** No validation for invalid salary inputs (negative numbers, non-numeric values).  
- **Fix:**  
  - Added input validation to ensure salary input is numeric and positive.  
  - Implemented exception handling for robust user input processing.  

## 5. Code Duplication  
- **Issue:** Salary input was handled outside the function, reducing encapsulation.  
- **Fix:**  
  - Encapsulated salary processing logic into a `SalaryCalculator` class.  
  - Reduced redundancy by ensuring input processing is handled in a single place.  

## 6. Converted to Object-Oriented Programming (OOP)  
- **Issue:** Code was procedural, making future scalability difficult.  
- **Fix:**  
  - Introduced a `SalaryCalculator` class to encapsulate related logic.  
  - Enhanced modularity and maintainability.  

## Final Improvements  
✅ **Improved Code Readability:** Implemented proper formatting and comments.  
✅ **Converted to Object-Oriented Programming (OOP):** Introduced a `SalaryCalculator` class to enhance modularity.  
✅ **Enhanced User Experience:** Improved output formatting for better clarity.  
✅ **Error Handling & Input Validation:** Ensured the program does not crash due to invalid inputs.    


## Challenges & Solutions
- The challenged we've experienced was that me as the lead developer had changes in our readme and didn't push it. Then our documenter updated the readme and pushed it.
I forgot my changes in readme and proceed to refractoring but then I noticed that I didnt also pushed the initial commit and I had to do it again. After that, errors shpwed up
saying "error: Pulling is not possible because you have unmerged files." the file became red text.
- For our solution, I had to fix the merge conflict by accepting both changes and then commited and push it again.