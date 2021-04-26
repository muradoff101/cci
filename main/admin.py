from django.contrib import admin
# from django.contrib.admin import forms
from django import forms

from main.models import *
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class NewsAdminForm(forms.ModelForm):
    desc_tk = forms.CharField(
        label="Описание (туркм.)", widget=CKEditorUploadingWidget())
    desc_ru = forms.CharField(label="Описание (рус.)",
                              widget=CKEditorUploadingWidget())
    desc_en = forms.CharField(label="Описание (анг.)",
                              widget=CKEditorUploadingWidget())

    class Meta:
        model = News
        fields = '__all__'


class TPPNewsAdminForm(forms.ModelForm):
    desc_tk = forms.CharField(
        label="Описание (туркм.)", widget=CKEditorUploadingWidget())
    desc_ru = forms.CharField(label="Описание (рус.)",
                              widget=CKEditorUploadingWidget())
    desc_en = forms.CharField(label="Описание (анг.)",
                              widget=CKEditorUploadingWidget())

    class Meta:
        model = TPPNews
        fields = '__all__'


class ExhibitionsAdminForm(forms.ModelForm):
    desc_tk = forms.CharField(
        label="Описание (туркм.)", widget=CKEditorUploadingWidget())
    desc_ru = forms.CharField(label="Описание (рус.)",
                              widget=CKEditorUploadingWidget())
    desc_en = forms.CharField(label="Описание (анг.)",
                              widget=CKEditorUploadingWidget())

    class Meta:
        model = Exhibitions
        fields = '__all__'


class ForeignExhibitionsAdminForm(forms.ModelForm):
    desc_tk = forms.CharField(
        label="Описание (туркм.)", widget=CKEditorUploadingWidget())
    desc_ru = forms.CharField(label="Описание (рус.)",
                              widget=CKEditorUploadingWidget())
    desc_en = forms.CharField(label="Описание (анг.)",
                              widget=CKEditorUploadingWidget())

    class Meta:
        model = ForeignExhibitions
        fields = '__all__'


class QuotesAdminForm(forms.ModelForm):
    text_tk = forms.CharField(
        label="Описание (туркм.)", widget=CKEditorUploadingWidget())
    text_ru = forms.CharField(label="Описание (рус.)",
                              widget=CKEditorUploadingWidget())
    text_en = forms.CharField(label="Описание (анг.)",
                              widget=CKEditorUploadingWidget())

    class Meta:
        model = Quotes
        fields = '__all__'


class AboutUsAdminForm(forms.ModelForm):
    about_tk = forms.CharField(
        label="О нас (туркм.)", widget=CKEditorUploadingWidget())
    about_ru = forms.CharField(
        label="О нас (рус.)", widget=CKEditorUploadingWidget())
    about_en = forms.CharField(
        label="О нас (анг.)", widget=CKEditorUploadingWidget())
    desc_tk = forms.CharField(
        label="Описание (туркм.)", widget=CKEditorUploadingWidget())
    desc_ru = forms.CharField(label="Описание (рус.)",
                              widget=CKEditorUploadingWidget())
    desc_en = forms.CharField(label="Описание (анг.)",
                              widget=CKEditorUploadingWidget())

    class Meta:
        model = Quotes
        fields = '__all__'


class QuestionAnswerAdminForm(forms.ModelForm):
    answer_tk = forms.CharField(
        label="Ответ (туркм.)", widget=CKEditorUploadingWidget())
    answer_ru = forms.CharField(
        label="Ответ (рус.)", widget=CKEditorUploadingWidget())
    answer_en = forms.CharField(
        label="Ответ (анг.)", widget=CKEditorUploadingWidget())

    class Meta:
        model = QuestionAnswer
        fields = '__all__'


class InvestmentRecipientAdminForm(forms.ModelForm):
    desc_tk = forms.CharField(
        label="Описание (туркм.)", widget=CKEditorUploadingWidget())
    desc_ru = forms.CharField(label="Описание (рус.)",
                              widget=CKEditorUploadingWidget())
    desc_en = forms.CharField(label="Описание (анг.)",
                              widget=CKEditorUploadingWidget())

    class Meta:
        model = InvestmentRecipient
        fields = '__all__'


class TurkmenCommercialOffersAdminForm(forms.ModelForm):
    desc_tk = forms.CharField(
        label="Описание (туркм.)", widget=CKEditorUploadingWidget())
    desc_ru = forms.CharField(label="Описание (рус.)",
                              widget=CKEditorUploadingWidget())
    desc_en = forms.CharField(label="Описание (анг.)",
                              widget=CKEditorUploadingWidget())

    class Meta:
        model = TurkmenCommercialOffers
        fields = '__all__'


class ForeignCommercialOffersAdminForm(forms.ModelForm):
    desc_tk = forms.CharField(
        label="Описание (туркм.)", widget=CKEditorUploadingWidget())
    desc_ru = forms.CharField(label="Описание (рус.)",
                              widget=CKEditorUploadingWidget())
    desc_en = forms.CharField(label="Описание (анг.)",
                              widget=CKEditorUploadingWidget())

    class Meta:
        model = ForeignCommercialOffers
        fields = '__all__'


class InvestorQuestionnaireAdminForm(forms.ModelForm):
    desc_tk = forms.CharField(
        label="Описание (туркм.)", widget=CKEditorUploadingWidget())
    desc_ru = forms.CharField(label="Описание (рус.)",
                              widget=CKEditorUploadingWidget())
    desc_en = forms.CharField(label="Описание (анг.)",
                              widget=CKEditorUploadingWidget())

    class Meta:
        model = InvestorQuestionnaire
        fields = '__all__'


class ParcipantEventsAdminForm(forms.ModelForm):
    desc_tk = forms.CharField(
        label="Описание (туркм.)", widget=CKEditorUploadingWidget())
    desc_ru = forms.CharField(label="Описание (рус.)",
                              widget=CKEditorUploadingWidget())
    desc_en = forms.CharField(label="Описание (анг.)",
                              widget=CKEditorUploadingWidget())

    class Meta:
        model = ParcipantEvents
        fields = '__all__'


class ServicesAdminForm(forms.ModelForm):
    name_tk = forms.CharField(
        label="Название (туркм.)", widget=CKEditorUploadingWidget())
    name_ru = forms.CharField(label="Название (рус.)",
                              widget=CKEditorUploadingWidget())
    name_en = forms.CharField(label="Название (анг.)",
                              widget=CKEditorUploadingWidget())

    class Meta:
        model = Services
        fields = '__all__'


class BenefitsAdminForm(forms.ModelForm):
    desc_tk = forms.CharField(
        label="Преимущества (туркм.)", widget=CKEditorUploadingWidget())
    desc_ru = forms.CharField(
        label="Преимущества (рус.)", widget=CKEditorUploadingWidget())
    desc_en = forms.CharField(
        label="Преимущества (анг.)", widget=CKEditorUploadingWidget())

    class Meta:
        model = Benefits
        fields = '__all__'


class TendersAdminForm(forms.ModelForm):
    desc_tk = forms.CharField(
        label="Описание (туркм.)", widget=CKEditorUploadingWidget())
    desc_ru = forms.CharField(label="Описание (рус.)",
                              widget=CKEditorUploadingWidget())
    desc_en = forms.CharField(label="Описание (анг.)",
                              widget=CKEditorUploadingWidget())

    class Meta:
        model = Tenders
        fields = '__all__'


class MembershipJoiningAdminForm(forms.ModelForm):
    desc_tk = forms.CharField(
        label="Описание (туркм.)", widget=CKEditorUploadingWidget())
    desc_ru = forms.CharField(label="Описание (рус.)",
                              widget=CKEditorUploadingWidget())
    desc_en = forms.CharField(label="Описание (анг.)",
                              widget=CKEditorUploadingWidget())

    class Meta:
        model = MembershipJoining
        fields = '__all__'


class TppBranchesAdminForm(forms.ModelForm):
    desc_tk = forms.CharField(
        label="Описание (туркм.)", widget=CKEditorUploadingWidget())
    desc_ru = forms.CharField(label="Описание (рус.)",
                              widget=CKEditorUploadingWidget())
    desc_en = forms.CharField(label="Описание (анг.)",
                              widget=CKEditorUploadingWidget())

    class Meta:
        model = TppBranches
        fields = '__all__'


class AddressToPeopleForm(forms.ModelForm):
    desc_tk = forms.CharField(
        label="Описание (туркм.)", widget=CKEditorUploadingWidget())
    desc_ru = forms.CharField(label="Описание (рус.)",
                              widget=CKEditorUploadingWidget())
    desc_en = forms.CharField(label="Описание (анг.)",
                              widget=CKEditorUploadingWidget())

    class Meta:
        model = AddressToPeople
        fields = '__all__'


# Register your models here.
@admin.register(MainSlider)
class AdminMainSlider(admin.ModelAdmin):
    list_display = ('get_image', "ordering", 'image_tk')


@admin.register(Months)
class AdminMonths(admin.ModelAdmin):
    list_display = ('name_tk', 'name_ru', 'name_en')


@admin.register(News)
class AdminNews(admin.ModelAdmin):
    list_display = ('get_image', 'title_tk', 'title_ru', 'date', 'month')
    list_filter = ('month',)
    prepopulated_fields = {"slug": ("title_en",)}
    list_per_page = 10
    form = NewsAdminForm


@admin.register(TPPNews)
class AdminTPPNews(admin.ModelAdmin):
    list_display = ('get_image', 'title_tk', 'title_ru', 'date', 'month')
    list_filter = ('month',)
    prepopulated_fields = {"slug": ("title_en",)}
    list_per_page = 10
    form = TPPNewsAdminForm


# @admin.register(ForeignNews)
# class AdminForeignNews(admin.ModelAdmin):
#     list_display = ('image', 'title_tk', 'title_ru', 'title_en', 'month')
#     list_filter = ('month',)


@admin.register(Partners)
class AdminPartners(admin.ModelAdmin):
    list_display = ('get_image', )
    list_per_page = 10


@admin.register(Exhibitions)
class AdminExhibitions(admin.ModelAdmin):
    list_display = ('title_ru', 'title_tk', "virtual")
    prepopulated_fields = {"slug": ("title_en",)}
    list_filter = ("virtual",)
    list_per_page = 15
    form = ExhibitionsAdminForm


@admin.register(ForeignExhibitions)
class AdminForeignExhibitions(admin.ModelAdmin):
    list_display = ("name_tk", "name_ru")
    prepopulated_fields = {"slug": ("name_en",)}
    list_per_page = 15
    form = ForeignExhibitionsAdminForm


@admin.register(VirtualExpoImages)
class AdminVirtualExpoImages(admin.ModelAdmin):
    list_display = ("get_image", "ordering")


@admin.register(Quotes)
class AdminQuotes(admin.ModelAdmin):
    list_display = ("get_image", "text_tk", "text_ru")
    form = QuotesAdminForm


@admin.register(AboutUs)
class AdminAboutUs(admin.ModelAdmin):
    list_display = ("get_image", "about_tk", "about_ru")
    form = AboutUsAdminForm


@admin.register(Contacts)
class AdminContacts(admin.ModelAdmin):
    list_display = ("phone", "faks", "address_tk", "email", "website")


@admin.register(QuestionAnswer)
class AdminQuestionAnswer(admin.ModelAdmin):
    list_display = ("question_tk", "answer_tk", )
    form = QuestionAnswerAdminForm

# @admin.register(TppAdvantages)
# class AdminTppAdvantages(admin.ModelAdmin):
#     list_display = ("advantage_tk", "advantage_ru")
#     form = AdvantagesAdminForm


@admin.register(Benefits)
class AdminBenefits(admin.ModelAdmin):
    list_display = ("desc_tk", "desc_ru")
    form = BenefitsAdminForm


@admin.register(Tenders)
class AdminTenders(admin.ModelAdmin):
    list_display = ("desc_tk", "desc_ru")
    form = TendersAdminForm
    save_on_top = True


@admin.register(MembershipJoining)
class AdminMembershipJoining(admin.ModelAdmin):
    list_display = ("desc_tk", "desc_ru")
    save_on_top = True
    form = MembershipJoiningAdminForm


@admin.register(TppBranches)
class AdminTppBranches(admin.ModelAdmin):
    list_display = ("name_tk", "address_tk", "phone", "fax")
    save_on_top = True
    form = TppBranchesAdminForm


@admin.register(ReklamBanner)
class AdminReklamBanner(admin.ModelAdmin):
    list_display = ("get_image", )


@admin.register(PartnersRegistry)
class AdminPartnersRegistry(admin.ModelAdmin):
    list_display = ("get_image", "name_tk", "phone", "faks")


@admin.register(InvestmentRecipient)
class AdminInvestmentRecipient(admin.ModelAdmin):
    list_display = ("desc_tk", "desc_ru")
    form = InvestmentRecipientAdminForm


@admin.register(InvestorQuestionnaire)
class AdminInvestorQuestionnaire(admin.ModelAdmin):
    list_display = ("desc_tk", "desc_ru")
    form = InvestorQuestionnaireAdminForm


@admin.register(Services)
class AdminServices(admin.ModelAdmin):
    list_display = ("pk", "name_tk")
    form = ServicesAdminForm


@admin.register(TurkmenCommercialOffers)
class AdminTurkmenCommercialOffers(admin.ModelAdmin):
    list_display = ("name_tk", "offer_num", "desc_tk")
    form = TurkmenCommercialOffersAdminForm


@admin.register(ForeignCommercialOffers)
class AdminTurkmenCommercialOffers(admin.ModelAdmin):
    list_display = ("name_tk", "offer_num", "desc_tk")
    form = ForeignCommercialOffersAdminForm


@admin.register(ParcipantEvents)
class AdminParcipantEvents(admin.ModelAdmin):
    list_display = ("desc_tk", "desc_ru")
    form = ParcipantEventsAdminForm


@admin.register(TPPInfo)
class AdminTPPInfo(admin.ModelAdmin):
    list_display = ("phone", "email", "address_tk")


@admin.register(Gallery)
class AdminGallery(admin.ModelAdmin):
    list_display = ("get_image", )
    list_per_page = 10


@admin.register(AddressToPeople)
class AdminAddressToPeople(admin.ModelAdmin):
    list_display = ("desc_ru", "desc_tk")
    form = AddressToPeopleForm


admin.site.site_header = 'Панель администратора'
