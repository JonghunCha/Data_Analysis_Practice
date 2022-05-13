/*
https://leetcode.com/problems/group-sold-products-by-the-date/
중복제거 및 GROUP BY를 묻는 문제다.
*/
SELECT sell_date,
    COUNT(DISTINCT(product)) AS num_sold,
    GROUP_CONCAT(DISTINCT(product)) AS products
FROM Activities
GROUP BY sell_date
ORDER BY sell_date