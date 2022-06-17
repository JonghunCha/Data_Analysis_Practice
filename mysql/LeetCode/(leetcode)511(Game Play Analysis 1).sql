/*
문제 링크 : https://leetcode.com/problems/game-play-analysis-i/
MIN, GROUP BY를 이용하여 해결할 수 있는 문제다.
*/
SELECT player_id, MIN(event_date) AS first_login
FROM Activity
GROUP BY player_id;