from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

# Helper for quarter star values
def quarter_star(value):
    # Make sure rating is in 0.25 increments
    if (value * 100) % 25 != 0:
        raise ValidationError("Rating must be in 0.25 increments.")

# Model for games saved to user's library
class SavedGame(models.Model):
    STATUS_CHOICES = [
        ("played", "Played"),
        ("playing", "Currently Playing"),
        ("want", "Want to Play"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rawg_id = models.IntegerField()
    title = models.CharField(max_length=200)
    cover_image = models.URLField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="want")

    def __str__(self):
        return f"{self.title} ({self.user.username})"

# Model for adding reviews and ratings to games
class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rawg_id = models.IntegerField() # RAWG game ID from API

    # Allows ratings in quarter stars (1.25, 3.75)
    rating = models.DecimalField(
        decimal_places=2,
        max_digits=3,
        validators=[MinValueValidator(0.00), MaxValueValidator(5.00), quarter_star],
    )

    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ("user", "rawg_id") # allows one review per user per game

    def __str__(self):
        return f"{self.user.username} - {self.rawg_id} ({self.rating})"