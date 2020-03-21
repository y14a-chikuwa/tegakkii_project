"""tegakkii_project URL Configuration

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

from django.conf.urls import url, static
# 追記（読み込むようにします） 
# https://qiita.com/tiruka/items/6f8d8e1039a2e8ed2b5e


from django.contrib import admin
from django.urls import path

# needs to be changed
import tegakkii.views as tegakkii_view




urlpatterns = [
    path('admin/', admin.site.urls),
    url('^welcome/', tegakkii_view.ViewForTegakkii.as_view())
]

# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 
