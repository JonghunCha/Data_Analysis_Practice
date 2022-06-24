/*
문제 링크 : https://leetcode.com/problems/capital-gainloss/
operation을 case별로 나눈 뒤 sum을 하면 된다.
*/
SELECT stock_name, sum(CASE
                        WHEN operation = "Buy" THEN -price
                        ELSE price
                       END) AS capital_gain_loss
FROM Stocks
GROUP BY stock_name;