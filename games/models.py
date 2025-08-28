from django.db import models

class Game(models.Model):
    PLATFORM_CHOICES = [
        ("PS", "PlayStation"),
        ("XB", "Xbox"),
        ("NS", "Nintendo Switch"),
    ]

    title = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)  # ex.: 99999.99
    stock = models.PositiveIntegerField(default=0)
    platform = models.CharField(max_length=2, choices=PLATFORM_CHOICES)
    cover = models.ImageField(upload_to="games/covers/", blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} ({self.get_platform_display()})"
