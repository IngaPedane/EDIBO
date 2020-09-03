CREATE DEFINER=`u24`@`%` FUNCTION `MyFUNC_7`(solis int) RETURNS int(11)
BEGIN 
	DECLARE lielums, done int;
    DECLARE mainig1 integer;
	DECLARE mainig2 varchar(10);
    
    DECLARE cursors_ieksh_tabulas CURSOR FOR SELECT ID, FName FROM MyTBL_7A;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;
    
    SET lielums = 0;
    SET done = FALSE;
    OPEN cursors_ieksh_tabulas;
    lasiishanas_cikls: LOOP
		FETCH cursors_ieksh_tabulas INTO mainig1, mainig2;
        IF done OR mainig2 LIKE "Sam" THEN
			LEAVE lasiishanas_cikls;
		END IF;
        SET lielums = lielums + mainig1;
	END LOOP;
	CLOSE cursors_ieksh_tabulas;
    
    RETURN lielums * solis;
    
END