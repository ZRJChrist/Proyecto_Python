from django.urls import path
from . import views

urlpatterns = [
    path('members/', views.member_all, name='member_all'),
    path('members/new/', views.member_new, name='member_new'),
    path('members/<int:member_id>/edit/', views.member_edit, name='member_edit'),
    path('members/<int:member_id>/delete/', views.member_delete, name='member_delete'),
    
    path('courts/', views.court_all, name='court_all'),
    path('courts/new/', views.court_new, name='court_new'),
    path('courts/<int:court_id>/edit/', views.court_edit, name='court_edit'),
    path('courts/<int:court_id>/delete/', views.court_delete, name='court_delete'),

    path('books/', views.book_all, name='book_all'),
    path('books/new/', views.book_new, name='book_new'),
    path('books/<int:book_id>/edit/', views.book_edit, name='book_edit'),
    path('books/<int:book_id>/delete/', views.book_delete, name='book_delete'),
]