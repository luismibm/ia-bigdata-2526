# Fase 1: Documento Técnico

Luis Miguel Benítez | IA & Big Data 2025-26

## Fuentes

Opiniones de clientes (Texto y puntuación)  
CSV · Semi-estructurado

Ventas Diarias (Registro de transacciones)  
CSV · Estructurado

Interacciones (Fecha y tipo)  
CSV · Estructurado

## Transformación prevista
Limpiar los datos. Estandarizar campos como vfechas y tipos de datos.

## Elección de flujo
He elegido ETL porque me parece que se ajusta más a un tipo de carga incremental en la cual es posible actualizar sin recargar.

## Bibliografía

**Artículo: Data Lake vs Data Warehouse**
[(Enlace)](ttps://www.initiumsoft.com/blog_initium/data-lake-vs-data-warehouse/)

Leí este artículo para afianzar las diferencias y tomar una decisión.

**Hilo de Reddit: Figuring uout an ETL Pipeline**
[(Enlace)](https://www.reddit.com/r/dataengineering/comments/11zp198/need_help_figuring_out_an_etl_pipeline_for_csv/?tl=es-419)

Para mi Reddit es una vieja confiable, haciando una busqueda de ETL vs ELT me apareció este hilo. Aunque no influya en el propio trabajo, me confirmó que la selección de ETL para este supuesto fue correcta.