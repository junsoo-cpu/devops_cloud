
from django.views.generic import (
    ListView,
    DetailView,

)



from shop.models import Shop

shop_list = ListView.as_view(
    model=Shop,
)

shop_detail = DetailView.as_view(
    model=Shop,
)