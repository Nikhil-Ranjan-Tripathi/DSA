# Write your MySQL query statement below
select v.customer_id, Count(*) as count_no_trans
from Visits v left join Transactions T
on v.visit_id = t.visit_id
where t.transaction_id is Null
group by v.customer_id