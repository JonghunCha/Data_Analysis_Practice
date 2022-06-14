/*
문제 링크 : https://leetcode.com/problems/find-followers-count/
GROUP BY, ORDER BY, COUNT를 이용하여 해결할 수 있다.
*/
SELECT user_id, COUNT(follower_id) AS followers_count
FROM Followers
GROUP BY user_id
ORDER BY user_id;