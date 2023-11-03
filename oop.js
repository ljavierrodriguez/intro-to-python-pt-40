// OOP (Object Oriented Programming) (Programacion Orientada a Objeto)
/*
1.- Clases y Objetos
2.- Abstraccion
3.- Encapsulamiento
4.- Herencia
5.- Polimorfismo
*/

class Persona {
    nombre = null;
    apellido = null;
    edad = null;

    constructor(nombre, apellido, edad){
        this.nombre = nombre;
        this.apellido = apellido;
        this.edad = edad;
    }

    comer(){
        return ("Comer")
    }
    caminar(){
        return ("Caminar")
    }
    correr(){
        return ("Correr")
    }
}

let p1 = new Persona("John", "Doe", "Unknown"); // creando una instancia de Persona
console.log(p1);
let p2 = new Persona("Jane", "Doe", "Unknown");
console.log(p2.nombre);
console.log(p2.comer())


class Libro {
    constructor(title, author){
        this.title = title;
        this.author = author;
    }

    mostrarInformacion(){
        return `Title: ${this.title}\nAuthor: ${this.author}`
    }
}

let libro1 = new Libro("Cuando Quiero Llorar no LLoro", "Gabriel Garcia Marquez");

console.log(libro1.mostrarInformacion())


class Estudiante extends Persona {
    grado = null;
    facultad = null;

    constructor(nombre, apellido, edad, grado, facultad){
        super(nombre, apellido, edad)
        this.grado = grado;
        this.facultad = facultad;
    }

    comer(){
        return "Comer de Estudiante"
    }

}

let est1 = new Estudiante("Tommy", "Doe", "18", "2do", "Medicina")
console.log(est1)
console.log(est1.comer())