import datetime as dt
from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.views.decorators.http import require_POST
from django.db.transaction import atomic, non_atomic_requests
from django.http import HttpResponse, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from secrets import compare_digest
from webhooks.models import AcmeWebhookMessage
from main.models import *
import json
from django.utils import timezone

@csrf_exempt
@require_POST
@non_atomic_requests
def aftership(request):
    #given_token = request.headers.get("Acme-Webhook-Token", "")
    #if not compare_digest(given_token, settings.ACME_WEBHOOK_TOKEN):
    #    return HttpResponseForbidden(
    #        "Incorrect token in Acme-Webhook-Token header.",
    #        content_type="text/plain",
    #)
    #AcmeWebhookMessage.objects.filter(
    #    received_at__lte=timezone.now() - dt.timedelta(days=7)
    #).delete()
    payload = json.loads(request.body)
    #AcmeWebhookMessage.objects.create(
    #    received_at=timezone.now(),
    #    payload=payload,
    #)
    process_webhook_payload(payload)
   
    return HttpResponse(payload, content_type="text/plain")

@atomic
def process_webhook_payload(payload):
    print(payload)
    listreg=Class_NetSuite(payload)
    
    