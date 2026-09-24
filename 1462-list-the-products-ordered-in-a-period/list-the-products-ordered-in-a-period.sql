# Write your MySQL query statement below
select product_name, unit from (
select p.product_name, sum(o.unit) as unit, o.order_date from Orders o left join Products p
on p.product_id = o.product_id
where o.order_date between '2020-02-01' and '2020-02-29'
group by p.product_name
having unit>=100)t