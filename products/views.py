# from django.shortcuts import render
#
# # Create your views here.
# def index(request):
#     context = {
#         'title': 'SAFA umbrella',
#         'is_promotion' : True,
#         'username' : 'valeriy',
#     }
#     return render(request,  'products/index.html', context)
#
# def products(request):
#     context = {
#         'title' : 'SAFA umbrella - Каталог',
#         'products' : [
#             {
#                 'image' : "/static/vendor/img/products/Adidas-hoodie.png",
#                 'name' : 'Зонт-трость SAFA umbrella',
#                 'price' : 6090,
#                 'description' : 'Прочные спицы, плотная ткань купола - что же еще нужно для счастья?. Стиль и комфорт – это образ жизни.',
#             },
#             {
#                 'image': "/static/vendor/img/products/Blue-jacket-The-North-Face.png",
#                 'name' : 'Серый зонт с видом на СПб',
#                 'price' : 3725,
#                 'description': 'Прочная ткань. Водонепроницаемое покрытие. Легкие и прочные спицы из стекловолокна.',
#             },
#             {
#                 'image': "/static/vendor/img/products/Brown-sports-oversized-top-ASOS-DESIGN.png",
#                 'name': 'Зонт "Paris"',
#                 'price': 2390,
#                 'description': 'Зонт-автомат. Купол из ткани эпонж. Имеет систему антиветер',
#             },
#             {
#                 'image': "/static/vendor/img/products/Black-Nike-Heritage-backpack.png",
#                 'name': 'Яркий, цветной зонт с достопримечательностями СПб',
#                 'price': 2340,
#                 'description': 'Плотная ткань. Легкий материал.',
#             },
#             {
#                 'image': "/static/vendor/img/products/Black-Dr-Martens-shoes.png",
#                 'name': 'Мужской зонт',
#                 'price': 3590,
#                 'description': 'Классический мужской зонт. Материал купола - эпонж.',
#             },
#             {
#                 'image': "/static/vendor/img/products/Dark-blue-wide-leg-ASOs-DESIGN-trousers.png",
#                 'name': 'Голубой зонт "Saint-Petersburg"',
#                 'price': 2890,
#                 'description': 'Легкая эластичная ткань. Прочные спицы из стекловолокна',
#             }
#         ]
#     }
#     return render(request, 'products/products.html',context)

from django.contrib.auth.decorators import login_required
from gjango.shortcuts import HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.views.generic.list impprt ListView

from common.views import TitleMixin
from products.models import Basket, Product, ProductCategory

class ProductsListView(TitleMixin, ListView):
    model = Product
    template_name = 'products/products.html'
    paginate_by = 3
    title = 'SAFA umbrella - Каталог'

    def get_queryset(self):
        queryset = super(ProductsListView, self).get_queryset()
        category_id = self.kwargs.get('category_id')
        return queryset.filter(category_id=category_id) if category_id else queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductsListView, self).get_context_data()
        context['categories'] = ProductCategory.objects.all()
        return context


@login_required
def basket_add(request, product_id):
    Basket.create_or_update(product_id, request.user)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

@login_required
def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


