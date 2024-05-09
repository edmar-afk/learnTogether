from django.urls import path
from . import views


urlpatterns = [
    path('approve-teacher/<int:user_id>/', views.approve_teacher, name='approve_teacher'),
    path('disapprove-teacher/<int:user_id>/', views.disapprove_teacher, name='disapprove_teacher'),
    path('approve-student/<int:user_id>/', views.approve_student, name='approve_student'),
    path('disapprove-student/<int:user_id>/', views.disapprove_student, name='disapprove_student'),
    path('<int:student1_id>/deletestudent1/', views.deleteStudent1, name='deletestudent1'),
    
    path('<int:message_id>/deletemessage/', views.deleteMessage, name='deletemessage'),
    
    path('mainmessage', views.mainMessage, name='mainmessage'),
    path('message', views.mainStudents, name='students'),
    path('mainLogin7Jk2Pf9Wd4Gh5Tq8L3Zp0Rx6V', views.mainLogin, name='mainLogin'),
    path('mainDashboardsdklAJKhISAn', views.mainDashboard, name='mainDashboard'),
    
    
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('homepage', views.homepage, name='homepage'),
    path('logout', views.logoutUser, name='logout'), 
    path('login', views.user_login, name='login'),
    path('loginStudent', views.loginStudent, name='loginStudent'),
    path('loginTeacher', views.loginTeacher, name='loginTeacher'),
    
    path('studForum', views.studForum, name='studForum'),
    path('studAnnouncement', views.studAnnouncement, name='studAnnouncement'),
    path('studTopic', views.studTopic, name='studTopic'),
    path('studEvent', views.studEvent, name='studEvent'),
    
    path('forum_page', views.forum_page, name='forum_page'),
    path('forum_page1', views.forum_page1, name='forum_page1'),
    path('webinar_page', views.webinar_page, name='webinar_page'),
    
    path('studentList', views.studentLists, name='studentList'),
    path('forum', views.forum, name='forum'),
    path('topics', views.topics, name='topics'),
    path('announcement', views.announcements, name='announcement'),
    path('event', views.events, name='event'),

    path('<int:forum_id>/deleteforum/', views.deleteForum, name='deleteforum'),
    path('<int:topic_id>/deletetopic/', views.deleteTopic, name='deletetopic'),
    path('<int:announcement_id>/deleteannouncement/', views.deleteAnnouncement, name='deleteannouncement'),
    path('<int:webinar_id>/deletewebinar/', views.deleteWebinar, name='deletewebinar'),
    path('<int:event_id>/deleteevent/', views.deleteEvent, name='deleteevent'),
    path('<int:student_id>/deletestudent/', views.deleteStudent, name='deletestudent'),
    path('<int:teacher_id>/deleteteacher/', views.deleteTeacher, name='deleteteacher'),
]