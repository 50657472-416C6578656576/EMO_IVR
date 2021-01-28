from django.contrib.auth import views as auth_views
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='homepage'),

    # Competitions part
    path('comp/search/', views.Search.as_view(template_name='competition/competition_search_list.html'), name='search'),
    path('my_comps/', views.MyCompList.as_view(template_name='competition/my_competitions_list.html'), name='my_comp_list'),
    path('my_team', views.my_team, name='my_team'),
    path('comp/<int:pk>', views.CompDetailView.as_view(), name='comp_details'),
    path('my_team/sportsmen/', views.add_sprtmn, name='sportsmen_list'),
    path('comp/add/', views.add_comp, name='add_competition'),

    # Account
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path("login/", auth_views.LoginView.as_view(template_name='account/login.html'), name="login"),
    path("signup/", views.SignupView.as_view(), name="signup"),
    path("profile/", auth_views.PasswordChangeView.as_view(
        template_name='account/profile.html',
        # success_url =''
    ),
         name='profile'),
    path("password_change/done/", auth_views.PasswordChangeDoneView.as_view(
        template_name='account/password_change_done.html',
    ),
         name='password_change_done'),

    # Forget Password
    path('password_reset/',
         auth_views.PasswordResetView.as_view(
             template_name='commons/password-reset/password_reset.html',
             subject_template_name='commons/password-reset/password_reset_subject.txt',
             email_template_name='commons/password-reset/password_reset_email.html',
         ),
         name='password_reset'),
    path('password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='commons/password-reset/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='commons/password-reset/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='commons/password-reset/password_reset_complete.html'
         ),
         name='password_reset_complete'),
]