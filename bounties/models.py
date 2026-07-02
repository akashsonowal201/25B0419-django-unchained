from django.db import models
# Create your models here.
from django.contrib.auth.models import User


class Bounty(models.Model):

    STATUS_CHOICES = [

        ("wanted", "Wanted"),
        ("captured", "Captured")

    ]

    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="bounties"
    )

    target_name = models.CharField(max_length=200)

    reward = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="wanted"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.target_name