/*
문제 링크 : https://leetcode.com/problems/patients-with-a-condition/
LIKE를 통해 원하는 문자가 있는지 검사하면 된다.
*/
SELECT patient_id, patient_name, conditions
FROM Patients
WHERE conditions LIKE "DIAB1%" OR conditions LIKE "% DIAB1%";