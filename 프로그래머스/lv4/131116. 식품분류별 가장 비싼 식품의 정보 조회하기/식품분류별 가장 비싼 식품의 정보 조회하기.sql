-- 코드를 입력하세요
SELECT T2.CATEGORY, T2.PRICE, T2.PRODUCT_NAME
FROM (
    SELECT category, MAX(price) as max_price
    FROM food_product
    group by category
) T1 INNER JOIN food_product as T2 ON T1.category = T2.category AND T1.max_price = T2.price
# GROUP BY CATEGORY
HAVING CATEGORY REGEXP '과자|국|김치|식용유'
ORDER BY PRICE DESC
