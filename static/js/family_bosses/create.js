const $form = document.getElementById('famile_boss') 
sendForm($form, 'POST',
    client =>  {
        show_alert(true, `${client.first_name} ${client.last_name} registrado con exito`)
    })