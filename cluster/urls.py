from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name="home"),
    path('contact-us/', views.contact_us, name="contact_us"),
    path('contact-us-responses/', views.contact_us_responses, name="contact_us_responses"),
    path('products/', views.Products.as_view(
        template_name="cluster/products.html"),
         name="products"),
    path('products/<int:pk>/', views.product_detail, name="product"),
    path('products/<int:pk>/update/', views.ProductUpdateView.as_view(
        template_name="cluster/admin/product_form.html"),
         name="update_product"),
    #path('products/<int:pk>/delete/', views.ProductDeleteView.as_view(), name="delete_product"),
    path('articles/', views.article.as_view(), name="articles"),
    path('articles/<int:pk>/', views.article_detail, name="article"),
    path('articles/<int:pk>/update/', views.ArticleUpdateView.as_view(
        template_name="cluster/admin/article_form.html"),
         name="update_article"),
    path('article/<int:pk>/delete/', views.ArticleDeleteView.as_view(
        template_name="cluster/admin/article_confirm_delete.html"),
         name="delete_article"),
    path('updates/', views.updates, name="updates"),
    path('add-member/', views.add_member, name="add_member"),
    path('our-team/', views.our_team, name="our_team"),
    path('our-team/<int:pk>/update/', views.OurTeamUpdateView.as_view(
        template_name="cluster/admin/our_team_form.html"),
         name="update_our_team"),
    path('our-team/<int:pk>/delete/', views.OurTeamDeleteView.as_view(
        template_name="cluster/admin/our_team_confirm_delete.html"),
         name="delete_our_team"),
    path('support-us/', views.support_us, name="support_us"),
    path('login/',views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('delete_product/', views.delete_product, name='delete_product'),    
    path('delete_article/', views.delete_article, name='delete_article'),    

]
