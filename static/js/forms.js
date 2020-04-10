/**
 * Realiza una peticion con la url, payload y metodo especificado.
 * Retorn una promesa con la respuesta del servidor
 * 
 * @param {json} payload 
 * @param {string} url 
 * @param {string} method 
 * 
 * @returns {Promise}
 */
function sendData(payload, url, method) {
    return new Promise( (resolve, reject) => {
        toggleLoading()
        const headers = {
            "X-CSRFToken": getCookie('csrftoken'),
            'Content-Type': 'application/json',
            "X-Requested-With": "XMLHttpRequest",
        }
        opts = {method,headers}
        if (method != 'GET') {
            opts['body'] = JSON.stringify(payload)
        }
        fetch(url, opts)
        .then( response => {
            okey_fetch = response.ok
            status_fetch = response.status
            return response.json()
        })
        .then( data => {
            toggleLoading()    
            if (okey_fetch) {
                resolve(data)
            } else {
                show_alert(okey_fetch, JSON.stringify(data))
                reject(data)
            }
        })
        .catch( e => {
            toggleLoading()    
            console.error(e)
            if (status_fetch<500) {
                show_alert(false, 'Verifique los datos ingresados')
            } else {
                show_alert(false, 'Ups! Esto es vergonzoso. Verifique sus datos e intente de nuevo.\nSi el error persiste; por favor notique de esto al equipo de desarrollo.')
            }
        })
        
    })
}

/**
 * Selecciona por medio de un selector dado todos los item(clave:valor)
 * y los retorna como un JSON
 * 
 * @param {string} selector 
 */
function getJsonFromForm(selector) {
    elements = document.querySelectorAll(selector)
    data = {}
    elements.forEach( element => {
        if ((element.type != 'radio') || (element.type == 'radio' && element.checked)) {            
            key = element.getAttribute('name')
            value = element.value
            data[key] = value
        }
    } )
    return data
}