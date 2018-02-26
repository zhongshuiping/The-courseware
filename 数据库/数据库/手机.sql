
SELECT COUNT(*) FROM phone
-- 华为手机
SELECT * FROM phone WHERE title LIKE '%华为%' OR title LIKE '%荣耀%' OR title LIKE '%HUAWEI%' OR title LIKE '%huawei%'
-- 百元机
SELECT * FROM phone WHERE  price LIKE '______'

-- 千员机
SELECT * FROM phone WHERE  price LIKE '_______'

-- 1000-2000
SELECT * FROM phone WHERE  price LIKE '_1______'

-- 2000-3000
SELECT * FROM phone WHERE  price LIKE '_2______'

-- 3000-4000
SELECT * FROM phone WHERE  price LIKE '_3______'

-- 4000-5000
SELECT * FROM phone WHERE  price LIKE '_4______'

-- 5000-6000
SELECT * FROM phone WHERE  price LIKE '_5______'

-- 6000-7000
SELECT * FROM phone WHERE  price LIKE '_6______'

-- 7000-8000
SELECT * FROM phone WHERE  price LIKE '_7______'

-- 8000-9000
SELECT * FROM phone WHERE  price LIKE '_8______'

-- 9000-10000
SELECT * FROM phone WHERE  price LIKE '_9______'

-- 10000-11000
SELECT  * FROM phone WHERE  price LIKE '_10______'

DELETE FROM phone  WHERE title LIKE '港版现货，限量抢购' OR title LIKE '现货速发，无需等待。'



