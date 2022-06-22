/*
문제 링크 : https://leetcode.com/problems/find-total-time-spent-by-each-employee/
SUM과 GROUP BY로 해결할 수 있는 문제.
*/
SELECT event_day AS day, emp_id, SUM(out_time - in_time) AS total_time
FROM Employees
GROUP BY event_day, emp_id;
