from django.db.models.signals import post_save
from django.contrib.auth.models import User, Group
from django.contrib.auth.models import Group

from .models import Customer

def customer_profile(sender, instance, created, **kwargs):
    if created:
        group, _ = Group.objects.get_or_create(name="customer")
        instance.groups.add(group)

        Customer.objects.get_or_create(
            user=instance,
            defaults={
                'name': instance.username,
            }
        )
        print("Profile created")

post_save.connect(customer_profile, sender=User)

# def customer_profile(sender, instance, created, **kwargs):

#     group = Group.objects.get(name="customer")
#     instance.groups.add(group)

#     Customer.objects.create(
#         user=instance,
#         name=instance.username,
#     )

#     print("Profile created")

# post_save.connect(customer_profile, User)
