-- # Write your MySQL query statement below
-- SELECT 
--     round(AVG(
--         CASE
--             WHEN t.order_date = t.customer_pref_delivery_date THEN 1
--             ELSE 0
--         END
--     ) * 100, 2) AS immediate_percentage
-- FROM Delivery t
-- WHERE t.order_date = (
--     SELECT MIN(t2.order_date)
--     FROM Delivery t2
--     WHERE t2.customer_id = t.customer_id
-- );


select round( 100* sum(order_date=customer_pref_delivery_date)/count(*),2) as immediate_percentage from
Delivery 
where (customer_id, order_date) in (
    select customer_id, min(order_date) from Delivery
    group by customer_id
)