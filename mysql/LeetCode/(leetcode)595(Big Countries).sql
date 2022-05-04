/*
문제 링크 : https://leetcode.com/problems/big-countries/
OR을 사용한 방법과 UNION을 사용한 방법 두 가지를 작성한다.
*/
--1. OR
SELECT name, population, area
FROM World
WHERE area >= 3000000 OR population >= 25000000;

--2. UNION
SELECT name, population, area
FROM World
WHERE area >= 3000000
UNION
SELECT name, population, area
FROM World
WHERE population >= 25000000