CREATE FUNCTION getNthHighestSalary(n INT) RETURNS INT
BEGIN
  set n=n-1;
  RETURN (
    select distinct salary
    from Employee
    order by salary desc
    limit 1 offset n
  );
END

-- SELECT DISTINCT salary
-- FROM Employee
-- ORDER BY salary DESC
-- LIMIT 1 OFFSET N-1;