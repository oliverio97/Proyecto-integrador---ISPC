




const formulario = document.getElementById("formulario"); // esta variable accede al formulario
const inputs = document.querySelectorAll("#formulario input") // esta variable accede a todos los inputs dentro de formulario, almacenándolos en una lista
const select = document.querySelector("#formulario select")
const expresiones = {
	usuario: /^[a-zA-Z0-9\_\-]{4,16}$/, // Letras, numeros, guion y guion_bajo
	nombre: /^[a-zA-ZÀ-ÿ\s]{1,40}$/, // Letras y espacios, pueden llevar acentos.
    apellido: /^[a-zA-ZÀ-ÿ\s]{1,40}$/, // Letras y espacios, pueden llevar acentos.
	contraseña: /^(?=.*(a-z))^(?=.*(A-Z))^(?=.*[0-9])^(?=.{8,})$/, // 6 a 12 caracteres, incluyendo por lo menos 1 número y una mayúscula.
	email: /^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$/,
	telefono: /^\d{7,14}$/ // 7 a 14 numeros.
}
// objeto con todos los inputs del formulario, estableciendolos por defecto en false, es decir que no me deja enviar
// el formulario hasta que los complete (si quisiera que un campo no fuera obligatorio habría que ponerlo por defecto en true)

const campos = {
    nombre: false,
    apellido: false,
    contraseña: false,    
    email: false,    
    genero: false,
    telefono: false
}

// función para ejecutarse al levantar la tecla o hacer click afuera del input. El parámetro x hace referencia
// al input, y con target.name se accede al "name" del input. Entonces para cada input (case) se establece una
// determinada validación. test() lo que hace es tomar como argumento lo ingresado en el input y comprobar si se cumple la validación, 
// en cuyo caso devuelve true. classlist lo que hace es agregar o remover una clase. 

const validarFormulario = (x) => {
    switch (x.target.name) {
        case "nombre":
            validarCampo(expresiones.nombre,x.target,"nombre")            
            break;
        case "apellido":
            validarCampo(expresiones.apellido,x.target,"apellido")    
            break;
        case "contraseña":
            validarCampo(expresiones.contraseña,x.target,"contraseña")
            validarContraseña2()    
            break;
        case "repetir contraseña":
            validarContraseña2()          
            break;        
        case "email":
            validarCampo(expresiones.email,x.target,"email")    
            break;        
        case "telefono":
            validarCampo(expresiones.telefono,x.target,"telefono")    
            break;
        case "genero":
            if ((document.querySelector("#grupo__genero .form-select").value)=="0"){
                document.getElementById("grupo__genero").classList.add("formulario__grupo-incorrecto");
                document.getElementById("grupo__genero").classList.remove("formulario__grupo-correcto");
                document.querySelector("#grupo__genero .formulario__input-error").classList.add('formulario__input-error-activo')
                document.querySelector("#grupo__genero i").classList.add('fa-check-circle');
                document.querySelector("#grupo__genero i").classList.remove('fa-times-circle')
            } else {document.getElementById("grupo__genero").classList.remove("formulario__grupo-incorrecto");
                    document.getElementById("grupo__genero").classList.add("formulario__grupo-correcto");
                    document.querySelector("#grupo__genero .formulario__input-error").classList.remove('formulario__input-error-activo');
                    document.querySelector("#grupo__genero i").classList.add('fa-check-circle');
                    document.querySelector("#grupo__genero i").classList.remove('fa-times-circle')}
            break

    }
    
}


const validarCampo = (expresion,input,campo) => {
    if (expresion.test(input.value)){
        document.getElementById(`grupo__${campo}`).classList.remove("formulario__grupo-incorrecto");
        document.getElementById(`grupo__${campo}`).classList.add("formulario__grupo-correcto");
        document.querySelector(`#grupo__${campo} i`).classList.add('fa-check-circle');
        document.querySelector(`#grupo__${campo} i`).classList.remove('fa-times-circle');
        document.querySelector(`#grupo__${campo} .formulario__input-error`).classList.remove('formulario__input-error-activo');
        campos[campo] = true;
        

    } else {
        document.getElementById(`grupo__${campo}`).classList.add("formulario__grupo-incorrecto");
        document.getElementById(`grupo__${campo}`).classList.remove("formulario__grupo-correcto");
        document.querySelector(`#grupo__${campo} i`).classList.add('fa-times-circle');
        document.querySelector(`#grupo__${campo} i`).classList.remove('fa-check-circle');
        document.querySelector(`#grupo__${campo} .formulario__input-error`).classList.add('formulario__input-error-activo');
        campos[campo] = false
    }
}

const validarContraseña2 = () => {
    if ((document.querySelector("#grupo__repetir_contraseña .form-control").value)==
        (document.querySelector("#grupo__contraseña .form-control").value)) {
            document.getElementById("grupo__repetir_contraseña").classList.remove("formulario__grupo-incorrecto");
            document.getElementById("grupo__repetir_contraseña").classList.add("formulario__grupo-correcto");
            document.querySelector("#grupo__repetir_contraseña i").classList.add('fa-check-circle');
            document.querySelector("#grupo__repetir_contraseña i").classList.remove('fa-times-circle');
            document.querySelector("#grupo__repetir_contraseña .formulario__input-error").classList.remove('formulario__input-error-activo');
            campos["contraseña"] = true;
    } else {
            document.getElementById("grupo__repetir_contraseña").classList.add("formulario__grupo-incorrecto");
            document.getElementById("grupo__repetir_contraseña").classList.remove("formulario__grupo-correcto");
            document.querySelector("#grupo__repetir_contraseña i").classList.add('fa-times-circle');
            document.querySelector("#grupo__repetir_contraseña i").classList.remove('fa-check-circle');
            document.querySelector("#grupo__repetir_contraseña .formulario__input-error").classList.add('formulario__input-error-activo');
            campos["contraseña"] = false;
        
    }
}




// Acá se accede a la variable select, que contiene al campo género del formulario.
select.addEventListener("keyup",validarFormulario);
select.addEventListener("blur",validarFormulario);

// Acá se accede a cada elemento de la variable inputs (o sea cada input del formulario) con forEach. 
// A continuación se definen dos funciones flecha sin nombre. La primera realiza a cada input un eventlistener que toma
// como parámetros "keyup", el evento que desencadena la función, y una función. La función se ejecuta al presionar una tecla el usuario en el input,
// eso indica keyup (levantar la tecla). La segunda funciona igual solo que se ejecuta con el evento "blur", que se activa al hacer click fuera del input
inputs.forEach((input) =>{
    input.addEventListener("keyup",validarFormulario);
    input.addEventListener("blur",validarFormulario);

});


// EventListener es un escuchador que indica al navegador que este atento a la 
// interaccion del usuario, en este caso la funcion se desencadena con el evento "submit", que se 
// ejecuta al hacer click en el boton enviar del formulario. 
// La funcion lo que hace es prevenir que se envien los datos del formulario, ya que no tenemos adonde enviarlos.

formulario.addEventListener("submit",function Enviar(evento){
    evento.preventDefault();
    if(campos.nombre && campos.apellido && campos.email && campos.telefono && campos.contraseña){
        formulario.reset();

    }
});