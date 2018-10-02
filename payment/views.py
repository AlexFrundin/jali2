from django.shortcuts import render, get_object_or_404
from decimal import Decimal
from django.conf import settings
from django.urls import reverse
from mainapp.models import *
from paypal.standard.forms import PayPalPaymentsForm
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def PaymentProcess(request):
    name = request.POST.get('Your-name')
    phone = request.POST.get('Phone')
    category = request.POST.get('Dropdown')
    msg =  request.POST.get('Your-message')
    gg = Consultation(name=name, phone = phone, category = category, text = msg)
    gg.save()

    args = {}
    args['id'] = gg.id
    host = request.get_host()

    paypal_dict = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': '1',
        'item_name': f'Consultations {name}',
        "invoice": f"{args['id']}",
        'currency_code': 'USA',
        'notify_url': 'http://{}{}'.format(host, reverse('paypal-ipn')),
        'return_url': 'http://{}{}'.format(host, reverse('done')),
        'cancel_return': 'http://{}{}'.format(host, reverse('canceled'))
    }

    form = PayPalPaymentsForm(initial=paypal_dict)
    context = {"form": form}
    return render(request, 'payment/process.html', {'form':form})

@csrf_exempt
def PaymentDone(request):
    return render(request, 'payment/done.html')

@csrf_exempt
def PaymentCanceled(request):
    return render(request, 'payment/canceled.html')
