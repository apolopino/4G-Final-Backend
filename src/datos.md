## CONSIDERACIONES PARA LLENAR LA BASE DE DATOS A TRAVES DE INSOMNIA O SIMILAR

- Este archivo es para alimentar la base de datos a traves del metodo POST de cada enpoint.

- Considerar que los campos llenados que aluden a algun ID relacionado por FK debemos revisar sea un ID existente, de otra forma arrojara error "Cannot add or update a child row", aunq igualmente luego se llenar con null y relacionarlo a traves del administrador de la base de datos de forma manual. 

- Considerar tambien que muchos campos son unicos y al insertar el contenido en la base de datos puede q rechace el contenido si es el mismo insertado en otra instancia.

## DESAFIOS 
```
{
    "nombreDesafio": "Desafio 1",
    "descripcionDesafio": "Mejorar mi capacidad para organizarme",
    "feat1": "feature 1",
    "feat2": "feature 2",
    "feat3": "feature 3",
    "photoURL": "https://lamenteesmaravillosa.com/wp-content/uploads/2013/10/estanteria-forma-cabeza-libros-interior.jpg"
    },
{
    "nombreDesafio": "Desafio 2",
    "descripcionDesafio": "Mejorar mi alimentacion",
    "feat1": "feature 1",
    "feat2": "feature 2",
    "feat3": "feature 3",
    "photoURL": "https://www.clinicasobesitas.com/wp-content/uploads/2020/08/plato-saludable-2.jpg"
    },
{
    "nombreDesafio": "Desafio 3",
    "descripcionDesafio": "Modo Zen",
    "feat1": "feature 1",
    "feat2": "feature 2",
    "feat3": "feature 3",
    "photoURL": "https://ganar-ganar.mx/wp-content/uploads/2020/05/zen.jpg"
    },
{
    "nombreDesafio": "Desafio 4",
    "descripcionDesafio": "Leer mas",
    "feat1": "feature 1",
    "feat2": "feature 2",
    "feat3": "feature 3",
    "photoURL": "http://cdn2.dineroenimagen.com/media/dinero/styles/xlarge/public/images/2019/12/knowledge-10520101920.jpg"
    }
```

## EXTRA POST (Receta o rutina)
```
{
    "actividad": "Trabajo de core",
    "tipo": "Rutina",
    "descripcion": "Ejercicios enfocados en fortalecer la zona abdominal y espalda",
    "urlFoto": "https://marchasyrutas.b-cdn.net/wp-content/uploads/2017/06/los-mejores-ejercicios-de-abdominales-isometricos.jpg",
    "urlVideo": "https://www.youtube.com/watch?v=2tXQbi16EdI",
    "dia": "1"
    },
{
    "actividad": "Movilidad",
    "tipo": "Rutina",
    "descripcion": "ejercicios enfocados a mejorar la movilidad general",
    "urlFoto": "https://static.vecteezy.com/system/resources/previews/001/408/384/non_2x/yoga-poses-and-exercises-flat-character-set-vector.jpg",
    "urlVideo": "https://www.youtube.com/watch?v=BFJnw_7Q6wg",
    "dia": "1"
    },
{
    "actividad": "Trabajo de piernas",
    "tipo": "Rutina",
    "descripcion": "ejercicios enfocados a fortalecer piernas",
    "urlFoto": "https://i.ytimg.com/vi/A9OpakdHZzE/maxresdefault.jpg",
    "urlVideo": "https://www.youtube.com/watch?v=EecYrKhgAYI",
    "dia": "1"
    },
{
    "actividad": "Como leer mas",
    "tipo": "Rutina",
    "descripcion": "Recomendaciones para leer mas",
    "urlFoto": "https://www.comunidadbaratz.com/wp-content/uploads/Leer-es-un-modo-de-entretenimiento-y-conocimiento-que-desde-hace-tiempo-convive-y-compite-contra-otras-formas-de-ocio-e-informacion.jpg",
    "urlVideo": "https://m.elmostrador.cl/cultura/2020/08/20/diez-trucos-para-leer-mas/",
    "dia": "1"
    }
```

## TEMPLATETODO
```
{
  "name": "Template To Do3",
	"idDia": null
    }  
```

## TODOUSUARIO
```
{
    "actividad": "lavar ropa2",
    "done": false,
    "fecha": "2021-08-25",
    "userID": 2
    }
```