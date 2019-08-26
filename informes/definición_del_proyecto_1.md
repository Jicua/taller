Marco Teórico
-------------

La manera en que se comunican las empresas con sus clientes evoluciona de la mano con los avances tecnológicos y en la actualidad se ve una clara tendencia al uso de las redes sociales. Las empresas hacen uso de los beneficios de las redes sociales, por ejemplo, promocionar sus productos, dar a conocer ofertas, etc. Pero no solo se limita al marketing y publicidad si no que también pueden ayudar en otros ámbitos del negocio como soporte en línea, atención de post ventas, transacciones, etc. 

>“En algunos países, WhatsApp es como el oxígeno” – Jan Koum, cofundador de WhatsApp.

Nuestro proyecto se centrará en la atención al cliente, principalmente la reserva de horas. Esto lo realizaremos mediante una solución informática que incluirá un sistema automatizado de mensajería instantánea, utilizando la aplicación para smartphones WhatsApp, el cual capturará las peticiones de los clientes y las procesará transformándolas en información útil para facilitar las operaciones diarias de la empresa. 
Gracias a la masiva adopción de la aplicación de mensajería instantánea WhatsApp por el público chileno cada vez más empresas optan por usar esta herramienta para comunicarse con sus clientes. Es probable que el público este dispuesto a comunicarse con la empresa mediante una plataforma que esta acostumbrada a utilizar diariamente, como lo es WhatsApp, que por otros medios como mails o formularios web.

En el mundo moderno de hoy la mayoría de las interacciones entre la gente suceden en las redes sociales. Ahora más transacciones se realizan en plataformas sociales que en páginas web. La gente se ha dado cuenta de los beneficios de usar las aplicaciones para conectarse con las empresas. WhatsApp es la próxima mejor plataforma para ofrecer productos y servicios.

>“Si recibes un mensaje de WhatsApp, probablemente lo vas a abrir. Eso es lo interesante.” Harper Reed, emprendedor estadounidense.

Esta frase ejemplifica la importancia de WhatsApp y su influencia en el público. Por esto los chatbots de WhatsApp podrían ser una ventaja para cualquier negocio.

WhatsApp es usado en más de 180 países alrededor del mundo, tiene más del 40% de cuota de mercado, más de 1.500 millones de usuarios y es el líder indiscutido del mercado. 

Fuente:https://chatbotsmagazine.com/a-step-by-step-guide-to-creating-whatsapp-chatbot-for-business-275dc3924b17

En la gran mayoría de las empresas existe una persona encarga de responder a los mensajes. Esto tiene varios inconvenientes, tanto desde el punto de vista de la empresa como del cliente. Para la empresa se gastan recursos al tener a una persona dedicada a esta labor y para el cliente, ya que no siempre recibe una atención inmediata pues el encargado puede estar ocupado o atendiendo a otras solicitudes. En contraste al reemplazarse esta persona por un sistema automatizado, se ahorran recursos y se mejora la atención al cliente.


Solución tecnológica
---------------------

Formulación

Principalmente nuestro sistema organizará la agenda del mecánico, lo que le permitirá tener un flujo de trabajo más ordenado y hará más eficiente la comunicación con sus clientes. 

Básicamente el funcionamiento del sistema es el siguiente: Un servidor Windows server 2012 R2 ejecutará el explorador web Google Chrome en el cual mediante Selenium y un script en Python controlará una instancia de WhatsApp web recibiendo y respondiendo los mensajes de los clientes cotejando con una base de datos 
(mySql) en el mismo servidor, para asignarles sus citas y posteriormente notificarles cuando pueden retirar su vehículo. Paralelamente la aplicación móvil del mecánico se actualizará con la base de datos del servidor para informar al mecánico su agenda próxima. 

El sistema estará disponible idealmente todos los días del año, siempre que todos los dispositivos involucrados cuenten con una conexión a internet. En cuanto a seguridad, la información que maneja el sistema no es sensible (no incluye contraseñas, tarjetas de crédito, mails, etc.) aún así se aprovecha la encriptación de extremo a extremo que provee WhatsApp para asegurar la información en tránsito contra ciber ataques, mientras que el servidor que almacena esta información cuenta con las actualizaciones más recientes del software que utiliza minimizando la posibilidad de que haya vulnerabilidades.
