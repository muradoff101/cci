"""sergi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from main.views import *


urlpatterns = [
    path('', MainPageView.as_view(), name="main_page_link"),
    path('about/', AboutUsPageView.as_view(), name="aboutus_page_link"),
    path('contacts/', ContactsPageView.as_view(), name="contacts_page_link"),
    path('faq/', QuestionAnswerPageView.as_view(), name="faq_page_link"),
    path('benefits/', BenefitsPageView.as_view(), name="benefits_page_link"),
    path('exhibitions/', ExhibitionsListPageView.as_view(), name="exhibitions_page_link"),
    path('foreign-exhibitions/', ForeignExhibitionsListPageView.as_view(), name="foreign_exhibitions_page_link"),
    path('foreign-exhibitions/<int:pk>', ForeignExDetailPageView.as_view(), name="foreign_ex_detail_page_link"),
    path('tenders/', TendersListPageView.as_view(), name="tenders_page_link"),
    path('membership-joining/', MembershipJoiningPageView.as_view(), name="membership_joining_page_link"),
    path('news/', NewsListPageView.as_view(), name="news_page_link"),
    path('news/<int:pk>/', NewsDetailPageView.as_view(), name="news_detail_page_link"),
    path('turkmen-offer/', TurkmenOfferPageView.as_view(), name="turkmen_offer_page_link"),
    path('foreign-offer/', AbroadOfferPageView.as_view(), name="abroad_offer_page_link"),
    path('investment-projects/', InvestmentProjectsPageView.as_view(), name="investment_projects_page_link"),
    path('conferences/', ConferencesPageView.as_view(), name="conferences_page_link"),
    path('partners/', PartnersReestryView.as_view(), name="partners_registry_page_link"),
    path('investment-recipient/', InvestmentRecipientView.as_view(), name="investment_recipient_page_link"),
    path('investment-questionare/', InvestorQuestionnaireView.as_view(), name="investment_questionare_page_link"),
    path('baranches/<int:pk>', TppBranchesPageView.as_view(), name="branches_page_link"),
    path('services/', ServicesView.as_view(), name="services_page_link"),
    path('addresses/', AddressPageView.as_view(), name="address_page_link"),
    path('parcipants-events/', ParcipantEventsPageView.as_view(), name="parcipant_events_page_link"),

]
