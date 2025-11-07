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


-- Task: Update the salary of the employee with first_name 'Ahsan' to 550000.