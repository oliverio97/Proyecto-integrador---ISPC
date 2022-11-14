(function () {
  'use strict'

  // Fetch all the forms we want to apply custom Bootstrap validation styles to
  var forms = document.querySelectorAll('.needs-validation')
  

  // Loop over them and prevent submission
  Array.prototype.slice.call(forms)
    .forEach(function (form) {
      form.addEventListener('submit', function (event) {
        if (!form.checkValidity()) {
          event.preventDefault()
          event.stopPropagation()  
        }
        form.classList.add('was-validated')
		const formRegis = document.formRegis;
	
	
	
	
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

    if (formRegis.Dni.value == 0){
		alert('el campo DNI esta vacio');
		formulario.dni.value = "";
		formulario.dni.focus();
		return false;
	}

    if (formRegis.genero.value == ''){
		alert('el campo genero esta vacio');
		formRegis.genero.options[indice].focus();
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

    if (formRegis.provincia.value == 0){
		alert('el campo provincia esta vacio');
		formRegis.provincia.value = "";
		formRegis.provincia.focus();
		return false;
	}

    if (formRegis.ciudad.value == 0){
		alert('el campo ciudad esta vacio');
		formRegis.ciudad.value = "";
		formRegis.ciudad.focus();
		return false;
	}

    if (formRegis.calle.value == 0){
		alert('indica el nombre de tu calle');
		formRegis.calle.value = "";
		formRegis.calle.focus();
		return false;
	}
	
	if (formRegis.altura.value == 0){
		alert('indica la altura de tu calle');
		formRegis.altura.value = "";
		formRegis.altura.focus();
		return false;
	}

    if (formRegis.tel.value == 0){
		alert('el campo teléfono esta vacio');
		formRegis.tel.value = "";
		formRegis.tel.focus();
		return false;
	}

	if (formRegis.fechnac.value == 0){
		alert('el campo fecha de nacimiento esta vacio');
		formRegis.fechnac.value = "";
		formRegis.fechnac.focus();
		return false;
	}
	
	
      } , false)
	
	
    })
	
}

		
 ) ()

