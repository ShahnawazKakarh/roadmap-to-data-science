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

-- Alter and Update Commands Difference?
-- Alter command is used to modify the structure of a database or schema of the database or object like a table,
-- whereas Update command is used to modify the data within the table. (DML)


-- Alter the employee table to modify the FirstName column to have a length of 60 characters.
ALTER TABLE SK.employee MODIFY FirstName varchar(60);

-- Delete the employee with EmpID 6 from the employee table.
DELETE FROM employee
WHERE EmpID = 6

-- Drop the employee table to remove all records.
DROP TABLE employee

-- Aggregate Functions
SELECT COUNT(*) As Total_Num_Employee FROM employee
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