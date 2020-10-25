from django.contrib import admin
from django.urls import path
from report import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('ReportListAllReceipt', views.ReportListAllReceipts),
    path('ReportUnpaidInvoices', views.ReportUnpaidInvoices),
    path('ReportDateAmountReceived', views.ReportDateAmountReceived)
]
