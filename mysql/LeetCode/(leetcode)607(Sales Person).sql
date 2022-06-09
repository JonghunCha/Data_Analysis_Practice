/*
문제 링크 : https://leetcode.com/problems/sales-person/
*/
SELECT name
FROM SalesPerson
WHERE sales_id NOT IN (SELECT o.sales_id
                       FROM Company c, Orders o
                       WHERE c.com_id = o.com_id AND c.name = "RED");