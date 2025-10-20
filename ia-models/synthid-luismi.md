# SynthID: Análisis de una aplicación para clasificar contenido creado por modelos generativos

Josep Tormo y Luis Miguel Benítez | IA & Big Data 2024-25

<!--
Redactado por personas reales, no por IA.
Esperemos que se aprecie el esfuerzo.
-->


## Resumen

SynthID esta diseñada para insertar marcas de agua digitales en contenido generado o modificado por inteligencia artificial.

Esto incluye imágenes, audio, videos y textos con el fin de identificar y diferenciar dicho contenido del producido por humanos. Estas son imperceptibles para las personas pero no para estas herramientas, Esto ayuda a combatir la desinformación y facilitar la trazabilidad en el uso de IA.


## Introducción

Hemos escogido esta herramienta porque creemos que respresenta una solución real a un problema  creciente. Con la evolucion de los models generativos, se dificulta día a día distinguir que contenido es o no generado por estos. 

Por ello, es necesaria una herramienta que ayude a verificar si un contenido esta creado o no por modelos de inteligencia artificial.

Synth-ID aplica un esquema de marca de agua generativa. Dicho de otra forma, a marca de agua se genera a la par que el contenido y existe dentro de este último.


## Desarrollo

### Contexto y objetivos

Hoy en día, es necesario asegurar la veracidad y origen del contenido. Siendo las principales razones:
- La desinformación que puede causar.
- El avance de nuevos modelos podría estar siendo mermado por la baja o nula calidad de los datos, siendo estos en su mayoría generados y por tanto interfiriendo en el entrenamiento.


### Tecnicas Usadas

Cuando una ia generativa crea contenido lo hace mediante un calculo probabilístico, SynthID modifica el procedimiento para inyectar una firma estadística sutil.

Utiliza un algoritmo que parte de una semilla aleatoria, este evalúa opciones candidatas y las somete a un proceso de eliminación como si de un torneo se tratase, aquellas opciones “ganadoras” forman parte de esta firma estadística.


### Resultados y ejemplos

Presentación de la herramienta, donde se puede apreciar su funcionalidad:
[Enlace](https://www.youtube.com/watch?v=9btDaOcfIMY)

## Conclusiones

En un mundo en que la IA está cada vez más presente, estas herramientas son necesarias. No solo para asegurar un uso ético y responsable, también para que estos mismos sistemas no sean redundantes y asegurar un estandar de calidad.

## Bibliografía

[SynthID Landing Page](https://deepmind.google/science/synthid)

[Paper: Scalable watermarking for identifying large lenguaje model outputs](https://www.nature.com/articles/s41586-024-08025-4)