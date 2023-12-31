"""
Amatak Online Shop
Copyright© Amatak Holdings Pty Ltd licensed under the MIT Agreement.
If you interesting to be part of this project pleaese contact:
Rony MAN <amatak.io@outlook.com>
for business <www.amatak.io>
OpenSource <www.amatak.org>
"""
from django.db.models.signals import post_save
from django.conf import settings
from django.db import models
from django.db.models import Sum
from django.shortcuts import reverse
from django_countries.fields import CountryField


CATEGORY_CHOICES = (
    ('WF', 'Women Fashion'),
    ('MF', 'Men Fashion'),
    ('PH &TE', 'Phones & Telecommunications'),
    ('CO&S', 'Computer,Office & Security'),
    ('C&E', 'Consumer & Electronics'),
    ('JW', 'Jewelry & Watches'),
    ('HPA', 'Home,pet & Appliances'),
    ('B&S', 'Bags & Shoes'),
    ('TKB', 'Toys, Kids & Babies'),
    ('OF&S', 'Outdoor Fun & Sports'),
    ('BH&H', 'Beauty, Health & Hair'),
    ('Au&Mo', 'Automobiles & Motorcycles'),
    ('T&HI', 'Tools & Home Improvement'),


)


LABEL_CHOICES = (
    ('L', 'larg'),
    ('M', 'Meduim'),
    ('S', 'Small'),
    ('XL', 'Extra larg'),
    ('XS', 'Extra Small'),
    ('XXL', 'Extra Extra larg'),
    ('XXS', 'Extra Extra Small'),
)

ADDRESS_CHOICES = (
    ('B', 'Billing'),
    ('S', 'Shipping'),
)

COLOR_CHOICES = (
    ('RD', 'Red'),
    ('Bk', 'Black'),
    ('BL', 'Blue'),
    ('PP', 'purple'),
    ('YL', 'Yellow'),
    ('OR', 'Orange'),
)
