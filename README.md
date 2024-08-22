# PUBLICART 2.0
Versión 2.0 del proyecto integrado de Alejandro Neal Chirino realizado en el grado superior de Desarrollo de Aplicaciones Web en el centro IES Martínez Montañés.

## Información del proyecto
La aplicación trata de una red social centrada en comunidades artísticas donde los apasionados del arte podrán compartir sus gustos, publicitarse y tradear entre ellos de manera segura.
<br>
Para llevar esto acabo los usuarios podrán crear perfiles donde podrán publicar sus obras o servicios que quieran ofrecer pudiendo agregar fotos, la opción de comentar y de poder comprar sus obra/servicio.
<br>
Existirá la opción de chats entre usuarios y grupos de usuarios para fortalecer la comunidad junto a grupos de difusión donde los usuarios podrán promocionarse con mayor facilidad.
<br>
Los usuarios podrán serguirse los unos a los otros para aumentar su alcance y hacer que les aparezcan contenido de su preferencia, dando también la opción de explorar obras de perfiles que no siguen y la búsqueda de usuarios.
<br>
Las compras se llevaran acabo con paypal para asegurar el importe y realizando los trámites necesarios para evitar estafas, ej.:reteniendo el pago hasta confirmar la que las dos partes han actuado acorde a lo acordado (está por determinar)
<br>
Para mejorar la confianza de los compradores, cada usuario tendrá un historial de ventas donde el comprador podrá dejar un comentario opinando del servicio.

## Información técnica
La lógica trasera, donde se manejará los datos y comportamiento del servidor será llevada a cabo con django rest framework; mientras que la lógica del cliente será manejada con vue.js

## Objetivos a conseguir
1. Mejorar el rendimiento de la aplicación en comparación con su versión anterior.
    - Actualizar la estructura de la base de datos
    - Redifinir los serializers y views para evitar grandes cantidades de consultas
    - Modificar consultas en el front para evitar cargar todos los datos en una página
1. Implementar mis conocimientos recientemente aprendidos sobre la tecnología Vue.js, ya que gracias a su estructura es más intuitivo y está mejor estructurado, a parte, da la opción de usar js en lugar de ts.