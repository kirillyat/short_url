import random
import string
from django.db import models


class Shortener(models.Model):
    original_url = models.URLField(max_length=2000)  # Stores the original long URL
    short_code = models.CharField(
        max_length=10, unique=True, blank=True
    )  # Unique short code

    def save(self, *args, **kwargs):
        # Generate a short code if it doesn't already exist
        if not self.short_code:
            self.short_code = self.generate_short_code()
        super().save(*args, **kwargs)

    def generate_short_code(self):
        # Generate a short code
        length = 6  # Length of the short code
        characters = string.ascii_letters + string.digits
        while True:
            short_code = "".join(random.choices(characters, k=length))
            if not Shortener.objects.filter(short_code=short_code).exists():
                return short_code
