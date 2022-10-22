function validar (){
	var formulario = document.formulario;
	if (formulario.email.value == 0){
		alert('el campo email esta vacio');
		formulario.email.value = "";
		formulario.email.focus();
		return false;
	}
	if (formulario.password.value == 0){
		alert('el campo contraseña esta vacio');
		formulario.password.value = "";
		formulario.password.focus();
		return false;
	}
}

function validarRegistro(){
	var formRegis = document.formRegis;
	if (formRegis.dni.value == 0){
		alert('el campo DNI esta vacio');
		formulario.dni.value = "";
		formulario.dni.focus();
		return false;
	}
	if (formRegis.nombre.value == 0){
		alert('el campo nombre esta vacio');
		formRegis.nombre.value = "";
		formRegis.nombre.focus();
		return false;
	}
	if (formRegis.apellido.value == 0){
		alert('el campo apellido esta vacio');
		formRegis.apellido.value = "";
		formRegis.apellido.focus();
		return false;
	}
	if (formRegis.email.value == 0){
		alert('el campo email esta vacio');
		formRegis.email.value = "";
		formRegis.email.focus();
		return false;
	}
	if (formRegis.password.value == 0){
		alert('el campo contraseña esta vacio');
		formRegis.password.value = "";
		formRegis.password.focus();
		return false;
	}
	if (formRegis.fechnac.value == 0){
		alert('el campo fecha de nacimiento esta vacio');
		formRegis.fechnac.value = "";
		formRegis.fechnac.focus();
		return false;
	}
	if (formRegis.tel.value == 0){
		alert('el campo teléfono esta vacio');
		formRegis.tel.value = "";
		formRegis.tel.focus();
		return false;
	}
	if (formRegis.direccion.value == 0){
		alert('el campo dirección esta vacio');
		formRegis.direccion.value = "";
		formRegis.direccion.focus();
		return false;
	}
	if (formRegis.ciudad.value == 0){
		alert('el campo ciudad esta vacio');
		formRegis.ciudad.value = "";
		formRegis.ciudad.focus();
		return false;
	}
	
	if (formRegis.provincia.value == 0){
		alert('el campo provincia esta vacio');
		formRegis.provincia.value = "";
		formRegis.provincia.focus();
		return false;
	}
	
}
function validarSelect(){
	var indice = document.formRegis.select.selectedIndex 
	var valor = document.formRegis.select.options[indice].value
	if (valor == 'seleccionar'){
		alert('el campo seleccion esta vacio');
		formRegis.select.options[indice].value = "";
		formRegis.select.options[indice].focus();

	}

} 