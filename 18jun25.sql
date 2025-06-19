SELECT * FROM products;

SELECT * FROM products
WHERE price >= 2500; 


CREATE TABLE SalesData (
    SaleID INT IDENTITY(1,1) PRIMARY KEY,
    ProductName VARCHAR(100),
    Category VARCHAR(50),
    UnitsSold INT,
    UnitPrice DECIMAL(10,2),
    SaleDate DATE
);


-- Inserting randomized sample data using a loop
DECLARE @i INT = 1;
WHILE @i <= 1000
BEGIN
    INSERT INTO SalesData (ProductName, Category, UnitsSold, UnitPrice, SaleDate)
    VALUES (
        CONCAT('Product_', FLOOR(RAND() * 20 + 1)),
        CASE FLOOR(RAND() * 5)
            WHEN 0 THEN 'Mouse'
            WHEN 1 THEN 'Keyboard'
            WHEN 2 THEN 'Speaker'
            WHEN 3 THEN 'Storage'
            ELSE 'Monitor'
        END,
        FLOOR(RAND() * 10 + 1),
        CAST((FLOOR(RAND() * 4000 + 500)) AS DECIMAL(10,2)),
        DATEADD(DAY, -FLOOR(RAND() * 180), GETDATE())
    );
    SET @i += 1;
END;


SELECT DISTINCT(productname)
FROM SalesData;

EXEC sp_rename "salesdata", "sales";


SELECT saleid, saledate, productname
FROM sales
ORDER BY UnitPrice;


SELECT saleid, saledate, unitprice
FROM sales
ORDER BY unitprice DESC;


SELECT TOP 5 *
FROM sales;


ALTER TABLE sales
ADD sale_value INT;


UPDATE sales
SET sale_value = UnitPrice * UnitsSold;


SELECT TOP 5 *
FROM sales;


SELECT saleid, saledate, sale_value
FROM sales
ORDER BY sale_value ASC;


SELECT saleid, saledate, sale_value
FROM sales
ORDER BY sale_value DESC;


SELECT saleid, saledate, sale_value
FROM sales
WHERE saleid BETWEEN 0 AND 100;


SELECT MAX(saleid), MIN(saleid)
FROM sales;


SELECT saleid, saledate, sale_value
FROM sales
WHERE saleid BETWEEN 1 AND 250
ORDER BY saleid ASC;


SELECT productname
FROM sales;


SELECT DISTINCT(Category)
FROM sales;


SELECT *
FROM sales
WHERE Category = 'storage'
OR Category = 'monitor';


SELECT TOP 50 *
FROM sales
WHERE Category = 'storage'
OR Category = 'monitor';


SELECT MAX(UnitPrice), MIN(unitprice), MAX(unitprice) - MIN(unitprice) AS range
FROM sales;


SELECT TOP 3 *
FROM sales;


SELECT saleid, saledate, sale_value
FROM sales
WHERE unitprice < 500;


SELECT saleid, saledate, sale_value
FROM sales
WHERE unitprice < 1000;


SELECT saleid, saledate, sale_value, UnitsSold
FROM sales
WHERE unitssold < 5;


SELECT saleid, saledate, sale_value, UnitsSold
FROM sales
WHERE unitssold >= 10;


SELECT TOP 3 *
FROM sales;



-- Creating new table for practice

CREATE TABLE UPI_Transactions (
    TransactionID INT IDENTITY(1,1) PRIMARY KEY,
    SenderUPI VARCHAR(100),
    ReceiverUPI VARCHAR(100),
    Amount DECIMAL(10,2),
    TransactionStatus VARCHAR(20),
    TransactionDate DATETIME,
    Remark VARCHAR(255)
);


DECLARE @i INT = 1;

WHILE @i <= 1000
BEGIN
    INSERT INTO UPI_Transactions (
        SenderUPI, ReceiverUPI, Amount, TransactionStatus, TransactionDate, Remark
    )
    VALUES (
        CONCAT('user', FLOOR(RAND() * 100 + 1), '@upi'),
        CONCAT('merchant', FLOOR(RAND() * 100 + 1), '@ybl'),
        ROUND(RAND() * 5000 + 10, 2), -- ₹10 to ₹5010
        CASE FLOOR(RAND() * 3)
            WHEN 0 THEN 'SUCCESS'
            WHEN 1 THEN 'PENDING'
            ELSE 'FAILED'
        END,
        DATEADD(DAY, -FLOOR(RAND() * 180), GETDATE()),
        CONCAT('Payment for order #', FLOOR(RAND() * 10000 + 1000))
    );

    SET @i += 1;
END;


SELECT TOP 5 *
FROM UPI_Transactions;


SELECT DISTINCT(senderupi)
FROM UPI_Transactions;


SELECT *
FROM UPI_Transactions
ORDER BY Amount DESC;


SELECT DISTINCT(transactionstatus)
FROM UPI_Transactions;


SELECT transactionid, transactiondate, amount, transactionstatus
FROM UPI_Transactions
WHERE amount BETWEEN 0 AND 2500;


SELECT transactionid, transactiondate, amount, transactionstatus
FROM UPI_Transactions
WHERE amount BETWEEN 2500 AND 5000;

-- end of module


-- second module 

EXEC sp_rename "upi_transactions", "upi";


SELECT TOP 5 *
FROM upi;


SELECT transactionid, transactiondate, amount
FROM upi
WHERE transactionstatus = 'PENDING';


SELECT COUNT(transactionid)
FROM UPI
WHERE transactionstatus = 'FAILED';


SELECT COUNT(transactionid)
FROM UPI
WHERE transactionstatus = 'PENDING';


SELECT COUNT(transactionid)
FROM UPI
WHERE transactionstatus = 'SUCCESS';


SELECT TOP 10 *
FROM upi;


SELECT TOP 25 *
FROM upi
ORDER BY transactiondate ASC;


SELECT *
FROM upi
WHERE transactionstatus = 'FAILED'
AND amount > 2000;


SELECT TOP 10 *
FROM upi
WHERE transactionstatus = 'PENDING'
AND amount >=1500;

-- End of script











