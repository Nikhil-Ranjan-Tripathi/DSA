# Write your MySQL query statement below
-- select MAX(num) as num from 
-- (select num, count(*) as temp from MyNumbers
-- group by num having temp = 1)t

select (select num from MyNumbers
group by num
having count(*)=1
order by num desc
limit 1) as num