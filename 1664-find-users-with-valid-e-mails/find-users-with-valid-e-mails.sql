# Write your MySQL query statement below

SELECT user_id, name, mail
FROM Users
WHERE REGEXP_like(mail, '^[a-zA-Z][a-zA-Z0-9_.-]*@leetcode\\.com$', 'c');

/*
"^" marks the start of the string, without ^, MySQL can find a matching portion somewhere inside the email. Similarly "$", marks the end of the string. "*" means the there can be 0 to multiple characters of the following type.
In REGEXP, '.' means “any single character”, while '\.' means a literal dot '.'
'c' is for stating the case-senstivity of the string.
*/