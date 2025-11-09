-- Select all records from the employee table.
SELECT * FROM employee

-- Update the LastName of the employee with EmpID 6 to "Tanwar".
UPDATE employee SET LastName = "Tanwar"
WHERE EmpID = 6

-- Update the Salary of the employee with EmpID 4 to 350000.
UPDATE employee SET Salary = 350000
WHERE EmpID = 4

-- DDL Language: Defining and modifying database structures.
-- DDL Commands: Data Definition Language Commands like Create, Drop, Alter
-- Example: Create the employee table with EmpID as primary key and auto incremented.

-- What are about READ? DML or DDL?
-- READ is part of DML (Data Manipulation Language) as it involves retrieving data from the database without altering its structure.

-- DML Language: Defining and manipulating data within database structures.
-- DML Commands: Data Manipulation Language Commands like Insert, Update, Delete, Read
-- Example: Insert multiple employee records into the employee table.


-- Difference between MODIFY, ALTER and UPDATE? Which one is DDL and which one is DML?

-- ANSWER:
-- UPDATE is used to change existing data/records in a table, making it a DML command.
-- It modifies the data stored within the table without changing its structure.
-- Example: Updating an employee's salary or name.
-- Example of UPDATE:
UPDATE employee SET Salary = 600000 WHERE EmpID = 2;

-- ALTER is a DDL command used to change the structure of a database object, such as a table.
-- It allows you to add, delete, or modify columns and constraints in a table.
-- Example of ALTER:
ALTER TABLE employee ADD COLUMN Department VARCHAR(50);

-- MODIFY is a clause used within the ALTER command to change the definition of a column in a table, making it part of DDL.
-- It is specifically used to alter the data type, size, or other attributes of an existing column.
-- Example of MODIFY:
ALTER TABLE employee MODIFY COLUMN Salary INT NOT NULL;


-- Alter the employee table to modify the FirstName column to have a length of 60 characters.
ALTER TABLE SK.employee MODIFY FirstName varchar(60);

-- Delete the employee with EmpID 6 from the employee table.
DELETE FROM employee
WHERE EmpID = 6

-- Drop the employee table to remove all records.
DROP TABLE employee

-- Aggregate Functions
-- Aggregate functions perform a calculation on a set of values and return a single value.
-- Common aggregate functions include COUNT, SUM, AVG, MAX, and MIN.
SELECT COUNT(*) FROM SK.employee;
SELECT COUNT(*) As Total_Num_Employee FROM employee

SELECT AVG(Salary) As Avg_Salary FROM employee
SELECT MAX(Salary) As Max_Salary FROM employee
SELECT MIN(Salary) As Min_Salary FROM employee
SELECT SUM(Salary) As Total_Cost_Company FROM employee

-- Create Courses table with CourseID as primary key and auto incremented.
CREATE TABLE Courses(
CourseID INT AUTO_INCREMENT,
CourseName	varchar(50) NOT NULL,
CourseDuration INT NOT NULL,
CourseFee INT NOT NULL,
PRIMARY KEY(CourseID)
)

-- Show all tables in the current database.
SHOW TABLES

-- Create Students table with StudentID as primary key and auto incremented.
CREATE TABLE Students(
StudentID	INT	AUTO_INCREMENT,
S_FirstName	varchar(50) NOT NULL,
S_LastName	varchar(50) NOT NULL,
S_Email varchar(50) NOT NULL,
S_Phone	varchar(50) NOT NULL,
S_EnrollmentDate timestamp NOT NULL,
Selected_Course	INT NOT NULL,
Years_Of_Exp INT NOT NULL,
S_Company varchar(50) NOT NULL,
Batch_Start_Date timestamp NOT NULL,
Location varchar(50) NOT NULL,
PRIMARY KEY(StudentID)
)