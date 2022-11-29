from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from profiles.views import (UserNetAPIList, UserNetAPIUpdate, UserNetAPIDestroy,
                            PostAPIList, PostAPIUpdate, PostAPIDestroy,
                            CommentAPIList, CommentAPIUpdate, CommentAPIDestroy,
                            MessageAPIList, MessageAPIUpdate, MessageAPIDestroy
                            )


urlpatterns = [
    path('admin/', admin.site.urls),
    # Profiles
    path('api/v1/users/', UserNetAPIList.as_view()),
    path('api/v1/users_update/<int:pk>/', UserNetAPIUpdate.as_view()),
    path('api/v1/user_delete/<int:pk>/', UserNetAPIDestroy.as_view()),

    # Posts
    path('api/v2/post/', PostAPIList.as_view()),
    path('api/v2/post_update/<int:pk>/', PostAPIUpdate.as_view()),
    path('api/v2/post_delete/<int:pk>/', PostAPIDestroy.as_view()),

    # Comments
    path('api/v3/comment/', CommentAPIList.as_view()),
    path('api/v3/comment_update/<int:pk>/', CommentAPIUpdate.as_view()),
    path('api/v3/comment_delete/<int:pk>/', CommentAPIDestroy.as_view()),

    # Djoser
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('auth/', include('djoser.urls.authtoken')),

    # Messanger
    path('api/v4/chat/', MessageAPIList.as_view()),
    path('api/v4/chat_update/<int:pk>/', MessageAPIUpdate.as_view()),
    path('api/v4/chat_delete/<int:pk>/', MessageAPIDestroy.as_view()),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

