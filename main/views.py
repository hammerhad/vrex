from django.shortcuts import render

from .models import Category, Restaurant, Product, Model3D, MainPageMenu, Awards, Text3D


# creditentials = {
#       'Authorization': 'Bearer pat-eu1-e8184039-2b60-4f51-896b-049f08c824be',
#       'Content-Type': 'application/json'
#     }

# def createCustomer (request, name, email, *args):
# 	print('gamovida eg dedamotynuli')
# 	r = requests.post('https://api.hubapi.com/crm/v3/objects/contacts',headers= creditentials, json= {"properties": {
# 	  "company": "Biglytics",
# 	  "email": "bcooper@biglytics.net",
# 	  "firstname": "Bryan",
# 	  "lastname": "Cooper",
# 	  "phone": "(877) 929-0687",
# 	  "website": "biglytics.net"
# 	}})
# 	return render(request, 'home.html', {'r': r})

def home(request, id):
	restaurant = Restaurant.objects.get(id=id)
	context = {

		'title':'title2',
		'model1': Model3D.objects.get(name="First_Object"),
		'restaurant': restaurant,
		'models': Model3D.objects.filter(Restaurant_id=id),
		'model2': Model3D.objects.get(name="second_Object"),
		'model3': Model3D.objects.get(name="third_Object"),
		'model4': Model3D.objects.get(name="fourth_Object"),
		'MainPageMenu': MainPageMenu.objects.get(name="menu"),
		'restaurant': Restaurant.objects.get(slug="SlugRest"),
		'MainPageMenu2': MainPageMenu.objects.get(name="logo"),
		'd3text1': Text3D.objects.get(name="ceo"),
		'd3text2': Text3D.objects.get(name="meore"),
	}
	return render(request, 'main/home.html', context)

def restaurant(request, id):
    # retrieve the restaurant object with the given id
    restaurant = Restaurant.objects.get(id=id)
    awards = Awards.objects.filter(Restaurant_id=id)
    products = Product.objects.filter(Restaurant_id=id)
    
    # do something with the restaurant object...
    
    # render the response
    return render(request, 'main/tester.html', {'restaurant': restaurant, 'awards': awards, 'products': products})


def index(request):
	context = {

		# 'title':'title2',
		# 'products': Product.objects.all(),
		# 'categories': Category.objects.all(),

	}
	return render(request, 'main/index.html', context)

def menupage(request, id):
	restaurant = Restaurant.objects.get(id=id)
	context = {

		'title':'title2',
		'restaurant': restaurant,
		'products': Product.objects.all(),
		'categories': Category.objects.filter(Restaurant_id=id),

	}
	return render(request, 'main/menu.html', context)
