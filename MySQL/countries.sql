USE world;
-- 1
SELECT countries.name AS country, languages.language, languages.percentage
FROM countries
JOIN languages ON countries.id = languages.country_id
WHERE languages.language = "Slovene"
ORDER BY languages.percentage DESC;
-- 2
SELECT countries.name, COUNT(*) AS Cities
FROM cities
LEFT JOIN countries ON cities.country_id = countries.id
GROUP BY countries.name
ORDER BY Cities DESC;
-- 3
SELECT cities.name, cities.population
FROM cities
WHERE cities.country_code = "MEX" AND cities.population > 500000
ORDER BY cities.population DESC;
-- 4
SELECT countries.name, languages.language, languages.percentage
FROM countries
JOIN languages on countries.id = languages.country_id
WHERE languages.percentage > 89
GROUP BY countries.name
ORDER BY languages.percentage DESC;
-- 5
SELECT countries.name, countries.surface_area, countries.population
FROM countries
WHERE population > 100000 AND surface_area < 501;
-- 6
SELECT countries.name, countries.government_form, countries.capital, countries.life_expectancy
FROM countries
WHERE government_form = "Constitutional Monarchy" AND capital > 200 AND life_expectancy > 75;
-- 7
SELECT countries.name AS country_name, cities.name, cities.district, cities.population
FROM cities
JOIN countries ON countries.id = cities.country_id
WHERE cities.district = "Buenos Aires" AND cities.population > 500000;
-- 8
SELECT region, COUNT(*) AS Countries
FROM countries
-GROUP BY region
ORDER BY countries DESC;