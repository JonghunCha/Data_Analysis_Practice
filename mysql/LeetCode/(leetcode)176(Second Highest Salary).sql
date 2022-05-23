/*
문제 링크 : https://leetcode.com/problems/second-highest-salary/
MAX를 이용하여 해결할 수 있다.
*/
SELECT MAX(salary) AS SecondHighestSalary
FROM Employee
WHERE salary < (SELECT MAX(salary) FROM Employee);