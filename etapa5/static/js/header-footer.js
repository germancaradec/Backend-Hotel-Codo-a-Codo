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

        //armamos bloque footer
        let footer2 =`
            <a href="#header"><img src="static/imagenes/logo-negro-furaveri.png" alt="Logo Hotel" class="logo-footer"></a>
            <section class="social">
                <a href="https://www.facebook.com/" target="_blank"><img src="static/imagenes/facebook.png" alt="Facebook"></a>
                <a href="https://www.instagram.com/" target="_blank"><img src="static/imagenes/instagram.png" alt="Instagram"></a>
                <a href="https://www.twitter.com" target="_blank"><img src="static/imagenes/twitter.png" alt="Twitter"></a>
                <a href="https://www.whatsapp.com/" target="_blank"><img src="static/imagenes/whatsapp.png" alt="Watsapp"></a>
            </section>
        `;
        document.getElementById("footer2").innerHTML = footer2




//armamos bloque menuAdmin
let menuAdmin =`
         <nav id="func-admin" class="funcAdminInactivo">
                <a href="listadoCotizaciones.html"> 
                    <button class="boton-header">LISTAR COTIZACIONES</button>
                </a>
                <a href="modificacionesCotizaciones.html"> 
                    <button class="boton-header">MODIFICAR COTIZACIÓN</button>
                </a>
                <a href="listadoEliminarCotizaciones.html"> 
                    <button class="boton-header">ELIMINAR COTIZACIÓN</button>
                </a>
            </nav>
            <nav id="func-admin" class="funcAdminInactivo">
                <a href="listadoConsultas.html"> 
                    <button class="boton-header">LISTAR CONSULTAS</button>
                </a>
                <a href="modificaciones.Consultas.html"> 
                    <button class="boton-header">MODIFICAR CONSULTAS</button>
                </a>
                <a href="listadoEliminarConsultas.html"> 
                    <button class="boton-header">ELIMINAR CONSULTAS</button>
                </a>
            </nav>
`;
document.getElementById("menuAdmin").innerHTML = menuAdmin

