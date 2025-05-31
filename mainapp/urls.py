
from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
  
  path('',views.home,name='home'),
  path('about/', views.about, name="about"),
  path('contact/', views.contact, name="contact"),
  path('about/', views.about, name="about"),
  path('contact/', views.contact, name="contact"),
  path('admin_panel/dashboard', views.adminPanel, name="admin_panel"),
  path('admin_panel/login/', views.adminLogin, name="admin_login"),

  path('admin_panel/logout/', views.adminLogout, name="admin_logout"),
  path('student/login/', views.studentLogin, name="student_login"),
  path('admin_panel/add_student/', views.addStudent, name="add_student"),
  path('admin_panel/about/', views.adminAbout, name="admin_about"),
  path('admin_panel/update_about/<str:id>/', views.updateAbout, name="update_about"),

  path('admin_panel/contact/', views.adminContact, name="admin_contact"),
  path('admin_panel/update_contact/<str:id>/', views.updateContact, name="update_contact"),
  path('admin_panel/manage_students/', views.manageStudent, name="manage_students"),
  path('admin_panel/update_student/<str:id>/', views.updateStudent, name="update_student"),
  path('admin_panel/delete_student/<str:id>/', views.deleteStudent, name="delete_student"),
  path('admin_panel/add_notice/', views.addNotice, name="add_notice"),

  path('admin_panel/manage_notices/', views.manageNotices, name="manage_notices"),
  path('admin_panel/delete_notice/<str:id>/', views.deleteNotice, name="delete_notice"),
  path('admin_panel/update_notice/<str:id>/', views.updateNotice, name="update_notice"),

  path('admin_panel/add_teacher/', views.addTeacher, name="add_teacher"),
  path('admin_panel/manage_teacher/', views.manageTeachers, name="manage_teachers"),
  path('admin_panel/delete_teacher/<str:id>/', views.deleteTeacher, name="delete_teacher"),

  path('student/dashboard/', views.studentDashboard, name="student_dashboard"),
  path('student/student_settings/student_logout', views.studentLogout, name="student_logout"),
  path('student/update_teacher/<str:id>/', views.updateFaculty, name="update_teacher"),
  path('student/view_notices/', views.viewNotices, name="view_notices"),
  path('student/student_settings/', views.studentSettings, name="student_settings"),
  path('teacher_panel/', views.teacherPanel, name="teacher_panel"),
  # path('teacher_panel/dashboard/', views.teacherPanel, name="teacher_dashboard"),

  path('teacher/login/', views.teacherLogin, name="teacher_login"),
  path('student/notices/', views.teachernotices, name="teacher_notices"),
  # path('student/video/', views.teachervideo, name="teacher_video"),
  path('teacher_panel/logout/', views.teacherLogout, name="teacher_logout"),
  # path('teachervideo/', views.teachervideo, name='teachervideo'),
  # urls.py
  path('delete-video/<int:video_id>/', views.delete_video, name='delete_video'),
  ]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

# from . import views
