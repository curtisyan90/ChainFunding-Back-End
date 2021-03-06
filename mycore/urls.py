"""mycore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from allauth.account.views import confirm_email
from django.conf.urls import url

from rest_auth.views import PasswordResetConfirmView
from rest_auth.registration.views import VerifyEmailView
# mysearcher
from mysearcher.views import SearcherViewSet
from mywallet.views import WalletAddressViewSet, TransferLogsViewSet
from mynotice.views import NoticeViewSet
from myfundingprojects.views import FundingProjectsViewSet
# from myfundingprojects.views import UserFundingSharesViewSet
# from myfundingprojects.views import FundingProjectsViewSetAdmin
from mylikelists.views import UserLikeListsViewSet

from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

router = DefaultRouter(trailing_slash=False)
router.register('search', SearcherViewSet, 'search')
router.register('wallet', WalletAddressViewSet, 'wallet')
router.register('transferlog', TransferLogsViewSet, 'transferlog')
router.register('notice', NoticeViewSet, 'notice')
router.register('fundingprojects', FundingProjectsViewSet, 'fundingprojects')
router.register('likelist', UserLikeListsViewSet, 'likelist')

schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

# /<str:uidb64>/<str:token>
urlpatterns = [
    # Root
    path('', include(router.urls)),
    path('admin/', admin.site.urls),

    # Auth
    path('rest-auth/password/reset/confirm', PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    # path('rest-auth/registration/verify-email/(?P<key>.+)/$', VerifyEmailView.as_view(),
    #      name='account_confirm_email'),
    url(r'^rest-auth/', include('rest_auth.urls')),  # rest auth url
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),  # register url
    url(r'^account/', include('allauth.urls')),
    url(r'^accounts-rest/registration/account-confirm-email/(?P<key>.+)/$', confirm_email,
        name='account_confirm_email'),

    # Api view
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
