from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import PageContent, SiteImage

def home(request):
    content = PageContent.objects.filter(page="home")
    return render(request, "website/home.html", {"contents": content})

def about(request):
    content = PageContent.objects.filter(page="about")
    return render(request, "website/about.html", {"contents": content})


def partner(request):
    content = PageContent.objects.filter(page="partner")
    return render(request, "website/partner.html", {"contents": content})


def profile(request):
    content = PageContent.objects.filter(page="profile")
    return render(request, "website/profile.html", {"contents": content})


def serve_image(request, pk):
    img = get_object_or_404(SiteImage, pk=pk)
    return HttpResponse(img.image_data, content_type=img.content_type)



#from .models import SiteLogo

#def home(request):
    #site_logo = SiteLogo.objects.first()   # get first logo from DB
    ##return render(request, "website/home.html", {"site_logo": site_logo})


#from django.shortcuts import render
#from .models import RealTimeUser

#def home(request):
    #users = RealTimeUser.objects.all()[:5]  # fetch 5 users for display
    #count = RealTimeUser.objects.count()
    #return render(request, "website/home.html", {"users": users, "count": count})

#from .models import PromoImage

#ef home(request):
    #promo = PromoImage.objects.last()  # Get the latest image
    #return render(request, 'website/home.html', {'promo': promo})





from django.shortcuts import render
from .models import Mission, Vision, Feature, Banner

def about(request):
    mission = Mission.objects.first()
    vision = Vision.objects.first()
    features = Feature.objects.all()
    banner = Banner.objects.first()
    return render(request, 'website/about.html', {
        "mission": mission,
        "vision": vision,
        "features": features,
        "banner": banner,
    })


from django.shortcuts import render
from .models import KnowledgeSection, Section


def blogs(request):
    sections_knowledge = KnowledgeSection.objects.all()
    stocks = Section.objects.filter(name="Stocks").first()
    mutualfunds = Section.objects.filter(name="Mutual Funds").first()
    personalfinance = Section.objects.filter(name="Personal Finance").first()
    futures = Section.objects.filter(name="Futures & Options").first()
  

    
    return render(
        request,
        'website/blogs.html',
        {
            "sections_knowledge": sections_knowledge,
            
            "stocks": stocks,
            "mutualfunds": mutualfunds,
            "personalfinance": personalfinance,
            "futures": futures,
            
        }
    )



from django.shortcuts import render
from .models import PartnerBanner, PartnerBenefit
from .models import PartnerFeature

def partner(request):
    banner = PartnerBanner.objects.first()
    benefit = PartnerBenefit.objects.filter(is_active=True).first()
    features = PartnerFeature.objects.filter(is_active=True)[:4]
    return render(
        request,
        "website/partner.html",
        {
            "banner": banner,
            "benefit": benefit,
            "features": features
        }
    )


# core/context_processors.py
#from .models import Footer

#def footer_context(request):
    #footer = Footer.objects.first()
    #return {"footer": footer}


# views.py
#from django.shortcuts import render

#def profile_view(request):
    #return render(request, 'profile.html')



from django.shortcuts import render
from .models import HeroSection
from .models import HighlightImage
from .models import PromoImage
from .models import StepIcon
from .models import BusinessCard
from .models import BackgroundImage
from .models import Account

from django.shortcuts import render
from .models import HeroSection, HighlightImage, PromoImage, StepIcon, BusinessCard, BackgroundImage, Account


def home(request):
    hero = HeroSection.objects.prefetch_related("users").first()
    highlight = HighlightImage.objects.first()
    promo = PromoImage.objects.last()
    icons = StepIcon.objects.all().order_by("id")
    cards = BusinessCard.objects.all()
    bg_img = BackgroundImage.objects.first()
    account = Account.objects.prefetch_related("metrics").first()

    if not account:
        # dummy fallback
        chart_json = {
            "labels": ["Jun", "Jul", "Aug", "Sep", "Oct"],
            "balance": [40, 80, 20, 70, 50],
            "equality": [20, 40, 40, 60, 90],
            "drawdown_used_pct": 25,
            "drawdown_left_pct": 75,
            "goal_completed_pct": 11,
            "goal_pending_pct": 89,
        }
        return render(request, "website/home.html", {"account": None, "chart_json": chart_json})

    labels = [m.label for m in account.metrics.all()]
    balance = [m.balance for m in account.metrics.all()]
    equality = [m.equality for m in account.metrics.all()]

    chart_json = {
        "labels": labels or ["Jun", "Jul", "Aug", "Sep", "Oct"],
        "balance": balance or [40, 80, 20, 70, 50],
        "equality": equality or [20, 40, 40, 60, 90],
        "drawdown_used_pct": account.drawdown_used_pct,
        "drawdown_left_pct": account.drawdown_left_pct,
        "goal_completed_pct": account.goal_completed_pct,
        "goal_pending_pct": account.goal_pending_pct,
    }
    return render(
        request,
        "website/home.html",
        {
            "hero": hero,
            "highlight": highlight,
            "promo": promo,
            "icons": icons,
            "cards": cards,
            "bg_img": bg_img,
            "account": account,
            "chart_json": chart_json,
           
        },
    )


# views.py
 





from django.shortcuts import render
from .models import ImageAsset

def profile(request):
    # Fetch the first image asset (e.g., the golden bull)
    image_asset = ImageAsset.objects.first()
    return render(request, 'website/profile.html', {'image_asset': image_asset})



