-- https://app.codesignal.com/challenge/DFTWNgu9rmv543KXs
CREATE PROCEDURE suspectsInvestigation()
BEGIN
	/* Write your SQL here. Terminate each statement with a semicolon. */
    SELECT id,name,surname
    FROM Suspect
    WHERE height <= 170 and UPPER(name) LIKE 'B%' and UPPER(surname) LIKE 'GRE_N';
END

