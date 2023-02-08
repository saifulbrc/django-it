from django.shortcuts import render, HttpResponseRedirect
from django.views import View
from .models import Product, Category

class Home(View):
        def post(self,request):
            pass
        def get(self,request):
            return HttpResponseRedirect(f'/store{request.get_full_path()[1:]}')
def store(request):
            P= Product.get_all_products()
            C=Category.get_all_categories()
            data={}
            data['products']=P
            data['categories']=C
            return render(request,'itshop/index.html',data)
            