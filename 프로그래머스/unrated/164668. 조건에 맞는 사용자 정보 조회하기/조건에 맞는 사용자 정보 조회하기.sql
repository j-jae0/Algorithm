SELECT T1.USER_ID, T2.NICKNAME, T1.TOTAL_SALES
FROM (SELECT WRITER_ID AS USER_ID, SUM(PRICE) AS TOTAL_SALES
      FROM USED_GOODS_BOARD 
      WHERE STATUS = 'DONE' 
      GROUP BY WRITER_ID 
      HAVING SUM(PRICE) >= 700000) AS T1
INNER JOIN USED_GOODS_USER AS T2 ON T1.USER_ID = T2.USER_ID
ORDER BY T1.TOTAL_SALES