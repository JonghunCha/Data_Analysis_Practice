/*
문제 링크 : https://leetcode.com/problems/top-travellers/
JOIN과 CASE를 이용하여 해결할 수 있다.
*/
SELECT Users.name, CASE
                        WHEN Rides.distance IS NOT NULL THEN SUM(Rides.distance)
                        ELSE 0
                   END AS travelled_distance
FROM Users LEFT JOIN Rides ON Users.id = Rides.user_id
GROUP BY Users.id
ORDER BY travelled_distance DESC, name ASC;