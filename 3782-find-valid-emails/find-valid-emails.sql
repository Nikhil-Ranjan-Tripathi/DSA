# Write your MySQL query statement below
select user_id, email from Users
where regexp_like(email, '^[0-9a-zA-Z_]*@[a-zA-Z]+\\.com$', 'c')
order by user_id

-- *  →  0 or more
-- +  →  1 or more