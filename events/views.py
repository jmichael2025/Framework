from django.shortcuts import render, redirect
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.urls import reverse
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth import get_user_model

from.models import Event 
from .forms import EventForm, RegisterForm


def home(request):
    events = Event.objects.all()
    return render(request, 'events/home.html', {'events': events})

def event_list(request):
    events = Event.objects.all()
    return render(request, 'events/event_list.html', {'events': events})

def event_detail(request, event_id):
    event = Event.objects.get(id=event_id)
    return render(request, 'events/event_detail.html', {'event': event})

def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
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
    events = Event.objects.filter(created_by=request.user)

    return render(
        request,
        'events/dashboard.html',
        {'events': events}
    )