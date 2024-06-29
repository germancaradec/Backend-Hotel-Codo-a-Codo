function fechaTruncada(fechaParam) {
    // Crear una nueva fecha
    var diferencia = 1000 * 60 * 60 * 3 * 1;
    var fecha1 = new Date(fechaParam);
    var fecha = new Date(fecha1.getTime() + (diferencia)); // agregado de 3 horas para que sea de argentina

    // Obtener solo la parte de la fecha deseada
    const dia = String(fecha.getDate()).padStart(2, '0');
    const mes = String(fecha.getMonth() + 1).padStart(2, '0'); // Los meses en JavaScript van de 0 a 11
    const año = fecha.getFullYear();

    // Formatear la fecha DD/MM/YYYY
    const fechaTrunc = `${dia}/${mes}/${año}`;
    return fechaTrunc;
  }

  function fechaTipoDate(p_fecha){
    var diferencia = 1000 * 60 * 60 * 3 * 1;
    var fecha1 = new Date(p_fecha);
    var fecha = new Date(fecha1.getTime() + (diferencia));
    var year = fecha.getFullYear();
    var month = ('0' + (fecha.getMonth() + 1)).slice(-2); // Los meses empiezan desde 0
    var day = ('0' + fecha.getDate()).slice(-2);
    var fechaFormateada = year + '-' + month + '-' + day;
    return fechaFormateada;
}  