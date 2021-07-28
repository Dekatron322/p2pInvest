from django.urls import path

from . import views

app_name = "dashboard"
urlpatterns = [
	path('', views.DashboardView, name='index'),

	path('complete-sign-up/<str:username>/', views.CompleteSignUpView, name='complete_sign_up'),
	path('sign-in/', views.SignInView, name="sign_in"),
    path('sign-up/', views.SignUpView, name="sign_up"),
    path('sign-out/', views.SignOutView, name="sign_out"),

    path('profile/', views.ProfileView, name="profile"),
    path('investment/', views.InvestmentView, name="investment"),
    path('investment-detail/<int:investment_id>/', views.InvestmentDetailView, name="investment_detail"),
    path('commit/', views.CommitView, name="commit"),
    path('make-commit/<str:package_type>/', views.MakeCommitView, name="make_commit"),


    path('admin/', views.AdminView, name="admin"),
    path('admin-investment-detail/<int:investment_id>/', views.AInvestmentDetailView, name="a_investment_detail"),

]
