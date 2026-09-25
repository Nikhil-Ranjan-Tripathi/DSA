# Write your MySQL query statement below
select score, DENSE_RANK() over (order by score desc) as 'rank'
from Scores
-- | score | rank |
-- | ----- | ---- |
-- | 4     | 1    |
-- | 4     | 1    |
-- | 3.85  | 2    |
-- | 3.65  | 3    |
-- | 3.65  | 3    |
-- | 3.5   | 4    |

-- select score, RANK() over (order by score desc) as 'rank'
-- from Scores
-- | score | rank |
-- | ----- | ---- |
-- | 4     | 1    |
-- | 4     | 1    |
-- | 3.85  | 3    |
-- | 3.65  | 4    |
-- | 3.65  | 4    |
-- | 3.5   | 6    |


-- select score, ROW_NUMBER() over (order by score desc) as 'rank'
-- from Scores
-- | score | rank |
-- | ----- | ---- |
-- | 4     | 1    |
-- | 4     | 2    |
-- | 3.85  | 3    |
-- | 3.65  | 4    |
-- | 3.65  | 5    |
-- | 3.5   | 6    |