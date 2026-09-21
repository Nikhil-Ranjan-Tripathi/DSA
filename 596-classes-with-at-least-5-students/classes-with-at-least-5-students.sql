# Write your MySQL query statement below
select class from(select class, Count(*) as temp 
from Courses c 
group by class
having temp>=5)t

-- SELECT class
-- FROM Courses
-- GROUP BY class
-- HAVING COUNT(DISTINCT student) >= 5;