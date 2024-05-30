from django.urls import path
from persons.views import main, SkillList, PersonAgeUpdateView

app_name = "persons" 
urlpatterns = [
    path("", main, name="main"),
    path("skills/", SkillList.as_view(), name="skills"),
    path("age_form/", PersonAgeUpdateView.as_view(), name="age_form"),
]