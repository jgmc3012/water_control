import calendar
from decimal import Decimal
from django.db import transaction

from django.utils import timezone

from invoices.serializers import InvoiceSerializer


def get_range_date(year, month, day)->tuple:
    """
    Retorna un rango de fecha con una diferencia de
        - Un año.
        - Un mes.
        - Un dia.
    Segun la especificacion de la entrada
    """
    from_date = timezone.datetime(year=year,
                                    month=month if month else 1,
                                    day=day if day else 1
                                )
    if not month:
        to_date = timezone.datetime(year=year+1,month=1,day=1)
    elif day:
        to_date = timezone.datetime(year=year,month=month,day=day) + timezone.timedelta(days=1)
    else:
        to_year, to_month = calendar.nextmonth(year=year, month=month)
        to_date = timezone.datetime(year=to_year,month=to_month,day=1)

    return from_date, to_date

def pay_invoices(invoices:list, amount)->dict:
    """
    Recive una lista de facturas y un dinero para efectuar el pago de las mismas.
    
    Retorna:
    ok : Indica si se pudo o no cancelar el total de facturas pendientes.
    change : Monto restante del pago de facturas
    number_of_payments : Numero de facturas pagas
    unpaid_invoices : datos de las facturas que no se pudieron procesar.
    """
    ok = True
    amount = Decimal(amount)
    with transaction.atomic():
        for index, invoice in enumerate(invoices):
            if amount >= invoice.amount:
                amount -= invoice.amount
                invoice.pay()
            else:
                ok = False
                break
    if ok:
        number_of_payments = index+1
        unpaid_invoices = []
    else:
        number_of_payments = index
        unpaid_invoices = invoices[index:invoices.count()]
    return {
        'ok' : ok,
        'change' : amount,
        'number_of_payments' : number_of_payments,
        'unpaid_invoices' : InvoiceSerializer(unpaid_invoices, many=True).data,
    }