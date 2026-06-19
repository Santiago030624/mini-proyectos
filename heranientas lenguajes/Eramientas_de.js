/* */ //me sirve para hacer comentarios de multiples lineas.
//me sirve para hacer comentarios de una sola linea.
// \n me sirve para hacer un salto de linea

// ? me sirve para hacer preguntas o indicar opciones en una condicion ternaria
ejemplo = true ? "es verdadero" : "es falso";
console.log(ejemplo);

// ! me sirve para negar una condicion o valor booleano 
ejemplo2 = !false; // true
console.log(ejemplo2);


// let me sirve para declarar variable
let nombre = "Juan";
if (true) {
  let nombre = "Pedro"; // Esta variable es diferente a la de arriba
  console.log(nombre); // Imprime "Pedro"
}
console.log(typeof nombre); // Me dice el tipo de dato que es la variable

let simbolos = Symbol("carro"); //Symbol me sirve 
console.log(simbolos)

let letras = letras.split(""); //.split me Sirve para dividir un texto en partes y convertirlo en un array.


// const me sirve para declarar constantes y el valor que se ingrese sera inmutable
const apellido = {nombre:  "SANTIAGO"};
console.log(apellido)

Math.floor(4.7); // redondea un numero hacia abajo.

let bocal = "a".repeat(10)//me sirve para repetir las veces que indiquemas lavariable en este caso se imprimira 10 veces la letra "a"

const unir_join = ["hola", "SHARO"]
console.log(unir_join.join(' ')); // me sirve para unir todos los elementos de un array en una sola cadena (string)
// dentro de los parentecis va el separador que quiero usar entre los elementos (puede ser un espacio, coma, guion, o nada).

let reversa = "pablo";
let reversa2 = reversa.reberse() // me sirve para imprimir un estrin o numero de atras para adelante.

let convierte_mayusculas = "Hola";
console.log(convierte_mayusculas.toUpperCase()); // .toUpperCase me sirve para convertir un estring a mayuscula

let convierte_minuscula = "HOLA";
console.log(convierte_minuscula.toLowerCase()) // .toLowerCase convierte un estring en minuscula.

let remplasar = "Hola ana te amo";
console.log(remplasar.replace("ana", "SHARO")); // me sirve para remplasar un valor especifico con otro valor en una cadena. Solo reemplaza la primera ocurrencia por defecto.

let remplasa_todo_lo_nesesacio = "SHARI maria CUENCA";
console.log(remplasa_todo_lo_nesesacio.replaceAll("maria", "DANITZA")); //Para reemplazar todas las ocurrencias.

let elimina_espacios_en_blanco = " SHARIT TE AMO ";
console.log(elimina_espacios_en_blanco.trim())// Elimina los espacios en blanco de ambos extremos de una cadena.

let devuelve_caracter = "hola";
console.log(devuelve_caracter.charAt(1)); // Devuelve el carácter en un índice especificado en una cadena.




            //ARAIS Y SUS PROPIEDADES

            
            

// metodos de array

//Math.max me sirve para devolver el numero mas grande de una serie de numeros o de un array usando el operador spread(...)
let lista_numeros = [3, 5, 1, 8, 2];
let maximo = Math.max(...lista_numeros);
console.log(maximo); // Imprime 8

const frutas = ["manzana", "banana", "cereza"];

frutas[2] = "naranja"; // modifica los elementos del array

frutas.push("manzana"); // añade un elemento al final del array

frutas.unshift("fresa") // añade un elemento al inicio 

let elimina_ultimoelemento =frutas.pop() // elimina un elemento del final del array y lo devuelve
console.log(elimina_ultimoelemento);

let elimina_primerelemento = frutas.shift() // elimina el primer elemento del array y lo devuelve 
console.log(elimina_primerelemento);

frutas.sort(); // ordena los elementos de un array.
console.log(frutas);

frutas.reverse(); //invierte el orden de los elementos en un array. 
console.log(frutas);

console.log(frutas);

let fruta1 = frutas.indexOf("banana"); // devuelve el indice del elemento buscado
console.log(fruta1);

let fruta2 = frutas.lastIndexOf("naranja") // devuelve el ultimo indice del elemento buscado
console.log(fruta2);

let fruta3 = frutas.includes("naranja"); // devuelve true si el elemento existe en el array, de lo contrario devuelve false
console.log(fruta3);
 
frutas.filter(fruta => fruta.length > 5); // crea un nuevo array con todos los elementos que cumplan la condicion 

frutas.forEach(fruta => console.log(fruta)); // ejecuta una funcion para cada elemento del array

for(const contar of frutas){ // recorre cada elemento del array o de una palbra o un input.
  console.log(contar);
}

let numeros = [4, 2, 5, 1, 3];

let mapa = numeros.map(num => num * 2); // crea un nuevo array con los resultados de la funcion aplicada a cada elemento del array original.
console.log(mapa);

let filtrar = numeros.filter(num => num > 2); // crea un nuevo array con todos los elementos que cumplan la condicion.  
console.log(filtrar);

console.log(reducir);
let reducir = numeros.reduce((acumulador, num) => acumulador + num, 0); // reduce el array a un unico valor aplicando una funcion a un acumulador y a cada elemento del array.
console.log(letra)

numeros.splice(1, 4); // elimina elementos del array desde el indice especificado y la cantidad de elementos a eliminar.

let recorer =  numeros.forEach //Me sirve para recorre todos los elementos de una funcion


const unico = new set([]); //new set me sirve para  agregar  elementos unicos en un arrais bacio donde puedo agregar elementos con el add
// set me sirve para indicar o agregar elementos unicos
unico.add("a") // add me sireve para agregar un nuebo balor dentro del set
return unico.size; //.size me sirve para imprimir cuántos elementos únicos hay dentro del Set.

const bocales1 = ['a','e','i','0','u','A','E','I','O', 'U'];
let sacarbocales = bocales1.slice(0, 5); // .slice me sirve para copiar una parte de un array en otro array nuevo sin modificar el array original.
console.log(sacarbocales);


