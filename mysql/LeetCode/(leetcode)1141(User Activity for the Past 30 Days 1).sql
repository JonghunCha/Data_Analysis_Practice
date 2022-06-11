/*
문제 링크 : https://leetcode.com/problems/user-activity-for-the-past-30-days-i/
날짜 구간을 BETWEEN을 이용하여 지정하면 된다.
*/
SELECT activity_date AS day, COUNT(DISTINCT user_id) AS active_users
FROM Activity
WHERE activity_date BETWEEN "2019-06-28" AND "2019-07-27"
GROUP BY day;