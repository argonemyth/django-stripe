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
    """
    Handles all known webhooks (v2) from stripe, and calls signals.
    Plug in as you need.
    """
    http_method_names = ['post']

    def post(self, request, *args, **kwargs):
        #logger.debug("Got Post Request in WebhookSignalView - New signals")
        try:
            message = json.loads(request.raw_post_data)
            #logger.debug("Got webhook msg: %s" % message)
        except Exception as e:
            logger.error("Exception occurred: %s" % e)
            logger.debug("Here is the request: %s" % request)
            return HttpResponse(status=500)

        event = message[u'type']
        logger.debug("Got webhook event: %s" % event)
        signal = eval(event.replace('.', '_')) 
        if signal:
            sig_resp = signal.send_robust(sender=StripeWebhook, full_json=message)
            logger.debug("Signal Sent: %s" % sig_resp)

        return HttpResponse(status=200)

webhook_to_signal = csrf_exempt(WebhookSignalView.as_view())
