/*Cree una función JS que acepte 4 argumentos. Suma los dos primeros argumentos, luego los dos segundos 
y multiplícalos. Si el número creado es mayor que 50, la consola registra "¡El número es mayor que 50!". 
Si es más pequeño, la consola registra "¡El número es menor que 50!*/

const operador = function (a,b,c,d) {
    let sumaUno = a + b;
    let sumaDos = c + d;
    let multiplicación = sumaUno * sumaDos;
    
    if (multiplicación > 50) {
        console.log('El número es mayor que 50');
    } else if (multiplicación === 50) {
        console.log('El número es igual que 50');
    } else {
        console.log('El número es menor que 50')
    }
};

operador(10,15,1,1); //Salida --> El número es igual que 50