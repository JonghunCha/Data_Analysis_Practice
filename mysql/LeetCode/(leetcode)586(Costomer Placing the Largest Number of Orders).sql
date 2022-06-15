/*
문제 링크 : https://leetcode.com/problems/customer-placing-the-largest-number-of-orders/
LIMIT을 통해 출력 갯수를 제한하여 해결할 수 있다.
*/
SELECT customer_number
FROM Orders
GROUP BY customer_number
ORDER BY COUNT(*) DESC LIMIT 1;