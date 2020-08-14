from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from django.http import JsonResponse
import json
import datetime
from .models import * 
from django.contrib.auth.models import User

# Create your views here.
def makeCustomer(request):
	cust = Customer(user = request.user, name= request.user.username, email=request.user.email)
	cust.save()
	return render(request, 'product/makecustomer.html')
	
def home(request):
	if request.user.is_authenticated:
		
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		items = order.orderitem_set.all()
		cartItems = order.get_cart_items
	else:
		items = []
		order = {'get_cart_total':0, 'get_cart_items':0, 'shipping':False}
		cartItems = order['get_cart_items']
		

	context = {'items':items, 'order':order, 'cartItems':cartItems , 'things' : thing.objects.all()  }
	return render(request, 'product/home.html', context)

def cart(request):

	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		items = order.orderitem_set.all()
		cartItems = order.get_cart_items
	else:
		#Create empty cart for now for non-logged in user
		items = []
		order = {'get_cart_total':0, 'get_cart_items':0, 'shipping':False}
		cartItems = order['get_cart_items']

	context = {'items':items, 'order':order, 'cartItems':cartItems}
	return render(request, 'product/cart1.html', context)


def checkout(request):
	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		items = order.orderitem_set.all()
		cartItems = order.get_cart_items
	else:
		#Create empty cart for now for non-logged in user
		items = []
		order = {'get_cart_total':0, 'get_cart_items':0, 'shipping':False}
		cartItems = order['get_cart_items']

	context = {'items':items, 'order':order, 'cartItems':cartItems}
	return render(request, 'product/checkout.html', context)


def updateItem(request):
	data = json.loads(request.body)
	productId = data['productId']
	action = data['action']


	customer = request.user.customer
	product = thing.objects.get(id=productId)
	order, created = Order.objects.get_or_create(customer=customer, complete=False)
	orderItem , created = OrderItem.objects.get_or_create(order=order, product=product)

	if action == 'add':
		orderItem.quantity = (orderItem.quantity + 1)
	elif action == 'remove':
		orderItem.quantity = (orderItem.quantity - 1)

	orderItem.save()
	
	if orderItem.quantity <=0:
		orderItem.delete()



	return JsonResponse('Item was added', safe = False)



def confirmOrder(request):
	

	customer = request.user.customer
	order, created = Order.objects.get_or_create(customer=customer, complete=False)
	order.delete()
	return render(request, 'product/placed_order.html')
