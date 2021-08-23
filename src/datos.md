Este archivo es para alimentar la base de datos a traves del metodo POST de cada enpoint.

Considerar que los campos llenados que aluden a algun ID relacionado por FK debemos revisar sea un ID existente, de otra forma arrojara error "Cannot add or update a child row", aunq igualmente luego se llenar con null y relacionarlo a traves del administrador de la base de datos de forma manual. 


En cuanto a la fecha de la tabla TodoLog tambien hay q hacerlo de forma manual.

Considerar tambien que muchos campos son unicos y al insertar el contenido en la base de datos puede q rechace el contenido si es el mismo insertado en otra instancia.

{
  "desafios": [
    {
      "descripcion": "Mejorar mi capacidad para organizarme", 
      "dias del desafio": [
        {
          "id": 1, 
          "idDesafio": 1, 
          "idReceta": null, 
          "idRutina": null, 
          "numeroDia": 1
        }
      ], 
      "feat1": "1", 
      "feat2": "2", 
      "feat3": "3", 
      "id": 1, 
      "nombreDesafio": "Desafio 1", 
      "photoURL": "https://lamenteesmaravillosa.com/wp-content/uploads/2013/10/estanteria-forma-cabeza-libros-interior.jpg"
    }, 
    {
      "descripcion": "Mejorar mi alimentacion", 
      "dias del desafio": [], 
      "feat1": "4", 
      "feat2": "5", 
      "feat3": "6", 
      "id": 5, 
      "nombreDesafio": "Desafio 2", 
      "photoURL": "https://www.clinicasobesitas.com/wp-content/uploads/2020/08/plato-saludable-2.jpg"
    }, 
    {
      "descripcion": "Modo Zen", 
      "dias del desafio": [], 
      "feat1": "7", 
      "feat2": "8", 
      "feat3": "9", 
      "id": 6, 
      "nombreDesafio": "Desafio 3", 
      "photoURL": "https://ganar-ganar.mx/wp-content/uploads/2020/05/zen.jpg"
    }, 
    {
      "descripcion": "Leer mas", 
      "dias del desafio": [], 
      "feat1": "10", 
      "feat2": "11", 
      "feat3": "12", 
      "id": 7, 
      "nombreDesafio": "Desafio 4", 
      "photoURL": "http://cdn2.dineroenimagen.com/media/dinero/styles/xlarge/public/images/2019/12/knowledge-10520101920.jpg"
    }
  ], 
  "msg": "Hello, this is your GET /dias response "
}


{
  "msg": "Hello, this is your GET /rutina response ", 
  "rutina": [
    {
      "descripcion": "ejercicios enfocados en fortalecer la zona abdominal y espalda", 
      "id": 1, 
      "name": "Trabajo de core", 
      "urlFoto": "https://marchasyrutas.b-cdn.net/wp-content/uploads/2017/06/los-mejores-ejercicios-de-abdominales-isometricos.jpg", 
      "urlVideo": "https://www.youtube.com/watch?v=2tXQbi16EdI"
    }, 
    {
      "descripcion": "ejercicios enfocados a mejorar la movilidad general", 
      "id": 2, 
      "name": "Movilidad", 
      "urlFoto": "https://static.vecteezy.com/system/resources/previews/001/408/384/non_2x/yoga-poses-and-exercises-flat-character-set-vector.jpg", 
      "urlVideo": "https://www.youtube.com/watch?v=BFJnw_7Q6wg"
    }, 
    {
      "descripcion": "ejercicios enfocados a fortalecer piernas", 
      "id": 4, 
      "name": "Trabajo de piernas", 
      "urlFoto": "https://i.ytimg.com/vi/A9OpakdHZzE/maxresdefault.jpg", 
      "urlVideo": "https://www.youtube.com/watch?v=EecYrKhgAYI"
    }, 
    {
      "descripcion": "Recomendaciones para leer mas", 
      "id": 5, 
      "name": "Como leer mas", 
      "urlFoto": "https://www.comunidadbaratz.com/wp-content/uploads/Leer-es-un-modo-de-entretenimiento-y-conocimiento-que-desde-hace-tiempo-convive-y-compite-contra-otras-formas-de-ocio-e-informacion.jpg", 
      "urlVideo": "https://m.elmostrador.cl/cultura/2020/08/20/diez-trucos-para-leer-mas/"
    }
  ]
}


{
  "dias": [
    {
      "id": 1, 
      "idDesafio": 1, 
      "idReceta": null, 
      "idRutina": null, 
      "numeroDia": 1
    }, 
    {
      "id": 4, 
      "idDesafio": null, 
      "idReceta": null, 
      "idRutina": null, 
      "numeroDia": 2
    }, 
    {
      "id": 5, 
      "idDesafio": null, 
      "idReceta": null, 
      "idRutina": null, 
      "numeroDia": 3
    }, 
    {
      "id": 6, 
      "idDesafio": null, 
      "idReceta": null, 
      "idRutina": null, 
      "numeroDia": 4
    }
  ], 
  "msg": "Hello, this is your GET /dias response "
}

{
  "msg": "Hello, this is your GET /templatetodo response ",
  "templatetodo": [
    {
      "id": 1,
      "idDia": null,
      "name": "Template To Do"
    },
    {
      "id": 2,
      "idDia": null,
      "name": "Template To Do2"
    },
    {
      "id": 3,
      "idDia": null,
      "name": "Template To Do3"
    }
  ]
}

{
  "msg": "Hello, this is your GET /recetas response ",
  "recetas": [
    {
      "descripcion": "hdrhd",
      "id": 1,
      "name": "Receta 1",
      "urlFoto": "dfdfhda",
      "urlVideo": "fhd"
    },
    {
      "descripcion": "asfsa",
      "id": 3,
      "name": "Receta 2",
      "urlFoto": "asfa",
      "urlVideo": "afas"
    },
    {
      "descripcion": "dga",
      "id": 4,
      "name": "Receta 3",
      "urlFoto": "sdga",
      "urlVideo": "asdga"
    }
  ]
}

{
  "msg": "Hello, this is your GET /todolog response ",
  "todolog": [
    {
      "date": "2021-08-24",
			"desafioID": 1,
      "done": false,
			"userID": 1
    },
    {
      "date": "2021-08-24",
			"desafioID": 1,
      "done": false,
			"userID": 2
    }
  ]
}