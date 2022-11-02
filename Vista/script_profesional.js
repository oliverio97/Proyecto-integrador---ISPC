function onEnviar(){
    let form = document.getElementById("myform")
    pass1 = document.getElementById('pass1')
    pass2 = document.getElementById('pass2')
    
    if (pass1.value != pass2.value) { 
        alert("Las contraseñas no coinciden")
    }
    else (form.checkValidity())
    {
        alert("Los datos se enviaron correctamente")
    }


}