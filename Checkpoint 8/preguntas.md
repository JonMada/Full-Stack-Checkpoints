# 1. ¿Qué tipo de bucles hay en JS?

## 1.1. Bucle `for`

Un bucle `for` en JavaScript es una estructura de control que te permite repetir un bloque de código un número específico de veces. La sintaxis general de un bucle `for` es la siguiente:

```JavaScript
for (inicialización; condición; actualización) {
    //Cuerpo del bucle
}
```

**a. Inicialización**: se ejecuta una vez al principio de loop. Se utiliza para incializar el contador del bucle.

**b. Condición**: se evalúa antes de cada iteración del bucle. Si está condición es verdadera, el bloque de código del bucle se ejecuta; si es falsa, el bucle se detiene.

**c. Actualización**: se ejecuta al final de cada iteración del bucle. Se utiliza para actualizar el contador del bucle.

<p align="center">
  <img src="https://lenguajejs.com/fundamentos/estructuras-de-control/flujo-de-ejecucion/bucles-flujo-repeticion.png" alt="imagen bucle">
</p>


### Ejemplo aplicado de un bucle `for`
Imaginemos que tenemos una variable denominada `jugadores`que consta de una matriz en la que sus elementos están compuestos por los jugadores de nuestro equipo preferido. Nuestra misión, en este caso, sería conseguir que cada jugador fuese apareciendo de manera secuencial en la consola de nuestro terminal. **¿Cómo lo podríamos hacer?**

```JavaScript
const jugadores = ['Williams', 'Guruzeta', 'Sancet', 'Nico'];

for(let i = 0; i < jugadores.length; i++) {
    console.log(jugadores[i]);
} //Salida del terminal --> Williams, Guruzeta, Sancet, Nico
```
+ `let i = 0`: con esta parte del código estamos creando nuestra variable contador del bucle, que en este caso es 0, por lo que se iniciará a partir de esa cifra.
+ `i < jugadores.length`: con este condicional lo que queremos decir es que el loop se ejecute siempre y cuando la variable `i` sea menor a la longitud de nuestra matriz, en este caso es 4, ya que está conformada por 4 elementos. Por lo que si los seleccionamos a través de su indice, tal y como lo vamos a hacer, el index de nuestra matriz de 4 elementos es: 0,1,2,3; siempre vamos a querer que este sea menor a la longitud de nuestro array.
+ `i++`: en esta parte parte del bucle estamos diciendo que en cada iteración el valor de la variable contado `i` se incremente en 1. 
+ `console.log(jugadores[i])`: en esta parte del bloque de código estamos aprovechando el método `array[index]` para en cada iteración imprimir un elemento (jugador) de la lista. Es decir, en la primera iteración, nuesta `i = 0` tal y como hemos establecido en bucle, por lo que estamos diciendo que se imprima el primer elemento de nuestra matriz contenida en la variable `jugadores`. (`jugadores[0] = 'Williams'`)
+ La impresión se seguirá en loop hasta que la condición anteriormente mencioanda (`i < jugadores.length`) no se cumpla, momento en el cual se interrumpirá el bucle.  
## 1.2. Bucle `for...in`
El bucle `for...in` en JavaScript se utiliza para iterar sobre las propiedades enumerables de un objeto. No se recomienda su aplicación en matrices debido a algunas limitaciones y posibles problemas. En su lugar, es preferible utilizar un bucle `for` estándar. *Algunos de los problemas de su uso en matrices son los siguientes*: 
**<p>Iteración sobre todas las propiedades enumerables del objeto:** El bucle `for...in` itera sobre todas las propiedades enumerables de un objeto, incluyendo las propiedades que pueda tener la matriz, como length y cualquier otra propiedad que se haya agregado manualmente. </p>
**<p>Orden de las propiedades:** El orden en que se iteran las propiedades de un objeto con `for...in` no está garantizado según la especificación de JavaScript. Esto significa que los elementos de la matriz pueden no iterarse en el orden esperado, especialmente si la matriz tiene propiedades adicionales o si ha sido modificada de alguna manera.</p>
**<p>Propiedades no numéricas:** Si la matriz contiene propiedades no numéricas (por ejemplo, si se ha agregado una `string`), estas también se iterarán con `for...in`, lo que puede no ser deseado en el contexto de iterar sobre los elementos de la matriz.</p>

### Ejemplo aplicado de un bucle `for...in`
Imaginemos que tenemos un objeto denominada `persona` y queremos que en la consola se nos impriman los valores de cada clave-valor que compone nuestro objeto. Un bucle `for...in` lograría resolver ese propósito.

```JavaScript
const persona = {
  nombre: 'Jon',
  edad: 30,
  ciudad: 'Sopela'
};

for (let propiedad in persona) {
  console.log(`${propiedad} : ${persona[propiedad]}`);
}
/*
Salida --> 
nombre: Jon
edad: 30
ciudad: Sopela
*/
```

En el código anterior podemos observar dos bloques. Por un lado, nuestro objeto persona, con sus key-values; y, por otro lado, nuestro `for...in` loop que desgranaremos a continuación:
+ Se define un objeto llamado persona que contiene tres propiedades: nombre, edad y ciudad, cada una con su respectivo valor.


+ Se inicia un bucle `for...in` con la declaración `for (let propiedad in persona)`. Esto significa que se recorrerán todas las propiedades enumerables del objeto persona, y en cada iteración, la variable propiedad tomará el nombre de cada propiedad.
+ `console.log(${propiedad} : ${persona[propiedad]});`: esta línea imprime en la consola el nombre de la propiedad actual (propiedad) y luego el valor correspondiente a esa propiedad en el objeto persona (`persona[propiedad]`). Esto se hace utilizando la interpolación de cadenas `${}`, donde `${propiedad}` representa el nombre de la propiedad y `${persona[propiedad]}` representa el valor de esa propiedad en el objeto persona.
## 1.3. Función `forEach()`
`forEach()` es una función de  JavaScript que se utiliza para iterar sobre elementos de un array y realizar una acción en cada uno de ellos. La función `forEach()` recorre cada elemento del array y se ejecuta lo que se determine sobre él. **La sintaxis general es la siguiente:** 

```JavaScript
array.forEach(function(elemento) {
  // Acciones a realizar en cada elemento
});
```
+ `function(elemento)`: la función anónima toma como parámetro un elemento, el cual representa cada elemento de la array sobre la que se está ejecutando la función.
  
### Ejemplo aplicado

```JavaScript
const numeros = [1,2,3,4,5];

numeros.forEach(function(numero){
    console.log(numero * 2);
});

// Salida --> 2,4,6,8,10
```
En este ejemplo contamos de inicio con una matriz que se encuentra dentro de una variable denominada `numeros`. A esa matriz le estamos aplicando la función `forEach()` a través de la cual cogemos cada elemento de la misma, en este caso representado por el parámetro `numero`, y de manera secuencial, uno por uno, va a multiplicarlos por 2, tal y como se observar en el `console.log(numero * 2)`.

## 1.4. `While` loop.

Un `while` loop en JavaScript es una estructura de control que se utiliza para ejecutar repetidamente un bloque de código mientras se cumpla una condición específica. **La sintaxis general de un bucle `while` es la siguiente**:
```JavaScript
while (condición) {
  // Bloque de código a ejecutar mientras la condición sea verdadera
}
```
+ `condición`: representa una expresión booleana que se evalúa en cada iteración del bucle. Si la condición es verdadera, el bloque de código dentro del bucle se ejecutará. Si la condición es falsa, el bucle se detendrá.
  
<p align="center">
  <img src="https://www.javascripttutorial.net/wp-content/uploads/2022/01/javascript-while.svg" alt="imagen.whileLoop">
</p>

### Ejemplo aplicado
```JavaScript
let contador = 0;

while (contador < 5) {
    console.log(`El contador es: ${contador}`);
    contador ++;
}
//Salida --> El contador es: 0, El contador es: 1,...,El contador es: 4
```

+ `let contador = 0;`: se inicializa una variable llamada contador con el valor 0. Esta variable se utilizará para llevar el seguimiento del progreso del bucle.
+ `while (contador < 5) { ... }`: se inicia un bucle `while` que continuará ejecutándose mientras el valor de `contador` sea menor que 5. Esto significa que el bucle se ejecutará hasta que contador alcance el valor de 5.
+ Dentro del bucle:
  + `console.log(El contador es: ${contador});`: se utiliza `console.log()` para imprimir en la consola el mensaje "El contador es: " seguido del valor actual de contador. Se utiliza la interpolación de cadenas `${}` para insertar el valor de la variable `contador` en la cadena de texto.
  + `contador ++;`: se incrementa el valor de contador en uno en cada iteración del bucle. Esto es importante para evitar un bucle infinito y para que en algún momento la condición `contador < 5` se vuelva falsa y el bucle termine.

## 1.5. `do...while` loop.
Es similar al bucle `while`, pero en este caso el bloque de código se ejecuta al menos una vez, antes de verificar la condición. Es útil  cuando necesitas ejecutar un bloque de código al menos una vez, independientemente de si la condición es verdadera desde el principio. Un ejemplo común es la validación de entrada del usuario, donde quieres asegurarte de que el usuario ingrese datos válidos antes de continuar. **La sintaxis básica es la siguiente:**

```JavaScript
do {
    //código a ejecutar al menos una vez
} while (condición);
```

### Ejemplo aplicado
Retomando el ejemplo anterior del contador, imaginemos que queremos crear un contador que imprima los número del 1 al 5. Para ello, utilizaremos la siguiente sintaxis:

```JavaScript
let contador = 1;

do {
    console.log(`El contador es: ${contador}`.)
    contador ++;
} while (contador < 6);

/*Salida -->
El contador es 1, El contador es 2,...El contador es 5*/
```

En estas líneas de código, en primer lugar estamos creando la variable contador, que es igual a 1. Posteriormente, mediante el `do` estamos imprimiendo el contador y incrementando en 1 el valor de esa variable contador; para después comprobar que la condición `contador` es menor que 6. A diferencia que en el `while`, aún no cumpliéndose la condición, imaginemos que el contador inicial hubiese sido igual a 6, este se habría impreso una vez, ya que el programa se ejecutaría antes de llegar a la condición, momento en el que se hubiese paralizado el bucle. 

# 2. ¿Cuáles son las diferencias entre const, let y var?

Las diferencias principales entre `const`, `let` y `var` en JavaScript radican en cómo manejan el alcance y la mutabilidad de las variables.

## 2.1. `Var`

+ Tiene un alcance de función. Esto significa que la variable declarada con var estará disponible dentro de la función en la que se declaró, incluso si es declarada dentro de un bloque {}.
+ Se puede redeclarar y reasignar.
+ No respeta el bloque {} en cuanto al alcance. Es decir, una variable declarada con var dentro de un bloque estará disponible fuera de ese bloque.

```JavaScript
var x = 10;

if (x > 0) {
    var y = 20;
    console.log(x); //Salida --> 10
}

console.log(y); //Salida --> 20
```

## 2.2. `let`
+ Tiene un alcance de bloque. Esto significa que la variable declarada con let estará disponible solo dentro del bloque en el que se declaró.
+ No se puede redeclarar dentro del mismo ámbito, pero sí se puede reasignar.
+ No está disponible para su uso antes de la declaración.

```JavaScript
let x = 10;

if (x > 0) {
    let y = 20;
    console.log(x); //Salida --> 10
}

console.log(y); //Salida --> Undefined
```

## 2.3. `const`
+ Al igual que let, tiene un alcance de bloque.
+ No se puede reasignar ni redeclarar. Sin embargo, cabe matizar que esto no impide la modificación de los tipos mutables, es decir, si una variable constante contiene un objeto o un arrray, los valores intenos de ambas áun pueden ser modificados. 
+ No está disponible para su uso antes de la declaración.
+ Es útil para declarar valores constantes que no cambiarán durante la ejecución del programa.

```JavaScript
const x = 10;
x = 20; // Error: Assignment to constant variable
```

# 3. ¿Qué es una función de flecha?
Las funciones de felcha tiene una sintaxis más corta y más intuitiva en comparación con las funciones tradicionales. Las diferencias clave más reseñables son:

## 3.1. Sintaxis más concisa.
La sintaxis de las funciones de flecha es más corta y concisa que la de las funciones regulares, además de no requerir de la palabre clave `function`.

```JavaScript
// Función tradicional
function suma(a, b) {
  return a + b;
}

// Función de flecha equivalente
const suma = (a, b) => a + b;
```

## 3.2.  Palabra clave `this`
En las funciones de flecha  el valor de `this`se hereda del contexto circundante donde se definió la función, mientras que en las funciones tradicionales, `this` puede cambiar dependiendo de como se llama a la función. Es decir, utilizan el this del contexto léxico en el que están definidas, esto significa que `this` en una función de flecha se refiere al `this` del ámbito que la contiene. Como ejemplo, imaginemos que tenemos un objeto `contador` que tiene dos métodos, uno incrementa el contador en una unidad y el otro muestra el contador.

```JavaScript 
  const contador = {
    valor: 0,
    incrementador () {
        this.valor ++;
    },
    mostrarContador () {
        const retorno = () => {
            console.log(`El contador es: ${this.valor}`);
        };
        retorno();
    },
  };

    contador.incrementador();
    contador.mostrarContador(); //Salida -->> El contador es: 1
```
En este caso el `this` dentro de la función de retorno se hereda del contexto de la función `mostrarContador`, que pertenece al objeto `contador`. Por lo tanto, `this.valor` se referirá a la propiedad `valor`del objeto `contador`.

# 4. ¿Qué es la deconstrucción de variables?
La deconstrucción de variables es una característica de JavaScript que permite intercambiar los valores de dos variables de manera concisa y elegante. 

<p align="center">
  <img src="https://i.ytimg.com/vi/7OFwvmpxT2U/maxresdefault.jpg" alt="imagen desestructuración de variables">
</p>

## Ejemplo básico:
En primer lugar, definimos nuestras variables.
```JavaScript
let numeroUno = 10;
let numeroDos = 20;
```
Una vez definidas nuestras variables, podemos utilizar la sintaxis de deconstrucción, la cual se hace asignando las variables en el lado izquierdo de la asignación con los valores que se quieran intercambiar, separados por comas y entre `[ ]`, para luego asignar las variables originales en el lado derecho, con la  misma sintaxis. 

```Javascript
[numeroUno, NumeroDos] = [numeroDos, numeroUno];

console.log(numeroUno); //salida --> 20
console.log(numeroDos); //salida --> 10
``` 

En nuestro ejemplo, estamos intercambiando los valores de las variables `numeroUno` y `numeroDos`.

## Ejemplo aplicado a matrices:
Asimismo, la deconstrucción aplicada a matrices en JavaScript permite extraer los valores del array y asignarlos a variables de manera indivual de forma compacta y sumamente legible.

```JavaScript
const matriz = [1,2,3,4,5];
```

Partiendo de nuestra variable `matriz` se utiliza la sintaxis de corchetes `[ ]` para especificar las variables a las que deseas asignar los valores.

```JavaScript
const [a,b,c,d,e] = matriz
```

Esto asginará el primer valor del array (1) a la variable a, el segundo valor (2) a la variable b, y así sucesivamente hasta terminar la asignación.

```JavaScript
console.log(a); //salida --> 1
console.log(b); //salida --> 2
console.log(c); //salida --> 3
console.log(d); //salida --> 4
console.log(e); //salida --> 5
```

## Ejemplo aplicado a objetos:
La deconstrucción también es útil en JavaScript para poder pasar objetos como argumentos de una función. Los pasos a seguir son los siguientes:

#### 1º Definimos la función:

```JavaScript
const mostrarInfo = ({nombre, edad, ciudad}) => {
    console.log(`Nombre: ${nombre}, Edad: ${edad}, Ciudad: ${ciudad}`);
}
```

Las llaves `{ }` en el argumento de una función se utilizan para indicar la deconstrución de un objeto. Cuando pasamos un objeto como argumento de una función y lo envolvemos entre llaves en la lista de argumentos, estamos indicando que deseamos extraer las propiedades específicas de ese objeto.

#### 2º Construimos nuestro objeto:
```JavaScript
const persona = {
    nombre: 'Jon',
    edad: 30,
    ciudad: 'Sopela'
};
```
Al llamar a la función le pasamos el objeto que acabamos de crear `persona` como argumento. JavaScript extraerá automáticamente las propiedad `nombre`, `edad` y `ciudad` del objeto.

#### 3º Llamamos a nuestra función:
```JavaScript
mostrarInfo(persona); //salida --> Nombre: Jon, Edad: 30, Ciudad: Sopela
```

# 5. ¿Qué hace el operador de extensión en JS?

<p align="center">
  <img src="https://miro.medium.com/v2/resize:fit:1085/1*KtIm1M2zG4kDZTl8Qsep7g.jpeg" alt="spread operator">
</p>
El operador de extensión, comúnmente conocido como 'spread operator', es una característica de JavaScript que permite expandir una expresión iterable, como lo son las matrices o los objetos, en lugares donde se esperan múltiples argumentos o elementos. A continuación, se mostrarán diferentes modos de aplicación de este operador.

## 5.1. Combinación de matrices

El spread operator `...` nos permite combinar matrices de manera rápida y clara.

```JavaScript
const arr1 = [1,2,3];
const arr2 = [4,5,6];

const cojuntoMatrices = [...arr1, ...arr2];

console.log(conjuntoMatrices); //salida --> [1,2,3,4,5,6]
```

## 5.2. Combinación de objetos
De igual manera, el operador de extensión permite combinar objetos, de manera similar al caso de las matrices.

```JavaScript
const objeto1 = {a:1, b: 2};
const objeto2 = {c:3, d:4};

const objetosUnidos = {...objeto1,...objeto2};

console.log(objetosUnidos); //salida --> {a:1, b:2, c:3, d: 4}
```

## 5.3. Para la clonación de matrices u objetos
Aplicado a una matriz se vería de esta forma:
```JavaScript
const matrizOriginal = [1,2,3,4,5];
const matrizClonada = [...matrizOriginal];

console.log(matrizClonada); //salida --> [1,2,3,4,5]
console.log(matrizOriginal); //salida --> [1,2,3,4,5]
```

Aplicado a un objeto se vería de esta otra forma:

```JavaScript
const objeto = {a: 1, b: 2};
const objetoClonado = {...objeto};

console.log(objetoClonado); //salida --> {a: 1, b: 2}
console.log(objeto); //salida --> {a: 1, b: 2}
```

## 5.4. Para pasar argumentos a funciones 

```JavaScript
const suma = (a, b, c) => {
  return a + b + c;
}

const matriz = [1, 2, 3];


// Usamos el 'spread operator' para pasar los elementos de la matriz como argumentos a la función suma

const resultado = suma(...matriz);

console.log(resultado); //salida --> 6
```
En este ejemplo, `suma(...matriz)` expande los elementos de la matriz `[1, 2, 3]` como argumentos individuales para la función `suma()`. Por lo tanto, la función `suma()` recibirá 1, 2, y 3 como sus tres argumentos `(a,b,c)`, y nos devolverá la suma de estos números, que es 6.

## 5.5. Spread operator aplicado a la deconstrucción de objeto
De igual manera `...` puede ser aplicado a objetos de manera que nos permita extraer algunas propiedades de un objeto y luego recopilar el resto de propiedades, de la cuales no se hace mención expresa, en otro objeto.

```JavaScript
const persona = {
    nombre: 'Jon',
    edad: 30,
    ciudad: 'Sopela',
    ocupación: 'Estudiante',
};
```

Imaginemos que del objeto persona queremos extraer las propiedades nombre y edad, y el resto recopilarlar en un objeto que denominaremos `detalles`. Para tal fin utilizaremos la siguiente sintaxis:

```JavaScript
const {nombre, edad, ...detalles} = persona;

console.log(nombre); //salida --> Jon
console.log(edad); //salida --> 30
console.log (detalles); //salida --> {ciudad:'Sopela', ocupación: 'Estudiante'}
```
# 6. ¿Qué es la programación orientada a objetos?
La programación orientada a objetos, también conocida como OOP por sus siglás en inglés, es un modelo de programación que se basa en la creación de objetos que pueden contener tanto datos (propiedades) como comportamientos (métodos), a partir de las denominadas clases.

<p align = center>
    <img src = 'https://miro.medium.com/v2/resize:fit:828/format:webp/1*zNUWr9Z_P-RF_sAaDAab0g.png'>

## 6.1. Clases
+ Una clase es como un plano o una plantilla a partir de la cual podemos crear objetos. En ella se definen las propiedades y comportamientos que los objetos de esa clase tendrán.
+ En JavaScript, una clase se dine utilizan la palabra clave `class`, seguida del nombre de la clase y su contenido en llaves ({ }).
+ En una clase, las propiedades se definen utilizando variables dentro del cuerpo de clase.
+ En cuanto a los métodos, estos se definen utilizando funciones dentro del cuerpo de la misma.

**Ejemplo**
Imaginemos que estamos creando una clase que denominaremos `Persona` en la que definiremos la propiedades que queremos introducir e implementaremos una pequeña función dentro de la misma (método) en la que se imprima el nombre y la edad de la misma. A continuación se mostrará la sintaxis necesaria.

```JavaScript
class Persona {
    constructor (nombre, edad) {
        this.nombre = nombre;
        this.edad = edad;
    }

    saludar () {
        console.log(`Mi nombre es ${this.nombre} y tengo ${this.edad} años.`);
    }
}
```

`Constructor` es un método especial dentro de una clase que es llamado de manera automáica cuando creamos una instancia de clase (objeto). En este caso, el constructor toma dos parámetros, nombre y edad, y los asigna a las propiedades nombre y edad del objeto creado.

## 6.2. Objetos
+ Un objeto es una isntancia de una clase. Se crea a partir de la clase utilizando la palabra clave `new`.
+ Los objetos tienen propiedades asociadas con ese objeto y son accesible mediante la notación `objeto.propiedad`.
+ Los objetos pueden tener métodos que representa el comportamiento asociado con ese objeto. Estos métodos se puede llamar utilizando la notación `objeto.metodo()`.

**Ejemplo**
Retomando la clase anterior `Persona` vamos a crear una instancia de clase, también llamado objeto, a partir de ese molde a la que le denominaremos `jon`.

```JavaScript
const jon = new Persona ('Jon', 30);
```

Una vez creada esta instancia de clase, podemos acceder a las propiedades y los métodos mediante las notaciones anteriormente mencionadas.

```JavaScript
console.log(jon.nombre); //salida --> Jon
console.log(jon.edad); //salida --> 30

console.log(jon.saludar()); //salida --> Mi nombre es Jon y tengo 30 años. 
```

## 6.3. Métodos
Dentro de los métodos de una clase podemos encontrar de dos tipos, los **métodos de instancia** y los **métodos estáticos**. Los métodos de instancia sse refieren a los métodos específicos de una clase. Estos métodos son funciones que pueden ser llamadas en una instancia particular de una clase y operan con los datos espcíficos de esa instancia. Un ejemplo claro de esta tipología sería el método `saludar()` que hemos utilizado en el ejemplo anterior.
Por otro lado, en lo que respecta a los métodos estáticos, son aquellos que están asociados con la clase en sí misma en lugar de estar asociados con instancias individuales de la clase. Estos métodos son funciones a las que se pueden llamar directamente en clase, sin la necesidad de crear una instancia de la misma. La palabra clave para crearlos es `static.

**Ejemplo**
```JavaScript
class Calculadora {
    static sumar (a,b) {
        return a + b;
    }
}

console.log(Calculadora.sumar(5,3)); //salida --> 8
```
Como vemos en este ejemplo podemos llamar al método `sumar()` directamente desde la clase `Calculadora` sin la necesidad de crear ninguna instancia de clase. 

# 7. ¿Qué es una promesa en JS?
<p align = center>
    <img src = 'https://www.alexlintu.com/content/images/2021/04/Group-74.png'>

Las promesas en JavaScript son objetos que representan el resultado eventual de una operación asíncrona. Una promesa puede estar en uno de los siguientes estados:
+ *Pendiente*: es el estado incial, la promesa está esperando que la operación asíncrona se complete.
+ *Cumplido* (resolve): la operación asíncrona se completó con éxito.
+ *Rechazada* (reject): la operación asíncrona falló.

**Pero...¿Qué es una operación asíncrona?**
Hace referencia a una tarea que no se ejecuta de manera secuencial con el resto del código. En lugar de esperar a que una tarea se complete antes de continuar con el siguiente paso, el programa puede seguir ejecutando otras instrucciones mientras espera que la operación asíncrona termine. 

## 7.1. Sintaxis básica

La sintaxis básica de una promesa en JavaScript consta de tres partes principales: la creación de la promesa, el manejo de su estado y la ejecución de acciones en función de su resultado.

**Creación de la promesa:**
Para crear una promesa, utilizamos la palabra clave `new` seguida de la clase `Promise`. Dentro del constructor de Promise, pasamos una función con dos parámetros: `resolve` y `reject`. resolve se llama cuando la operación prometida se completa exitosamente, mientras que reject se llama cuando la operación falla.

```JavaScript
const miPromesa = new Promise((resolve, reject) => {
  // Aquí va la operación asincrónica
});
```

**Manejo de la promesa:**
Después de crear la promesa, podemos encadenar métodos then() y catch() para manejar el resultado de la promesa. `then()` se ejecuta cuando la promesa se resuelve correctamente, mientras que `catch()` se ejecuta cuando la promesa es rechazada (falla).

```JavaScript
miPromesa
  .then(resultado => {
    // Manejar el resultado exitoso
  })
  .catch(error => {
    // Manejar el error
  });
```

## 7.2. Ejemplo aplicado
Imaginemos que prometemos a un amigo que le ayudaremos a mudarse este fin de semana. Tu amigo no sabe si podrás ayudarle o no hasta que llegue el fin de semana. Por lo que la promesa puede pasar por estos tres estados:

+ Pendiente: antes de llegar el fin de semana, tu promesa esta pendiente. Nuestro amigo no sabe si le podremos ayudar o no.
+ Cumplida: cuando llega el fin de semana vas a ayudarle, nuestra promesa se cumple.
+ Rechazada: surge algun evento inesperado y no podemos ir a ayudarle. La promesa, por así decirlo, se 'rechaza'.

```JavaScript
//Definimos la promesa de ayudar
let nuestraPromesa = new Promise ((resolve, reject) => {
    //Simulamos si pudimos ayudar o no
    let pudimosAyudar = true;

    //Comprobamos si te ayudamos
    if (pudimosAyudar) { //esto es igual a si pudimosAyudar es igual a true
        resolve('Pudimos ayudarte');
    } else {
        reject('No pudimos ayudarte');
    }
});

//Manejamos nuestra promesa
nuestraPromesa.then((mensaje) => {
    console.log(mensaje);
}).catch ((error) =>{
    console.error(error);
});
``` 

+ Si la promesa se resuelve correctamente, como es nuestro caso, ya que `puedimosAyudar = true`, la función de devolución de la llamada dentro de `then()` se ejecutará y `mensaje`contendrá el valor pasado al método `resolve`. En este caso la salida de nuestro terminal sería: `Pudimos ayudarte`.

+ Imaginemos hipotéticamente que nuestra promesa fuese rechazada, la función de devolución de llamada dentro de `catch()` se ejecutará y `error` contedrá el valor que hayamos pasado a `reject()`.
+ Por aclarar, el `console.error()`es un método similar al clásico `console.log()`, pero en este caso se utiliza para imprimir mensajes de error. Estos mensajes suelen ser destacados visualmente en la consola. 

# 8. ¿Qué hacen async y await por nosotros?
Son características de JavaScrip que se utilizan para trabajar con funciones asincrónicas de manera más limpia y legible.

## 8.1. `async` function: 
+ Una función asincrónica se declara usando la palabra clave `async`. 
+ Las funciones asincrónicas pueden contener expresiones `await`, que pausan la ejecución de la función hasta que la promesa sea resuelta.
+ Las funciones asincrónicas siempre devuelven una promesa. Si la función devuelve un valor, la promesa será resuelta con ese valor. Si la función arroja una excepción (rejected), la promesa será rechazada con el valor de excepción.

## 8.2. `await`:

+ La palabra `await` sólo puede ser utilziada dentro de una función `async`. 
+ `await` pausa la ejecución de la función asincrónica hasta que la promesa proporcionada sea resuelta o rechazada.
+ En definitva, el uso combinado de ambos recursos nos permite controlar el flujo de ejecución de manera más clara y legible, asegurando que las acciones se realicen de manera secuencial, en lugar de ejecutarse en paralelo. 

<p align = center>
    <img src="https://i1.wp.com/blog.codeanalogies.com/wp-content/uploads/2019/12/AsyncAwaitDiagram2.jpg?fit=730%2C419&ssl=1">
</p>

## 8.3. Ejemplo aplicado
Imaginemos que tenemos una web en la que contamos con un acceso de usuario y un programa para la actualización de sus datos. En nuestro desarrollo, querríamos que en primer lugar se ejecutase el acceso a usuario, independientemente de lo que tardara, antes de que se actualizasen sus datos, ya que en caso contrario, digamos que en un ejecución paralela de ambas, esto nos podría llevar a errores. Para controlar ese flujo procederíamos de la siguiente manera:

```JavaScript
const login = () => {
    return new Promise ((resolve, reject) => {
        setTimeout(() =>{
            resolve('Usuario logenadose...');
        },4000);
    });
}

const actualizarCuenta = () => {
    return new Promise ((resolve, reject) => {
        setTimeout(() =>{
            resolve('Datos del usuario actualizándose...');
        },2000);
    });
}

async function actividadesAcceso () {
    const returnedLogin = await login();
    console.log(returnedLogin);

    const returnedActualizarCuenta = await actualizarCuenta ();
    console.log(returnedActualizarCuenta);
}

```

**Definición de las funciones `login()` y `actualizarCuenta()`:**
+ `login()`: Esta función devuelve una promesa que se resuelve después de un retraso de 4 segundos. Dentro de la promesa, se resuelve con el mensaje "Usuario logueándose...".
+ `actualizarCuenta()`: Similar a login(), esta función devuelve una promesa que se resuelve después de un retraso de 2 segundos. Dentro de la promesa, se resuelve con el mensaje "Datos del usuario actualizándose...".

**Función `actividadesAcceso()`:**
+ Esta función es una función asíncrona.Esto significa que puede contener operaciones asíncronas y puede usar la palabra clave await para esperar a que las promesas se resuelvan.

**Uso de `await` para esperar a que las promesas se resuelvan:**
+ `const returnedLogin = await login();`: Aquí, estamos esperando a que la función login() se resuelva. Una vez que se resuelve, el resultado se almacena en returnedLogin. Durante este tiempo, el hilo de ejecución se bloquea y no pasa a la siguiente línea hasta que la promesa de login() se resuelve.
+ `console.log(returnedLogin);`: Luego, imprimimos el mensaje resuelto de la promesa de login().
+ `const returnedActualizarCuenta = await actualizarCuenta();`: Después, esperamos a que la función actualizarCuenta() se resuelva de manera similar. El resultado se almacena en returnedActualizarCuenta.
+ `console.log(returnedActualizarCuenta);`: Finalmente, imprimimos el mensaje resuelto de la promesa de actualizarCuenta().


