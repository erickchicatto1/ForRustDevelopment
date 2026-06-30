// Programa básico en Rust para aprender funciones y conceptos básicos

// Función principal (siempre es el punto de entrada)
fn main() {
    println!("Hola, bienvenido a Rust 🚀");

    // Variables
    let nombre = "Eric";
    let edad = 25;

    saludar(nombre);

    let suma = sumar(5, 3);
    println!("La suma es: {}", suma);

    // Condicional
    if edad >= 18 {
        println!("Eres mayor de edad");
    } else {
        println!("Eres menor de edad");
    }

    // Bucle
    for i in 1..=5 {
        println!("Número: {}", i);
    }

    // Uso de función con retorno
    let resultado = es_par(10);
    println!("¿El número es par? {}", resultado);
}

// Función sin retorno
fn saludar(nombre: &str) {
    println!("Hola, {} 👋", nombre);
}

// Función con parámetros y retorno
fn sumar(a: i32, b: i32) -> i32 {
    a + b // en Rust no se usa 'return' si es la última línea
}

// Función que devuelve booleano
fn es_par(numero: i32) -> bool {
    numero % 2 == 0
}
