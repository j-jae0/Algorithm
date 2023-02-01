-- 코드를 입력하세요
SELECT MONTH(START_DATE) AS MONTH, CAR_ID, COUNT(*) AS RECORDS
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
WHERE CAR_ID IN (SELECT CAR_ID
                 FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
                 WHERE DATE_FORMAT(START_DATE, "%Y-%m") REGEXP "2022-08|2022-09|2022-10"
                 GROUP BY CAR_ID
                 HAVING COUNT(*) >= 5)
  AND DATE_FORMAT(START_DATE, "%Y-%m") REGEXP "2022-08|2022-09|2022-10"
GROUP BY MONTH, CAR_ID

ORDER BY MONTH, CAR_ID DESC