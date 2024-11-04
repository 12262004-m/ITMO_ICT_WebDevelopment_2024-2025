from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.http import Http404
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, ReviewForm
from .models import Hotel, Room, Reservation, Review


def user_registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration.html', {'form': form})


def get_all_hotels(request):
    hotels = Hotel.objects.all()
    return render(request, 'hotels.html', {'hotels': hotels})


def get_hotel_info(request, hotel_id):
    try:
        hotel = Hotel.objects.get(pk=hotel_id)
    except:
        raise Http404("Hotel does not exist")
    rooms = hotel.rooms.all()
    return render(request, 'hotel_info.html', {'hotel': hotel, 'rooms': rooms})


@login_required
def get_all_reservations(request):
    reservations = Reservation.objects.filter(user=request.user)
    return render(request, 'all_reservations.html', {'reservations': reservations})


@login_required
def create_reservation(request, room_id):
    try:
        room = Room.objects.get(pk=room_id)
    except Room.DoesNotExist:
        raise Http404("Room does not exist")
    if request.method == 'POST':
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        reservation = Reservation(user=request.user, hotel=room.hotel, room=room, start_date=start_date, end_date=end_date)
        reservation.save()
        return redirect('all_reservations')
    return render(request, 'create_reservation.html', {'room': room})


@login_required
def update_reservation(request, reservation_id):
    try:
        reservation = Reservation.objects.get(pk=reservation_id)
    except Reservation.DoesNotExist:
        raise Http404("Reservation does not exist")
    if request.method == 'POST':
        reservation.start_date = request.POST.get('start_date')
        reservation.end_date = request.POST.get('end_date')
        reservation.save()
        return redirect('all_reservations')
    return render(request, 'update_reservation.html', {'reservation': reservation})


@login_required
def delete_reservation(request, reservation_id):
    try:
        reservation = Reservation.objects.get(pk=reservation_id)
    except Reservation.DoesNotExist:
        raise Http404("Reservation does not exist")
    if request.method == 'POST':
        reservation.delete()
        return redirect('all_reservations')
    return render(request, 'delete_reservation.html', {'reservation': reservation})


@login_required
def create_review(request, reservation_id):
    try:
        reservation = Reservation.objects.get(pk=reservation_id, user=request.user)
    except Reservation.DoesNotExist:
        raise Http404("Reservation does not exist")
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.reservation = reservation
            review.user = request.user
            review.save()
            return redirect('all_reservations')
    else:
        form = ReviewForm()
    return render(request, 'create_review.html', {'form': form, 'reservation': reservation})


@login_required
def get_all_reviews(request, room_id):
    try:
        room = Room.objects.get(pk=room_id)
    except Room.DoesNotExist:
        raise Http404("Room does not exist")
    reviews = Review.objects.filter(reservation__room=room)
    return render(request, 'all_reviews.html', {'room': room, 'reviews': reviews})
