/*
Full stack Development Assignment 1 SQL code
Written By Harry Parker
Harry Parker : 29191718@students.lincoln.ac.uk
*/

-- =========================================================
-- STEP 1: CREATE DATABASE AND TABLES
-- =========================================================
CREATE DATABASE FullstackDevelopment_Assignment1; -- Creates the Database/Schema that I will be working in
USE FullstackDevelopment_Assignment1; -- Tells the Software which Database I will be working in

CREATE TABLE  tbl_DriversLicense( -- Creates table and names it
    DriversLicenseID int PRIMARY KEY NOT NULL, -- Adds column for Primary Key
    DriversLicenseOrigin varchar(50) -- Adds Column for Drivers License Origin
);  

CREATE TABLE  tbl_Person( -- Creates table and names it 
    PersonID int PRIMARY KEY    NOT NULL AUTO_INCREMENT, -- Creates Primary Key for Person table 
    DriversLicenseID int,
    FOREIGN KEY (DriversLicenseID) REFERENCES tbl_DriversLicense(DriversLicenseID), -- Creates Foreign Key to make it so drivers license and person tables can be joined to share information 
    Forename varchar(50), -- set at 50 characters as most names do not exceed this amount
    Surname varchar(50), -- set at 50 characters as most names do not exceed this amount
    Address varchar(100), -- set at 100 characters as most addresses do not exceed this amount
    State varchar(100),  -- set at 100 characters as most States do not exceed this amount
    ZipCode varchar(5),  -- set at 5 characters as most ZipCodes do not exceed this amount
    City varchar(50),  -- set at 50 characters as most City names do not exceed this amount
    DOB varchar(10),   -- set at 10 characters as most DOB should not take more than that
    Height varchar(5),  -- set at 5 characters as Height should not exceed this amount 
    Weight varchar(5),  -- set at 5 characters as Height should not exceed this amount 
    EyeColour varchar(6),  -- set at 6 characters as Eye colour should not exceed this amount
    PhoneNum varchar(12),  -- set as varchar 12 as phone numbers only take set amounts of numbers, and numbers starting with 0 cause issues 
    FOREIGN KEY (DriversLicenseID) REFERENCES tbl_DriversLicense(DriversLicenseID) -- Creates Foreign Key to make it so people can have Violations
);

CREATE TABLE  tbl_Officers( -- Creates and names table 
    OfficerID int PRIMARY KEY NOT NULL AUTO_INCREMENT,
    PersonID int,
    FOREIGN KEY (PersonID) REFERENCES tbl_Person(PersonID), -- Sets foreign key
    ViolationsRecorded int
);

CREATE TABLE  tbl_ViolationTypes( -- Creates table and names it
    ViolationTypeID int PRIMARY KEY NOT NULL AUTO_INCREMENT, -- Adds column for Primary Key
    ViolationName varchar(100), -- Name of violation likely wont exceed 100 chars
    ViolationClass varchar(10) -- Penalty amount likely not higher than 25 chars
);

CREATE TABLE  tbl_Violations( -- Creates table and names it
    ViolationsID int PRIMARY KEY NOT NULL AUTO_INCREMENT, -- Adds column for Primary Key
    OfficerID int,
    FOREIGN KEY (OfficerID) REFERENCES tbl_Officers(OfficerID), -- Sets foreign key
    ViolationTypeID int,
    FOREIGN KEY (ViolationTypeID) REFERENCES tbl_ViolationTypes(ViolationTypeID), -- Sets foreign key
    Location varchar(100), -- Location of violation likely not more than 100 chars
    District varchar(100),
    ViolationDate varchar(10),
    ViolationTime varchar(8),
    ViolatorID int,
    FOREIGN KEY (ViolatorID) REFERENCES tbl_Person(PersonID) -- Sets foreign key
);

Create TABLE tbl_VehicleMake(
    VehicleMakeID int PRIMARY KEY NOT NULL AUTO_INCREMENT,
    VehicleName varchar(50), -- varchar 50 should not be exceeded in naming cars 
    DriveType varchar(3), -- AWD, FWD, RWD 
    VehicleManual bool, -- fale is automatic
    VehicleBrand varchar(50),
    CarWeight int,
    VehicleYear int
);

CREATE TABLE  tbl_Vehicles( -- Creates table and names it
    VIN int PRIMARY KEY NOT NULL AUTO_INCREMENT, -- Adds column for Primary Key
    VehicleLicense varchar(50), -- set at 50 characters as Vehicle license would likely not exceed this amount
    VehicleState varchar(50),-- set at 50 characters as Vehicle state would likely not exceed this amount
    VehicleColour varchar(35), -- set at 50 characters as longest vehicle colour is 35 chars at "British Racing Green Ultra Metallic"
    VehicleMakeID int,
    FOREIGN KEY (VehicleMakeID) REFERENCES tbl_VehicleMake(VehicleMakeID),
    VehicleAddress varchar(50), -- set as 50 as address likely isn't longer than 50
    VehicleOwner int,
    FOREIGN KEY (VehicleOwner) REFERENCES tbl_Person(PersonID) -- Sets foreign key
);

-- =========================================================
-- STEP 2: POPULATE TABLES
-- =========================================================

-- =========================================================
-- Populating Violations Types
-- =========================================================

INSERT INTO tbl_ViolationTypes(ViolationName, ViolationClass)
VALUES
("Abandonment of child under two","C"),
("Giving false statements to procure cremation","I"),
("Burglary (domestic)","E"),
("Burglary (non-domestic)","E"),
("Abduction of woman by force","J"),
("Forgery of driving documents","H"),
("Armed robbery","B");

-- =========================================================
-- Populating Person Table
-- =========================================================

INSERT INTO tbl_DriversLicense (DriversLicenseID, DriversLicenseOrigin)
VALUES
-- Person 1
(1, 'Mississippi State'),
-- Person 2
(2, 'Indiana'),
-- Person 3
(3, 'Texas'),
-- Person 4
(4, 'Kansas'),
-- Person 5
(5, 'Oklahoma');

INSERT INTO tbl_Person(DriversLicenseID, Forename, Surname, Address, State, ZipCode, City, DOB, Height,  Weight, EyeColour, PhoneNum)
VALUES
-- Person 1
(1,"Ryan","Graham","30367 Alvarez Motorway","Mississippi State", "57843", "West Laurenfort", "2001-11-14","6.1" ,"113.2", "Grey", "07968178644"),
-- Person 2
(2,"Rose","Davis","566 Peterson Skyway Apt. 948","Indiana State", "12346", "Coxton", "1934-12-19","6.4" ,"52.2", "Blue", "07549552762"),
-- Person 3
(3,"Denise","Carter","723 Phillips Tunnel Suite 779","Texas State", "06724", "North Steve", "1984-02-16","6.3" ,"92.4", "Brown", "07226683061"),
-- Person 4
(4,"John","Morgan","79850 Jermaine Burgs Apt. 950","Kansas State", "30767", "Dianaview", "1961-09-19","6.6" ,"63.8", "Grey", "07990673772"),
-- Person 5
(5,"Michele","Sharp","04820 Nicole Points Apt. 978","Oklahoma State", "76305", "Kristenberg", "1992-04-26","5.2" ,"56.8", "Blue", "07529054736");

-- =========================================================
-- Populating Officers
-- =========================================================

INSERT INTO tbl_Officers(PersonID)
VALUES
-- Officer 1
(1),
-- Officer 2
(5);

-- =========================================================
-- Populating Violations
-- =========================================================

INSERT INTO tbl_Violations(OfficerID, ViolationTypeID, Location, District, ViolationDate, ViolationTime, ViolatorID)
VALUES
-- Officer 1
(1,7,"Texas","County Sheriffs Office", "12/03/1950", "16:42:59",2),
(1,1,"Oklahoma","Oklahoma City Police Department", "27/06/2003", "11:27:48",3),
(1,5,"Kansas","Kansas City Police Department", "29/08/1998", "07:28:32",4),
(1,1,"Texas", "County Sheriffs Office", "03/02/1996", "14:56:12",3),
-- Officer 2
(2,4,"Indiana","Indianapolis Metropolitan Police Department (IMPD)", "13/05/2000", "18:32:47",2);

-- =========================================================
-- Populating VehicleMakes
-- =========================================================
INSERT INTO tbl_VehicleMake(VehicleName ,DriveType, VehicleManual, VehicleBrand,CarWeight, VehicleYear)
VALUES
("Toyota Corolla", "FWD", false, "Toyota", 1290, 2019),
("BMW M3", "RWD", true, "BMW", 1725, 2020),
("Ford F-150", "AWD", false, "Ford", 2040, 2021);

-- =========================================================
-- Populating Vehicles
-- =========================================================
INSERT INTO tbl_Vehicles(VehicleLicense, VehicleState, VehicleColour, VehicleMakeID, VehicleAddress, VehicleOwner)
VALUES
("JTN-4821", "Texas", "Red", 1, "30367 Alvarez Motorway",1 ),
("7KZP310", "Indiana", "Green", 2, "566 Peterson Skyway Apt. 948",2 ),
("TXR-5M82", "Mississippi", "Orange", 3, "30367 Alvarez Motorway",5 );

-- =========================================================
-- ROLEs
-- =========================================================
-- Create Users login and passwords
CREATE USER 'Admin'@'%' IDENTIFIED BY 'AdminPassword';
CREATE USER 'Officer'@'%' IDENTIFIED BY 'OfficerPassword';
CREATE USER 'Civilian'@'%' IDENTIFIED BY 'CivilianPassword';

GRANT ALL PRIVILEGES ON FullstackDevelopment_Assignment1.* TO 'Admin'@'%'; -- Allows admins to create and delete and just do whatever they want 
-- Only admins have access for vehicle types as officers would not have to create new vehicle types
GRANT SELECT, INSERT, UPDATE ON FullstackDevelopment_Assignment1.tbl_Violations TO 'Officer'@'%'; -- Allows officers to select, insert and update, but not delete 
GRANT SELECT ON FullstackDevelopment_Assignment1.tbl_Person TO 'Officer'@'%';
GRANT SELECT ON FullstackDevelopment_Assignment1.tbl_ViolationTypes TO 'Officer'@'%';
GRANT SELECT ON FullstackDevelopment_Assignment1.tbl_Vehicles TO 'Officer'@'%';
-- Allows the Civilians to view violations but nothing else 
GRANT SELECT ON FullstackDevelopment_Assignment1.tbl_Violations TO 'Civilian'@'%';

FLUSH PRIVILEGES;

-- =========================================================
-- Making Queries
-- =========================================================
-- Query 1: Create a new record for a correction notice 
INSERT INTO tbl_Violations(OfficerID, ViolationTypeID, Location, District, ViolationDate, ViolationTime, ViolatorID)
VALUES(2,5,"Oklahoma","County Sheriffs Office", "27/05/2025", "19:28:29",4);

-- Query 2: Update a correction notice: Previous query input incorrectly, needs updating 
UPDATE tbl_Violations 
SET Location = "Oklahoma Police Department"
WHERE OfficerID = 2
    AND ViolationTypeID =5
    AND Location = "Oklahoma"
    AND ViolatorID = 4
    AND ViolationDate = "27/05/2025"
    AND ViolationTime = "19:28:29";

-- Query 3: Delete an outdated or incorrect vehicle record
-- To start, I need an outdated or incorrect vehicle record, so I'll make one now
INSERT INTO tbl_Vehicles(VehicleLicense, VehicleState, VehicleColour, VehicleMakeID, VehicleAddress, VehicleOwner)
VALUES("ABD123", "Canada", "Green", 1, "123, springfield road", 1);

DELETE FROM tbl_Vehicles
WHERE VehicleLicense = "ABD123"
    AND VehicleState = "Canada"
    AND VehicleColour = "Green"
    AND VehicleMakeID = 1
    AND VehicleAddress = "123, springfield road"
    AND VehicleOwner = 1;

-- Query 4: List all violations with violator names, officer names, and violation type details
SELECT 
    v.ViolationsID,
    vt.ViolationName,
    violator.Forename AS ViolatorForename,
    violator.Surname AS ViolatorSurname,
    officerPerson.Forename AS OfficerForename,
    officerPerson.Surname AS OfficerSurname
FROM tbl_Violations v
JOIN tbl_Person violator
    ON v.ViolatorID = violator.PersonID
JOIN tbl_Officers o
    ON v.OfficerID = o.OfficerID
JOIN tbl_Person officerPerson
    ON o.PersonID = officerPerson.PersonID
JOIN tbl_ViolationTypes vt
    ON v.ViolationTypeID = vt.ViolationTypeID
ORDER BY v.ViolationsID;

-- Query 5: Retrieve all vehicles owned by people who have received violations
SELECT DISTINCT v.* -- Distinct makes it so if someone has more than one violation, there car will only appear once 
FROM tbl_Vehicles v
JOIN tbl_Violations viol
    ON v.VehicleOwner = viol.ViolatorID;

-- Query 6: Show violations by Location and officer, grouped by district

SELECT  
    v.District,
    v.Location,
    CONCAT(op.Forename, ' ', op.Surname) AS OfficerName,
    COUNT(v.ViolationsID) AS NumberOfViolations
FROM tbl_Violations v
JOIN tbl_Officers o ON v.OfficerID = o.OfficerID
JOIN tbl_Person op ON o.PersonID = op.PersonID
GROUP BY v.District, v.Location, OfficerName
ORDER BY v.District, v.Location, OfficerName;

-- Query 7:Count of violations per officer over the past 25 Years
SELECT 
    CONCAT(p.Forename, ' ', p.Surname) AS OfficerName,
    COUNT(v.ViolationsID) AS ViolationCount
FROM tbl_Violations v
JOIN tbl_Officers o ON v.OfficerID = o.OfficerID
JOIN tbl_Person p ON o.PersonID = p.PersonID
WHERE STR_TO_DATE(v.ViolationDate, '%d/%m/%Y') >= DATE_SUB(CURDATE(), INTERVAL 25 YEAR)
GROUP BY OfficerName
ORDER BY ViolationCount DESC;

-- Query 8: Count how many people under 50 have received violations

SELECT 
    COUNT(DISTINCT p.PersonID) AS Under21Violators
FROM tbl_Violations v
JOIN tbl_Person p ON v.ViolatorID = p.PersonID
WHERE TIMESTAMPDIFF(YEAR, STR_TO_DATE(p.DOB, '%Y-%m-%d'), CURDATE()) < 50;

-- Query 9: Count violations by location and type
SELECT 
    v.Location,
    vt.ViolationName,
    COUNT(v.ViolationsID) AS ViolationCount
FROM tbl_Violations v
JOIN tbl_ViolationTypes vt ON v.ViolationTypeID = vt.ViolationTypeID
GROUP BY v.Location, vt.ViolationName
ORDER BY v.Location, ViolationCount DESC;

-- Query 10:List all violators whose eye color is not blue AND height > ‘6’ feet

SELECT 
    p.PersonID,
    p.Forename,
    p.Surname,
    p.Height,
    p.EyeColour
FROM tbl_Person p
JOIN tbl_Violations v ON p.PersonID = v.ViolatorID
WHERE p.EyeColour <> 'Blue'
  AND p.Height > 6;

-- Query 11: Retrieve vehicles that are manually driven and over a certain weight
SELECT 
    vm.VehicleName,
    vm.VehicleBrand,
    vm.VehicleYear,
    vm.CarWeight,
    vm.DriveType,
    v.VehicleColour,
    v.VehicleLicense,
    CONCAT(p.Forename, ' ', p.Surname) AS OwnerName
FROM tbl_VehicleMake vm
JOIN tbl_Vehicles v ON vm.VehicleMakeID = v.VehicleMakeID
JOIN tbl_Person p ON v.VehicleOwner = p.PersonID
WHERE vm.VehicleManual = 1
  AND vm.CarWeight > 1500
ORDER BY vm.CarWeight;

