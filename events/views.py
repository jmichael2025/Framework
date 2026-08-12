
from django.shortcuts import render, redirect
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.urls import reverse
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import query

from.models import Event ,Registration
from .forms import EventForm, RegisterForm


def home(request):
    events = Event.objects.all()
    return render(request, 'events/home.html', {'events': events})

def event_list(request):
    query = request.GET.get('q', '')

    events = Event.objects.all()

    if query:
        events = events.filter(
            models.Q(title__icontains=query) |
            models.Q(description__icontains=query)
        )

    return render(
        request,
        'events/event_list.html',
        {
            'events': events,
            'query': query,
        }
    )

def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)

    is_registered = False

    if request.user.is_authenticated:
        is_registered = Registration.objects.filter(
            user=request.user,
            event=event
        ).exists()

    attendees = None
    if request.user == event.created_by:
        attendees = Registration.objects.filter(event=event).select_related('user')

    return render(
        request,
        'events/event_detail.html',
        {
            'event': event,
            'is_registered': is_registered,
            'attendees': attendees
        }
    )


def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.created_by = request.user
            event.save()
            return redirect('event_list')
    else:
        form = EventForm()
    return render(request, 'events/create_event.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()

            uid = urlsafe_base64_encode(force_bytes(user.pk))
            token = default_token_generator.make_token(user)

            verification_url = request.build_absolute_uri(
                reverse(
                    'verify_email',
                    kwargs={
                        'uidb64': uid,
                        'token': token,
                    }
                )
            )

            send_mail(
                'Verify your CampusConnect account',
                f'Click the following link to verify your email:\n\n{verification_url}',
                None,
                [user.email],
            )

            return render(
                request,
                'events/email_verification_sent.html'
            )

    else:
        form = RegisterForm()

    return render(request, 'events/register.html', {'form': form})


def verify_email(request, uidb64, token):
    User = get_user_model()

    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return render(request, 'events/email_verified.html')
    else:
        return render(request, 'events/verification_failed.html')

def dashboard(request):
    created_events = Event.objects.filter(created_by=request.user)

    registered_events = Event.objects.filter(registrations__user=request.user)

    return render(
        request,
        'events/dashboard.html',
        {'created_events': created_events, 'registered_events': registered_events}
    )

def edit_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)

    if event.created_by != request.user:
        return redirect('event_detail', event_id=event.id)

    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)

        if form.is_valid():
            form.save()
            return redirect('event_detail', event_id=event.id)

    else:
        form = EventForm(instance=event)

    return render(
        request,
        'events/edit_event.html',
        {'form': form, 'event': event}
    )

def delete_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)

    if event.created_by != request.user:
        return redirect('event_detail', event_id=event.id)

    if request.method == 'POST':
        event.delete()
        return redirect('event_list')

    return render(
        request,
        'events/delete_event.html',
        {'event': event}
    )

def register_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)

    if request.method == 'POST':
        Registration.objects.get_or_create(
            user=request.user,
            event=event
        )

        return redirect('event_detail', event_id=event.id)

    return redirect('event_detail', event_id=event.id)

def cancel_registration(request, event_id):
    event = get_object_or_404(Event, id=event_id)

    if request.method == 'POST':
        Registration.objects.filter(
            user=request.user,
            event=event
        ).delete()

    return redirect('event_detail', event_id=event.id)