from django.urls import path, include

urlpatterns = [
    # path('blog/', include(('film_box.blog.urls', 'blog')))
    path('authentication/', include('film_box.authentication.urls')),
]
