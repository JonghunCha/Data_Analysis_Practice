/*
문제 링크 : https://leetcode.com/problems/delete-duplicate-emails/
DELETE문을 사용할 수 있는지 묻는 문제다.
*/
DELETE p1
FROM Person p1, Person p2
WHERE p1.email = p2.email AND p1.id > p2.id;