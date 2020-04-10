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
                console.error(data)
                let listStr = ''
                for (key in data) {
                    listStr += `<li>${key} -> ${data[key]}</li>`
                }
                const msg = listStr ? `<ul>${listStr}</ul>`:JSON.stringify(data)
                show_alert(okey_fetch, msg)
                reject(data)
            }
        })
        .catch( e => {
            toggleLoading()    
            console.error(e)
            if (status_fetch<500) {
                if (status_fetch==404) {
                    show_alert(false, 'Recurso no encontrado')
                } else {
                    show_alert(false, 'Verifique los datos ingresados')
                }
            } else {
                show_alert(false, 'Ups! Esto es vergonzoso. Verifique sus datos e intente de nuevo.\nSi el error persiste; por favor notifique de esto al equipo de desarrollo.')
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

/**
 * 
 * @param {*} form Un elemento formulario
 * @param {*} method Metodo http (GET, POST, PUT, DELETE)
 * @param {*} replaceInURLFunction algunas url de formularios(el atributo action) contiene un numero generico 12345, que debe ser remplazado. Esta funcion debe retornar dicho replace. Tambien puedes editar el action del form en esta funcion.
 * 
 * @returns {Promise}
 */
function sendForm(form, method='POST', replaceInURLFunction=null, resolve=console.log, reject=console.error) {
    form.addEventListener('submit', function (event) {
        event.preventDefault()
        const data = getJsonFromForm("[api='water_control']")
        const replaceInURL = replaceInURLFunction!= null ? replaceInURLFunction(data):''
        const url = this.action.replace('12345', replaceInURL)
        sendData(data, url, method)
        .then(response => resolve(response))
        .catch(response => reject(response))
    })
}