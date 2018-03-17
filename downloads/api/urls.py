from django.conf.urls import url,include
from .views import (
    BrochureList,
    PublicationList,
    RegisterationFormList,
    CTB_NewsletterList,
    ImportantDocumentList,
)

urlpatterns = [
    url(r'^brochure/list/$', BrochureList.as_view(), name = 'BrochureList'),
    url(r'^publication/list/$', PublicationList.as_view(), name = 'PublicationList'),
    url(r'^registration_form/list/$', RegisterationFormList.as_view(), name = 'RegisterationFormList'),
    url(r'^ctb_newsletter/list/$', CTB_NewsletterList.as_view(), name = 'CTBNewsletterList'),
    url(r'^important_document/list/$', ImportantDocumentList.as_view(), name = 'ImportantDocumentList'),
]