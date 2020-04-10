const $submit = document.getElementById('submit')
const $year = document.getElementById('year')
const $month = document.getElementById('month')
const $day = document.getElementById('day')

$year.addEventListener('change', function(event) {
    const year = parseInt(this.value)
    this.value = year
    disabledElement(year, $submit)
    disabledElement(year, $month, '0')
    disabledElement(parseInt($month.value), $day, '0')
})

$month.addEventListener('change', function (event) {
    const month = parseInt(this.value)
    disabledElement(month, $day, '0')
    const HTMLString = snipetOptionsDaysMonth(month)
    insertElement('#day',HTMLString)
})

function disabledElement(condition, element, value=null) {
    if (condition) {
        if (element.disabled) {
            element.disabled = false
        }
    } else if (!element.disabled) {
        element.disabled = true
        if (value != null && element.value != value) {
            element.value = value
        }
    }
}

function snipetOptionsDaysMonth(month) {
    const limitDay = [0,31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    let snippetDays = `<option value="0">Todos</option>\n`
    for (let i = 1; i <= limitDay[month]; i++) {
        snippetDays += `<option value="${i}">${i}</option>\n`
    }
    return `${snippetDays}`
}