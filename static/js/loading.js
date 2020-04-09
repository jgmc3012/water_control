const loadingStr = (`
    <div id="modalLoading">
        <div class="modal-backdrop fade show">
        </div>
        <div 
            class="modal fade show"
            tabindex="-1"
            role="dialog"
            aria-labelledby="exampleModalCenterTitle"
            aria-hidden="true"
            style="display: block;"
        >
            <div class="modal-dialog modal-dialog-centered">
              <div class="modal-content">
                <div class="modal-header">
                  <h3 class="modal-title d-inline" style="margin: auto;">Realizando Peticiones...</h3>
                </div>
                <div class="modal-body">
                    <div class="text-center">
                        <div class="spinner-border" style="width: 3rem; height: 3rem;">
                            <span class="sr-only">Loading...</span>
                        </div>
                    </div>
                </div>
                <div class="modal-footer">
                  <button type="button" class="btn btn-danger">Cancelar</button>
                </div>
              </div>
            </div>
        </div>
    </div>
`)


toggleLoading = () => {
    let loaderModal = document.getElementById('modalLoading')
    if (loaderModal) {
        loaderModal.remove()
    } else {
        loaderModal = createTemplate(loadingStr)
        let container = document.querySelector('body')
        container.append(loaderModal)
    }
}