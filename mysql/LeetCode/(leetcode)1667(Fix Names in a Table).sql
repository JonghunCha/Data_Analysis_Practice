/*
문제 링크 : https://leetcode.com/problems/fix-names-in-a-table/
문자열 CONCAT과 UPPER, LOWER을 통한 대소문자 변환에 관한 문제다.

LEFT는 왼쪽으로부터 지정한 길이 만큼을 반환하고, RIGHT는 오른쪽부터 지정한 길이 만큼을 반환한다.

또한 user_id의 오름차순으로 ORDER BY를 통해 정렬하였다.
*/
SELECT user_id, CONCAT(UPPER(LEFT(name, 1)), LOWER(RIGHT(name, length(name) - 1))) AS name
FROM Users
ORDER BY user_id ASC