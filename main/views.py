
from main.models import Profile,  posts
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
import uuid
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from math import ceil
from django.http import HttpResponse

# Create your views here.

@login_required
def index(request):
    return render(request , 'index.html')


def home(request):
    
    # post = post.objects.all()
    # print(posts)
    # n = len(post)
    # nSlides = n//4 + ceil((n/4)-(n//4))
    allposts = []
    catposts = posts.objects.values('category', 'id')
    cats = {item['category'] for item in catposts}
    for cat in cats:
        post = posts.objects.filter(category=cat)
        n = len(post)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allposts.append([post, range(1, nSlides), nSlides])

    # params = {'no_of_slides':nSlides, 'range': range(1,nSlides),'posts': posts}
    # allposts = [[posts, range(1, nSlides), nSlides],
    #             [posts, range(1, nSlides), nSlides]]
    params = {'allposts':allposts}
    return render(request, 'home.html', params)


def login_attempt(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user_obj = User.objects.filter(username = username).first()
        if user_obj is None:
            messages.success(request, 'User does not exist.')
            return redirect('/login')
        
        
        profile_obj = Profile.objects.filter(user = user_obj ).first()

        if not profile_obj.is_verified:
            messages.success(request, 'Email is not verified.')
            return redirect('/login')

        user = authenticate(username = username , password = password)
        if user is None:
            messages.success(request, 'Wrong password.')
            return redirect('/login')
        
        login(request , user)
        return redirect('/')

    return render(request , 'login.html')

def register_attempt(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(password)

        try:
            if User.objects.filter(username = username).first():
                messages.success(request, 'Username already exists.')
                return redirect('/register')

            if User.objects.filter(email = email).first():
                messages.success(request, 'Email already exists.')
                return redirect('/register')
            
            user_obj = User(username = username , email = email)
            user_obj.set_password(password)
            user_obj.save()
            auth_token = str(uuid.uuid4())
            profile_obj = Profile.objects.create(user = user_obj , auth_token = auth_token)
            profile_obj.save()
            send_mail_after_registration(email , auth_token)
            return redirect('/token')

        except Exception as e:
            print(e)


    return render(request , 'register.html')

def success(request):
    return render(request , 'success.html')


def token_send(request):
    return render(request , 'token_send.html')



def verify(request , auth_token):
    try:
        profile_obj = Profile.objects.filter(auth_token = auth_token).first()
    

        if profile_obj:
            if profile_obj.is_verified:
                messages.success(request, 'Your mail is already verified.')
                return redirect('/login')
            profile_obj.is_verified = True
            profile_obj.save()
            messages.success(request, 'Your mail has been verified.')
            return redirect('/login')
        else:
            return redirect('/error')
    except Exception as e:
        print(e)
        return redirect('/')

def error_page(request):
    return  render(request , 'error.html')





def postview(request , post_id):
    post = posts.objects.filter(id = post_id)
       
    return render(request , 'main/postview.html' , {'post':post[0]})
    
    


def send_mail_after_registration(email , token):
    subject = 'Email Verification for seekhade.info'
    message = f'Hi! click on the link to verify your email http://127.0.0.1:8000/verify/{token}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message , email_from ,recipient_list )
    
