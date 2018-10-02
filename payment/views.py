from django.shortcuts import render, get_object_or_404
from decimal import Decimal
from django.conf import settings
from django.urls import reverse
from mainapp.models import *
from paypal.standard.forms import PayPalPaymentsForm
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def PaymentProcess(request):
    if request.method == 'POST':
        name = request.POST.get('NameClient')
        phone = request.POST.get('Phone')
        category = request.POST.get('Dropdown')
        msg =  request.POST.get('Your-message')

        gg = Consultation( name=name, phone = phone, category = category, text = msg)
        gg.save()
        print(name, phone, category, msg)
        args = {}
        args['id'] = gg.id
        host = request.get_host()
        print(gg.id)
        print('http://{}{}'.format(host, reverse('paypal-ipn')))
        print('http://{}{}'.format(host, reverse('done')))
        print('http://{}{}'.format(host, reverse('canceled')))

        paypal_dict = {
            'business': settings.PAYPAL_RECEIVER_EMAIL,
            'amount': '1',
            'item_name': 'Consultations',
            "invoice": str(args['id']),
            'currency_code': 'USA',
            'notify_url': 'http://{}{}'.format(host, reverse('paypal-ipn')),
            'return_url': 'http://{}{}'.format(host, reverse('done')),
            'cancel_return': 'http://{}{}'.format(host, reverse('canceled'))
        }

        form = PayPalPaymentsForm(initial=paypal_dict)
        context={}
        context['mp_9'] = Bottom_footer.objects.get(id=1)
        context["form"] = form
        return render(request, 'payment/process.html', context)

@csrf_exempt
def PaymentDone(request):
    return render(request, 'payment/done.html')

@csrf_exempt
def PaymentCanceled(request):
    return render(request, 'payment/canceled.html')
