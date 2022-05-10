/*
문제 링크 : https://leetcode.com/problems/calculate-special-bonus/
IF를 사용한 방법과 CASE를 사용한 방법 두 가지를 작성하였다.
*/
--1. IF
SELECT employee_id,
    IF(employee_id % 2 != 0 AND name NOT LIKE "M%", salary, 0) AS bonus
FROM Employees

--2. CASE
SELECT employee_id,
    CASE
        WHEN (employee_id % 2 != 0 AND name NOT LIKE "M%") THEN salary
        ELSE 0
    END AS bonus
FROM Employees
