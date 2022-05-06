/*
문제 링크 : https://leetcode.com/problems/find-customer-referee/
IS NULL을 사용하여 referee_id가 null인 row를 추출하였다.
*/
SELECT name
FROM Customer
WHERE referee_id != 2 OR referee_id IS NULL;