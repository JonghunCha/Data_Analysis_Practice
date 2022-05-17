/*
문제 링크 : https://leetcode.com/problems/employees-with-missing-information/
각각의 테이블에서 missing information에 해당하는 employee_id를 추출하고 이를 UNION한 뒤 오름차순으로 정렬하면 된다.
*/
SELECT employee_id
FROM Employees
WHERE employee_id NOT IN (SELECT employee_id FROM Salaries)
UNION
SELECT employee_id
FROM Salaries
WHERE employee_id NOT IN (SELECT employee_id FROM Employees)
ORDER BY employee_id ASC;