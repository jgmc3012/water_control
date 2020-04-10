from django.db import transaction

from consumption_histories.models import ConsumptionHistory
from invoices.models import Invoice


def create_consumption_and_invoice(measurer, measure):
    with transaction.atomic():
        consumption_history = ConsumptionHistory.objects.create(
            from_date = measurer.last_visit,
            consumption = measurer.calculate_consumption(measure),
            measurer = measurer
        )
        measurer.register_visit(measure)
        invoice = Invoice(
            detail = consumption_history,
            client = measurer.house.familyboss,
            place = measurer.house
        )
        invoice.save()

    return {
        'consumption' : consumption_history.consumption,
        'amount' : invoice.amount,
        'house' : measurer.house.house_id
    }
