# Write your MySQL query statement below
select patient_id, patient_name, conditions from Patients
where conditions Regexp '(^| )DIAB1'

/*
(^| ) means the DIAB1 is either at the beginning or there is a space prefix to DIAB1.
also we can get the same result by


SELECT patient_id,patient_name,conditions
from Patients 
where conditions LIKE 'DIAB1%' OR conditions LIKE '% DIAB1%';


*/