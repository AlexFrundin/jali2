from django.db import models
from django.utils.safestring import mark_safe
# Create your models here.


class Consultation(models.Model):
    class Meta:
        verbose_name = '1.Consultation'
        verbose_name_plural = '1.Consultations'

    name = models.CharField(max_length=128)
    phone = models.CharField(max_length=64)
    category = models.CharField(max_length=64)
    text = models.TextField()

    is_paid = models.BooleanField(default=False)
    def __str__(self):
        return self.phone

# Content

class MpHeadBlock1(models.Model):

    class Meta:
        verbose_name = 'Top slider'
        verbose_name_plural = 'Top slider'

    def __str__(self):
        return "Top slider"
        # return "%s" % self.code

    main_title = models.CharField('Main title',max_length=128)
    flink_name = models.CharField('First link name',max_length=128)
    flink_url = models.CharField('First link url',max_length=128)
    slink_name = models.CharField('Second link name',max_length=128)
    slink_url = models.CharField('Second link url',max_length=128)


class MpHead(models.Model):

    class Meta:
        verbose_name = 'Header vallue'
        verbose_name_plural = 'Header vallue'

    def __str__(self):
        return "Header vallue"
        # return "%s" % self.code

    tytle_1 = models.CharField('First element title',max_length=128)
    vallue1 = models.CharField('First element vallue',max_length=128)

    tytle_2 = models.CharField('Second element title',max_length=128)
    vallue2 = models.CharField('Second element vallue',max_length=128)

    tytle_3 = models.CharField('Third element title',max_length=128)
    vallue3 = models.CharField('Third element vallue',max_length=128)

    tytle_4 = models.CharField('Fourth element title',max_length=128)
    vallue4 = models.CharField('Fourth element vallue',max_length=128)


class Ticker(models.Model):

    class Meta:
        verbose_name = 'Ticker'
        verbose_name_plural = 'Tickers'

    def __str__(self):
        return self.ticker_text
        # return "%s" % self.code

    ticker_text = models.TextField("Ticker text")


class Services(models.Model):

    class Meta:
        verbose_name = '2.Service'
        verbose_name_plural = '2.Services`'

    def __str__(self):
        return self.s_title
        # return "%s" % self.code


    s_title =     models.CharField(' Service title',max_length=128)
    s_shortdesc = models.TextField(' Service short description')
    s_desc =      models.TextField(' Service full description')
    mp_icon = models.ImageField('Icon for Mainpage')
    sp_icon = models.FileField('Icon for Service page')

    def get_prev_icon(self):
        return mark_safe('<img src="{}" width="30" height="30" class="image"/>'.format(self.mp_icon.url))

    def get_prev_sp_icon(self):
        return mark_safe('<img src="{}" width="30" height="30" class="image"/>'.format(self.sp_icon.url))

    get_prev_sp_icon.short_description = u'SP_Icon'
    get_prev_icon.short_description = u'Icon'

class Services_section(models.Model):

    class Meta:
        verbose_name = 'Service section'
        verbose_name_plural = 'Service section'

    def __str__(self):
        return "Change services section title"
        # return "%s" % self.code

    f_title = models.CharField(' Main page< first service title', max_length=128)
    s_title = models.CharField(' Main page< second service title', max_length=128)
    link = models.CharField(' Main page< name link', max_length=30)


class Form_section(models.Model):

    class Meta:
        verbose_name = 'ConsultationOrder'
        verbose_name_plural = '6.ConsultationOrders'

    def __str__(self):
        return self.s_name

    s_name = models.CharField('Name of the sections', max_length=128)
    price = models.IntegerField(default=50)

class Scroll_menu_text(models.Model):

    class Meta:
        verbose_name = 'Scroll menu section'
        verbose_name_plural = 'Scroll menu sections'

    def __str__(self):
        return self.s_name
        # return "%s" % self.code

    s_name = models.CharField('Name of the item', max_length=128)
    s_text = models.TextField('Text')


class Review(models.Model):

    class Meta:
        verbose_name = '3.Review'
        verbose_name_plural = '3.Reviews on the main page'

    def __str__(self):
        return self.title
        # return "%s" % self.code

    title = models.CharField('Review title', max_length=128)
    text_1 = models.TextField('Text 1')
    text_2 = models.TextField('Text 2')
    author_name = models.CharField('Author name', max_length=128)
    author_img = models.ImageField("Author img 120x120")

    def get_prev(self):
        return mark_safe('<img src="{}" width="30" height="30" class="image"/>'.format(self.author_img.url))

    get_prev.short_description = "Image"


class Bottom_footer(models.Model):

    class Meta:
        verbose_name = 'Bottom footer'
        verbose_name_plural = 'Bottom footer'

    def __str__(self):
        return "Bottom footer items"
        # return "%s" % self.code

    item_1 = models.CharField('#1 item', max_length=128)
    item_2 = models.CharField('#2 item', max_length=128)
    item_3 = models.CharField('#3 item', max_length=128)


class News(models.Model):

    class Meta:
        verbose_name = '4.News'
        verbose_name_plural = '4.News'

    def __str__(self):
        return self.title
        # return "%s" % self.code

    title = models.CharField('News title', max_length=128)
    date = models.DateField(auto_now=True)
    short_desc = models.TextField('Short description')
    full_desc = models.TextField('Short description')
    image = models.ImageField('News image')
    on_main_page = models.BooleanField("On main page?", default=False)

    def get_prev(self):
        return mark_safe('<img src="{}" width="30" height="30" class="image"/>'.format(self.image.url))

    get_prev.short_description = u'Image'


class Page(models.Model):

    class Meta:
        verbose_name = '5.Page'
        verbose_name_plural = '5.Pages'

    def __str__(self):
        return self.title
        # return "%s" % self.code

    title = models.CharField('News title', max_length=128)
    link = models.CharField('Link name', max_length=128)
    full_desc = models.TextField('Short description')


class Slider2(models.Model):

    class Meta:
        verbose_name = 'Slider'
        verbose_name_plural = 'Sliders'

    def __str__(self):
        return self.title
        # return "%s" % self.code

    title = models.CharField('News title', max_length=128)
    url = models.CharField('Link address', max_length=128)
    full_desc = models.TextField('Text')
