SELECT U.USER_ID,
       U.NICKNAME,
       CONCAT(U.CITY, ' ', U.STREET_ADDRESS1, ' ', U.STREET_ADDRESS2) AS '전체주소',
       CONCAT(LEFT(TLNO, 3), '-', MID(TLNO, 4, 4), '-', RIGHT(TLNO, 4)) AS '전화번호'
       FROM (SELECT WRITER_ID AS USER_ID
      FROM USED_GOODS_BOARD
      GROUP BY WRITER_ID
      HAVING COUNT(BOARD_ID) >= 3) AS B
INNER JOIN USED_GOODS_USER AS U ON B.USER_ID = U.USER_ID
ORDER BY U.USER_ID DESC