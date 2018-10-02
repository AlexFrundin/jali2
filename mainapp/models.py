from django.db import models
# Create your models here.


class Consultation(models.Model):

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
        verbose_name = 'Service'
        verbose_name_plural = 'Services`'

    def __str__(self):
        return self.s_title
        # return "%s" % self.code


    s_title =     models.CharField(' Service title',max_length=128)
    s_shortdesc = models.TextField(' Service short description')
    s_desc =      models.TextField(' Service full description')
    mp_icon = models.ImageField('Icon for Mainpage')
    sp_icon = models.FileField('Icon for Service page')


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
        verbose_name = 'Form section'
        verbose_name_plural = 'Form sections'

    def __str__(self):
        return self.s_name
        # return "%s" % self.code

    s_name = models.CharField('Name of the sections', max_length=128)


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
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews on the main page'

    def __str__(self):
        return self.title
        # return "%s" % self.code

    title = models.CharField('Review title', max_length=128)
    text_1 = models.TextField('Text 1')
    text_2 = models.TextField('Text 2')
    author_name = models.CharField('Author name', max_length=128)
    author_img = models.ImageField("Author img 120x120")


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
        verbose_name = 'News'
        verbose_name_plural = 'News'

    def __str__(self):
        return self.title
        # return "%s" % self.code

    title = models.CharField('News title', max_length=128)
    date = models.DateField(auto_now=True)
    short_desc = models.TextField('Short description')
    full_desc = models.TextField('Short description')
    image = models.ImageField('News image')
    on_main_page = models.BooleanField("On main page?", default=False)


class Page(models.Model):

    class Meta:
        verbose_name = 'Page'
        verbose_name_plural = 'Pages'

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
