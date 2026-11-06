--cd C:\Users\mihai\PycharmProjects\pythonTest\SQL
--sqlite3 data_db.db






--CREATE TABLE student (
--    Year INTEGER,
--    Make TEXT,
--    Model TEXT,
--    Price REAL
--);
--CREATE TABLE Carrr (
--    Make TEXT,
--    Model TEXT,
--    Price REAL,
--    Dollar TEXT
--);
--
--SELECT * from student;

INSERT INTO Carrr (Make, Model, Price, Dollar) VALUES ('Ukraine', 'Volvo', 1090, '$');
INSERT INTO Carrr (Make, Model, Price, Dollar) VALUES ('France', 'Reno', 25000, '₱');
INSERT INTO Carrr (Make, Model, Price, Dollar) VALUES ('Russian', 'Mazda', 21640, '₴');
INSERT INTO Carrr (Make, Model, Price, Dollar) VALUES ('USA', 'Crasler', 0.1100, '$');
INSERT INTO Carrr (Make, Model, Price, Dollar) VALUES ('Ukraine', 'Жигули', 300, '₴');
INSERT INTO Carrr (Make, Model, Price, Dollar) VALUES ('Ukraine', 'Mitsubishi', 1600, '₴');
INSERT INTO Carrr (Make, Model, Price, Dollar) VALUES ('Germany', 'BMW', 30.500, '€');
INSERT INTO Carrr (Make, Model, Price, Dollar) VALUES ('Russian', 'Honda', 1910, '$');
INSERT INTO Carrr (Make, Model, Price, Dollar) VALUES ('Britany', 'Nissan', 13600, '€');
INSERT INTO Carrr (Make, Model, Price, Dollar) VALUES ('Japan', 'Opel', 7100, '$');

--SELECT Model, Price from Car;
--SELECT Model, Price from Car WHERE Price <= 25000;
--SELECT Make, Price from Car WHERE Price IS NOT 25000 and Price = NOT 61000;
--SELECT Make, Price from Carrr WHERE Price IS NOT 25000 and Make LIKE '%r%';
SELECT Make, Price from Carrr WHERE Price IS NOT 19000 and Make LIKE '%n' or Make LIKE 'U%';

UPDATE Carrr SET Make = 'USA' WHERE Make = 'America';
UPDATE Carrr SET Model ='Ford' where Model= 'Жигули';

DELETE FROM Carrr where Price >= 50000;
DELETE from Carrr where Model IS 'Ford' or Dollar = '₱';