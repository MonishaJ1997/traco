




from django.contrib import admin
from .models import RealTimeUser

@admin.register(RealTimeUser)
class RealTimeUserAdmin(admin.ModelAdmin):
    list_display = ('name', 'joined_at')

from django.contrib import admin
from .models import PromoImage

admin.site.register(PromoImage)


from django.contrib import admin
from .models import StepIcon

admin.site.register(StepIcon)

from django.contrib import admin
from .models import BusinessCard

admin.site.register(BusinessCard)


from django.contrib import admin
from .models import Mission

@admin.register(Mission)
class MissionAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "image")   # show these in list view
    search_fields = ("title", "description")           # enable search

from django.contrib import admin
from .models import Vision

@admin.register(Vision)
class VisionAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "image")


from django.contrib import admin
from .models import Feature

@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ("title", "description")

from django.contrib import admin
from .models import Banner

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ("title", "highlight", "background")


from django.contrib import admin
from .models import KnowledgeSection

@admin.register(KnowledgeSection)
class KnowledgeAdmin(admin.ModelAdmin):
    list_display = ("title", "highlight", "main_image","star_icon_top","star_icon_bottom")



from django.contrib import admin
from .models import Section, Card

class CardInline(admin.TabularInline):
    model = Card
    extra = 1

class SectionAdmin(admin.ModelAdmin):
    inlines = [CardInline]

admin.site.register(Section, SectionAdmin)




from django.contrib import admin
from .models import PartnerBanner

@admin.register(PartnerBanner)
class PartnerBannerAdmin(admin.ModelAdmin):
    list_display = ("title", "is_active")
    list_filter = ("is_active",)
    search_fields = ("title",)

from django.contrib import admin
from .models import PartnerBenefit

@admin.register(PartnerBenefit)
class PartnerBenefitAdmin(admin.ModelAdmin):
    list_display = ("highlight_text", "is_active")
    list_filter = ("is_active",)
    search_fields = ("highlight_text",)


from django.contrib import admin
from .models import PartnerFeature

admin.site.register(PartnerFeature)


# core/admin.py
from django.contrib import admin
from .models import Footer

@admin.register(Footer)
class FooterAdmin(admin.ModelAdmin):
    list_display = ("id", "logo", "facebook_link", "twitter_link", "instagram_link")



from django.contrib import admin
from .models import SiteLogo
from django.utils.html import format_html

class SiteLogoAdmin(admin.ModelAdmin):
    list_display = ('alt_text', 'preview')

    def preview(self, obj):
        return format_html('<img src="{}" style="height:40px;" />', obj.image.url)

admin.site.register(SiteLogo, SiteLogoAdmin)

from django.contrib import admin
from .models import HeroSection, HeroUser

class HeroUserInline(admin.TabularInline):
    model = HeroUser
    extra = 1

@admin.register(HeroSection)
class HeroSectionAdmin(admin.ModelAdmin):
    inlines = [HeroUserInline]

admin.site.register(HeroUser)


from django.contrib import admin
from .models import HighlightImage

admin.site.register(HighlightImage)


from django.contrib import admin
from .models import ImageAsset

@admin.register(ImageAsset)
class ImageAssetAdmin(admin.ModelAdmin):
    list_display = ('title', 'image')


from django.contrib import admin
from .models import BackgroundImage

admin.site.register(BackgroundImage)


# dashboard/admin.py
from django.contrib import admin
from .models import Account, MetricPoint

class MetricPointInline(admin.TabularInline):
    model = MetricPoint
    extra = 1
    fields = ("order", "label", "balance", "equality")
    ordering = ("order",)

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = (
        "user", "email", "balance", "equality", "risk_capital",
        "drawdown_limit", "evaluation",
    )
    inlines = [MetricPointInline]

@admin.register(MetricPoint)
class MetricPointAdmin(admin.ModelAdmin):
    list_display = ("account", "order", "label", "balance", "equality")
    list_editable = ("order", "label", "balance", "equality")
    list_filter = ("account",)
    ordering = ("account", "order")




