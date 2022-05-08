/*
문제 링크 : https://leetcode.com/problems/customers-who-never-order/
as를 이용하여 결과의 column 이름을 설정하며 NOT IN을 이용하여 포함되지 않는 row를 선택하는 것을 묻는 문제다.
*/
SELECT name as Customers
FROM Customers
WHERE id NOT IN
    (SELECT customerId
    FROM Orders);