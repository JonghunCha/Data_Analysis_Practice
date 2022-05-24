/*
문제 링크 : https://leetcode.com/problems/combine-two-tables/
left join을 이용하여 해결가능한 문제다.
*/
SELECT p.firstName, p.lastName, a.city, a.state
FROM Person p LEFT JOIN Address a ON p.personId = a.personId