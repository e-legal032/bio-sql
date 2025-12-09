--1. Listar pacientes ordenados por nombre ascendente
SELECT nombre, sexo, fumador, diabetes, obesidad FROM paciente
ORDER BY nombre ASC;

--2. Listar pacientes ordenados por fecha de nacimiento descendente
SELECT nombre, sexo, fecha_nacimiento FROM paciente
ORDER BY fecha_nacimiento DESC;

--3. Listar pacientes ordenados primero por sexo y luego por nombre.
SELECT nombre, sexo, fecha_nacimiento FROM paciente
ORDER BY sexo ASC, nombre ASC;

--4. Listar pacientes ordenados por la longitud del nombre.
SELECT nombre, sexo, fecha_nacimiento FROM paciente
ORDER BY LENGTH(nombre) DESC;

--5. Listar pacientes ordenados por edad calculada (de mayor a menor).
SELECT nombre, sexo, fecha_nacimiento,
    AGE(CURRENT_DATE, fecha_nacimiento) AS edad 
FROM paciente
ORDER BY edad DESC; 

--6. Listar pacientes ordenados por IMC calculado (peso / altura²).
--mi tabla paciente no tiene datos de peso ni altura ni otro dato para calcular

--7. Listar pacientes ordenados por año de nacimiento.
SELECT nombre, sexo, fecha_nacimiento FROM paciente
ORDER BY EXTRACT(YEAR FROM fecha_nacimiento) ASC;

--8. Listar pacientes ordenados con CASE: primero mujeres, luego hombres, luego otros.
SELECT nombre, sexo, fecha_nacimiento FROM paciente
ORDER BY CASE
    WHEN sexo = 'F' THEN 1
    WHEN sexo = 'M' THEN 2
    ELSE 3
END;   


