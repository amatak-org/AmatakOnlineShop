"""
Amatak Online Shop
Copyright© Amatak Holdings Pty Ltd licensed under the MIT Agreement.
If you interesting to be part of this project pleaese contact:
Rony MAN <amatak.io@outlook.com>
for business <www.amatak.io>
OpenSource <www.amatak.org>
"""
from django import forms
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget

PAYMENT_CHOICES = (
    ('S', 'Stripe'),
    ('P', 'PayPal')
)
class PaymentForm(forms.Form):
    stripeToken = forms.CharField(required=False)
    save = forms.BooleanField(required=False)
    use_default = forms.BooleanField(required=False)