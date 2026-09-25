# Write your MySQL query statement below
SELECT customer_id
FROM Customer
group by customer_id
having COUNT(Distinct(product_key)) = (
    select count(*) from Product
)