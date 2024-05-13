from django.urls import path
from .views import NewCard, ResultView, CardView, PresentationView, ThankYouView, MessageView, InTouchView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', NewCard.as_view(), name='index'),
    path('<slug:user_slug>/', ResultView.as_view(), name='result'),
    path('<slug:user_slug>/card', CardView.as_view(), name='card'),
    path('<slug:user_slug>/presentation/', PresentationView.as_view(), name='presentation'),
    path('<slug:user_slug>/thank_you/', ThankYouView.as_view(), name='thank_you'),
    path('<slug:user_slug>/message/', MessageView.as_view(), name='message'),
    path('<slug:user_slug>/in_touch/', InTouchView.as_view(), name='in_touch'),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
