/*
문제 링크 : https://leetcode.com/problems/customer-who-visited-but-did-not-make-any-transactions/
*/
SELECT v.customer_id, count(v.visit_id) AS count_no_trans
FROM Visits v
WHERE v.visit_id NOT IN (SELECT visit_id FROM Transactions)
GROUP BY v.customer_id;