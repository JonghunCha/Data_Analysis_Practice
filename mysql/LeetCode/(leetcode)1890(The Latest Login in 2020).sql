/*
문제 링크 : https://leetcode.com/problems/the-latest-login-in-2020/
MAX를 통해 가장 최근의 날짜를 추출하고, YEAR를 통해 2020년인 time_stamp만 추출하면 된다.
*/
SELECT user_id, MAX(time_stamp) AS last_stamp
FROM Logins
WHERE YEAR(time_stamp) = "2020"
GROUP BY user_id;