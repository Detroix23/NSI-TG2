# SQL Requests cheat sheet.

## Database creation.

Create a database `Name`:
```sql
CREATE DATABASE <Name>;
```

Select a database `Name`:
```sql
USE <Name>;
```

Modify a database `Name`:
```sql
ALTER DATABASE <Name>;
```

Delete a database `Name`:
```sql
DROP DATABASE <Name>;
```

## Table edition.

Create an example table:
```sql
CREATE TABLE Employees (
	id INT PRIMARY_KEY,
	first_name VARCHAR(50),
	last_name VARCHAR(50),
	salary DECIMAL(10, 2),
);
```

Append new records:
```sql
INSERT INTO Employees (id, first_name, last_name, salary)
VALUES
	(1, "Bob", "Lenon", 10000.00),
	(2, "Lob", "Benon", 14000.00);
```

Add a new attribute `new_column` to table `Name`:
```sql
ALTER TABLE Name
ADD COLUMN new_column INT;
```

Select data in table:
```sql
SELECT * FROM Employees;
SELECT (last_name, first_name) FROM Employees;

SELECT DISTINCT last_name FROM Employees;
```

Conditions:
```sql
SELECT * FROM Employees
WHERE 
	id = 5
	OR last_name IN ("Bob", "Frank")
	AND salary BETWEEN 50000.00 AND 150000.00
	AND NOT first_name IS NULL;
```

Update values:
```sql
UPDATE Employees
SET salary = 100000.00
WHERE first_name = "Bob";

DELETE FROM Employees
WHERE id = 1;
```

Join tables:
```sql
SELECT * FROM Employees
JOIN department ON Employees.department_id = Departments.id
WHERE department = "HR";

SELECT * FROM Employees
CROSS JOIN Departments;
```

## Functions.

Sorting:
```sql
SELECT * FROM Employees
ORDER BY salary DESC
```

Aggregation:
```sql
SELECT COUNT(*) FROM Employees;
SELECT SUM(salary) FROM Employees;
SELECT AVG(salary) FROM Employees;
```

Wildcard `%`:
```sql
SELECT * FROM Employees
WHERE first_name LIKE "B%"
```

