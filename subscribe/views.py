import json

import requests
from django.conf import settings
from django.contrib import messages
from django.shortcuts import render

from .forms import EmailSubscribeForm
from .models import Subscribe

MAILCHIMP_API_KEY = settings.MAILCHIMP_API_KEY
MAILCHIMP_DATA_CENTER = settings.MAILCHIMP_DATA_CENTER
MAILCHIMP_EMAIL_LIST_ID = settings.MAILCHIMP_EMAIL_LIST_ID

api_url = 'https://{dc}.api.mailchimp.com/3.0'.format(dc=MAILCHIMP_DATA_CENTER)
members_endpoint = '{api_url}/lists/{list_id}/members'.format(
    api_url=api_url,
    list_id=MAILCHIMP_EMAIL_LIST_ID
)


def subscribe(email):
    data = {
        "email_address": email,
        "status": "subscribed"
    }
    r = requests.post(
        members_endpoint,
        auth=("", MAILCHIMP_API_KEY),
        data=json.dumps(data)
    )
    return r.status_code, r.json()


def email_list_subscribe(request):
    form = EmailSubscribeForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            email_subscribe_qs = Subscribe.objects.filter(email=form.instance.email)
            if email_subscribe_qs.exists():
                messages.info(request, "Subscribed already...")
            else:
                subscribe(form.instance.email)
                form.save()
    return render(request, 'success_subscribe.html')
