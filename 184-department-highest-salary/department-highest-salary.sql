# Write your MySQL query statement below
-- select d.name as Department, e.name as Employee, e.Salary as Salary from Employee e left join Department d
-- on e.departmentId = d.id
-- where Salary = (
--     select max(e2.salary) from Employee e2
--     where e2.departmentId = e.departmentId
-- )

-- SELECT
--     Department,
--     Employee,
--     Salary
-- FROM (
--     SELECT
--         d.name AS Department,
--         e.name AS Employee,
--         e.salary AS Salary,
--         DENSE_RANK() OVER (
--             PARTITION BY e.departmentId
--             ORDER BY e.salary DESC
--         ) AS rnk
--     FROM Employee e
--     JOIN Department d
--         ON e.departmentId = d.id
-- ) t
-- WHERE rnk = 1;

-- select d.name, e.name, e.salary from Employee e left join Department d
-- on e.departmentId = d.id
-- order by e.departmentId, e.salary

select d.name as Department, e.name as Employee, e.salary as Salary from Employee e left join Department d on e.departmentId = d.id
where (e.departmentId, e.salary) in (select departmentId, Max(salary) from Employee group by departmentId)