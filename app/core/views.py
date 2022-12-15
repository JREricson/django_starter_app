from django.shortcuts import render


def landing_page(request):
    return render(request, "core_landing_page.html", {})
