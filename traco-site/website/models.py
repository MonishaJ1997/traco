from django.db import models



class SiteImage(models.Model):
    name = models.CharField(max_length=100)   # e.g. "hero_image"
    content_type = models.CharField(max_length=100)  # e.g. "image/png"
    image_data = models.BinaryField()         # actual image bytes
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class PageContent(models.Model):
    page = models.CharField(max_length=50)   # e.g. "home", "about", "blogs"
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=300, blank=True)
    body = models.TextField(blank=True)
    image = models.ForeignKey(SiteImage, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.page} - {self.title}"




class SiteLogo(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="logos/")

    def __str__(self):
        return self.name







from django.db import models

class RealTimeUser(models.Model):
    name = models.CharField(max_length=100)
    profile_image = models.ImageField(upload_to='users/')  # stored in MEDIA
    joined_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name




from django.db import models

class PromoImage(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='promo_images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title



from django.db import models

class StepIcon(models.Model):
    name = models.CharField(max_length=100)   # e.g., "Apply", "Assessment"
    icon = models.ImageField(upload_to="step_icons/")  # uploaded image

    def __str__(self):
        return self.name


class BusinessCard(models.Model):
    image = models.ImageField(upload_to='cards/')

    def __str__(self):
        return f"BusinessCard {self.id}"   # Convert id to string

from django.db import models

class Mission(models.Model):
    title = models.CharField(max_length=255, default="Our Mission")
    description = models.TextField()
    image = models.ImageField(upload_to="mission_images/")

    def __str__(self):
        return self.title


from django.db import models

class Vision(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to="vision/")

    def __str__(self):
        return self.title

class Feature(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    icon = models.ImageField(upload_to="feature_icons/", blank=True, null=True)

    def __str__(self):
        return self.title


from django.db import models

class Banner(models.Model):
    title = models.CharField(max_length=255, default="About")
    highlight = models.CharField(max_length=255, default="TRACO")  # highlighted part in green
    background = models.ImageField(upload_to="banners/")

    def __str__(self):
        return f"{self.title} {self.highlight}"





from django.db import models

class KnowledgeSection(models.Model):
    title = models.CharField(max_length=255, default="Don’t Just Gain info")
    highlight = models.CharField(max_length=255, default="Build Knowledge")
    description = models.TextField(default="Whether you’re a new investor or a market expert, we’ve got something for everyone at the TRACO blog")
    main_image = models.ImageField(upload_to="knowledge/")  # person image

    # Optional star icons (if you want dynamic upload)
    star_icon_top = models.ImageField(upload_to="knowledge/icons/", blank=True, null=True)
    star_icon_bottom = models.ImageField(upload_to="knowledge/icons/", blank=True, null=True)

    def __str__(self):
        return f"{self.title} - {self.highlight}"


from django.db import models

class Section(models.Model):
    name = models.CharField(max_length=100)   # Example: Stocks, Mutual Funds, Personal Finance, Futures & Options

    def __str__(self):
        return self.name


class Card(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name="cards")
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200, blank=True, null=True)
    read_time = models.CharField(max_length=50)   # Example: "5 Mins Read"
    date = models.DateField()
    image = models.ImageField(upload_to="cards/")
    description = models.TextField()

    def __str__(self):
        return self.title

from django.db import models

class PartnerBanner(models.Model):
    title = models.CharField(max_length=200, default="Welcome to the First Step of Becoming a TRACO Partner")
    image = models.ImageField(upload_to="partners/")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


from django.db import models

class PartnerBenefit(models.Model):
    highlight_text = models.CharField(max_length=255, help_text="Text in bold green")
    description = models.TextField(help_text="Text below highlight")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.highlight_text[:50]


from django.db import models

class PartnerFeature(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.ImageField(upload_to="features/")  # upload icons
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


# core/models.py
from django.db import models

class Footer(models.Model):
    logo = models.ImageField(upload_to='logos/')
    facebook_link = models.URLField(blank=True, null=True)
    twitter_link = models.URLField(blank=True, null=True)
    instagram_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return "Footer Content"

from django.db import models

class SiteLogo(models.Model):
    image = models.ImageField(upload_to='logos/')
    alt_text = models.CharField(max_length=100, default='IT IRAO')

    def __str__(self):
        return self.alt_text


from django.db import models

class HeroSection(models.Model):
    heading = models.CharField(max_length=200)
    subheading = models.CharField(max_length=200, blank=True, null=True)
    right_image = models.ImageField(upload_to="hero/")

    def __str__(self):
        return self.heading


class HeroUser(models.Model):
    hero = models.ForeignKey(HeroSection, related_name="users", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="hero/users/")

    def __str__(self):
        return f"User for {self.hero.heading}"


        from django.db import models

class HighlightImage(models.Model):
    image = models.ImageField(upload_to="highlight/")
    background_color = models.CharField(max_length=50, default="#000000")  # hex or CSS color

    def __str__(self):
        return f"Highlight Image {self.id}"

# models.py
from django.db import models

class ImageAsset(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')  # Upload path inside MEDIA_ROOT

    def __str__(self):
        return self.title


from django.db import models

class BackgroundImage(models.Model):
    title = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='backgrounds/')  # File stored in media/backgrounds/

    def __str__(self):
        return self.title or "Background Image"



# dashboard/models.py
# dashboard/models.py

from django.db import models


class Account(models.Model):
    user = models.CharField(max_length=100)
    email = models.EmailField()
    avatar = models.ImageField(upload_to="avatars/", blank=True, null=True)

    # top cards
    balance = models.FloatField(default=0)
    equality = models.FloatField(default=0)
    risk_capital = models.FloatField(default=0)
    drawdown_limit = models.FloatField(default=0)
    evaluation = models.FloatField(default=15000)

    # donuts
    drawdown_used_pct = models.PositiveSmallIntegerField(default=25)   # used %
    goal_completed_pct = models.PositiveSmallIntegerField(default=11) # done %

    def __str__(self):
        return self.user

    @property
    def drawdown_left_pct(self):
        return 100 - self.drawdown_used_pct

    @property
    def goal_pending_pct(self):
        return 100 - self.goal_completed_pct


class MetricPoint(models.Model):
    """
    One row per month (or label) for the line chart
    """
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="metrics")
    order = models.PositiveSmallIntegerField(default=0)
    label = models.CharField(max_length=20)  # e.g. Jun, Jul
    balance = models.FloatField(default=0)   # green line
    equality = models.FloatField(default=0)  # red line

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return f"{self.account} - {self.label}"




