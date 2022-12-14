-- 코드를 입력하세요
SELECT T1.YEAR, T1.MONTH, COUNT(T1.USER_ID) AS PUCHASED_USERS
     , ROUND((COUNT(T1.USER_ID) / (SELECT COUNT(USER_ID) FROM USER_INFO WHERE YEAR(JOINED) = 2021)), 1) AS PUCHASED_RATIO
FROM (
      SELECT DISTINCT YEAR(SALES_DATE) AS YEAR, MONTH(SALES_DATE) AS MONTH, USER_ID
      FROM ONLINE_SALE
) AS T1 JOIN USER_INFO AS T2 ON T1.USER_ID = T2.USER_ID AND T2.JOINED LIKE '2021%'
GROUP BY T1.YEAR, T1.MONTH
ORDER BY T1.YEAR, T1.MONTH