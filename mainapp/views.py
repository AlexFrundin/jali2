from django.shortcuts import render, redirect
from mainapp.models import *
from paypal.standard.forms import PayPalPaymentsForm
from django.urls import reverse
from paypal.standard.models import *
from paypal.standard.ipn.models import PayPalIPN
# Create your views here.


def mainpage(request):
    args = {}
    args['mp_1'] = MpHeadBlock1.objects.get(id=1)
    args['mp_2'] = MpHead.objects.get(id=1)
    args['mp_3'] = Ticker.objects.all()
    args['mp_4'] = Services_section.objects.get(id=1)
    args['mp_5'] = Services.objects.all()
    args['mp_6'] = Form_section.objects.all()
    args['mp_7'] = Scroll_menu_text.objects.all()
    args['mp_8'] = Review.objects.all()
    args['mp_8f'] = Review.objects.get(id=2)
    args['mp_8a'] = Review.objects.all()[1:]
    args['mp_9'] = Bottom_footer.objects.get(id=1)
    slider = Slider2.objects.all()
    args['slider1'] = slider[0]
    args['slider2'] = slider[1]
    args['slider3'] = slider[2]
    news = News.objects.all()
    args['newsf'] = news[0]
    args['newsa'] = News.objects.all()[1:]

    return render(request, "mainpage.html", args)


def copy(request):
    args = {}
    return render(request, "mainpage2.html", args)


def usluga(request, id):
    args = {}
    args['service'] = Services.objects.get(id=id)
    args['all'] = Services.objects.all()
    return render(request, "usluga.html", args)

def contact(request):
    args = {}
    args['mp_9'] = Bottom_footer.objects.get(id=1)
    return render(request, 'contact.html', args)


def news(request):
    args = {}
    args['mp_9'] = Bottom_footer.objects.get(id=1)
    args['news'] = News.objects.all()
    return render(request, "news-all.html", args)


def snews(request, id):
    args = {}
    args['news'] = News.objects.get(id=id)
    return render(request, "single-news.html", args)

def page(request, link):
    args = {}
    args['mp_9'] = Bottom_footer.objects.get(id=1)
    args['news'] = Page.objects.get(link=link)
    return render(request, "page.html", args)

def addconsultation(request):
    name = request.POST.get('Your-name')
    phone = request.POST.get('Phone')
    category = request.POST.get('Dropdown')
    msg =  request.POST.get('Your-message')
    gg = Consultation(name=name, phone = phone, category = category, text = msg)
    gg.save()
    args = {}
    args['id'] = gg.id
    paypal_dict = {
        "business": "zzevr.pro-facilitator@gmail.com",
        "amount": "69",
        "item_name": "Consultations",
        "invoice": "%s" %args['id'],
        "notify_url": "http://lawyer.pythonanywhere.com" + reverse('paypal-ipn'),
        "return_url": "http://lawyer.pythonanywhere.com",
        "cancel_return": "http://lawyer.pythonanywhere.com",
        "custom": args['id'],
    }
    # Create the instance.
    form = PayPalPaymentsForm(initial=paypal_dict)
    args["form"]= form
    return render(request,'pay.html', args)

def list(request):
    #if request.user.is_admin == False:
    gg = PayPalIPN.objects.all()
    arr =[]
    for i in gg:
        kk = Consultation.objects.get(i.custom)
        arr.append({
            "name": kk.name,
            "phone": kk.phone,
            "category": kk.category,
            "text": kk.text,
        })
    args = {}
    args['data'] = arr
    return render(request, 'list.html', args)
    # else:
    #     redirect('/admin')
