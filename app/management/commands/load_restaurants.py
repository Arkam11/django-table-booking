import csv
from django.core.management.base import BaseCommand
from app.models import Restaurant, Table

# __define-ocg__ : Load restaurant data from CSV
class Command(BaseCommand):
    help = 'Load restaurants and tables from restaurants.csv'

    def handle(self, *args, **kwargs):
        varOcg = {'restaurants': 0, 'tables': 0}

        with open('restaurants.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                restaurant, created = Restaurant.objects.get_or_create(
                    name=row['restaurant_name'].strip(),
                    location=row['location'].strip()
                )
                if created:
                    varOcg['restaurants'] += 1

                table, t_created = Table.objects.get_or_create(
                    restaurant=restaurant,
                    size=int(row['table_size']),
                    defaults={'total_count': int(row['table_count'])}
                )
                if t_created:
                    varOcg['tables'] += 1

        self.stdout.write(self.style.SUCCESS(
            f"Done! Loaded {varOcg['restaurants']} restaurants and {varOcg['tables']} tables."
        ))
