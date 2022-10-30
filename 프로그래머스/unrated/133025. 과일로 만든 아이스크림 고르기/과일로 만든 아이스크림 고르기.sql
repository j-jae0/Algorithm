-- 코드를 입력하세요
SELECT fh.FLAVOR
FROM first_half as fh
    INNER JOIN icecream_info as ii ON fh.FLAVOR = ii.FLAVOR
WHERE fh.TOTAL_ORDER > 3000
    AND ii.INGREDIENT_TYPE = "fruit_based"
ORDER BY fh.TOTAL_ORDER DESC
