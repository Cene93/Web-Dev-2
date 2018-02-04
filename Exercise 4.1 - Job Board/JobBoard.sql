CREATE TABLE JobAd (
	ID INTEGER PRIMARY KEY AUTOINCREMENT,
	JobTypeID INTEGER,
	ModeratorID INTEGER,
	CompanyID INTEGER,
	RegionID INTEGER,
	CategoryID INTEGER
);

CREATE TABLE Users (
	ID INTEGER PRIMARY KEY AUTOINCREMENT,
	FirstName TEXT,
	LastName TEXT,
	IsEmployed INTEGER
);

CREATE TABLE Company (
	ID INTEGER PRIMARY KEY AUTOINCREMENT,
	Name TEXT
);

CREATE TABLE Region (
	ID INTEGER PRIMARY KEY AUTOINCREMENT,
	Name TEXT
);

CREATE TABLE JobType (
	ID INTEGER PRIMARY KEY AUTOINCREMENT,
	Type TEXT
);

CREATE TABLE Category (
	ID INTEGER PRIMARY KEY AUTOINCREMENT,
	Category TEXT
);

CREATE TABLE Moderator (
	ID INTEGER PRIMARY KEY AUTOINCREMENT,
	UserID INTEGER,
	CompanyID INTEGER
);

CREATE TABLE Application (
	ID INTEGER PRIMARY KEY AUTOINCREMENT,
	UserID INTEGER,
	JobAdID INTEGER
);
    
    
--//////////////////  DATA  /////////////////////////    

INSERT INTO Users (FirstName, LastName, IsEmployed)
	VALUES  ('Daniel', 'Morgan', 0),
			('Leo', 'Harvey', 1),
			('Julia', 'Gordon', 1),
			('Alicia', 'Day', 0),
			('Ryan', 'Wilson', 0),
			('Liam', 'Edwards', 1),
			('Karoline', 'Mueller', 1),
			('Robin', 'Schulman', 1),
			('Philipp', 'Krieger', 0),
			('Pia', 'Schaeffer', 0),
			('Hannah', 'Tangemann', 0),
			('Lina', 'Oberhauser', 0),
			('Christoph', 'Fichte', 0),
			('Benjamin', 'Maisel', 0),
			('Reiner', 'Hochmeister', 0),
			('William', 'Dawson', 0),
			('Samuel', 'Campbell', 0),
			('Gracie', 'Parker', 0),
			('Sarah', 'Dudley', 0),
			('Danny', 'Rogers', 0);

INSERT INTO Company (Name)
	VALUES  ('Alligator Systems'),
			('Apricot Solutions'),
			('Whirlpool Limited'),
			('Crux Corporation'),
			('Spicurity');
			
INSERT INTO JobType (Type)
	VALUES  ('Full-Time'),
			('Part-Time'),
			('Student'),
			('Internship');
			
INSERT INTO Category (Category)
	VALUES  ('Accounting'),
			('IT'),
			('Marketing'),
			('Sales'),
			('Web Development'),
			('Web Design');

INSERT INTO Region (Name)
	VALUES  ('Los Angeles, CA'),
			('San Francisco, CA'),
			('New York, NY'),
			('Berlin, GER'), 
			('München, GER');
			

INSERT INTO Moderator (UserID, CompanyID)
	VALUES  (2, 1),
			(3, 2),
			(6, 3),
			(7, 4),
			(8, 5);
			
INSERT INTO JobAd (JobTypeID, ModeratorID, CompanyID, RegionID, CategoryID)
	VALUES  (3, 1, 1, 3, 4),
			(1, 1, 1, 3, 5),
			(4, 5, 5, 4, 3),
			(1, 4, 4, 5, 1),
			(2, 4, 4, 5, 2),
			(3, 3, 3, 2, 6),
			(3, 2, 2, 1, 2);

INSERT INTO Application (UserID, JobAdID)
	VALUES  (1, 1),
			(4, 2),
			(5, 3),
			(9, 4),
			(10, 5),
			(11, 6),
			(12, 7),
			(13, 3),
			(14, 5),
			(15, 1),
			(16, 3),
			(17, 7),
			(18, 4),
			(19, 6),
			(20, 3);
            
			
--//////////////////  QUERIES  /////////////////////////            

            
SELECT Region.Name, COUNT(*) FROM JobAd
	JOIN Region On Region.ID = JobAd.RegionID
	GROUP BY Region.Name

	
SELECT Category.Category, Company.Name FROM JobAd
	JOIN Category ON JobAd.CategoryID = Category.ID
	JOIN Company ON JobAd.CompanyID = Company.ID
	WHERE Category.Category = 'IT'
	

SELECT COUNT(*) FROM Application
	JOIN JobAd ON Application.JobAdID = JobAd.ID
	JOIN Category ON JobAd.CategoryID = Category.ID
	JOIN Users ON Application.UserID = Users.ID
	WHERE Category.Category = 'Accounting'
	


SELECT COUNT(*) FROM JobAd
	JOIN JobType ON JobAd.JobTypeID = JobType.ID
	WHERE JobType.Type = 'Full-Time'
	
