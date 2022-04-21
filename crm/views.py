from django.shortcuts import render
from .models import Order
from .forms import OrderForm
from cms.models import CmsSlider
from price.models import PriceTable, PriceCard
from telebot.sendmsg import sendTelegram
import requests
# Create your views here.
import socket
hostname = socket.gethostname()
IP = socket.gethostbyname(hostname)

def first_page(request):
    slider_list = CmsSlider.objects.all()
    pc_2 = PriceCard.objects.get(pk=2)
    pc_3 = PriceCard.objects.get(pk=3)
    pc_1 = PriceCard.objects.get(pk=1)
    price_table = PriceTable.objects.all()
    form = OrderForm()
    dict_obj = {
        'slider_list': slider_list,
        'pc_1': pc_1,
        'pc_2': pc_2,
        'pc_3': pc_3,
        'price_table': price_table,
        'form': form
    }
    return render(request, './index.html', dict_obj)

def sent_page(request):
    if request.POST:
        name = request.POST['name']
        phone = request.POST['phone']
        element = Order(order_name = name, order_phone = phone)
        element.save()
        sendTelegram(tg_name=name, tg_phone=phone, ip=IP)
        return render(request, './sent.html', {'name': name})
    else:
       return render(request, './sent.html')