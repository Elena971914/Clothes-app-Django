from django.db.models.signals import pre_save
from django.utils import timezone
from django.dispatch import receiver

from clothesDjango.orders.models import Order


@receiver(pre_save, sender=Order)
def update_order_status(sender, instance, **kwargs):
    if instance.pk:
        old_instance = sender.objects.get(pk=instance.pk)
        if old_instance.date_of_purchase != instance.date_of_purchase:
            if (timezone.now() - instance.date_of_purchase).days > 3:
                instance.status = 'Sent'
            else:
                instance.status = 'In Process'
