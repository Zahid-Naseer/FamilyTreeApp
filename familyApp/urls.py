from django.urls import path
from . import views

urlpatterns = [
    path('',                              views.landing,          name='landing'),
    path('register/',                     views.register_view,    name='register'),
    path('login/',                        views.login_view,       name='login'),
    path('logout/',                       views.logout_view,      name='logout'),
    path('home/',                         views.base,             name='base'),
    path('account/', views.account_settings, name='account_settings'),
    path('tree/',                         views.tree_view,        name='treeView'),
    path('add/',                          views.add_new_person,   name='addNew'),
    path('relationship/',                 views.add_relationship, name='addRelationship'),
    path('person/<int:person_id>/',       views.person_detail,    name='person_detail'),
    path('person/<int:person_id>/edit/',  views.edit_person,      name='editPerson'),
    path('person/<int:person_id>/claim/', views.claim_profile,    name='claimProfile'),
    path('person/<int:person_id>/delete/',views.delete_person,    name='deletePerson'),
    path('members/', views.family_members, name='family_members'),
    path('export/excel/', views.export_excel, name='export_excel'),
    path('export/pdf/',   views.export_pdf,   name='export_pdf'),
    path('marriages/', views.marriages_list, name='marriages_list'),
    path('marriages/<int:marriage_id>/delete/', views.delete_marriage, name='delete_marriage'),
    path('marriages/<int:marriage_id>/edit/', views.edit_marriage, name='edit_marriage'),
    
]