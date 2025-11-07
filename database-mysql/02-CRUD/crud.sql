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

-- Task: Retrieve all records from the employee table.
SELECT * FROM SK.employee;

-- Task: Insert a new employee record into the employee table.
INSERT INTO SK.employee (FirstName, LastName, Age, Salary, Location) VALUES ("Haris", "Raza", 26, 600000, "Multan");

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
INSERT INTO SK.employee VALUES ("Shahnawaz", "Khan", 28, 100000, "Islamabad");
INSERT INTO SK.employee VALUES ("Junaid", "Younas", 22, 150000, "Karachi");
INSERT INTO SK.employee VALUES ("Amjad", "Ali", 24, 200000, "Lahore");
INSERT INTO SK.employee VALUES ("Ajmal", "Zia", 23, 300000, "Peshawar");
INSERT INTO SK.employee VALUES ("Waleed", "Ali", 29, 400000, "Quetta");
INSERT INTO SK.employee VALUES ("Ahsan", "Khan", 27, 500000, "Faisalabad");

-- Task: Update the salary of the employee with FirstName 'Ahsan' to 550000.