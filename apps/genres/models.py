from django.db import models

CATEGORY_CHOICES = (
    (1, 'Fiction'),
    (2, 'Non-Fiction'),
)


class Genre(models.Model):
    category = models.IntegerField(choices=CATEGORY_CHOICES)
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
