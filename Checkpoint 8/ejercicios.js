/*Ejercio 1: Cree un bucle for en JS que imprima cada nombre en esta lista. 
miLista = “velma”, “exploradora”, “jane”, “john”, “harry” */

const miLista = ['velma', 'exploradora', 'jane', 'john', 'harry'];

for (nombre in miLista) {
    console.log(miLista[nombre]);
}

/*Ejercicio 2: Cree un bucle while que recorra la misma lista y también imprima los nombres. 
Nota: Recuerda crear un contador para que el ciclo no sea infinito. */

let contador = 0

while (contador < miLista.length)  {
    console.log(miLista[contador]);
    contador ++;
}

/*Ejercicio 3: Cree una función de flecha que devuelva "Hola mundo".*/

const saludo = () => {
    return 'Hola mundo.'
};

console.log(saludo());