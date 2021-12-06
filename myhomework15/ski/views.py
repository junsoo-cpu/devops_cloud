from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

from ski.models import Resort


def resort_list(request: HttpRequest) -> HttpResponse:
    qs = Resort.objects.all()
    # templates_name = "ski/resot_list.html"


    query = request.GET.get("query", "")
    if query:
        qs = qs.filter(name__icontains=query)

    context_data = {
        "resort_list": qs,
    }

    return render(request, "ski/resort_list.html", context_data)


def resort_detail(request: HttpRequest, pk=int) -> HttpResponse:
    resort = Resort.objects.get(pk=pk)
    context_data = {
        "resort": resort,
    }
    return render(request, "ski/resort_detail.html", context_data)
