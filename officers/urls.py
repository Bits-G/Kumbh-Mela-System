# from django.urls import path
# from . import views

# urlpatterns = [
#     path('login/', views.admin_login, name='admin_login'),
#     path('logout/', views.admin_logout, name='admin_logout'),
#     path('kumbh-mela/', views.kumbh_mela_dashboard, name='kumbh_mela_dashboard'),

#     path('officers/', views.officer_list, name='officer_list'),
#     path('officers/add/', views.officer_add, name='officer_add'),
#     path('officers/<int:pk>/edit/', views.officer_edit, name='officer_edit'),
#     path('officers/<int:pk>/delete/', views.officer_delete, name='officer_delete'),
#     path('officers/<int:pk>/pdf/', views.generate_officer_pdf, name='officer_pdf'),

#     path('search/', views.search_officers, name='search_officers'),
# ]





from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.admin_login, name='admin_login'),
    path('logout/', views.admin_logout, name='admin_logout'),
    path('dashboard/', views.kumbh_mela_dashboard, name='kumbh_mela_dashboard'),
    path('officers/', views.officer_list, name='officer_list'),
    path('officers/add/', views.officer_add, name='officer_add'),
    path('officers/<int:pk>/edit/', views.officer_edit, name='officer_edit'),
    path('officers/<int:pk>/delete/', views.officer_delete, name='officer_delete'),
    path('officers/<int:pk>/pdf/', views.generate_officer_pdf, name='generate_officer_pdf'),
    path('officers/<int:pk>/qr/', views.officer_qr_code, name='officer_qr_code'),
    path('officers/import/', views.officer_import, name='officer_import'),
    path('search/', views.search_officers, name='search_officers'),
    path('search/pdf/', views.search_results_pdf, name='search_results_pdf'),
    path('search/qr/', views.search_results_qr, name='search_results_qr'),
]