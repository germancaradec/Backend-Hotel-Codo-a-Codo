// armamos bloque header 
let header = `
<a href="index.html"><img src="static/imagenes/logo-blanco-furaveri.png" class="logo" alt="Logo Hotel Furaveri" ></a>
            
<label for="check-btn" class="check-btn">
    <svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" fill="currentColor" class="icon-menu" viewBox="0 0 16 16">
        <path fill-rule="evenodd" d="M2.5 12a.5.5 0 0 1 .5-.5h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1-.5-.5m0-4a.5.5 0 0 1 .5-.5h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1-.5-.5m0-4a.5.5 0 0 1 .5-.5h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1-.5-.5"/>
    </svg>
</label>
<input type="checkbox" id="check-btn">

<nav class="menu">
    <ul class="lista">
        <li class="li"><a class="item" href="index.html">HOME</a></li>
        <li class="li"><a class="item" href="habitaciones.html">HABITACIONES</a></li>
        <li class="li"><a class="item" href="gastronomia.html">GASTRONOMIA</a></li>
        <li class="li"><a class="item" href="contacto.html">CONTACTO</a></li>
    </ul>
</nav>
`; 
document.getElementById("header").innerHTML = header


//armamos bloque footer
let footer =`
<a href="#header"><img src="static/imagenes/logo-negro-furaveri.png" alt="Logo Hotel" class="logo-footer"></a>
<section class="social">
    <a href="https://www.facebook.com/" target="_blank"><img src="static/imagenes/facebook.png" alt="Facebook"></a>
    <a href="https://www.instagram.com/" target="_blank"><img src="static/imagenes/instagram.png" alt="Instagram"></a>
    <a href="https://www.twitter.com" target="_blank"><img src="static/imagenes/twitter.png" alt="Twitter"></a>
    <a href="https://www.whatsapp.com/" target="_blank"><img src="static/imagenes/whatsapp.png" alt="Watsapp"></a>
</section>
`;
document.getElementById("footer").innerHTML = footer


//validación del formulario de contacto
function validarFormulario() {
     //definimos variables de datos necesarias

    let nombre = document.getElementById("nom").value
    let apellido = document.getElementById("ape").value
    let correo = document.getElementById("correo").value
    let consulta = document.getElementById("consulta").value
    let telefono = document.getElementById("tel").value
    let check = document.getElementById("check")


    //realizamos validación de email con expresión regular
    function validarCorreo(correo) {
        const regex = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/
        return regex.test(correo)
    }

    //realizamos la validación de campos obligatorios + email con formato correcto
    if ( nombre === "" || apellido === "" || consulta === "" || validarCorreo(correo) === false ) {
        document.getElementById("solicitud").textContent = 
        `Verifique los datos ingresados`
    } else {
        document.getElementById("solicitud").textContent = 
        `Consulta enviada exitosamente. Le responderemos a su email dentro de las próximas 48hs. ¡Muchas gracias por contactarnos!`
    }

    //validamos la posibilidad de recibir información al telefono (cargando el número y tildando el checkbox, sumado a las condiciones anteriores)
    if ( nombre !== "" && apellido !== "" && consulta !== "" && validarCorreo(correo) !== false &&telefono !== "" && check.checked === true) {
        document.getElementById("solicitud-tel").textContent = 
        `También le enviaremos a su teléfono información de nuestras mejores promociones`
    }
    }

    function limpiarFormulario() {
        //limpiamos los inputs del formulario
    document.getElementById("nom").value = ""
    document.getElementById("ape").value = ""
    document.getElementById("correo").value = ""
    document.getElementById("consulta").value = ""
    document.getElementById("tel").value = ""
    check.checked = false
    document.getElementById("solicitud").textContent = ""
    document.getElementById("solicitud-tel").textContent = ""
    }
