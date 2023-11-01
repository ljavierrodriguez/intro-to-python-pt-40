// Tipo de Datos y Variables
/* 

String
Number
Boolean
Undefined

Object:
    Null
    Literal Object
    Array

function

*/

let nombre = "";
let apellido = '';
let direccion = `Lorem ipsum dolor sit amet consectetur adipisicing
 elit. Possimus minima fuga nam ${nombre} inventore ${apellido} dolor adipisci reiciendis
  praesentium dolorum obcaecati, veniam pariatur. Est, quisquam? 
  Libero autem animi temporibus porro enim quia!`; // string

let edad = 40;
let precio = 10.50;
let grados = -10;
let saldo = -1.5; // number

let active = true; // boolean 
let open = false; // boolean

let peso; // undefined
let users = null; // object 


let persona = {
    nombre: "",
    apellido: ""
}

persona.nombre = "John"
persona["apellido"] = "Doe"

let nombres = ["Hugo", "Paco", "Luis"];
nombres[1] = "Donald"

nombres.push("Mickey")

function nombreFuncion(){

}

const nombreFuncion2 = function(){
    
}