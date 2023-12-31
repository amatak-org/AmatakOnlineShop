"""
Amatak Online Shop
Copyright© Amatak Holdings Pty Ltd licensed under the MIT Agreement.
If you interesting to be part of this project pleaese contact:
Rony MAN <amatak.io@outlook.com>
for business <www.amatak.io>
OpenSource <www.amatak.org>
"""
import random
import string

import stripe
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.views.generic import ListView, DetailView, View

from amatak_shop.forms.checkout import CheckoutForm
from amatak_shop.forms.coupon import CouponForm
from amatak_shop.forms.refund import RefundForm
from amatak_shop.forms.payment import PaymentForm
from amatak_shop.models.order import *



class OrderSummaryView(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            context = {
                'object': order
            }
            return render(self.request, 'amatak_shop/store/order_summary.html', context)
        except ObjectDoesNotExist:
            messages.warning(self.request, "You do not have an active order")
            return redirect("/")
