from stripe import convert_to_stripe_object

from django.http import Http404, HttpResponse
from django.utils import simplejson as json
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View, FormView

from .settings import STRIPE_SECRET_KEY
from .forms import CardTokenForm
from .signals import * 

import logging

logger = logging.getLogger(__name__)

class BaseCardTokenFormView(FormView):
    template_name = 'django_stripe/card_form.html'
    form_class = CardTokenForm

    def get_last4(self):
        return None

    def get_form_kwargs(self):
        kwargs = super(BaseCardTokenFormView, self).get_form_kwargs()
        kwargs.update({
            'initial': {
                'last4': self.get_last4(),
            }
        })

        return kwargs

class WebhookSignalView(View):
    http_method_names = ['post']
    event_signals = {
        'charge.succeeded': charge_succeeded,
        'charge.failed': charge_failed,
        'charge.refunded': charge_refunded,
        'customer.created': customer_created,
        'customer.deleted': customer_deleted,
        'customer.subscription.created': subscription_created,
        'customer.subscription.updated': subscription_updated,
        'customer.subscription.deleted': subscription_deleted,
        'customer.subscription.trial_will_end': subscription_trial_will_end,
        'invoice.created': invoice_created,
        'invoice.updated': invoice_updated,
        'invoice.payment_succeeded': invoice_payment_succeeded,
        'invoice.payment_failed': invoice_payment_failed,
        'ping': ping,
    }

    def post(self, request, *args, **kwargs):
        logger.debug("Got Post Request in WebhookSignalView - New signals")
        try:
            message = json.loads(request.raw_post_data)
            #logger.debug("Got webhook msg: %s" % message)
        except Exception as e:
            logger.error("Exception occurred: %s" % e)
            logger.debug("Here is the request: %s" % request)
            return HttpResponse(status=500)

        event = message[u'type']
        logger.debug("Got webhook event: %s" % event)

        if event not in self.event_signals:
            logger.debug("webhook event not found.")
            raise Http404

        try:
            for key, value in message.iteritems():
                if isinstance(value, dict) and 'object' in value:
                    logger.debug(message[key])
                    #message[key] = convert_to_stripe_object(value, STRIPE_SECRET_KEY)
        except Exception as e:
            logger.error("Exception occurred: %s" % e)

        """
        signal = self.event_signals.get(event)
        signal.send_robust(sender=StripeWebhook, **message)
        """

        return HttpResponse(status=200)

webhook_to_signal = csrf_exempt(WebhookSignalView.as_view())
