from .models import AboutSite

def about_site(request):
    about_sites = AboutSite.objects.first()

    ctx = {
        'about_sites': about_sites
    }
    return ctx