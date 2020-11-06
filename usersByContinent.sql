# https://app.codesignal.com/challenge/ys7Eh8cW5sgtQuT2u

CREATE PROCEDURE usersByContinent()
BEGIN
    /* Write your SQL here. Terminate each statement with a semicolon. */
    SELECT continent, SUM(users) as users
    FROM countries
    GROUP BY continent
    ORDER BY users DESC;
END