USE db24;

DELIMITER $$
CREATE PROCEDURE MyPROC_7 (IN inID INT)
BEGIN
	SELECT * FROM MyTBL_7A WHERE ID=inID;
END;$$
DELIMITER ;