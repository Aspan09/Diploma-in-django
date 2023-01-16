from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from friendship.models import Friend, Follow, Block
from friendship.views import (
    all_users,
    block_add,
    block_remove,
    blockers,
    blocking,
    follower_add,
    follower_remove,
    followers,
    following,
    friendship_accept,
    friendship_add_friend,
    friendship_cancel,
    friendship_reject,
    friendship_request_list,
    friendship_request_list_rejected,
    friendship_requests_detail,
    view_friends,
)
from profiles.views import (UserNetAPIList, UserNetAPIUpdate, UserNetAPIDestroy,)
from user_messages.views import (MessageAPIList, MessageAPIUpdate, MessageAPIDestroy, MessagesAPIPrivate, )
from posts.views import (PostAPIList, PostAPIUpdate, PostAPIDestroy,
                            CommentAPIList, CommentAPIUpdate, CommentAPIDestroy,)
from groups.views import (UserSendMessageInGroupSerializerAPIList,
                            UserSendMessageInGroupSerializerAPIUpdate,
                            UserSendMessageInGroupSerializerAPIDestroy,
                            GroupAPIList, GroupAPIUpdate, GroupAPIDestroy,
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
    path('api/v4/chat_all/', MessageAPIList.as_view()),
    path('api/v4/chat_update/<int:pk>/', MessageAPIUpdate.as_view()),
    path('api/v4/chat_delete/<int:pk>/', MessageAPIDestroy.as_view()),

    path('api/v4/private_message/<slug:user_name>/', MessagesAPIPrivate.as_view()),

    # User_send
    path('api/v5/user_send_message_in_group/', UserSendMessageInGroupSerializerAPIList.as_view()),
    path('api/v5/user_send_message_in_group/<int:pk>/', UserSendMessageInGroupSerializerAPIUpdate.as_view()),
    path('api/v5/user_send_message_in_group/<int:pk>/', UserSendMessageInGroupSerializerAPIDestroy.as_view()),

    # Groups
    path('api/v6/groups/', GroupAPIList.as_view()),
    path('api/v6/groups_update/<int:pk>/', GroupAPIUpdate.as_view()),
    path('api/v6/groups_delete/<int:pk>/', GroupAPIDestroy.as_view()),

    # ------------------------------------------------
    # ADD FRIEND
    path('api/v7/friend/add/<slug:to_username>/', view=friendship_add_friend, name="friendship_add_friend", ),

    # ------------------------------------------------
    # ACCEPT FRIEND
    path('api/v7/friend/accept/<int:friendship_request_id>/', view=friendship_accept, name="friendship_accept", ),

    # ------------------------------------------------
    # REJECT FRIEND
    path('api/v7/friend/reject/<int:friendship_request_id>/', view=friendship_reject, name="friendship_reject", ),

    # ------------------------------------------------
    # FRIENDS VIEW
    path('api/v7/friends/<slug:username>/', view=view_friends, name="friendship_view_friends", ),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

