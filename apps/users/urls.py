from django.conf.urls import url
from apps.organization.views import OrgView, AddAsk, TeacherListView, TeacherDeatailView
from apps.users.views import UserInfoView, MyFavOrgView, MyFavCourseView, MyFavTeacherView
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^info/$', UserInfoView.as_view(), name='info'),
    url(r'^mycourse/$',login_required(TemplateView.as_view(template_name='usercenter-mycourse.html'), login_url='/login/'),
        {"current_page": "mycourse"}, name='mycourse'),
    url(r'^myfavorg/$', MyFavOrgView.as_view(), name='myfavorg'),
    url(r'^myfav_teacher/$', MyFavTeacherView.as_view(), name='myfav_teacher'),
    url(r'^myfav_course/$', MyFavCourseView.as_view(), name='myfav_course'),
 ]