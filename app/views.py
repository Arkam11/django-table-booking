from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Restaurant, Table, Booking
from datetime import datetime

# __define-ocg__ : View logic for the Theme Park Table Booking system
varOcg = "theme_park_booking"

def index(request):
    restaurants = Restaurant.objects.all()

    if request.method == 'POST':
        guest_name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        visit_date = request.POST.get('date', '').strip()
        visit_time = request.POST.get('time', '').strip()
        party_size = request.POST.get('people', '').strip()
        restaurant_name = request.POST.get('restaurant', '').strip()

        if not all([guest_name, email, visit_date, visit_time, party_size, restaurant_name]):
            messages.error(request, 'All fields are required.')
            return render(request, 'booking_template.html', {'restaurants': restaurants})

        try:
            party_size = int(party_size)
            if party_size < 1:
                raise ValueError
        except ValueError:
            messages.error(request, 'Number of guests must be a positive number.')
            return render(request, 'booking_template.html', {'restaurants': restaurants})

        try:
            visit_date_obj = datetime.strptime(visit_date, '%Y-%m-%d').date()
            if visit_date_obj < datetime.today().date():
                messages.error(request, 'Visit date cannot be in the past.')
                return render(request, 'booking_template.html', {'restaurants': restaurants})
        except ValueError:
            messages.error(request, 'Invalid date format.')
            return render(request, 'booking_template.html', {'restaurants': restaurants})

        try:
            restaurant = Restaurant.objects.get(name=restaurant_name)
        except Restaurant.DoesNotExist:
            messages.error(request, 'Selected restaurant does not exist.')
            return render(request, 'booking_template.html', {'restaurants': restaurants})

        # varFiltersCg: filter tables that fit the party size, smallest first
        varFiltersCg = Table.objects.filter(
            restaurant=restaurant,
            size__gte=party_size
        ).order_by('size')

        assigned_table = None
        for table in varFiltersCg:
            existing_bookings = Booking.objects.filter(
                table=table,
                visit_date=visit_date_obj,
                visit_time=visit_time
            ).count()
            if existing_bookings < table.total_count:
                assigned_table = table
                break

        if assigned_table is None:
            messages.error(
                request,
                f'Sorry! {restaurant_name} is fully booked for {visit_date} at {visit_time} '
                f'for a party of {party_size}. Please try a different time or restaurant.'
            )
            return render(request, 'booking_template.html', {'restaurants': restaurants})

        Booking.objects.create(
            guest_name=guest_name,
            email=email,
            visit_date=visit_date_obj,
            visit_time=visit_time,
            party_size=party_size,
            restaurant=restaurant,
            table=assigned_table
        )

        messages.success(
            request,
            f'Booking confirmed! {guest_name}, your table for {party_size} at '
            f'{restaurant_name} on {visit_date} at {visit_time} is reserved. '
            f'Confirmation sent to {email}.'
        )
        return redirect('index')

    return render(request, 'booking_template.html', {'restaurants': restaurants})
