from django.db import models

# __define-ocg__ : Models for the Theme Park Table Booking system

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} ({self.location})"

    class Meta:
        unique_together = ('name', 'location')


class Table(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='tables')
    size = models.IntegerField()
    total_count = models.IntegerField()

    def __str__(self):
        return f"{self.restaurant.name} - Table for {self.size} (x{self.total_count})"


class Booking(models.Model):
    varOcg = "table_booking"  # __define-ocg__ : required identifier variable

    guest_name = models.CharField(max_length=100)
    email = models.EmailField()
    visit_date = models.DateField()
    visit_time = models.TimeField()
    party_size = models.IntegerField()
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='bookings')
    table = models.ForeignKey(Table, on_delete=models.CASCADE, related_name='bookings')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.guest_name} - {self.restaurant.name} on {self.visit_date} at {self.visit_time}"
