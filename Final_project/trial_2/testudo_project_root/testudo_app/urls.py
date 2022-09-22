from django.contrib import admin
from django.urls import path,include
from .views import homepage, save_to_list, search, search_gen_ed, search_core,department_link, list_professors, google_search,register, homepage_after_register,login, homepage_after_login,search_no_user,search_gen_ed_no_user,search_core_no_user,show_saved_courses

urlpatterns = [
    path('', homepage,name='homepage'),
    path('search/<str:user>',search, name='search'),
    path('gen_ed_serch/<str:user>', search_gen_ed, name='gen_ed_search'),
    path('core_search/<str:user>', search_core,name='core_search'),
    path('dept_click/<str:dept_id>/<str:user>',department_link,name='dept_click'),
    path('professors/<str:course_id>/<str:user>',list_professors,name='list_professors'),
    path('google_search/<str:name>',google_search, name='google_search'),
    path('register', register, name = 'register'),
    path('registered/<str:message>',homepage_after_register,name='homepage_with_message'),
    path('login', login, name='login'),
    path('homepage_after_login/<str:user>',homepage_after_login, name='homepage_after_login'),
    path('logout', homepage, name='logout'),
    path('search_no_user', search_no_user,name='search_no_user'),
    path('search_gen_ed_no_user',search_gen_ed_no_user, name='search_gen_ed_no_user'),
    path('search_core_no_user', search_core_no_user,name='search_core_no_user'),
    path('save/<str:user>/<str:course_id>', save_to_list,name='save_to_list' ),
    path('show_saved_courses/<str:user>',show_saved_courses,name='show_saved_courses'),
]
