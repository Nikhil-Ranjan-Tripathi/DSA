# Write your MySQL query statement below
-- select adda as id, sum(s) as num from (select requester_id as adda, count(*) as s from RequestAccepted
-- group by requester_id
-- union
-- select accepter_id as adda, count(*) as s from RequestAccepted
-- group by accepter_id) as temp
-- group by adda
-- order by num desc
-- limit 1

select adda as id, count(*) as num from (select requester_id as adda from RequestAccepted
union all
select accepter_id as adda from RequestAccepted) as temp
group by adda
order by num desc
limit 1