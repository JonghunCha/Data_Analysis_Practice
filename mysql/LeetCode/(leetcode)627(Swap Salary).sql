/*
문제 링크 : https://leetcode.com/problems/swap-salary/
제약 조건으로 SELECT를 사용하지 말라고 되어 있다.

따라서 UPDATE, SET을 이용하여 해결하였다.

또한 IF를 사용한 경우와 CASE를 사용한 경우 2가지를 작성하였다.
*/
--1. CASE
UPDATE Salary
SET sex =
    CASE
        WHEN sex = "m" THEN "f"
        ELSE "m"
    END

--2.
UPDATE Salary
SET sex = IF(sex = "m", "f", "m")