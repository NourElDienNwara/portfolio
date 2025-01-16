from django.shortcuts import render


def handel404(request, exception):
    return render(request, "error404.html", status=404)


def handel500(request):
    return render(request, "error500.html", status=500)
