# Write your MySQL query statement below
select MAX(num) as num from 
(select num, count(*) as temp from MyNumbers
group by num having temp = 1)t