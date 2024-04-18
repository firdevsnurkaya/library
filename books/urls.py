from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("books/", views.books, name="books"),
    path("books/<int:id>/", views.bookdetail, name="book-detail"),
    path("books/<str:name>/", views.bookdetailname, name="book-detail-name"),
    path("books/category/<int:category_id>", views.getBooksByCategoryId, name = "category_id"),
    path("books/category/<str:category_name>/", views.getBooksByCategory, name= "category"),
    path("books/author", views.getBooksByAuthor, name= "author"),
    path("authors/", views.authors, name="authors"),
    path("categories/", views.categories, name="categories"),
    # path("index/", views.index, name="index"),
]

# http://localhost:8000/ ==> index fonksiyonunun çalışmasını sağlayacak
# http://localhost:8000/index/ ==> index fonksiyonunun çalışmasını sağlayacak
# http://localhost:8000/books/ ==> index fonksiyonunun çalışmasını sağlayacak
# http://localhost:8000/books/index/ ==> index fonksiyonunun çalışmasını sağlayacak


# http://localhost:8000/books/ ==> kitaplar sayfasına gitsin