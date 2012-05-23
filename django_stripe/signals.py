from django.dispatch import Signal


# Webhooks
charge_succeeded = Signal(providing_args=[ 
    'customer',
    'invoice',
    'amount',
    'livemode',
])

charge_failed = Signal(providing_args=[ 
    'customer',
    'amount',
    'failure_message',
    'card',
])

charge_refunded = Signal(providing_args=[ 
    'customer',
    'invoice',
    'amount_refunded',
    'livemode',
])

customer_created = Signal(providing_args=[
    'id',
    'account_balance',
    'livemode',
    'subscription',
])

customer_deleted = Signal(providing_args=[
    'id',
    'account_balance',
    'livemode',
    'subscription',
])

subscription_created = Signal(providing_args=[
    'customer',
    'current_period_end',
    'start',
    'cancel_at_period_end',
    'plan'
])

subscription_updated = Signal(providing_args=[
    'customer',
    'cancel_at_period_end', #this value determins if an user cancelled the plan or not
    'plan',
    'canceled_at',
])

subscription_deleted = Signal(providing_args=[
    'customer',
    'status',
    'ended_at',
])

subscription_trial_will_end = Signal(providing_args=[
    'customer',
    'status',
    'plan'
])

invoice_created = Signal(providing_args=[
    'customer',
    'line',
    'paid',
    'livemode',
])

invoice_updated = Signal(providing_args=['invoice']) #modify

invoice_payment_succeeded = Signal(providing_args=[
    'customer',
    'total',
    'date',
    'period_end',
    'discount',
    'livemode',
])

invoice_payment_failed = Signal(providing_args=[
    'customer',
    'livemode',
])
"""
# Below are for webhook V1
upcoming_invoice_updated = Signal(providing_args=['customer'])
recurring_payment_failed = Signal(providing_args=[
    'customer',
    'attempt',
    'invoice',
    'payment',
    'livemode',
])

invoice_ready = Signal(providing_args=[
    'customer',
    'invoice'
])

recurring_payment_succeeded = Signal(providing_args=[
    'customer',
    'invoice',
    'payment',
    'livemode',
])

subscription_trial_ending = Signal(providing_args=[
    'customer',
    'subscription',
])

subscription_final_payment_attempt_failed = Signal(providing_args=[
    'customer',
    'subscription',
])
"""

ping = Signal()

class StripeWebhook(object):
    pass
