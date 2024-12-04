from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Shortener


def redirect_to_original(request, short_code):
    # Redirect the short code to the original URL
    url = get_object_or_404(Shortener, short_code=short_code)
    return HttpResponseRedirect(url.original_url)


def main_page(request):
    # Handle form submission
    if request.method == "POST":
        original_url = request.POST.get("original_url")  # Get the submitted URL

        # Create a new Shortener object and generate short URL
        shortener = Shortener.objects.create(original_url=original_url)

        # Build full URL including short code
        full_shortened_url = request.build_absolute_uri(f"/{shortener.short_code}")

        # Pass the short URL to the same template for display
        return render(request, "short_url.html", {"short_url": full_shortened_url})

    # Render the form again for GET requests
    return render(request, "short_url.html")
