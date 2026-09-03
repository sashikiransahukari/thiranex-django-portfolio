from django.shortcuts import render
from .models import ContactMessage


def home(request):
    success_message = ""

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        if name and email and message:
            ContactMessage.objects.create(
                name=name,
                email=email,
                message=message
            )

            success_message = "Message sent successfully! Thank you for contacting me."

    return render(
        request,
        "portfolio_app/index.html",
        {
            "success_message": success_message
        }
    )