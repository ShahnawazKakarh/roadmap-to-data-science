-- Switch to the SK database.
Select database();
USE SK;


-- Insert multiple employee records into the employee table.
INSERT INTO SK.employee VALUES ("Shahnawaz", "Khan", 28, 100000, "Islamabad");
INSERT INTO SK.employee VALUES ("Junaid", "Younas", 22, 150000, "Karachi");
INSERT INTO SK.employee VALUES ("Amjad", "Ali", 24, 200000, "Lahore");
INSERT INTO SK.employee VALUES ("Ajmal", "Zia", 23, 300000, "Peshawar");
INSERT INTO SK.employee VALUES ("Waleed", "Ali", 29, 400000, "Quetta");
INSERT INTO SK.employee VALUES ("Ahsan", "Khan", 27, 500000, "Faisalabad");

-- Task: Insert a new employee record with missing FirstName.
-- What will happen when you run the following query?
-- FirstName is missing in the VALUES clause.
INSERT INTO SK.employee (LastName, Age, Salary, Location) VALUES ("Raza", 20, 800000, "Hyderabad");

-- Drop the employee table to remove all records.
DROP TABLE SK.employee;

-- NOT NULL Constraint Example
-- Create the employee table with NOT NULL constraint on respective columns.
CREATE TABLE SK.employee (
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    Age INT NOT NULL,
    Salary INT NOT NULL,
    Location VARCHAR(100) NOT NULL
);

-- Insert multiple employee records into the employee table.
INSERT INTO SK.employee VALUES (1, "Shahnawaz", "Khan", 28, 100000, "Islamabad");
INSERT INTO SK.employee VALUES (2, "Junaid", "Younas", 22, 150000, "Karachi");
INSERT INTO SK.employee VALUES (3, "Amjad", "Ali", 24, 200000, "Lahore");
INSERT INTO SK.employee VALUES (4, "Ajmal", "Zia", 23, 300000, "Peshawar");
INSERT INTO SK.employee VALUES (5, "Waleed", "Ali", 29, 400000, "Quetta");
INSERT INTO SK.employee VALUES (6, "Ahsan", "Khan", 27, 500000, "Faisalabad");

-- Task: Describe the structure of the employee table.
DESC SK.employee;

-- Task: Retrieve all records from the employee table.
SELECT * FROM SK.employee;

-- Task: Insert a new employee record into the employee table.
INSERT INTO SK.employee (EmpID, FirstName, LastName, Age, Salary, Location) VALUES (7, "Haris", "Raza", 26, 600000, "Multan");

-- Drop the employee table to remove all records.
DROP TABLE SK.employee;

-- EmpID is missing as it will distinguish each record uniquely.
-- EmpID will be then primary key and auto incremented.
-- Task: Create the employee table with EmpID as primary key and auto incremented.
CREATE TABLE SK.employee (
    EmpID INT PRIMARY KEY AUTO_INCREMENT,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    Age INT NOT NULL,
    Salary INT NOT NULL,
    Location VARCHAR(100) NOT NULL
);

-- There is another way to define primary key and auto increment.
-- Task: Create the employee table with EmpID as primary key and auto incremented using another syntax.
CREATE TABLE SK.employee (
    EmpID INT AUTO_INCREMENT,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    Age INT NOT NULL,
    Salary INT NOT NULL,
    Location VARCHAR(100) NOT NULL,
    PRIMARY KEY (EmpID)
);

-- Select specific columns from the employee table.
SELECT FirstName, LastName FROM employee

-- Order BY: Sort the results based on Salary in descending order and limit the output to top 2 records.
SELECT FirstName, LastName, Salary FROM employee WHERE Salary >= 50000
ORDER BY Salary DESC
LIMIT 2

-- Delete the employee table.
DROP TABLE employee
SHOW tables