# https://app.codesignal.com/challenge/ocvTHM4AMhjq3ucNv

CREATE PROCEDURE orderingEmails()
BEGIN
    /* Write your SQL here. Terminate each statement with a semicolon. */
    SELECT id,
           email_title,
           CASE
               WHEN size >= 1048576
                   THEN CONCAT(round(floor(size / POW(2, 20))), ' ', 'Mb')
               ELSE CONCAT(round(floor(size / POW(2, 10))), ' ', 'Kb')
               END as short_size
    FROM emails
    ORDER BY size DESC;
END