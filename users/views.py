from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404, reverse
from .models import Forum, Comments, Topics, TopicComments, Announcement, Events, Contact, Webinar
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.contrib.auth import authenticate, login
# Create your views here.

def approve_student(request, user_id):
    user = User.objects.get(pk=user_id)
    user.is_staff = True
    user.save()
    # You can redirect to a success page or to the same page
    return redirect('students')

def deleteStudent1(request, student_id):
    User.objects.filter(id=student_id).delete()
    messages.success(request, 'Student Removed')
    return redirect('/students')

def disapprove_student(request, user_id):
    user = User.objects.get(pk=user_id)
    user.is_staff = False
    user.save()
    # You can redirect to a success page or to the same page
    return redirect('students')


def approve_teacher(request, user_id):
    user = User.objects.get(pk=user_id)
    user.is_superuser = True
    user.save()
    # You can redirect to a success page or to the same page
    return redirect('mainDashboard')

def disapprove_teacher(request, user_id):
    user = User.objects.get(pk=user_id)
    user.is_superuser = False
    user.save()
    # You can redirect to a success page or to the same page
    return redirect('mainDashboard')

def logoutUser(request):
    auth.logout(request)
    messages.success(request, "Logged out Successfully!")
    return redirect('login')


def mainLogin(request):
    return render(request, 'main/mainLogin.html')

def mainStudents(request):
    students = User.objects.filter(last_name='Student').order_by('-id')
    teacher = User.objects.filter(last_name='Teacher').order_by('-id')
    
    context = {
        'students': students,
        'teacher':teacher,
    }
    return render(request, 'main/students.html', context)

def mainDashboard(request):
    students = User.objects.filter(last_name='Student').order_by('-id')
    teacher = User.objects.filter(last_name='Teacher').order_by('-id')
    
    context = {
        'students': students,
        'teachers':teacher,
    }
    return render(request, 'main/mainDashboard.html', context)

def homepage(request):
    return render(request, 'index.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        info = authenticate(username=username, password=password)
        if info is not None:
            login(request, info)
            if info.is_superuser:
                return redirect('forum')
            elif info.is_staff:
                return redirect('studForum')
            else:
                messages.error(request, "You are not approve to the admin. Please wait")
                return redirect('login')
        else:
            messages.error(request, "Invalid username or password")
            return redirect('login')
    return render(request, 'login.html')

def loginStudent(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if password1 == password2:
            if User.objects.filter(username=email).exists():
                messages.error(request, 'Email already taken.')
                return redirect('loginStudent')

            else:
                new_student = User.objects.create_user(
                    first_name=first_name, username=email, password=password1, last_name='Student', is_staff=True, is_superuser=False )
                new_student.save()
                
                messages.success(request, 'Account created')
                return redirect('login')
        else:
            messages.error(request, 'Password does not match.')
            return redirect('loginStudent')
    return render(request, 'LoginStudent.html')


def loginTeacher(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if password1 == password2:
            if User.objects.filter(username=email).exists():
                messages.error(request, 'Email already taken.')
                return redirect('loginTeacher')

            else:
                new_teacher = User.objects.create_user(
                    first_name=first_name, username=email, password=password1, last_name='Teacher', is_staff=False, is_superuser=True )
                new_teacher.save()
                
                messages.success(request, 'Account created')
                return redirect('login')
        else:
            messages.error(request, 'Password does not match.')
            return redirect('loginTeacher')
        
    return render(request, 'LoginTeacher.html')




@login_required(login_url='/login')
def studentLists(request):
   
   
    # Now you can use the teacher object as needed
    # For example, accessing its profile_pic, id_no, etc.
    students = User.objects.filter(last_name='Student')
    
    context = {
        'students': students,
        
    }
    return render(request, 'teacher/studentList.html', context)

def deleteStudent(request, student_id):
    User.objects.filter(id=student_id).delete()
    messages.success(request, 'Student Removed')
    return redirect('/studentList')

def deleteTeacher(request, teacher_id):
    User.objects.filter(id=teacher_id).delete()
    messages.success(request, 'Teacher Removed')
    return redirect('mainDashboard')

@login_required(login_url='/login')
def forum(request):
   
    students = User.objects.filter(last_name='Student')
    forums = Forum.objects.filter(uploader=request.user).annotate(comment_count=Count('comments')).order_by('-upload_date')
    comments_lists = Comments.objects.all().order_by('comment_date')

    if request.method == 'POST':
        if 'forum_form_submit' in request.POST:
            
            description = request.POST['description']
            file = request.FILES.get('file')  # Use get() to avoid KeyError
            
            new_forum = Forum.objects.create(description=description, uploader=request.user, file=file)
            new_forum.save()
            messages.success(request, 'Forum Added!')
             
        elif 'comment_form_submit' in request.POST:
            comment = request.POST['comment']
            commentor = request.POST['commentor']
            post_id = request.POST['post']  # Retrieve the post ID
        
            forum = get_object_or_404(Forum, pk=post_id)
        
            new_comment = Comments.objects.create(comment=comment, commentors=request.user, post=forum)
            new_comment.save()
    
    context = {
        'students': students,
        'forums': forums,
        'comments_lists': comments_lists,
    }
    return render(request, 'teacher/forum.html', context)


def deleteForum(request, forum_id):
    Forum.objects.filter(id=forum_id).delete()
    messages.success(request, 'Forum deleted')
    return redirect('/forum')



@login_required(login_url='/login')
def topics(request):
    
    # Now you can use the teacher object as needed
    # For example, accessing its profile_pic, id_no, etc.
    students = User.objects.filter(last_name='Student')
    topics = Topics.objects.filter(uploader=request.user).order_by('-id')
    
    if request.method == 'POST':
      
        description = request.POST['description']
        file = request.FILES['file']
        
        new_topic = Topics.objects.create(description=description, uploader=request.user, file=file)
        new_topic.save()
        messages.success(request, 'Resource Added!')
    context = {
        'students': students,
        'topics':topics,
    }
    return render(request, 'teacher/topic.html', context)

def deleteTopic(request, topic_id):
    Topics.objects.filter(id=topic_id).delete()
    messages.success(request, 'Resource deleted')
    return redirect('/topics')




@login_required(login_url='/login')
def announcements(request):
    students = User.objects.filter(last_name='Student')
    announcements = Announcement.objects.filter(uploader=request.user).order_by('-id')
    webinar = Webinar.objects.filter(uploader=request.user).order_by('-id')
    if request.method == 'POST':
        # Check which form was submitted
        if 'form1_submit' in request.POST:
            description = request.POST['description']
            
            # Check if a file was uploaded
            if 'file' in request.FILES:
                file = request.FILES['file']
                new_announcement = Announcement.objects.create(description=description, uploader=request.user, file=file)
                new_announcement.save()
                messages.success(request, 'Event Added!')
            else:
                # Handle case where no file was uploaded
                new_announcement = Announcement.objects.create(description=description, uploader=request.user)
                new_announcement.save()
                messages.success(request, 'Event Added!')
        
        elif 'form2_submit' in request.POST:
            description = request.POST['description']
            file = request.FILES['file']
        
            new_webinar = Webinar.objects.create(description=description, uploader=request.user, file=file)
            new_webinar.save()
            messages.success(request, 'Webinar Added!')

 
    context = {
        'students': students,
        'announcements': announcements,
        'webinar':webinar,
    }
    return render(request, 'teacher/announcement.html', context)

def deleteWebinar(request,  webinar_id):
    Webinar.objects.filter(id = webinar_id).delete()
    messages.success(request, 'Webinar deleted')
    return redirect('/announcement')



def webinar_page(request):
    # Get the forum_id from the query parameters
    webinar_id = request.GET.get('webinar_id')

    # Retrieve the webinar object using the webinar_id
    webinar = Webinar.objects.get(id=webinar_id)

    context = {
        'webinar': webinar, 
    
    }
    # Render the forum page template with the forum object and comments
    return render(request, 'webinar.html', context)



def deleteAnnouncement(request,  announcement_id):
    Announcement.objects.filter(id = announcement_id).delete()
    messages.success(request, 'Announcement deleted')
    return redirect('/announcement')






@login_required(login_url='/login')
def events(request):
   
    
    # Now you can use the teacher object as needed
    # For example, accessing its profile_pic, id_no, etc.
    students = User.objects.filter(last_name='Student')
    events = Events.objects.filter(uploader=request.user).order_by('-upload_date')
    
    if request.method == 'POST':
        
        description = request.POST['description']
        
        # Check if a file was uploaded
        if 'file' in request.FILES:
            file = request.FILES['file']
            new_event = Events.objects.create(description=description, uploader=request.user, file=file, like=0)
            new_event.save()
            messages.success(request, 'Event Added!')
        else:
            # Handle case where no file was uploaded
            new_event = Events.objects.create(description=description, uploader=request.user, like=0)
            new_event.save()
            messages.success(request, 'Success. Event added')
 
    context = {
        'students': students,
        'events': events,
    }
    return render(request, 'teacher/event.html', context)


def deleteEvent(request,  event_id):
    Events.objects.filter(id = event_id).delete()
    messages.success(request, 'Event deleted')
    return redirect('/event')



@login_required(login_url='/login')
def studForum(request):
   
    
    # Retrieve all forums with comment counts
    forums = Forum.objects.annotate(comment_count=Count('comments')).order_by('-upload_date')
    
    if request.method == 'POST':
        comment = request.POST['comment']
        commentor = request.POST['commentor']
        post_id = request.POST['post']  # Retrieve the post ID
        
        # Get the corresponding Forum instance
        forum = get_object_or_404(Forum, pk=post_id)
        
        new_comment = Comments.objects.create(comment=comment, commentors=request.user, post=forum)
        new_comment.save()
        
    comments_lists = Comments.objects.all().order_by('comment_date')
    
    context = {
       
        'forums': forums,
        'comments_lists': comments_lists,
    }
    return render(request, 'student/forums.html', context)


def forum_page(request):
   
    
    # Retrieve all forums with comment counts
    forums = Forum.objects.annotate(comment_count=Count('comments')).order_by('-upload_date')
    
    if request.method == 'POST':
        comment = request.POST['comment']
        
        post_id = request.POST['post']  # Retrieve the post ID
        
        # Get the corresponding Forum instance
        forum = get_object_or_404(Forum, pk=post_id)
        
        new_comment = Comments.objects.create(comment=comment, commentors=request.user, post=forum)
        new_comment.save()
    
    # Get the forum_id from the query parameters
    forum_id = request.GET.get('forum_id')

    # Retrieve the forum object using the forum_id
    forum = Forum.objects.get(id=forum_id)

    # Retrieve all comments related to the forum
    comments = Comments.objects.filter(post=forum)
    
    context = {
        'forum': forum, 
        'comments': comments,
    }
    # Render the forum page template with the forum object and comments
    return render(request, 'student/forumPost.html', context)





def forum_page1(request):
   
    
    # Retrieve all forums with comment counts
    forums = Forum.objects.annotate(comment_count=Count('comments')).order_by('-upload_date')
    
    if request.method == 'POST':
        comment = request.POST['comment']
        commentor = request.POST['commentor']
        post_id = request.POST['post']  # Retrieve the post ID
        
        # Get the corresponding Forum instance
        forum = get_object_or_404(Forum, pk=post_id)
        
        new_comment = Comments.objects.create(comment=comment, commentors=request.user, post=forum)
        new_comment.save()
    
    # Get the forum_id from the query parameters
    forum_id = request.GET.get('forum_id')

    # Retrieve the forum object using the forum_id
    forum = Forum.objects.get(id=forum_id)

    # Retrieve all comments related to the forum
    comments = Comments.objects.filter(post=forum)
    
    context = {
        'forum': forum, 
        'comments': comments,
    }
    # Render the forum page template with the forum object and comments
    return render(request, 'teacher/forumPost.html', context)





@login_required(login_url='/login')
def studAnnouncement(request):
   
    
    
    announcements = Announcement.objects.all().order_by('-upload_date')
    webinar = Webinar.objects.all().order_by('-id')
    context = {
        'webinar': webinar,
        'announcements':announcements 
    }
    return render(request, 'student/announcements.html',context)


@login_required(login_url='/login')
def studTopic(request):
   
    
    
    topics = Topics.objects.all().order_by('-upload_date')
    
    # Annotate the count of comments for each topic and order by upload date
    # topics_with_comment_count = Topics.objects.annotate(comment_count=Count('topiccomments')).order_by('-upload_date')
    
    comments_lists = Comments.objects.all()
    context = { 
        'topics': topics,
       
        'comments_lists': comments_lists, 
    }
    return render(request, 'student/topic.html', context)




@login_required(login_url='/login')
def studEvent(request):
   
    event_lists = Events.objects.all().order_by('-upload_date')
    
    
    context = {
        
        "event_lists": event_lists
    }
    return render(request, 'student/events.html',context)


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']  
       
       
        new_message = Contact.objects.create(name=name, email=email, message=message)
        new_message.save()
        messages.success(request, 'Message Delivered')
        return redirect('/contact')
    
    return render(request, 'contact.html')

def mainMessage(request):
    users_message = Contact.objects.all().order_by()
    
    context = {
        'users_message': users_message
    }
    return render(request, 'main/message.html', context)


def deleteMessage(request, message_id):
    Contact.objects.filter(id=message_id).delete()
    messages.success(request, 'Message Removed')
    return redirect('/mainmessage')

def about(request):
    return render(request, 'about.html')