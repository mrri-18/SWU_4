-- 코드를 작성해주세요
SELECT i.ITEM_ID, i.ITEM_NAME, i.RARITY
FROM ITEM_INFO i JOIN ITEM_TREE t
ON i.item_id=t.item_id
# 모든 업그레이드가 가능한 경우를 구함
WHERE t.PARENT_ITEM_ID IN ( 
    SELECT ITEM_ID
    FROM ITEM_INFO
    WHERE RARITY = 'RARE'
)
ORDER BY t.ITEM_ID DESc