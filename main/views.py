from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from main.models import *
from main.functions import *
from sergi.settings import LANGUAGE_CODE
from django.utils.translation import get_language
from main.forms import ApplicationForm


from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.


class BaseListView(ListView):
    paginate_by = 15

    def dispatch(self, *args, **kwargs):
        # if not self.request.user.is_authenticated:
        #     return redirect('/login/')
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tpp_info'] = TPPInfo.objects.all()[:1]
        context['title'] = 'Title'
        return context


class MainPageView(BaseListView):
    template_name = 'index.html'
    context_object_name = 'sliders'
    queryset = MainSlider.objects.all().order_by('ordering')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if get_language() == 'ru':
            context["title"] = 'Главная | ТППТ'
        elif get_language() == 'tk':
            context["title"] = 'Baş sahypa | TSSE'
        elif get_language() == 'en':
            context["title"] = 'Main page | CCIT'
        context['news'] = News.objects.all().order_by('-date')[:3]
        context['tpp_news'] = TPPNews.objects.all().order_by('-date')[:3]
        context['exhibitions'] = Exhibitions.objects.all().order_by('-pk')[:3]
        context['partners'] = Partners.objects.all()
        context['virtimages'] = VirtualExpoImages.objects.all().order_by(
            'ordering')
        context['quote'] = Quotes.objects.last()
        context["gallery"] = Gallery.objects.all().order_by("-pk")[:10]
        context['banner'] = ReklamBanner.objects.get()
        return context


class AboutUsPageView(BaseListView):
    template_name = "about.html"
    context_object_name = "info"
    queryset = AboutUs.objects.all()[:1]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if get_language() == 'ru':
            context["title"] = 'О нас | ТППТ'
        elif get_language() == 'tk':
            context["title"] = 'Biza barada | TSSE'
        elif get_language() == 'en':
            context["title"] = 'About us | CCIT'
        return context


class ContactsPageView(BaseListView):
    template_name = "contact.html"
    context_object_name = "info"
    queryset = Contacts.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if get_language() == 'ru':
            context["title"] = 'Контакты | ТППТ'
        elif get_language() == 'tk':
            context["title"] = 'Habarlaşmak | TSSE'
        elif get_language() == 'en':
            context["title"] = 'Contacts | CCIT'
        return context


class QuestionAnswerPageView(BaseListView):
    template_name = "faq.html"
    context_object_name = "info"
    queryset = QuestionAnswer.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if get_language() == 'ru':
            context["title"] = 'Вопрос-ответ | ТППТ'
        elif get_language() == 'tk':
            context["title"] = 'Sorag-jogap  | TSSE'
        elif get_language() == 'en':
            context["title"] = 'FAQ | CCIT'
        return context


class BenefitsPageView(BaseListView):
    template_name = "benefits.html"
    context_object_name = "benefits"
    queryset = Benefits.objects.all()[:1]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if get_language() == 'ru':
            context["title"] = 'Преимущества сотрудничества | ТППТ'
        elif get_language() == 'tk':
            context["title"] = 'Agzalygyň peýdalygy  | TSSE'
        elif get_language() == 'en':
            context["title"] = 'Membership benefits | CCIT'
        return context


class MembershipJoiningPageView(BaseListView):
    template_name = "membership_joining.html"
    context_object_name = "benefits"
    queryset = MembershipJoining.objects.all()[:1]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Agza bolmak | TSSE'
        if get_language() == 'ru':
            context["title"] = 'Начать сотрудничество | ТППТ'
        elif get_language() == 'tk':
            context["title"] = 'Agzalyga girmek  | TSSE'
        elif get_language() == 'en':
            context["title"] = 'Joining the membership | CCIT'
        return context


class TurkmenOfferPageView(BaseListView):
    template_name = "tm_commercial_offer.html"
    context_object_name = "offers"
    queryset = TurkmenCommercialOffers.objects.all().order_by('offer_num')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if get_language() == 'ru':
            context["title"] = 'Коммерческие предложения производителей Туркменистана | ТППТ'
        elif get_language() == 'tk':
            context["title"] = 'Türkmenistanly önüm öndürijileriň söwda teklipleri  | TSSE'
        elif get_language() == 'en':
            context["title"] = 'Commercial offers of manufacturers of Turkmenistan | CCIT'
        return context


class PartnersReestryView(BaseListView):
    template_name = "partners_list.html"
    context_object_name = "partners"
    paginate_by = 10
    queryset = PartnersRegistry.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if get_language() == 'ru':
            context["title"] = 'Реестр надежных партнеров | ТППТ'
        elif get_language() == 'tk':
            context["title"] = 'Yhtybarly işewür hyzmatdaşlary  | TSSE'
        elif get_language() == 'en':
            context["title"] = 'Reliable partnes registry | CCIT'
        return context


class AbroadOfferPageView(BaseListView):
    template_name = "foreign_commercial_offer.html"
    context_object_name = "offers"
    queryset = ForeignCommercialOffers.objects.all().order_by("offer_num")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if get_language() == 'ru':
            context["title"] = 'Коммерческие предложения зарубежных партнеров | ТППТ'
        elif get_language() == 'tk':
            context["title"] = 'Daşary ýurtly hyzmatdaşlaryň söwda teklipleri | TSSE'
        elif get_language() == 'en':
            context["title"] = 'Commercial offers of foreign partners | CCIT'
        return context


class InvestmentProjectsPageView(BaseListView):
    template_name = "empty.html"
    context_object_name = "info"
    queryset = MembershipJoining.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Agza bolmak | TSSE'
        return context


class ParcipantEventsPageView(BaseListView):
    template_name = "parcipant_events.html"
    context_object_name = "info"
    queryset = ParcipantEvents.objects.all()[:1]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if get_language() == 'ru':
            context["title"] = 'Начать сотрудничество | ТППТ'
        elif get_language() == 'tk':
            context["title"] = 'Agzalyga girmek  | TSSE'
        elif get_language() == 'en':
            context["title"] = 'Joining the membership | CCIT'
        return context


class ConferencesPageView(BaseListView):
    template_name = "empty.html"
    context_object_name = "info"
    queryset = MembershipJoining.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Agza bolmak | TSSE'
        return context


class ExhibitionsListPageView(BaseListView):
    template_name = "exhibition_list.html"
    context_object_name = "exhibitions"
    queryset = Exhibitions.objects.all().order_by('from_date')
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if get_language() == 'ru':
            context["title"] = 'Выставки | ТППТ'
        elif get_language() == 'tk':
            context["title"] = 'Sergiler  | TSSE'
        elif get_language() == 'en':
            context["title"] = 'Exhibitions | CCIT'
        return context


class ForeignExhibitionsListPageView(BaseListView):
    template_name = "foreign_exhibition_list.html"
    context_object_name = "exhibitions"
    queryset = ForeignExhibitions.objects.all().order_by('from_date')
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if get_language() == 'ru':
            context["title"] = 'Календарь выставок | ТППТ'
        elif get_language() == 'tk':
            context["title"] = 'Sergileriň sanawy  | TSSE'
        elif get_language() == 'en':
            context["title"] = 'Exhibitions list | CCIT'
        return context


class TendersListPageView(BaseListView):
    template_name = "tenders_list.html"
    context_object_name = "tenders"
    queryset = Tenders.objects.all()
    paginate_by = 25

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if get_language() == 'ru':
            context["title"] = 'Тендеры | ТППТ'
        elif get_language() == 'tk':
            context["title"] = 'Bäsleşikler  | TSSE'
        elif get_language() == 'en':
            context["title"] = 'Tenders | CCIT'
        return context


class NewsListPageView(BaseListView):
    template_name = "news.html"
    context_object_name = "news"
    queryset = News.objects.all().order_by('-date')
    paginate_by = 25

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Täzelikler | TSSE'
        return context


class NewsDetailPageView(DetailView):
    template_name = "news_detail.html"
    context_object_name = "news"

    def get_object(self):
        pk = self.kwargs.get('pk')
        obj = get_object_or_404(News, pk=pk)
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Täzelikler | TSSE'
        context['tpp_info'] = TPPInfo.objects.all()[:1]
        return context


class TppBranchesPageView(DetailView):
    template_name = "branches.html"
    context_object_name = "info"

    def get_object(self):
        pk = self.kwargs.get('pk')
        obj = get_object_or_404(TppBranches, pk=pk)
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Birlikleri | TSSE'
        context['tpp_info'] = TPPInfo.objects.all()[:1]
        return context


class ForeignExDetailPageView(DetailView):
    template_name = "foreign_ex_detail.html"
    context_object_name = "ex"

    def get_object(self):
        pk = self.kwargs.get('pk')
        obj = get_object_or_404(ForeignExhibitions, pk=pk)
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Täzelikler | TSSE'
        context['tpp_info'] = TPPInfo.objects.all()[:1]
        return context


class InvestmentRecipientView(BaseListView):
    template_name = "investment_recipient.html"
    context_object_name = "info"
    queryset = InvestmentRecipient.objects.all()
    form_class = ApplicationForm

    def post(self, request, *args, **kwargs):
        # if self.form.is_valid():

        subject = self.form.cleaned_data['subject']
        from_email = self.form.cleaned_data['from_email']
        message = self.form.cleaned_data['message']
        try:
            send_mail(f'{subject} от {from_email}', message,
                      from_email, 'conference@cci.gov.tm')
            return redirect('investment_recipient_page_link')
        except BadHeaderError:
            return redirect('investment_recipient_page_link')
        return redirect('investment_recipient_page_link')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if get_language() == 'ru':
            context["title"] = 'Анкета соискателя | ТППТ'
        elif get_language() == 'tk':
            context["title"] = 'Maýa goýujylaryň sowalnamasy  | TSSE'
        elif get_language() == 'en':
            context["title"] = 'Application form | CCIT'

        context['form'] = self.form_class
        return context


class InvestorQuestionnaireView(BaseListView):
    template_name = "investment_questionare.html"
    context_object_name = "info"
    queryset = InvestorQuestionnaire.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if get_language() == 'ru':
            context["title"] = 'Анкета инвестора | ТППТ'
        elif get_language() == 'tk':
            context["title"] = 'Maýa goýumdarlaryň sowalnamasy  | TSSE'
        elif get_language() == 'en':
            context["title"] = 'Investor questionnaire | CCIT'
        return context
        return context


class ServicesView(BaseListView):
    template_name = "services.html"
    context_object_name = "info"
    queryset = Services.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if get_language() == 'ru':
            context["title"] = 'Услуги | ТППТ'
        elif get_language() == 'tk':
            context["title"] = 'Hyzmatlar | TSSE'
        elif get_language() == 'en':
            context["title"] = 'Services | CCIT'
        return context


class AddressPageView(BaseListView):
    template_name = "address.html"
    context_object_name = "info"
    queryset = AddressToPeople.objects.all()[:1]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Agza bolmak | TSSE'
        if get_language() == 'ru':
            context["title"] = 'Начать сотрудничество | ТППТ'
        elif get_language() == 'tk':
            context["title"] = 'Agzalyga girmek  | TSSE'
        elif get_language() == 'en':
            context["title"] = 'Joining the membership | CCIT'
        return context


def SendMail(request):

    if request.method == 'GET':
        form = ApplicationForm()
    elif request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(f'{subject} от {from_email}', message,
                          settings.DEFAULT_FROM_EMAIL, settings.RECIPIENTS_EMAIL)
            except BadHeaderError:
                return HttpResponse('Ошибка в теме письма.')
            return redirect('investment_recipient_page_link')
