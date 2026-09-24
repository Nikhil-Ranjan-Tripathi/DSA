# Write your MySQL query statement below
select employee_id from Employees
union
select employee_id from Salaries
except
select e.employee_id from Employees e join Salaries s
where e.employee_id = s.employee_id
order by employee_id