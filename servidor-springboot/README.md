
********************************************
Pasos para ejecutar el proyecto
********************************************

**Paso 1) Descargar del GIT.**


**Paso 2) Configurar el Application properties.**

En el archivo "application.properties" que lo encuentra en la carpeta "src/main/resources" debe ajustar:
- spring.datasource.url (Es la localización de su base de datos postgres, "localhost" es el servidor, "5432" es el puerto y "sd" es el nombre de la base de datos)

Estos items puede dejarlo como está
- server.servlet.context-path= (El path principal de la aplicacion via URL, todos los subpath serán recepcionados por la aplicación)
- server.port (el numero de puerto HTTP que levantará la aplicación)


**Paso 3) Dar permisos de ejecución al script.**

Debe estar ubicado en la carpeta principal (donde estan los archivos pom.xml, mvnw, este archivo README.md, etc.)

Debe ejecutar el siguiente comando para dar persmiso de ejecución a su script (Linux/Mac):
     chmod +x mvnw 


**Paso 4) Ejecutar en modo localhost.**

Debe estar ubicado en la carpeta principal (donde estan los archivos pom.xml, mvnw, este archivo README.md, etc.)

./mvnw spring-boot:run


**Paso adicional en caso que desee Empaquetar (Si desea desplegar en un servidor)**

Debe estar ubicado en la carpeta principal (donde estan los archivos pom.xml, mvnw, este archivo README.md, etc.)
./mvnw clean package



****************************************************
Pasos seguidos para crear y desarrollar el proyecto
****************************************************

Paso 1) Se crea el proyecto basado en el Framework SpringBoot de Java
https://start.spring.io
Maven
Version 2.7.17
Jar
Java 11

Referencias:
https://spring.io/guides/gs/rest-service/
https://spring.io/guides/gs/accessing-data-jpa/
https://docs.spring.io/spring-data/jpa/docs/1.6.0.RELEASE/reference/html/jpa.repositories.html