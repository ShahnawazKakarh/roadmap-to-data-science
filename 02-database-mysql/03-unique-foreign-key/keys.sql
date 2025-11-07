-- Select all records from the employee table.
SELECT * FROM employee

-- Update the LastName of the employee with EmpID 6 to "Tanwar".
UPDATE employee SET LastName = "Tanwar"
WHERE EmpID = 6

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