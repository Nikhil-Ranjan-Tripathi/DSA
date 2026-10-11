# Write your MySQL query statement below
-- SELECT sp.name
-- FROM SalesPerson sp
-- WHERE NOT EXISTS (
--     SELECT 1
--     FROM Orders o
--     JOIN Company c
--         ON o.com_id = c.com_id
--     WHERE o.sales_id = sp.sales_id
--       AND c.name = 'RED'
-- );

select name from SalesPerson
where sales_id not in (select o.sales_id from Orders o inner join Company c on c.com_id=o.com_id
where c.name="RED")