-- 코드를 입력하세요
SELECT DATE_FORMAT(DATETIME, "%H") AS HOUR, COUNT(*)
FROM ANIMAL_OUTS
WHERE DATE_FORMAT(DATETIME, "%H") BETWEEN 9 AND 19
GROUP BY HOUR
ORDER BY HOUR