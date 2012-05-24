"""
Provides the following signals:

V1

- recurring_payment_failed
- invoice_ready
- recurring_payment_succeeded
- subscription_trial_ending
- subscription_final_payment_attempt_failed
- subscription_ping_sent

v2

- charge_succeeded
- charge_failed
- charge_refunded
- charge_disputed
- customer_created
- customer_updated
- customer_deleted
- customer_subscription_created
- customer_subscription_updated
- customer_subscription_deleted
- customer_subscription_trial_will_end
- customer_discount_created
- customer_discount_updated
- customer_discount_deleted
- invoice_created
- invoice_updated
- invoice_payment_succeeded
- invoice_payment_failed
- invoiceitem_created
- invoiceitem_updated
- invoiceitem_deleted
- plan_created
- plan_updated
- plan_deleted
- coupon_created
- coupon_updated
- coupon_deleted
- transfer_created
- transfer_failed
- ping
"""

from django.dispatch import Signal

# v2 webhooks
WEBHOOK2_ARGS = ["full_json"]
charge_succeeded = Signal(providing_args=WEBHOOK2_ARGS)
charge_failed = Signal(providing_args=WEBHOOK2_ARGS) 
charge_refunded = Signal(providing_args=WEBHOOK2_ARGS)
customer_created = Signal(providing_args=WEBHOOK2_ARGS)
customer_updated = Signal(providing_args=WEBHOOK2_ARGS)
customer_deleted = Signal(providing_args=WEBHOOK2_ARGS)
customer_subscription_created = Signal(providing_args=WEBHOOK2_ARGS)
customer_subscription_updated = Signal(providing_args=WEBHOOK2_ARGS)
customer_subscription_deleted = Signal(providing_args=WEBHOOK2_ARGS)
customer_subscription_trial_will_end = Signal(providing_args=WEBHOOK2_ARGS)
customer_discount_created = Signal(providing_args=WEBHOOK2_ARGS)
customer_discount_updated = Signal(providing_args=WEBHOOK2_ARGS)
customer_discount_deleted = Signal(providing_args=WEBHOOK2_ARGS)
invoice_created = Signal(providing_args=WEBHOOK2_ARGS)
invoice_updated = Signal(providing_args=WEBHOOK2_ARGS)
invoice_payment_succeeded = Signal(providing_args=WEBHOOK2_ARGS)
invoice_payment_failed = Signal(providing_args=WEBHOOK2_ARGS)
invoiceitem_created = Signal(providing_args=WEBHOOK2_ARGS)
invoiceitem_updated = Signal(providing_args=WEBHOOK2_ARGS)
invoiceitem_deleted = Signal(providing_args=WEBHOOK2_ARGS)
plan_created = Signal(providing_args=WEBHOOK2_ARGS)
plan_updated = Signal(providing_args=WEBHOOK2_ARGS)
plan_deleted = Signal(providing_args=WEBHOOK2_ARGS)
coupon_created = Signal(providing_args=WEBHOOK2_ARGS)
coupon_updated = Signal(providing_args=WEBHOOK2_ARGS)
coupon_deleted = Signal(providing_args=WEBHOOK2_ARGS)
transfer_created = Signal(providing_args=WEBHOOK2_ARGS)
transfer_failed = Signal(providing_args=WEBHOOK2_ARGS)
ping = Signal(providing_args=WEBHOOK2_ARGS)


# v1 webhooks
WEBHOOK_ARGS = ["customer", "full_json"]

recurring_payment_failed = Signal(providing_args=WEBHOOK_ARGS)
invoice_ready = Signal(providing_args=WEBHOOK_ARGS)
recurring_payment_succeeded = Signal(providing_args=WEBHOOK_ARGS)
subscription_trial_ending = Signal(providing_args=WEBHOOK_ARGS)
subscription_final_payment_attempt_failed = Signal(providing_args=WEBHOOK_ARGS)
subscription_ping_sent = Signal(providing_args=[])


class StripeWebhook(object):
    pass
