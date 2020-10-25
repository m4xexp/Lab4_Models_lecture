from django.contrib import admin
from django.urls import path
from report import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="home"),
    path('ReportListAllReceipt', views.ReportListAllReceipts),
    path('ReportUnpaidInvoices', views.ReportUnpaidInvoices),
    path('ReportDateProductSold', views.ReportDateProductSold)
]
