# Write your MySQL query statement below
-- select name, max(net_amount) from Users
-- where 

select name, balance as balance from(

select u.name, t.account, sum(t.amount) as balance from Transactions t left join Users u
on u.account = t.account
group by account)p

where balance>10000
