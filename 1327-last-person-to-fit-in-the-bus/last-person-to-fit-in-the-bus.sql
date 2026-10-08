# Write your MySQL query statement below
select person_name from (select person_name, sum(weight) over (order by turn)  as hehe from Queue
group by person_id
order by turn)t
where hehe<=1000
order by hehe desc
limit 1