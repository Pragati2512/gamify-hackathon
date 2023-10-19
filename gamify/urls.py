from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static
#from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', include('home.urls', namespace="home")),
    path('admin/', admin.site.urls),

    # path('online/', include('person.urls', namespace="person")),
    # path('study/', include('study.urls', namespace="study")),
    # path('assignment/', include('assignment.urls', namespace="assignment")),

    # path('tests/', include('exam.urls', namespace="exam")),
    # path('trial/', include('result.urls', namespace="result")),
    # path('accounts/', include('django.contrib.auth.urls')), # new
    # path(
    #     'change-password/',
    #     auth_views.PasswordChangeView.as_view(
    #         template_name='change-password.html',
    #         success_url = '/'
    #     ),
    #     name='change_password'
    #),


 ]

#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
