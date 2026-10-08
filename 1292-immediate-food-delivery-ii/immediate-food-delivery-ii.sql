# Write your MySQL query statement below
SELECT 
    round(AVG(
        CASE
            WHEN t.order_date = t.customer_pref_delivery_date THEN 1
            ELSE 0
        END
    ) * 100, 2) AS immediate_percentage
FROM Delivery t
WHERE t.order_date = (
    SELECT MIN(t2.order_date)
    FROM Delivery t2
    WHERE t2.customer_id = t.customer_id
);


