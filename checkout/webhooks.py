""" required imports for module functionality """
from django.http import HttpResponse
from django.conf import settings
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt

import stripe

from checkout.webhook_handler import StripeWH_Handler


@require_POST
@csrf_exempt
def webhook(request):
    """ Listen for webhooks from Stripe """
    # Setup
    wh_secret = settings.STRIPE_WH_SECRET
    stripe.api_key = settings.STRIPE_SECRET_KEY

    # Get webhook data and verify signature
    payload = request.body
    sig_header = request.META('HTTP_STRIPE_SIGNATURE')
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, wh_secret
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)
    except Exception as e:
        return HttpResponse(content=e, status=400)

    # Handle Event
    if event.type == 'payment_intent.succeeded':
        payment_intent = event.data.object # Contains a stripe.PaymentIntent
        print('Payment intent was successful!')
    elif event.type == 'payment_method.attached':
        payment_method = event.data.object # Contains a stripe.PaymentMethod
        print('PaymentMethod was attached to a Customer!')
    # Handle other events
    else:
        # Unexpected event type
        return HttpResponse(status=400)

    print('Success!')
    return HttpResponse(status=200)
