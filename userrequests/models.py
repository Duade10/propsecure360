from django.db import models
from cloudinary.models import CloudinaryField

class UserRequest(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    location_of_property = models.CharField(max_length=100)
    document_type = models.CharField(max_length=60)
    document = CloudinaryField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    user = models.ForeignKey(
        "users.User",
        related_name="requests",
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.title


class Quotation(models.Model):
    RESPONSE_ACCEPTED = "accepted"
    RESPONSE_DECLINED = "declined"
    RESPONSE_NEGOCIATE = "negociate"
    RESPONSE_PENDING = "pending"

    RESPONSE_CHOICES = (
        (RESPONSE_ACCEPTED, "Accepted"),
        (RESPONSE_DECLINED, "Declined"),
        (RESPONSE_NEGOCIATE, "Negociate"),
        (RESPONSE_PENDING, "Pending"),
    )
    user_request = models.ForeignKey(UserRequest, on_delete=models.CASCADE, related_name="quotations")
    description = models.TextField()
    price = models.FloatField()
    status = models.CharField(choices=RESPONSE_CHOICES, max_length=20)

    def __str__(self):
        return f"{self.user_request.title} - Quotation"