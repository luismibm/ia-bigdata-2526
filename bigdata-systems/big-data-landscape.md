#  Big Data: Paisaje

Luis Miguel Benítez | IA & Big Data 2025-26

<!--
Aunque ayudado por IA para la busqueda de información, esta ha sido "filtrada" y redactada con palabras propias <3
-->

### AWS S3

Amazon lo presenta como una herramienta de almacenamiento de objetos (Data Lake). Otros grandes como Google o Microsoft tienen "sus versiones" llamadas Google Cloud Storage y Azure Blob Storage.

Actua en la capa de alamacenamiento.


### Databricks

Databricks es dificl de clasificar, ya que parece hacer un poco de todo. En la landing aparece un apartado de USE CASES donde se mencionan AI, Governance, Warehousing, ETL, Data Sharing y Orchestration.

Una de las opciones que Perplexity compara con Databricks es Azure Synapse, aunque por su landing no queda tan claro que se tarte de el mismo tiempo de herramienta o que cumplan el mismo requisito.


### Tableau
Es una herramienta de Business Intelligence. La herramienta más parecida es Power BI y ambas tienen la misma aplicación: creación de dashboards y reporting. 

Como dato adicional, parece que ninguna de las opciones tiene un plan gratuito, ambas herramientas son de pago y enfocadas a entornos Corporate.


### Apache Kafka

Google la define como "plataforma de streaming de eventos de código abierto para recopilar, procesar y almacenar datos de streaming en tiempo real", por lo que está claro que pertenece a la categoría de streaming.

Lo curioso de esta opción es que uno de sus competidores es Apache Pulsar (también de Apache). Entre otras cosas, parece que Kafka es la opción más usada (siendo además algo más sencilla), mientras que Pulsar ofrece una alternativa qeu permite ir más al detalle con la contraparte de uqe añade complejidad.

https://kunalkkg.medium.com/the-battle-of-message-queues-apache-kafka-vs-apache-pulsar-102a6100b023 


### Elasticsearch
Además de motor de búsqueda, permite alamcenar datos estructurados, no estructurados y vectoriales en tiempo real. Por esto, lo categorizaría en ambas categorías/capas.

Como alternativa tenemos Apache Solr, aunque esta no parece nombrar nada de almacenamiento.


### Apache Airflow

Se define a si misma como una herramienta "to programmatically author, schedule and monitor workflow", haciendo esto que pertenezca a la categoría de Orquestación.

Otra opción que a primera vista es extremadamente similar es Prefect, Haciendo está también incapié en su uso exclusivo (o casi exclusivo) de Python.


### MongoDB

MongoDB entraría en la categoría de bases de datos NoSQL, alamcenando datos semi-estructurados. Un competidor sería Dynamo DB.


### Apache Spark

Spark es una herramienta disponible tanto para necesidades de Big Data como Machine Leraning, permitiendo parios tipos de procesamiento de datos como batch o streaming. Una alternativa podría ser Hadoop.


### Snowflake

Aunque los LLMs solo destacan de Snowflake el ser un Data Warehoude, realmentre la landing ofree má información, habiendo evolucionado de algo específico a un ecosistema entero que incluye funciones de almacenamiento y porcesamiento. Un competir podría ser el antes mencionado Databricks.


### dbt

Esta herramienta entraría en la capa de transformación, aunque parece diferenciarse de las anteriores por tener un sietam muy pulido, permitiendo uan transformación de los datos muy efectiva (también mencioan preparación de datos dento del Warehouse), centrandose en información en la que puedes confiar. 


<!--
https://github.com/luismibm/ia-bigdata-2526
-->