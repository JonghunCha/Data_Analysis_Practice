/*
문제 링크 : https://leetcode.com/problems/tree-node/
CASE를 이용하여 각 조건에 해당하는 노드를 검사한다.
*/
SELECT id,
    CASE
        WHEN p_id IS NULL THEN "Root"
        WHEN (p_id IS NOT NULL AND id IN (SELECT DISTINCT p_id FROM Tree)) THEN "Inner"
        ELSE "Leaf"
    END AS type
FROM Tree;