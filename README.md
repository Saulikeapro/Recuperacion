# Recuperacion

# Objetivo del proyecto

Desarollar un sistema el cual sea capaz de recomendar un medio de transporte a una persona dependiendo de las condiciones seleccionadas por el usuario

# Casos utilizados y explicación

Puede utilizarse para saber que metodo de transopre es mejor suponiendo que vives cerca de la escuela y hace buen clima puedes ir caminando en cambio si la distancia es media para ir caminando unos 20 minutos aprox te recomendara transporte publico(Camion) ya si la vives a 1 hora es recomendable usar automovil

# Descripción del la base de conocimiento

-La base de conocimientos se encuentra organizada de manera modular, lo que permite agregar, modificar o eliminar reglas sin necesidad de alterar el motor de inferencia, esta característica hace que el sistema sea flexible y escalable, manteniendo una clara separación entre el conocimiento del dominio y la lógica, esta base de conocimientos permite que el sistema experto analice una situación concreta, aplique el razonamiento definido por las reglas y genere una recomendación clara y coherente, cumpliendo con los principios de un sistema experto sencillo.

# Instrucciones para ejecutar el proyecto

-pip install tk para instalar tkinter
-Compilar el codigo, como tkinter es la unica libreria que se utiliza solo requiere eso

# Casos de prueba
Distancia corta, clima bueno, sin transporte público
<img width="366" height="402" alt="image" src="https://github.com/user-attachments/assets/12270da6-f7cc-42de-87d4-ceedce3642a7" />

Distancia media, clima malo, con transporte público
<img width="365" height="403" alt="image" src="https://github.com/user-attachments/assets/868a5bb8-2ca5-4a5b-a52b-cc1a5cbb50b7" />

Distancia larga, cualquier clima
<img width="369" height="403" alt="image" src="https://github.com/user-attachments/assets/bfe30d0d-33bf-4ba9-8ec0-32eb9ba4a91a" />

