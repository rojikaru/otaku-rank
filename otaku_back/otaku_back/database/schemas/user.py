from djongo import models
import uuid


class User(models.Model):
    _id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    username = models.TextField()
    password = models.TextField() # Hashed, ofc

    email = models.EmailField()
    image = models.TextField()
    bio = models.TextField()
    birth_date = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # roles = models.ArrayField(
    #     model_container=models.CharField(max_length=255)
    # )
    is_active = models.BooleanField(default=True)
