# Write your MySQL query statement below
select tweet_id from Tweets
where content in (
    select content from Tweets
    having char_length(content)>15
    )
