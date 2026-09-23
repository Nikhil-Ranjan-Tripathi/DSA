# Write your MySQL query statement below
select event_day as day, emp_id, sum(out_time) - sum(in_time) as total_time from Employees
group by event_day, emp_id


/*
select day, em_id, sum(in_time) as in_time, sum(out_time) as out_time from Employees
group by event_day, emp_id
*/