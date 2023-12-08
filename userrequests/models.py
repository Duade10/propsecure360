from django.db import models
from cloudinary.models import CloudinaryField

class UserRequest(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    location_of_property = models.CharField(max_length=100)
    document_type = models.CharField(max_length=60)
    document = CloudinaryField(blank=True, null=True)
    user = models.ForeignKey(
        "users.User",
        related_name="requests",
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.title