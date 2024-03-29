-- 코드를 입력하세요
# SELECT A.AUTHOR_ID, A.AUTHOR_NAME, B.CATEGORY,
#        (BS.SALES * B.PRICE) AS TOTAL_SALES
# FROM (SELECT BOOK_ID, SUM(SALES) AS SALES
#       FROM BOOK_SALES
#       WHERE DATE_FORMAT(SALES_DATE, "%Y-%m") = "2022-01" 
#       GROUP BY BOOK_ID
#      ) AS BS 
#     INNER JOIN BOOK AS B ON B.BOOK_ID = BS.BOOK_ID
#   INNER JOIN AUTHOR AS A ON B.AUTHOR_ID = A.AUTHOR_ID
# GROUP BY A.AUTHOR_ID, A.AUTHOR_NAME, B.CATEGORY
# ORDER BY A.AUTHOR_ID, B.CATEGORY DESC

SELECT A.AUTHOR_ID, A.AUTHOR_NAME, T1.CATEGORY, 
       SUM(T1.SALES * T1.PRICE) AS TOTAL_SALES
FROM (SELECT BS.BOOK_ID, BS.SALES, B.CATEGORY, B.AUTHOR_ID, B.PRICE 
    FROM (SELECT BOOK_ID, SUM(SALES) AS SALES
          FROM BOOK_SALES
          WHERE DATE_FORMAT(SALES_DATE, "%Y-%m") = "2022-01"
          GROUP BY BOOK_ID
          ORDER BY BOOK_ID) AS BS
        INNER JOIN BOOK AS B ON B.BOOK_ID = BS.BOOK_ID) AS T1
    INNER JOIN AUTHOR AS A ON T1.AUTHOR_ID = A.AUTHOR_ID
GROUP BY A.AUTHOR_ID, A.AUTHOR_NAME, T1.CATEGORY
ORDER BY A.AUTHOR_ID, T1.CATEGORY DESC