/*
문제 링크 : https://leetcode.com/problems/recyclable-and-low-fat-products/
WHERE절에 AND를 사용하는 방법으로 해결하였다.
*/
SELECT product_id
FROM Products
WHERE low_fats = "Y" AND recyclable = "Y";