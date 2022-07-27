from django.urls import path
from .views import ProductListView, ProductDetailView, PostListView, PostDetailView, UserListView, UserDetailView
# from .views import PostViewset, ProductViewset, UserViewset
from rest_framework.routers import SimpleRouter
from rest_framework.schemas import get_schema_view

urlpatterns = [
    path('',ProductListView.as_view()),
    path('pro/<int:pk>', ProductDetailView.as_view()),
    path('post/', PostListView.as_view()),
    path('post/<int:pk>', PostDetailView.as_view()),
    path('users/', UserListView.as_view()),
    path('users/<int:pk>', UserDetailView.as_view()),
    path('openapi', get_schema_view(
        title='Product API',
        description='Django Project API',
        version='1.0.0',
    ), name = 'openapi-schema'),
]


#
# router = SimpleRouter()
#
# router.register('post',PostViewset, basename='postpro')
# router.register('users', UserViewset, basename='user')
# router.register('', ProductViewset, basename='product')
# urlpatterns = router.urls