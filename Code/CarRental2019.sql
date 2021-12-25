CREATE DATABASE CarRental2019;
USE CarRental2019;


CREATE TABLE CUSTOMER
(
	CustID         		INT               	NOT NULL AUTO_INCREMENT,
    Name           		VARCHAR(30)      	NOT NULL,
    Phone          		VARCHAR(15)       	NOT NULL,
    PRIMARY KEY (CustID)
);

CREATE TABLE RENTAL
(
	CustID                INT                NOT NULL,
    VehicleID             VARCHAR(20)        NOT NULL,
    StartDate             DATE               NOT NULL,
    OrderDate             DATE               NOT NULL,
    RentalType            INT                NOT NULL,
    Qty                   INT                NOT NULL,
    ReturnDate            DATE               NOT NULL,
    TotalAmount           DECIMAL			 NOT NULL,
    PaymentDate           DATE,
    FOREIGN KEY (VehicleID) REFERENCES VEHICLE(VehicleID),
    FOREIGN KEY(CustId) REFERENCES CUSTOMER(CustId)
);
ALTER TABLE RENTAL
ADD Returned INT NOT NULL;

UPDATE RENTAL
SET Returned = 1
WHERE PaymentDate IS NOT NULL;

UPDATE RENTAL
SET Returned = 0
WHERE PaymentDate IS NULL;

SELECT * FROM RENTAL;

CREATE TABLE VEHICLE
(
	VehicleID           VARCHAR(20)         NOT NULL,
    Description         VARCHAR(150),
    Year                INT                 NOT NULL,
    Type                INT                 NOT NULL,
    Category            INT                 NOT NULL,
    PRIMARY KEY(VehicleID)
);

CREATE TABLE RATE
(
	Type                INT                 NOT NULL,
    Category            INT                 NOT NULL,
    Weekly              DECIMAL             NOT NULL,
    Daily               DECIMAL             NOT NULL
);


CREATE VIEW vRentalInfo AS
SELECT DISTINCT OrderDate, StartDate, ReturnDate, (ReturnDate-StartDate) AS TotalDays,
VEHICLE.VehicleID AS VIN, 
DESCRIPTION AS Vehicle,

CASE
	WHEN VEHICLE.Type = '1' THEN 'Compact'
	WHEN VEHICLE.Type = '2' THEN 'Medium'
	WHEN VEHICLE.Type = '3' THEN 'Large'
	WHEN VEHICLE.Type = '4' THEN 'SUV'
	WHEN VEHICLE.Type = '5' THEN 'Truck'
	WHEN VEHICLE.Type = '6' THEN 'VAN'
	END AS Type,
        
CASE
	WHEN VEHICLE.Category = '0' THEN 'Basic'
	WHEN VEHICLE.Category = '1' THEN 'Luxury'
	END AS Category,
        
CUSTOMER.CustID AS CustomerID, 
NAME AS CustomerName, 
RENTAL.TotalAmount AS OrderAmount,
        
CASE
	WHEN PaymentDate IS NULL THEN TotalAmount
	ELSE TotalAmount = 0
	END AS RentalBalance
	FROM CUSTOMER,VEHICLE,RENTAL,RATE
	WHERE CUSTOMER.CustID = RENTAL.CustID AND VEHICLE.VehicleID = RENTAL.VehicleID
	ORDER BY StartDate ASC;
    
SELECT * FROM vRentalInfo;

SET GLOBAL sql_mode=(SELECT REPLACE(@@sql_mode,'ONLY_FULL_GROUP_BY',''));

