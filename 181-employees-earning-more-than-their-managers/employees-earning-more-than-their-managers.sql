# Write your MySQL query statement below
select name as Employee from(
select e1.name, e1.salary, e2.salary as m_salary
from employee e1 cross join employee e2
on e1.managerId = e2.id)t
where salary>m_salary
