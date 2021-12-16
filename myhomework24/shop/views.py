from django.urls import reverse, reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from shop.forms import ShopForm, ReviewForm
from shop.models import Shop, Review

shop_list = ListView.as_view(
    model=Shop,
)

shop_detail = DetailView.as_view(
    model=Shop,
)


class ShopCreateView(CreateView):
    model = Shop
    form_class = ShopForm

    def get_success_url(self):
        shop_pk = self.object.pk
        return reverse("shop:shop_detail", args=[shop_pk])  # 문자열


shop_new = ShopCreateView.as_view()


class ShopUpdateView(UpdateView):
    model = Shop
    form_class = ShopForm

    def get_success_url(self):
        shop_pk = self.object.pk
        return reverse("shop:shop_detail", args=[shop_pk])


shop_edit = ShopUpdateView.as_view()

shop_delete = DeleteView.as_view(
    model=Shop,
    success_url=reverse_lazy("shop:shop_list"),
)


class ReviewCreateView(CreateView):
    model = Review
    form_class = ReviewForm

    def get_success_url(self):
        shop_pk = self.object.shop.pk
        return reverse("shop:shop_detail", args=[shop_pk])  # 문자열


review_new = ReviewCreateView.as_view()


class ReviewUpdateView(UpdateView):
    model = Review
    form_class = ReviewForm

    def get_success_url(self):
        shop_pk = self.object.shop.pk
        return reverse("shop:shop_detail", args=[shop_pk])


review_edit = ReviewUpdateView.as_view()

review_delete = DeleteView.as_view(
    model=Review,
    success_url=reverse_lazy("shop:shop_detail"),
)
