USE proyecto_1_adalab;

-- Muestrame todos los Hombres entre los 30-34 años
SELECT age, gender 
FROM data_xml
WHERE age = "30-34" AND gender = "Man";

-- Distribución por generos de las personas comprendidas entre los 30 y 34 años
SELECT COUNT(age), gender 
FROM data_xml
WHERE age = "30-34" 
GROUP BY gender;

-- Muestrame el número de personas no-binarias que hay por cada rango de edad.
SELECT DISTINCT age, COUNT(gender)
FROM data_xml
WHERE gender = "Nonbinary" 
GROUP BY age
ORDER BY age;

-- Muestrame la distribución de los datos según los rangos de edad.
SELECT DISTINCT age, COUNT(gender)
FROM data_xml
GROUP BY age
ORDER BY age;