const snippetFormPay = `
<div class='mt-2'>
    <form action="/api/family-bosses/12345/pay_invoices/">
        <div class="form-group">
            <label for="amount">Ingresa el monto a cancelar</label>
            <div class="input-group">
                <div class="input-group-prepend">
                    <span class="input-group-text">$</span>
                </div>
                <input type="number"
                    class="form-control" name="amount" id="amount" placeholder="600000.00">
                <div class="input-group-append">
                    <button class="btn btn-primary">Pagar</button>
                </div>
            </div>
        </div>
    </form>
</div>
`

const SnippetItemListInvoice = (from_date, to_date, consumption, amount) => `
<div class="card mt-2">
    <div class="card-header">
    </div>
    <div class="card-body text-center">
        <div class="row">
            <div class="col-lg-4 col-md-6 col-sm-12 mt-2">
                <h5 class="card-title font-weight-bold">
                    Rango de Fechas: 
                </h5>
                <div class="card-text">
                    ${from_date} hasta ${to_date}
                </div>
            </div>

            <div class="col-lg-4 col-md-6 col-sm-12 mt-2">
                <h5 class="card-title font-weight-bold">
                    Consumo: 
                </h5>
                <div class="card-text">
                    ${consumption} Metros Cubicos
                </div>
            </div>

            <div class="col-lg-4 col-md-6 col-sm-12 mt-2">
                <h5 class="card-title font-weight-bold">
                    Valor del servicio:
                </h5>
                <div class="card-text text-danger">
                    $${amount}
                </div>
            </div>
        </div>
    </div>
</div>
`

const SnippetListInvoices = (invoices) => {
    list = ''
    total = 0
    Array.from(invoices).forEach( invoice => {
        const { detail } = invoice
        list += SnippetItemListInvoice(detail.from_date, detail.to_date,
                                        detail.consumption, invoice.amount)
        total += parseFloat(invoice.amount)
    })
    return `
    <div>
        <h4 class="font-weight-bold">Listado de Pedidos de ${invoices[0].client}</h4>
        ${snippetFormPay}
        <div class="row">
            <div class="ml-auto text-center">
                <div class="font-weight-bold">Deuda hasta la fecha:</div>
                <p class="text-danger">$${total}</p>
            </div>
        </div>
        <div>${list}</div>
    </div>
    `
}