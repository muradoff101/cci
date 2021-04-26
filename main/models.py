from django.db import models
from datetime import datetime
from django.utils.html import mark_safe

# Create your models here.


class MainSlider(models.Model):
    image_tk = models.ImageField('Картинка (туркм.)', upload_to='slider/')
    image_ru = models.ImageField('Картинка (рус.)', upload_to='slider/')
    image_en = models.ImageField('Картинка (анг.)', upload_to='slider/')
    ordering = models.PositiveSmallIntegerField(
        default=1, verbose_name='Последовательность')

    class Meta:
        verbose_name = 'Слайдер'
        verbose_name_plural = 'Слайдеры'

    def __str__(self):
        return str(self.pk)

    def get_image(self):
        return mark_safe('<img src="%s" width="300" height="150" />' % (self.image_tk.url))
    get_image.short_description = 'Картинка слайдера'


class Months(models.Model):
    name_tk = models.CharField('Название (туркм.)', max_length=32, blank=False)
    name_ru = models.CharField('Название (рус.)', max_length=32, blank=False)
    name_en = models.CharField('Название (анг.)', max_length=32, blank=False)

    class Meta:
        verbose_name_plural = 'Месяца'
        verbose_name = 'Месяц'

    def __str__(self):
        return self.name_tk


class News(models.Model):
    title_tk = models.CharField(
        'Заголовок (туркм.)', max_length=255, blank=False)
    title_ru = models.CharField(
        'Заголовок (рус.)', max_length=255, blank=False)
    title_en = models.CharField(
        'Заголовок (анг.)', max_length=255, blank=False)
    desc_tk = models.TextField('Описание (туркм.)', blank=False)
    desc_ru = models.TextField('Описание (рус.)', blank=False)
    desc_en = models.TextField('Описание (анг.)', blank=False)
    image = models.ImageField(
        'Главная картинка', upload_to='news/', blank=False)
    date = models.DateField('Дата опубликования', default=datetime.now)
    month = models.ForeignKey(
        Months, verbose_name='Месяц опубликования', on_delete=models.PROTECT)
    slug = models.SlugField("Слаг")

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return self.title_tk

    def get_image(self):
        return mark_safe('<img src="%s" width="200" height="200" />' % (self.image.url))
    get_image.short_description = 'Картинка новостей'


class TPPNews(models.Model):
    title_tk = models.CharField(
        'Заголовок (туркм.)', max_length=255, blank=False)
    title_ru = models.CharField(
        'Заголовок (рус.)', max_length=255, blank=False)
    title_en = models.CharField(
        'Заголовок (анг.)', max_length=255, blank=False)
    desc_tk = models.TextField('Описание (туркм.)', blank=False)
    desc_ru = models.TextField('Описание (рус.)', blank=False)
    desc_en = models.TextField('Описание (анг.)', blank=False)
    image = models.ImageField(
        'Главная картинка', upload_to='tpp_news/', blank=False)
    date = models.DateField('Дата опубликования', default=datetime.now)
    month = models.ForeignKey(
        Months, verbose_name='Месяц опубликования', on_delete=models.PROTECT)
    slug = models.SlugField("Слаг")

    class Meta:
        verbose_name = 'Новость ТПП'
        verbose_name_plural = 'Новости ТПП'

    def __str__(self):
        return self.title_tk

    def get_image(self):
        return mark_safe('<img src="%s" width="200" height="200" />' % (self.image.url))
    get_image.short_description = 'Картинка новостей'


class Partners(models.Model):
    image = models.ImageField('Логотип', upload_to='partners/')

    class Meta:
        verbose_name_plural = 'Партнеры'
        verbose_name = 'Партнер'

    def __str__(self):
        return str(self.pk)

    def get_image(self):
        return mark_safe('<img src="%s" width="150" height="150" />' % (self.image.url))
    get_image.short_description = 'Логотипы партнеров'


class Exhibitions(models.Model):
    main_image = models.ImageField(
        upload_to='exhibitions/', verbose_name='Главная картинка', blank=True)
    title_tk = models.CharField(
        'Заголовок (туркм.)', max_length=255, blank=False)
    title_ru = models.CharField(
        'Заголовок (рус.)', max_length=255, blank=False)
    title_en = models.CharField(
        'Заголовок (анг.)', max_length=255, blank=False)
    desc_tk = models.TextField('Описание (туркм.)', blank=True, null=True)
    desc_ru = models.TextField('Описание (рус.)', blank=True, null=True)
    desc_en = models.TextField('Описание (анг.)', blank=True, null=True)
    # main_image = models.ImageField('Главная фотография', upload_to='exhibitions/main_images/', blank=True)
    slug = models.SlugField('Слаг', blank=False)
    virtual = models.BooleanField(
        default=False, verbose_name='Виртуальный тур')
    # installer_tk = models.CharField(
    #     max_length=255, null=True, verbose_name='Организаторы (туркм.)', blank=True)
    # installer_ru = models.CharField(
    #     max_length=255, null=True, verbose_name='Организаторы (рус.)', blank=True)
    # installer_en = models.CharField(
    #     max_length=255, null=True, verbose_name='Организаторы (анг.)', blank=True)
    from_date = models.DateField(
        verbose_name='С (дата)', null=True, blank=False)
    to_date = models.DateField(verbose_name='До (дата)', null=True, blank=True)

    class Meta:
        verbose_name = 'Выставка'
        verbose_name_plural = 'Выставки'

    def __str__(self):
        return self.title_ru

    # def get_image(self):
    #     return mark_safe('<img src="%s" width="150" height="150" />' % (self.main_image.url))
    # get_image.short_description = 'Картинка выставок'


class ExhibitionImages(models.Model):
    image = models.ImageField('Фотографии', upload_to='exhibitions/images/')
    exhibition = models.ForeignKey(
        Exhibitions, verbose_name='', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Выставки'
        verbose_name = 'Выставка'

    def __str__(self):
        return self.exhibition.title_tk


class ServicesTypes(models.Model):
    name_tk = models.CharField(
        'Название (туркм.)', max_length=128, blank=False)
    name_ru = models.CharField('Название (рус.)', max_length=128, blank=False)
    name_en = models.CharField('Название (анг.)', max_length=128, blank=False)

    class Meta:
        verbose_name = 'Вид услуги'
        verbose_name_plural = 'Виды услуг'

    def __str__(self):
        return self.name_tk


class Services(models.Model):
    name_tk = models.TextField('Название (анг.)', blank=False)
    name_ru = models.TextField('Название (рус.)', blank=False)
    name_en = models.TextField('Название (анг.)', blank=False)

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

    def __str__(self):
        return self.name_ru


class Activities(models.Model):
    name_tk = models.CharField(
        'Название (туркм.)', max_length=255, blank=False)
    name_ru = models.CharField('Название (рус.)', max_length=255, blank=False)
    name_en = models.CharField('Название (анг.)', max_length=255, blank=False)
    place_tk = models.CharField(
        'Место провождения (туркм.)', max_length=255, blank=False)
    place_ru = models.CharField(
        'Место провождения (рус.)', max_length=255, blank=False)
    place_en = models.CharField(
        'Место провождения (анг.)', max_length=255, blank=False)
    from_date = models.DateField('С какого', default=datetime.now)
    to_date = models.DateField('По какое', default=datetime.now)
    organizers_tk = models.CharField(
        'Организаторы (туркм.)', max_length=255, blank=False)
    organizers_ru = models.CharField(
        'Организаторы (рус.)', max_length=255, blank=False)
    organizers_en = models.CharField(
        'Организаторы (анг.)', max_length=255, blank=False)

    class Meta:
        verbose_name_plural = 'Мероприятия'
        verbose_name = 'Мероприятие'

    def __str__(self):
        return self.name_tk


class VirtualExpoImages(models.Model):
    image = models.ImageField(
        upload_to='virtualexpo/', verbose_name='Картинка')
    ordering = models.PositiveSmallIntegerField(
        default=1, verbose_name='Последовательность')

    class Meta:
        verbose_name_plural = "Картинки виртуальной экскурсии"
        verbose_name = "Картинка виртуальной экскурсии"

    def __str__(self):
        return str(self.pk)

    def get_image(self):
        return mark_safe('<img src="%s" width="250" height="150" />' % (self.image.url))
    get_image.short_description = 'Картинка виртуальной экскурсии'


class Quotes(models.Model):
    image = models.ImageField(upload_to='qoutes/', verbose_name='Картинка')
    title_tk = models.CharField(
        max_length=255, verbose_name='Заголовок (туркм.)')
    title_ru = models.CharField(
        max_length=255, verbose_name='Заголовок (рус.)')
    title_en = models.CharField(
        max_length=255, verbose_name='Заголовок (анг.)')
    text_tk = models.TextField(verbose_name='Текст (туркм.)')
    text_ru = models.TextField(verbose_name='Текст (рус.)')
    text_en = models.TextField(verbose_name='Текст (анг.)')

    class Meta:
        verbose_name = "Цитата"
        verbose_name_plural = "Цитаты"

    def __str__(self):
        return self.title_ru

    def get_image(self):
        return mark_safe('<img src="%s" width="200" height="150" />' % (self.image.url))
    get_image.short_description = 'Картинка цитаты'


class AboutUs(models.Model):
    main_image = models.ImageField(
        upload_to='about/', verbose_name='Главная картинка')
    about_tk = models.TextField(verbose_name='О нас (туркм.)')
    about_ru = models.TextField(verbose_name='О нас (рус.)')
    about_en = models.TextField(verbose_name='О нас (анг.)')
    first_image = models.ImageField(
        upload_to='about/', verbose_name='Первая картинка')
    second_image = models.ImageField(
        upload_to='about/', verbose_name='Вторая картинка')
    desc_tk = models.TextField(verbose_name='Описание (туркм.)')
    desc_ru = models.TextField(verbose_name='Описание (рус.)')
    desc_en = models.TextField(verbose_name='Описание (анг.)')

    class Meta:
        verbose_name_plural = "О нас"
        verbose_name = "О нас"

    def __str__(self):
        return self.about_ru

    def get_image(self):
        return mark_safe('<img src="%s" width="250" height="150" />' % (self.main_image.url))
    get_image.short_description = 'Картинка виртуальной экскурсии'


class Contacts(models.Model):
    phone = models.CharField(max_length=128, verbose_name='Телефон')
    faks = models.CharField(max_length=128, verbose_name='Факс')
    name_tk = models.CharField(
        'Название (туркм.)', max_length=255, blank=True, default="")
    name_ru = models.CharField(
        'Название (рус.)', max_length=255, blank=True, default="")
    name_en = models.CharField(
        'Название (анг.)', max_length=255, blank=True, default="")
    address_tk = models.CharField(
        max_length=255, verbose_name='Адрес (туркм.)')
    address_ru = models.CharField(max_length=255, verbose_name='Адрес (рус.)')
    address_en = models.CharField(max_length=255, verbose_name='Адрес (анг.)')

    name_tk1 = models.CharField(
        'Название (туркм.)', max_length=255, blank=True, default="")
    name_ru1 = models.CharField(
        'Название (рус.)', max_length=255, blank=True, default="")
    name_en1 = models.CharField(
        'Название (анг.)', max_length=255, blank=True, default="")
    phone2 = models.CharField(
        max_length=128, verbose_name='Телефон ВЭС', default="")
    faks2 = models.CharField(
        max_length=128, verbose_name='Факс ВЭС',  default="")
    name_tk3 = models.CharField(
        'Название (туркм.)', max_length=255, blank=True, default="")
    name_ru3 = models.CharField(
        'Название (рус.)', max_length=255, blank=True, default="")
    name_en3 = models.CharField(
        'Название (анг.)', max_length=255, blank=True, default="")
    phone3 = models.CharField(
        max_length=128, verbose_name='Телефон Выставочный отдел', default="")
    faks3 = models.CharField(
        max_length=128, verbose_name='Факс Выставочный отдел',  default="")
    # address_tk2 = models.CharField(
    #     max_length=255, verbose_name='Адрес ВЭС(туркм.)',  default="")
    # address_ru2 = models.CharField(
    #     max_length=255, verbose_name='Адрес ВЭС(рус.)',  default="")
    # address_en2 = models.CharField(
    #     max_length=255, verbose_name='Адрес ВЭС(анг.)', default="")

    email = models.EmailField(
        max_length=254, verbose_name='Электронная почта 1')
    email2 = models.EmailField(
        max_length=254, verbose_name='Электронная почта ВЭС', default="")
    email3 = models.EmailField(
        max_length=254, verbose_name='Электронная почта Выставочный отдел', default="")
    website = models.CharField(max_length=254, verbose_name='Веб сайт')

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"

    def __str__(self):
        return self.phone


class QuestionAnswer(models.Model):
    question_tk = models.CharField(
        max_length=255, verbose_name='Вопросы (туркм.)')
    question_ru = models.CharField(
        max_length=255, verbose_name='Вопросы (рус.)')
    question_en = models.CharField(
        max_length=255, verbose_name='Вопросы (анг.)')
    answer_tk = models.TextField(verbose_name='Ответы (туркм.)')
    answer_ru = models.TextField(verbose_name='Ответы (рус.)')
    answer_en = models.TextField(verbose_name='Ответы (анг.)')

    class Meta:
        verbose_name_plural = "Вопросы-ответы"
        verbose_name = "Вопрос-ответ"

    def __str__(self):
        return self.question_ru


class Benefits(models.Model):
    desc_tk = models.TextField(verbose_name="Преимущества (туркм.)")
    desc_ru = models.TextField(verbose_name="Преимущества (рус.)")
    desc_en = models.TextField(verbose_name="Преимущества (анг.)")

    class Meta:
        verbose_name = "Преимущество"
        verbose_name_plural = "Преимущества"

    def __str__(self):
        return self.desc_ru

# class TppAdvantages(models.Model):
#     advantage_tk = models.TextField(verbose_name='Преимущества (туркм.)')
#     advantage_ru = models.TextField(verbose_name='Преимущества (рус.)')
#     advantage_en = models.TextField(verbose_name='Преимущества (анг.)')
#
#     class Meta:
#         verbose_name_plural = "Преимущества"
#         verbose_name = "Преимущество"
#
#     def __str__(self):
#         return self.advantage_ru


class ForeignExhibitions(models.Model):
    main_image = models.ImageField(
        upload_to='foreign_exhibitions/', verbose_name='Главная картинка', blank=True)
    name_tk = models.CharField(
        max_length=255, verbose_name='Название (туркм.)')
    name_ru = models.CharField(max_length=255, verbose_name='Название (рус.)')
    name_en = models.CharField(max_length=255, verbose_name='Название (анг.)')
    desc_tk = models.TextField(verbose_name='Описание (туркм.)', blank=True)
    desc_ru = models.TextField(verbose_name='Описание (рус.)', blank=True)
    desc_en = models.TextField(verbose_name='Описание (анг.)', blank=True)
    slug = models.SlugField(default='', verbose_name='Слаг')
    from_date = models.DateField('С какого', default=datetime.now, blank=False)
    to_date = models.DateField('По какое', default=datetime.now, blank=True)

    class Meta:
        verbose_name = "Зарубежная выставка"
        verbose_name_plural = "Зарубежные выставки"

    def __str__(self):
        return self.name_ru

    # def get_image(self):
    #     return mark_safe('<img src="%s" width="250" height="150" />' % (self.main_image.url))
    # get_image.short_description = 'Картинка зарубежной выставки'


class Tenders(models.Model):
    name_tk = models.CharField(
        'Название (туркм.)', max_length=255, blank=False)
    name_ru = models.CharField('Название (рус.)', max_length=255, blank=False)
    name_en = models.CharField('Название (анг.)', max_length=255, blank=False)
    desc_tk = models.TextField(verbose_name='Описание (туркм.)')
    desc_ru = models.TextField(verbose_name='Описание (рус.)')
    desc_en = models.TextField(verbose_name='Описание (анг.)')
    date = models.DateField('Kакого', default=datetime.now)
    # to_date = models.DateField('По какое')
    organizers_tk = models.CharField(
        'Организаторы (туркм.)', max_length=255, blank=False)
    organizers_ru = models.CharField(
        'Организаторы (рус.)', max_length=255, blank=False)
    organizers_en = models.CharField(
        'Организаторы (анг.)', max_length=255, blank=False)
    # main_image = models.ImageField("Главная картинка", upload_to="tenders/")

    class Meta:
        verbose_name_plural = 'Тендеры'
        verbose_name = 'Тендер'

    def __str__(self):
        return self.name_ru


class MembershipJoining(models.Model):
    desc_tk = models.TextField(
        verbose_name='Описание (туркм.)', max_length=2000)
    desc_ru = models.TextField(verbose_name='Описание (рус.)', max_length=2000)
    desc_en = models.TextField(verbose_name='Описание (анг.)', max_length=2000)
    anketa_tk = models.FileField(
        verbose_name="Анкета (туркм.)", upload_to="membership_application/")
    anketa_ru = models.FileField(
        verbose_name="Анкета (рус.)", upload_to="membership_application/")
    anketa_en = models.FileField(
        verbose_name="Анкета (анг.)", upload_to="membership_application/")

    class Meta:
        verbose_name_plural = "Вступление в членство"
        verbose_name = "Вступление в членство"

    def __str__(self):
        return self.desc_ru


class TppBranches(models.Model):
    name_tk = models.CharField(
        'Название (туркм.)', max_length=255, blank=False)
    name_ru = models.CharField('Название (рус.)', max_length=255, blank=False)
    name_en = models.CharField('Название (анг.)', max_length=255, blank=False)
    address_tk = models.CharField(
        max_length=255, verbose_name='Адрес (туркм.)')
    address_ru = models.CharField(max_length=255, verbose_name='Адрес (рус.)')
    address_en = models.CharField(max_length=255, verbose_name='Адрес (анг.)')
    desc_tk = models.TextField(verbose_name='Описание (туркм.)')
    desc_ru = models.TextField(verbose_name='Описание (рус.)')
    desc_en = models.TextField(verbose_name='Описание (анг.)')
    phone = models.CharField("Тел.", max_length=32)
    fax = models.CharField("Факс", max_length=32)
    email = models.EmailField("E-mail", blank=True, null=True)
    email2 = models.EmailField("E-mail 2", blank=True, null=True)

    class Meta:
        verbose_name_plural = "Подразделения ТПП"
        verbose_name = "Подразделение ТПП"

    def __str__(self):
        return self.name_ru


class ReklamBanner(models.Model):
    image_tk = models.ImageField("Картинка (туркм.)", upload_to="banners/")
    image_ru = models.ImageField("Картинка (рус.)", upload_to="banners/")
    image_en = models.ImageField("Картинка (анг.)", upload_to="banners/")

    class Meta:
        verbose_name = "Рекламный баннер"
        verbose_name_plural = "Рекламные баннера"

    def __str__(self):
        return str(self.pk)

    def get_image(self):
        return mark_safe('<img src="%s" width="450" height="150" />' % (self.image_tk.url))
    get_image.short_description = 'Картинка баннера'


class PartnersRegistry(models.Model):
    name_tk = models.CharField(
        'Название (туркм.)', max_length=255, blank=False)
    name_ru = models.CharField('Название (рус.)', max_length=255, blank=False)
    name_en = models.CharField('Название (анг.)', max_length=255, blank=False)
    address_tk = models.CharField(
        max_length=255, verbose_name='Адрес (туркм.)')
    address_ru = models.CharField(max_length=255, verbose_name='Адрес (рус.)')
    address_en = models.CharField(max_length=255, verbose_name='Адрес (анг.)')
    phone = models.CharField(max_length=128, verbose_name='Телефон')
    faks = models.CharField(max_length=128, verbose_name='Факс')
    email = models.EmailField(
        max_length=254, verbose_name='Электронная почта', blank=True)
    website = models.CharField(
        max_length=254, verbose_name='Веб сайт', blank=True)
    activity_tk = models.CharField(
        'Сфера деятельности (туркм.)', max_length=255, blank=False)
    activity_ru = models.CharField(
        'Сфера деятельности (рус.)', max_length=255, blank=False)
    activity_en = models.CharField(
        'Сфера деятельности (анг.)', max_length=255, blank=False)
    logo = models.ImageField(
        'Логотип', upload_to='partners_registry/', blank=False)

    class Meta:
        verbose_name = "Партнер"
        verbose_name_plural = "Реестр партнеров"

    def __str__(self):
        return str(self.pk)

    def get_image(self):
        return mark_safe('<img src="%s" width="250" height="150" />' % (self.logo.url))
    get_image.short_description = 'Логотип'


class InvestmentRecipient(models.Model):
    desc_tk = models.TextField('Описание (туркм.)', blank=False)
    desc_ru = models.TextField('Описание (рус.)', blank=False)
    desc_en = models.TextField('Описание (анг.)', blank=False)
    anketa_tk = models.FileField(
        verbose_name="Анкета (туркм.)", upload_to="investment_recipient/")
    anketa_ru = models.FileField(
        verbose_name="Анкета (рус.)", upload_to="investment_recipient/")
    anketa_en = models.FileField(
        verbose_name="Анкета (анг.)", upload_to="investment_recipient/")

    class Meta:
        verbose_name_plural = "Анкета соискателя"
        verbose_name = "Анкета соискателя"

    def __str__(self):
        return self.desc_ru


class InvestorQuestionnaire(models.Model):
    desc_tk = models.TextField('Описание (туркм.)', blank=False)
    desc_ru = models.TextField('Описание (рус.)', blank=False)
    desc_en = models.TextField('Описание (анг.)', blank=False)
    anketa_tk = models.FileField(
        verbose_name="Анкета (туркм.)", upload_to="investment_questionnaire/")
    anketa_ru = models.FileField(
        verbose_name="Анкета (рус.)", upload_to="investment_questionnaire/")
    anketa_en = models.FileField(
        verbose_name="Анкета (анг.)", upload_to="investment_questionnaire/")

    class Meta:
        verbose_name_plural = "Анкета инвестора"
        verbose_name = "Анкета инвестора"

    def __str__(self):
        return self.desc_ru


class TurkmenCommercialOffers(models.Model):
    main_image = models.ImageField(
        upload_to='turkmencommercialoffers/', verbose_name='Главная картинка', blank=True)
    offer_num = models.PositiveSmallIntegerField("Номер предложения")
    name_tk = models.CharField(
        'Название (туркм.)', max_length=255, blank=False)
    name_ru = models.CharField('Название (рус.)', max_length=255, blank=False)
    name_en = models.CharField('Название (анг.)', max_length=255, blank=False)
    desc_tk = models.TextField('Описание (туркм.)', blank=False)
    desc_ru = models.TextField('Описание (рус.)', blank=False)
    desc_en = models.TextField('Описание (анг.)', blank=False)
    year = models.DecimalField("Год", max_digits=4, decimal_places=0)

    class Meta:
        verbose_name_plural = "Коммерческие предложения Туркменистана"
        verbose_name = "Коммерческое предложения Туркменистана"

    def __str__(self):
        return self.desc_ru


class ForeignCommercialOffers(models.Model):
    main_image = models.ImageField(
        "Главная картинка", upload_to="foreigncommercialoffers/", blank=True)
    offer_num = models.PositiveSmallIntegerField("Номер предложения")
    name_tk = models.CharField(
        'Название (туркм.)', max_length=255, blank=False)
    name_ru = models.CharField('Название (рус.)', max_length=255, blank=False)
    name_en = models.CharField('Название (анг.)', max_length=255, blank=False)
    desc_tk = models.TextField('Описание (туркм.)', blank=False)
    desc_ru = models.TextField('Описание (рус.)', blank=False)
    desc_en = models.TextField('Описание (анг.)', blank=False)
    year = models.DecimalField("Год", max_digits=4, decimal_places=0)
    country_tk = models.CharField(
        'Страна (туркм.)', max_length=255, blank=False)
    country_ru = models.CharField('Страна (рус.)', max_length=255, blank=False)
    country_en = models.CharField('Страна (анг.)', max_length=255, blank=False)

    class Meta:
        verbose_name_plural = "Зарубежные коммерческие предложения"
        verbose_name = "Зарубежные коммерческое предложения"

    def __str__(self):
        return self.desc_ru


class ParcipantEvents(models.Model):
    desc_tk = models.TextField('Описание (туркм.)', blank=False)
    desc_ru = models.TextField('Описание (рус.)', blank=False)
    desc_en = models.TextField('Описание (анг.)', blank=False)

    class Meta:
        verbose_name_plural = "Участникам мероприятий"
        verbose_name = "Участнику мероприятия"

    def __str__(self):
        return self.desc_ru


class TPPInfo(models.Model):
    phone = models.CharField("Телефон", max_length=32)
    email = models.EmailField("Электронная почта")
    address_tk = models.CharField(
        max_length=255, verbose_name='Адрес (туркм.)')
    address_ru = models.CharField(max_length=255, verbose_name='Адрес (рус.)')
    address_en = models.CharField(max_length=255, verbose_name='Адрес (анг.)')

    class Meta:
        verbose_name = "Информация"
        verbose_name_plural = "Информации"

    def __str__(self):
        return self.phone


class Gallery(models.Model):
    image = models.ImageField("Картинка", upload_to="gallery/")

    class Meta:
        verbose_name_plural = "Галерея"
        verbose_name = "Картинка"

    def __str__(self):
        return str(self.pk)

    def get_image(self):
        return mark_safe('<img src="%s" width="250" height="150" />' % (self.image.url))
    get_image.short_description = 'Картинка'


class AddressToPeople(models.Model):
    desc_tk = models.TextField('Описание (туркм.)', blank=False)
    desc_ru = models.TextField('Описание (рус.)', blank=False)
    desc_en = models.TextField('Описание (анг.)', blank=False)

    class Meta:
        verbose_name_plural = "Обращение"
        verbose_name = "Обращение"

    def __str__(self):
        return self.desc_ru
