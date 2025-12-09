-- Fetch all patients'names and sexes
SELECT nombre, sexo FROM paciente; 

-- Fetch male patients or born before 1950
SELECT nombre, sexo, fecha_nacimiento FROM paciente
WHERE sexo = 'M' OR fecha_nacimiento < '1950-01-01';

-- Fetch female patients born after 2000 and smokers
SELECT nombre, sexo, fecha_nacimiento, fumador FROM paciente
WHERE fecha_nacimiento > '2000-01-01' AND fumador = 'True';

-- Fetch female patients born after 1950, smokers and whose names end with "o"
SELECT nombre, sexo, fecha_nacimiento, fumador FROM paciente
WHERE sexo = 'F' AND fecha_nacimiento > '1950-01-01' AND fumador = 'True'
AND nombre LIKE '%o';

-- Fetch smoker patients born before 1980 and who are not women
SELECT nombre, sexo, fecha_nacimiento, fumador FROM paciente
WHERE fumador = 'True' AND fecha_nacimiento < '1980-01-01'
AND sexo <> 'F';

-- Fetch not women patients who or are smokers or have obesity and diabetes
SELECT nombre, sexo, fumador, obesidad, diabetes FROM paciente
WHERE sexo <> 'F' AND 
(fumador = 'True' OR (obesidad ='True' AND diabetes = 'True'));