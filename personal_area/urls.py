from django.urls import path
from . import views

app_name = 'personal_area'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('register/', views.RegistrationFormView.as_view(), name='register'),
    path('personal_area/', views.PersonalAreaView.as_view(), name='personal_area'),
    path('add_skills/', views.AddSkillsView.as_view(), name='add_skills'),
    path('add_hobbys/', views.AddHobbyView.as_view(), name='add_hobbys'),
    path('add_languages/', views.AddLanguageView.as_view(), name='add_languages'),
    path('edit_skills/<int:pk>/', views.EditUserSkillsView.as_view(), name='edit_skill'),
    path('edit_hobby/<int:pk>/', views.EditUserHobbyView.as_view(), name='edit_hobby'),
    path('edit_language/<int:pk>/', views.EditUserLanguagesView.as_view(), name='edit_language'),
]