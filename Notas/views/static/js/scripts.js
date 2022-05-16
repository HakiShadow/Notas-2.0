function checkkey(e)
{
    if(e.keyCode == 13) // 13 es el código de tecla del enter
        document.getElementById("formID").submit(); // envío el formulario
    return true; // Devuelvo true en caso de no ser el enter
}