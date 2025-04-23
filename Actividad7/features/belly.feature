# language: es

Característica: Característica del estómago

  Escenario: comer muchos pepinos y gruñir
    Dado que he comido 42 pepinos
    Cuando espero 2 horas
    Entonces mi estómago debería gruñir

  Escenario: comer pocos pepinos y no gruñir
    Dado que he comido 10 pepinos
    Cuando espero 2 horas
    Entonces mi estómago no debería gruñir

  Escenario: comer muchos pepinos y esperar menos de una hora
    Dado que he comido 50 pepinos
    Cuando espero media hora
    Entonces mi estómago no debería gruñir

  Escenario: comer pepinos y esperar en minutos
    Dado que he comido 30 pepinos
    Cuando espero 90 minutos
    Entonces mi estómago debería gruñir

  Escenario: comer pepinos y esperar en diferentes formatos
    Dado que he comido 25 pepinos
    Cuando espero "dos horas y treinta minutos"
    Entonces mi estómago debería gruñir
  
  Escenario: comer pepinos y esperar en horas, minutos y segundos
    Dado que he comido 35 pepinos
    Cuando espero "1 hora y 30 minutos y 45 segundos"
    Entonces mi estómago debería gruñir

  Escenario: comer una cantidad fraccionaria de pepinos
    Dado que he comido 0.5 pepinos
    Cuando espero 2 horas
    Entonces mi estómago no debería gruñir

  Escenario: intentar comer una cantidad negativa de pepinos
    Dado que he comido -21 pepinos
    Entonces deberia producirse un error

  Escenario: esperar usando horas en inglés
    Dado que he comido 20 pepinos
    Cuando espero "two hours and thirty minutes"
    Entonces mi estómago debería gruñir

  Escenario: comer pepinos y esperar un tiempo aleatorio
    Dado que he comido 25 pepinos
    Cuando espero un tiempo aleatorio entre 1 y 3 horas
    Entonces mi estómago debería gruñir

  Escenario: Manejar una cantidad no válida de pepinos
    Dado que he comido -5 pepinos
    Entonces deberia producirse un error

  Escenario: comer 1000 pepinos y esperar 10 horas
    Dado que he comido 1000 pepinos
    Cuando espero "10 horas"
    Entonces mi estómago debería gruñir

  Escenario: manejar tiempos complejos(es) 
    Dado que he comido 50 pepinos
    Cuando espero "1 hora, 30 minutos y 45 segundos"
    Entonces mi estómago debería gruñir

  Escenario: manejar tiempos complejos(en) 
    Dado que he comido 25 pepinos
    Cuando espero "thirty minutes and 1 hour, 45 seconds"
    Entonces mi estómago debería gruñir

  Escenario: comer mas de 10 pepinos y esperar mas de 1.5 horas
    Dado que he comido 15 pepinos
    Cuando espero 2 horas
    Entonces mi estómago debería gruñir

  Escenario: comer 10 pepinos y esperar suficiente
    Dado que he comido 10 pepinos
    Cuando espero 2 horas
    Entonces mi estómago no debería gruñir

  Escenario: comer mas de 10 pepinos pero esperar muy poco
    Dado que he comido 20 pepinos
    Cuando espero 30 minutos
    Entonces mi estómago no debería gruñir

  Escenario: no comer nada pepinos, y esperar cierto tiempo
    Dado que he comido 0 pepinos
    Cuando espero 3 horas
    Entonces mi estómago no debería gruñir

  Escenario: saber cuántos pepinos he comido
    Dado que he comido 15 pepinos
    Entonces deberia haber comido 15 pepinos

  Escenario: predecir si gruñire tras comer mas de 10 pepinos y esperar suficiente
    Dado que quiero saber si gruñire tras comer 12 pepinos
    Y espero 2 horas
    Entonces deberia predecirse que el estomago gruñira

  Escenario: predecir si no gruñire si como poco y espero suficiente
    Dado que quiero saber si gruñire tras comer 8 pepinos
    Y espero 2 horas
    Entonces deberia predecirse que el estomago no gruñira

  Escenario: saber cuantos pepinos puedo comer antes de gruñir
    Dado que he comido 8 pepinos
    Cuando pregunto cuantos pepinos mas puedo comer antes de gruñir
    Entonces deberia decirme que puedo comer 2 pepinos mas

  Escenario: Acabo de comer el limite exacto
    Dado que he comido 10 pepinos
    Cuando pregunto cuantos pepinos mas puedo comer antes de gruñir
    Entonces deberia decirme que puedo comer 0 pepinos mas

  Escenario: supongamos que como 12 pepinos en la fecha: 2025-02-22 10:00
    Dado que he comido 12 pepinos
    Cuando espero 2 horas
    Entonces deberia registrar la fecha actual 2025-02-22 12:00


