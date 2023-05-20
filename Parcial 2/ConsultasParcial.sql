USE parcialcentrosmayores;

-- 1
SELECT centros.Nombre AS CENTRO, adultos.Nombre as NOMBRE ,adultos.Apellido AS APELLIDO
FROM adultos inner join centros
on adultos.Centro = centros.Nombre
order by centros.Nombre and adultos.Apellido;

-- 2
SELECT categorias.Nombre as Categoria , actividades.Fecha as Fecha, actividades.Nombre as Nombre_actividad,
 actividades.Descripcion As Descripcion, centros.Direccion as Direccion
 from (actividades inner join categorias
 on actividades.iDCategoria= categorias.idCategoria) inner join centros 
 on actividades.Centro=centros.Nombre;


-- 3
SELECT actividades.Nombre AS NOMBRE, adultos.Nombre as Nombre_Participante,  inscripciones.Calificacion as CALIFICACION
FROM (inscripciones inner join actividades on inscripciones.IdActividad=actividades.idActividad) inner join adultos on inscripciones.IdAdulto=adultos.idAdulto
order by Calificacion;

-- 4
SELECT adultos.Nombre As Nombre, adultos.Apellido as Apellido from (inscripciones inner join actividades on inscripciones.idActividad=actividades.idActividad) inner join adultos on inscripciones.IdAdulto=adultos.idAdulto where actividades.idActividad=2;

-- 5
SELECT actividades.Fecha AS FECHA,  actividades.Nombre AS NOMBRE, inscripciones.Calificacion AS CALIFICACION FROM (inscripciones inner join actividades on inscripciones.IdActividad=actividades.idActividad) inner join adultos on inscripciones.IdAdulto=adultos.idAdulto where adultos.idAdulto=4444