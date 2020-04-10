const snippetCard = (date, paid, debt) =>`
<div class="card mt-3">
    <div class="card-header text-center font-weight-bold">
        ${date}
    </div>
    <div class="card-body">
        <div class="row">
            <div class="col-6 text-center">
            Total de cobros: <strong class="text-success">$${paid}</strong>
            </div>
            <div class="col-6 text-center">
            Total de Deudas: <strong class="text-danger">$${debt}</strong>
            </div>
        </div>
    </div>
</div>
`

const formatDate = (year, month, day) => {
    month = parseInt(month)
    day = parseInt(day)
    let format = `Año:${year} `
    if (month) {
        format += ` - Mes:${month}`
        if (day) {
            format += ` - Dia:${day}`
        }
    }
    return format
}

const snippetDetailList = (date,invoices) => {
    const struct = (body_str) => `
    <table class="table mt-3">
        <thead>
            <tr>
                <th>Fechas</th>
                <th>Casa</th>
                <th>Cliente</th>
                <th>Monto</th>
            </tr>
        </thead>
        <tbody>
        ${body_str}
        </tbody>
    </table>`
    let body = ''
    let totalPaid = 0
    let totalDebt = 0
    Array.from(invoices).forEach( invoice =>{
        const {detail, paid, place, client, amount} = invoice
        if (paid) {
            totalPaid += parseFloat(amount)
        } else {
            totalDebt += parseFloat(amount)
        }
        const classNamePaid = paid ? 'text-success':'text-danger'
        body += `
        <tr>
            <td scope="row"><strong>${detail.from_date}</strong> Al <strong>${detail.to_date}</strong></td>
            <td>${place}</td>
            <td>${client}</td>
            <td class="${classNamePaid}">$${amount}</td>
        </tr>
        `
    })    
    return `<div>${snippetCard(date, totalPaid, totalDebt)}${struct(body)}</div>` 

}
