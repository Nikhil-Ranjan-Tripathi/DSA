# Write your MySQL query statement below

select customer_number from Orders group by customer_number
having count(*) = (
    select max(temp) from(
        select customer_number, count(*) as temp from Orders
        group by customer_number
        order by count(*) desc
    )t
)
    

