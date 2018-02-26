CREATE DATABASE jingdong CHARSET=utf8;

CREATE TABLE goods(
    id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT NOT NULL,
    NAME VARCHAR(150) NOT NULL,
    cate_name VARCHAR(40) NOT NULL,
    brand_name VARCHAR(40) NOT NULL,
    price DECIMAL(10,3) NOT NULL DEFAULT 0,
    is_show BIT NOT NULL DEFAULT 1,
    is_saleoff BIT NOT NULL DEFAULT 0
);

SELECT NAME,price FROM goods WHERE cate_name = '超级本'
-- 去重更快
SELECT cate_name FROM goods GROUP BY cate_name

SELECT DISTINCT cate_name FROM goods

SELECT ROUND(AVG(price),2) FROM goods

SELECT AVG(price) ,cate_name FROM goods GROUP BY cate_name  

SELECT * FROM goods WHERE price > (SELECT AVG(price) FROM goods)

-- 找出每种商品中最贵的笔记本
SELECT * FROM goods AS n 
INNER JOIN 
(SELECT cate_name, MAX(price) AS m FROM goods GROUP BY cate_name) AS t2 
WHERE t2.m = n.price AND t2.cate_name = n.cate_name ORDER BY n.price ASC

CREATE TABLE goods_cate(
	id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT NOT NULL,
	NAME VARCHAR(20) NOT NULL	
)
-- 插入数据
INSERT INTO goods_cate(NAME) (SELECT cate_name FROM goods GROUP BY cate_name)

SELECT * FROM goods INNER JOIN goods_cate ON goods.cate_name = goods_cate.name

UPDATE goods AS g INNER JOIN (SELECT goods.cate_name,goods_cate.id FROM goods INNER JOIN goods_cate ON goods.cate_name = goods_cate.name) AS g2 ON g.cate_name =g2.cate_name  SET g.cate_name = g2.id	

CREATE TABLE goods_brands(
	id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT NOT NULL,
	NAME VARCHAR(10) NOT NULL
)

INSERT INTO goods_brands(NAME) SELECT brand_name FROM goods GROUP BY brand_name 

UPDATE (goods AS g INNER JOIN goods_brands AS b ON g.brand_name = b.name) SET  g.brand_name= b.id

DESC goods
ALTER  TABLE goods CHANGE cate_name cate_id INT UNSIGNED NOT NULL
ALTER  TABLE goods CHANGE brand_name brand_id INT UNSIGNED NOT NULL

