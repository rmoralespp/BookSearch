# BookSearch
Buscador de libros a partir de una BD local

# Tecnologías:
1.	**Python 2.7.14:** Lenguaje de Programación
2.	**PyQt 4:** Librería para la interfaz gráfica 
3.	**Sqlite 3:** Motor de BD 
4.	**Urllib:** Librería para hacer solicitudes web
5.	**Py2Exe:** Construir ejecutable de Window a partir de la aplicación en código Python.
# Arquitectura:
Se utilizó el modelo arquitectónico de 3 capas, definidas de la siguiente manera.
1.	**Capa Vista:** Se encarga de que el sistema interactúe con el usuario y viceversa
2.	**Capa Controlador:** Se reciben las peticiones del usuario, se procesa la información y se envían las respuestas tras el proceso.
3.	**Capa Servicio:** Es la encargada de la comunicación directa con la BD, además se utilizó para proveer servicios de paginado y notificaciones a las vistas de cambios en el Data Store.
# Patrones de Diseño:
1.	**Observer:** Encargado de notificar a las vistas suscritas a un determinado Data Store cuando se produce un cambio en su estado. Reduce el acoplamiento entre los componentes
2.	**Singleton:** Encargado de proveer una única instancia global a la aplicación de los Data Store que lo utilicen como metaclase.
3.	**Facade:** Proporcionar una interfaz simple para el subsistema servicios, de esta manera es utilizado como punto de entrada a él.
# Otro Elementos a destacar:
1.	**Thread:** Se utilizó para ejecutar procesos complejos en segundo plano de manera que impidiera el bloqueo de la interfaz gráfica que corre en el hilo principal.
2.	**Signals y Slots:** Se crearon señales propias que fueron conectadas a slots específicos, de esta manera cuando se iniciara y terminara un proceso en segundo plano, son notificados de estas acciones elementos que corren en el hilo principal.
3.	**Test:** Encargadas de probar y verificar el código de la aplicación
