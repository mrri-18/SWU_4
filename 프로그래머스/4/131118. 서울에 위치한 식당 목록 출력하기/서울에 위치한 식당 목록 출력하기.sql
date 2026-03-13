-- 코드를 입력하세요
SELECT i.REST_ID, 
    i.REST_NAME, 
    i.FOOD_TYPE, 
    i.FAVORITES, 
    i.ADDRESS, 
    round(avg(r.review_score),2) as SCORE
from REST_INFO i join rest_review r
on i.rest_id=r.rest_id
where address like "서울%"
group by rest_id
ORDER BY SCORE DESC, FAVORITES DESC
