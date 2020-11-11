# https://app.codesignal.com/challenge/33dzM2YeNqEK7ce3S


CREATE PROCEDURE suspectsInvestigation2()
BEGIN
    /* Write your SQL here. Terminate each statement with a semicolon. */
    SELECT id, name, surname
    FROM Suspect
    WHERE height <= 170
       OR UPPER(name) NOT LIKE 'B%'
       OR UPPER(surname) NOT LIKE 'GRE_N';
END