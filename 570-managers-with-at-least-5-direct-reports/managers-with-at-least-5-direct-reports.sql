# Write your MySQL query statement below
select name from Employee where id in (select managerId as county from Employee
group by managerId
having count(managerId)>=5)
