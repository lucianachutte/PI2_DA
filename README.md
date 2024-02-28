<p align="center"><h2>PROYECTO INDIVIDUAL Nº2 </h2></p> 
![image](https://github.com/lucianachutte/PI2_DA/blob/master/imagenes/SINIESTROS VIALES.png)

*<h3> INTRODUCCIÓN:</h3>*
Este proyecto implica desempeñar el papel de un Analista de Datos dentro de un equipo de una empresa consultora. Este equipo ha sido solicitado por el Observatorio de Movilidad y Seguridad Vial (OMSV), un centro de investigación bajo la Secretaría de Transporte del Gobierno de la Ciudad Autónoma de Buenos Aires (CABA), para llevar a cabo un proyecto de análisis de datos.

El objetivo principal es proporcionar información que ayude a las autoridades locales a tomar medidas para reducir el número de víctimas mortales en accidentes de tráfico en CABA. Para lograr esto, se cuenta con un conjunto de datos sobre homicidios en accidentes de tráfico ocurridos en la Ciudad de Buenos Aires entre 2016 y 2021.

*<h3> CONTEXTO:</h3>*
Los siniestros viales, también conocidos como accidentes de tráfico o accidentes de tránsito, son eventos que involucran vehículos en las vías públicas y pueden tener diversas causas, como colisiones entre automóviles, motocicletas, bicicletas o peatones, atropellos, choques con objetos fijos o caídas de vehículos. Estos incidentes pueden tener consecuencias que van desde daños materiales hasta lesiones graves o fatales para los involucrados.

La Ciudad Autónoma de Buenos Aires, ubicada en la provincia de Buenos Aires en Argentina, no es una excepción a esta problemática, ya que los siniestros viales son una preocupación importante debido al alto volumen de tráfico y la densidad poblacional. Estos incidentes pueden impactar significativamente en la seguridad de los residentes y visitantes de la ciudad, así como en la infraestructura vial y los servicios de emergencia. Con una población de 3,120,612 habitantes en una superficie de 200 km² según el censo de 2022, y un registro de 12,437,735 vehículos transitando por los peajes de las autopistas de acceso a CABA en julio de 2023, la prevención de siniestros viales y la implementación de políticas efectivas son fundamentales para abordar este problema de manera adecuada.

*<h3> DATOS:</h3>*
Se analizó el conjunto de datos denominado "Homicidios", que contiene los apartedos "Hechos" y "Víctimas" de la página [Link](https://data.buenosaires.gob.ar/dataset/victimas-siniestros-viales) del Gobierno de la Ciudad, son de uso público y se encuentran en formato excel.
- El apartado de "Hechos" contiene Id único del suceso, fecha en la que se produjo, la locación, y el rol de los participantes.
- El apartado "Víctimas" contiene datos sobre las mismas, como edad, sexo, y modo de desplazamiento; como así también el Id del hecho.
- Se ingesto otro dataset de la página del Gobierno de la Ciudad, para ver a qué barrios correspondía cada comuna [Link](https://buenosaires.gob.ar/sindicatura/universo-de-control/comunas-15)
- Se sacaron los datos oficiales de los censos 2010 y 2022 para establecer la cantidad de habitantes de la Ciudad Autónoma de Buenos Aires [Link](https://censo.gob.ar/index.php/datos_definitivos_caba)

*<h3>ANÁLISIS:</h3>*
- Para la elaboración de este proyecto se utilizó Python y Pandas para los procesos de extracción, transformación y carga de los datos, como así también para el análisis exploratorio de los datos se utilizó matplotlib y seaborn.
- Para la construcción de un dashboard interactivo se utilizó Power BI.

Se buscó valores faltantes, valores atípicos/extremos u outliers en el dataset,se trataron los valores 'Sin datos' y se verificó la inexistencia de duplicados en el proceso de Extracción, Transformación y Carga (ETL).
Se examinaron diferentes atributos del conjunto de datos, como roles, sexo, edad, entre otros.Se visualizó la distribución de roles en los accidentes, desglosada por género y edad,como asi tambien se examinó la cantidad de víctimas y se identificaron casos de accidentes con múltiples víctimas.
![image](https://github.com/lucianachutte/PI2_DA/blob/master/imagenes/1.png)

Se analizó la distribución de accidentes a lo largo del tiempo, identificando picos y tendencias estacionales.
![image](https://github.com/lucianachutte/PI2_DA/blob/master/imagenes/5.png)

Exploración de la Ubicación de los Accidentes,se exploró la cantidad de accidentes por comuna, identificando las comunas con mayor y menor número de accidentes de tránsito.
![image](https://github.com/lucianachutte/PI2_DA/blob/master/imagenes/4.png)

Se examinaron las intersecciones más frecuentes donde ocurrieron accidentes y se estudió el impacto del tipo de calle en la seguridad vial.
![image](https://github.com/lucianachutte/PI2_DA/blob/master/imagenes/3.png)


*<h3> KPIs:</h3>*
Se plantearon tres objetivos en relación a la disminución de la cantidad de víctimas fatales de los siniestros viales, desde los cuales se proponen tres indicadores de rendimiento clave o KPI.

:yellow_circle: Reducir en un 10% la tasa de homicidios en siniestros viales de los últimos seis meses, en CABA, en comparación con la tasa de homicidios en siniestros viales del semestre anterior .

Definimos a la tasa de homicidios en siniestros viales como el número de víctimas fatales en accidentes de tránsito por cada 100.000 habitantes en un área geográfica durante un período de tiempo específico. Su fórmula es: (Número de homicidios en siniestros viales / Población total) * 100,000

En el contexto del primer semestre del año 2021, la tasa de homicidios en siniestros viales fue de 1.77., es decir que se registraron aproximadamente 1.77 homicidios en accidentes de tránsito por cada 100,000 habitantes. Al calcular la tasa de homicidios viales para el segundo semestre de ese año, se pudo apreciar que fue del 1.35. Por lo tanto, se logró cumplir con la meta propuesta indicada precedentemente.


:yellow_circle: Reducir en un 7% la cantidad de accidentes mortales de motociclistas en el último año, en CABA, respecto al año anterior .

Definimos a la cantidad de accidentes mortales de motociclistas en siniestros viales como el número absoluto de accidentes fatales en los que estuvieron involucradas víctimas que viajaron en moto en un determinado periodo temporal. Su fórmula para medir la evolución de los accidentes mortales con víctimas en moto es: (Número de accidentes mortales con víctimas en moto en el año actual - Número de accidentes mortales con víctimas en moto en el año anterior) / (Número de accidentes mortales con víctimas en moto en el año anterior) * 100

En este caso, se calculó la Cantidad de accidentes mortales de motociclistas para el año 2020 (año anterior), el cual resultó de -44.00, de esta manera el objetivo a cumplir es de -40.92. Al momento de calcular la cantidad de accidentes mortales de motociclistas para el año 2021 resultó de 64.29 lo que significa que aumentó un 64% la cantidad de muertes de conductores de motociclistas respecto del 2021. Por lo tanto, no se logró cumplir con la meta propuesta indicada precedentemente.


:yellow_circle: Reducir en un 10% la cantidad de accidentes mortales producidos en el último año, en cruce de calles, en CABA, respecto al año anterior. Se define al número de víctimas fatales en accidentes de tránsito en cruce de calles por cada 100,000 habitantes en un área geográfica durante un período de tiempo específico, en este caso anual.(Número de accidentes mortales de víctimas en cruce de calles / Población total) *100,000

En el año 2020 (año anterior), la tasa de accidentes mortales producidos en cruce de calles fue de 2.03, es decir que se registraron aproximadamente 2.03 homicidios en accidentes de tránsito por cada 100,000 habitantes. Al calcular la tasa para el año actual, es decir 2021, se pudo apreciar que fue del 2.13. Por lo tanto, no se logró cumplir con la meta propuesta indicada precedentemente.
 

![image](https://github.com/lucianachutte/PI2_DA/blob/master/imagenes/kpi.png)

*<h3> CONCLUSIONES:</h3>*
Entre los años 2016 y 2021, ocurrieron 719 muertes por accidentes de tránsito en la Ciudad Autónoma de Buenos Aires. La mayoría de estos incidentes, cerca del 61%, tuvieron lugar entre 2016 y 2018, seguidos de una disminución en los años siguientes, 2019, 2020 y 2021. Diciembre emergió como el mes con mayor número de víctimas, mientras que los lunes fueron los días con más accidentes, principalmente entre las 06:00 y las 09:00 horas.

Por otro lado, se destaca que el 77% de las víctimas fueron hombres, con un pico en el grupo de edad de 35 a 44 años. Aproximadamente el 45% de los fallecidos conducían un vehículo, y el 42% viajaban en motocicleta. La mayoría de los accidentes, el 62%, ocurrieron en avenidas, y el 75% tuvo lugar en intersecciones de calles. Además, la Comuna 1, que incluye los barrios de Retiro, San Nicolás, Puerto Madero, San Telmo, Montserrat y Constitución, registró la mayor cantidad de accidentes.

Si bien se logró cumplir con la meta de reducir la tasa de homicidios por accidentes de tránsito para el segundo semestre de 2021, no se alcanzaron los objetivos de disminuir la cantidad de accidentes mortales entre motociclistas y en intersecciones de calles para el año 2021 en comparación con 2020.

*<h3> RECOMENDACIONES:</h3>*
 :small_blue_diamond: Reforzar controles en avenidas. 

:small_blue_diamond: Reforzar controles de motociclistas.

:small_blue_diamond: Reforzar campañas entre los días viernes y lunes.

:small_blue_diamond: Reforzar controles en la Comuna 1.

:small_blue_diamond: Realizar más campañas de educación vial, especialmente para el sexo masculino.