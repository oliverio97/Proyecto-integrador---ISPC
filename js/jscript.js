function validar (){
	let formulario = document.getElementById('formulario');
	
	if (formulario.email.value == 0){
		alert('el campo email esta vacio');
		formulario.email.value = "";
		formulario.email.focus();
		return false;
	}
	if (formulario.contrasena.value == 0){
		alert('el campo contraseña esta vacio');
		formulario.contrasena.value = "";
		formulario.contrasena.focus();
		return false;
	}
}