select * 
from employee;

select *
from department;

/*
Write a query to generate a list of employees with the following characteristics:
· All employees must be returned.

· The report must include the following columns from the table: Id, name, department_id, email.

· The report must also include the following calculated columns: The length of the email. The number of employees from the same department who have an email of the same length.

· The report must be ordered by department_id and length of the email column.
*/



/*
Write a query to generate a report of the employees, which includes at least the following columns:
· Id

· Name

· Hire_date,

· A count of the number of employees hired in the same year than the current employee or in the previous year.

The results must be ordered by the hire date.
*/



/*
Write a query to generate a list of all of the departments including their ID, name, and monthly budget, but also include a column that shows the accumulated budget (the sum of the budget of previous departments plus the current one). To decide the order in which the budgets are accumulated you must sort them by smallest to greatest budget.
*/


/*
Write a query to list all the employees. The result must include their name, department id, hire date, and a column called “hire_order” which is a number that indicates the order in which they were hired. This order is related to the department where they work only, so, the first employee that was hired in each department will have a hire_order of 1.
*/


/*
Write a query that returns the name, birthdate, and department id of an employee who was born in 1995, preferably from the ACCOUNTING department. If no employee from that department was born in 1995, return one from any other department.
*/


/*
Write a query that lists the different salaries that appear in the employee table. For each salary include a comma-separated list of the names of the employees that earn that amount. The list of employees for each salary must be ordered by the name of the employee, and the final result set must be ordered by salary from greatest to smallest.
*/


/*
Write a query to generate a list of all employees from the ACCOUNTING and HUMAN RESOURCES departments, ordered by department and birthdate. For every employee, the report must include the name, birthdate, and the name of the employee from the same department who follows him/her if you order them by age.
*/


/*
Write a query to generate a list of employees with the following conditions:
· The list must include only the employee with the highest salary in each department.

· It must include ID, name, salary, department_id, and an additional column with the ID of the employee with the second-highest salary in his/her department.

· Hint: You might need to use some kind of subquery.
*/


/*
Write a query to return the name and hire date of the first employee hired in each department.
The results must include the department_id, name of the employee and their hire date, and must be ordered by department id.
*/


/*
Write a query that will produce an employees’ report with the following information for each employee:
· Id, name, and department_id of the employee.

· Name of the employee who was the first hire in the department where the employee works.

· Salary of the employee who was the first hire in the department where the employee works.

· Bonus of the top earner among the employees who were hired in the same year as the employee, regardless of their department. If the bonus is null, the bonus must be shown as 0.

The report must be ordered by department_id and hire_date.
*/



