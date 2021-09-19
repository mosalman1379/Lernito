from django.urls import path
from lesson.views import BookListView, ChapterListView

app_name = 'lesson'
urlpatterns = [
    path('book/', BookListView.as_view(), name='BookList'),
    path('chapter/', ChapterListView.as_view(), name='ChapterList')
]
