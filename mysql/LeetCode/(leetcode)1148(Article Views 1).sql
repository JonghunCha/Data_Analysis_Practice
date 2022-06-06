/*
문제 링크 : https://leetcode.com/problems/article-views-i/
author_id와 view_id가 같은 것을 distinct로 뽑아낸 뒤 오름차순으로 정렬하면 된다.
*/
SELECT DISTINCT author_id AS id
FROM Views
WHERE author_id = viewer_id ORDER BY id ASC;