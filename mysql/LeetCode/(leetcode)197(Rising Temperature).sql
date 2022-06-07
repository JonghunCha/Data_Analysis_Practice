/*
문제 링크 : https://leetcode.com/problems/rising-temperature/
DATE_ADD를 통한 날짜 비교와 INNER JOIN을 이용하여 해결 가능하다
*/
SELECT w1.id
FROM Weather w1 INNER JOIN Weather w2
ON w1.recordDate = DATE_ADD(w2.recordDate, INTERVAL 1 DAY)
WHERE w1.temperature > w2.temperature;