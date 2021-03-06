from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from PIL import Image


def profile_image(request: HttpRequest) -> HttpResponse:
    canvas = Image.new("RGBA", (256, 256), (255, 0, 0, 255))

    response = HttpResponse(content_type="image/png")
    canvas.save(response, "PNG")

    return response


def login(request):
    pass


# signup = CreateView.as_view(
#     form_class=UserCreationForm,
#     success_url=reverse_lazy("accounts:login"),
#     template_name="accounts/signup_form.html",
# )

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("accounts:login")
    else:
        form = UserCreationForm()

    return render(request, "accounts/signup_form.html", {
        "form": form,
    })


def profile(request):
    pass


def logout(request):
    pass
