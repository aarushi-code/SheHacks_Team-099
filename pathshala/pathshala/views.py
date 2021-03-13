from django.http import HttpResponse, HttpResponseRedirect,JsonResponse
from django.shortcuts import render,redirect
from accounts.models import *
from questions.forms import *
from accounts.forms import *
from questions.forms import QuestionsForm
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth import get_user_model
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from accounts.tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from django.contrib.auth.decorators import login_required
from django.template.context_processors import csrf
from django.contrib.auth import authenticate, login, logout, get_user
from django.contrib.auth.forms import AuthenticationForm
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from decimal import Decimal
from paypal.standard.forms import PayPalPaymentsForm
import pyrebase
from firebase_admin import auth


# Create your views here.
def loginPage(request):
    if 'username' in request.session:    
        return redirect('dashboard')

    else:
        context = {}
        context.update(csrf(request))
        context['form_questions'] = QuestionsForm()
        context['form_signup'] = SignUpForm()
        context['form_login'] = AuthenticationForm()
        if 'email' in request.session:
            return HttpResponseRedirect('/dashboard/')
        else:
            return render(request, "login.html", context)


def SignUp(request):
    if 'username' in request.session:
        return redirect('dashboard')
    else:
        if request.method == "POST":
            form = SignUpForm(request.POST)
            if form.is_valid():
                ######Firebase######
                # username = request.POST.get('username')
                # name = request.POST.get('name')
                # mobile = request.POST.get('mobile')
                # password = request.POST.get('password1')
                # email = request.POST.get('email')	

                # user = auth.create_user_with_email_and_password(email, password)
                # uid = user['localId']
                # data = {"name":name ,"username":username,"mobile":mobile,"email":email,"first":"0"}
                # database.child("Accounts").child(uid).set(data)
                ########################################
                
                new_user = form.save()
                new_user.is_active = False
                new_user.save()
                '''
                current_site = get_current_site(request)
                mail_subject = 'Activate your account.'
                message = render_to_string('acc_active_email.html', {
                'user': new_user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(new_user.pk)),
                'token':account_activation_token.make_token(new_user),
                })
                to_email = form.cleaned_data.get('email')
                email = EmailMessage(
                            mail_subject, message, to=[to_email]
                )
                email.send()'''
                return HttpResponse('Our team will contact you shortly regarding the payment process.')
                
            else:
                print(form.errors)
                return HttpResponse("not a valid form")
            
        else:
            return redirect('landing')

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        User = get_user_model()
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # return redirect('home')
        return HttpResponse('Thank you for your email confirmation. Now you can login to your account.')
    else:
        return HttpResponse('Activation link is invalid!')

    # To be included in acc_active_email.html-
    #Please click on the link to confirm your registration,
    #http://{{ domain }}{% url 'activate' uidb64=uid token=token %}

def handle_login(request):
    print("####")
    
    ##########Firebase##########
    #email = request.POST.get('username')
    #password = request.POST.get('password')
    #try:
    #    user = auth.sign_in_with_email_and_password(email, password)
    #
    #except :
    #    message = "Invalid Login Credentials"
    #    return render(request,'login.html', {'message':message})
    #
    #uid = user['localId']
    #hopper_ref = database.child('Accounts').child(uid)
    #hopper_ref.update({
    #    'first': '1'
    #})

    #request.session['fav_color'] = str(uid)
    ########################################
    
    if 'username' in request.session :
        return redirect('dashboard')
    else:
        if request.method == 'POST':
            
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            print(user)
            
            if user != None:
                login(request, user)
                #messages.success(request, f'Welcome {username} !!')
                request.session['username'] = request.POST['username']
                #return redirect('account')
                #return redirect('dashboard')
                if user.first == True:
                    return redirect('dashboard')
                else:
                    user.first = True
                    user.save()
                    return render(request, 'afterlogin.html', {})
            else:
                #messages.info(request, f'Account does not exist. Please sign in.')
                return redirect('loginPage')
            
        else:
            form = AuthenticationForm(request.POST)
            return render(request, 'login.html', {'form_login': form})
    

def questionUpload(request):
    if request.method == 'POST':
        form = QuestionsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("Succesfully added the question")
        else:
            return HttpResponse("Please fill the valid form")
    else:
        return HttpResponse("404-page not found")

def accountPage(request):
    if 'username' in request.session:
        return render(request, "account.html", {'User': request.session['username']})
    else:
        return HttpResponseRedirect("/")


def logoutUser(request):
    del request.session['username']
    logout(request)    
    return HttpResponseRedirect('/')


# def index(request):
#     return render(request, 'index.html')
def landing_final(request):
    return render(request,'landing_final.html')

def room(request, room_name):
    return render(request, 'room.html', {
        'room_name': room_name
    })

def landing(request):
    if 'username' in request.session:
        User = request.session['username']
        return redirect('dashboard')
    else:
        User = 'Nouser'
    return render(request, 'landing_final.html',{ 'User': User})

def about(request):
    if 'username' in request.session:
        User = request.session['username']
    else:
        User = 'Nouser'
    return render(request, 'about.html',{ 'User': User})

def contact(request):
    if 'username' in request.session:
        User = request.session['username']
    else:
        User = 'Nouser'
    return render(request, 'contactus.html',{ 'User': User})

def coursePage(request):
    if 'username' in request.session:
        User = request.session['username']
    else:
        User = 'Nouser'
    return render(request, 'coursepage.html',{ 'User': User})

def pricing(request):
    if 'username' in request.session:
        User = request.session['username']
    else:
        User = 'Nouser'
    return render(request, 'pricing.html',{ 'User': User})


def features(request):
    if 'username' in request.session:
        User = request.session['username']
    else:
        User = 'Nouser'
    return render(request, 'features.html',{ 'User': User})

def faq_page(request):
    if 'username' in request.session:
        User = request.session['username']
    else:
        User = 'Nouser'
    return render(request, 'faq_page.html',{ 'User': User})

@csrf_exempt
def additional_details(request):
    if request.method == 'POST':
        
        user = get_user(request)
        user.Class = request.POST['Grade']
        user.Course = request.POST['Course']
        user.Board = request.POST['Board']
        user.Mentorship = request.POST['Mentorship']
        user.save()
        
        ################Firebase############
        #Class = request.POST.get('Grade')
        #Course = request.POST.get('Course')
        #Board = request.POST.get('Board')
        #Mentorship = request.POST.get('Mentorship')

        #uid = request.session['fav_color']
        #data = {"Class":Class ,"Course":Course,"Board":Board,"Mentorship":Mentorship}
        #database.child("Accounts").child(uid).update(data)
        ####################################
        return JsonResponse('', safe=False)
    else:
        return JsonResponse('404 error')


def dashboard(request):
    
    if 'username' in request.session or  get_user(request).is_authenticated:
        # User123 = request.session['username'] 
        User = get_user(request)   
    
        content = ({
            "selfie":User.selfie,
            "name":User.username,
            "email":User.email,
            "course":User.Course,
            "board":User.Board,
            "class":User.Class
        })
        contents={'dic1':content}
        return render(request,"dashboard_template/index.html",contents)
    else:
        #for i in request.session:
        print("###",request.session.itervalues())
        return HttpResponseRedirect("/")

""""
def checkout(request):
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
        #...
        #...

            cart.clear(request)

            request.session['order_id'] = o.id
            return redirect('process_payment')


    else:
        form = CheckoutForm()
        return render(request, 'payment/checkout.html', locals())

def process_payment(request):
    order_id = request.session.get('order_id')
    order = get_object_or_404(Order, id=order_id)
    host = request.get_host()
 
    paypal_dict = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': '%.2f' % order.total_cost().quantize(
            Decimal('.01')),
        'item_name': 'Order {}'.format(order.id),
        'invoice': str(order.id),
        'currency_code': 'USD',
        'notify_url': 'http://{}{}'.format(host,
                                           reverse('paypal-ipn')),
        'return_url': 'http://{}{}'.format(host,
                                           reverse('payment_done')),
        'cancel_return': 'http://{}{}'.format(host,
                                              reverse('payment_cancelled')),
    }
 
    form = PayPalPaymentsForm(initial=paypal_dict)
    return render(request, 'payment/process_payment.html', {'order': order, 'form': form})

@csrf_exempt
def payment_done(request):
    return render(request, 'payment/payment_done.html')


@csrf_exempt
def payment_canceled(request):
    return render(request, 'payment/payment_cancelled.html')

"""
def cart(request):

    User = get_user(request)   
    course = User.Course
    mentor = User.Mentorship
    stand = User.Class
    total=0
    
    if course == 'Regular' and mentor == '1v1' :
        total = 300
    elif course == 'Regular' and mentor == '1v5' :
        total=150
    elif course == 'Crash' and mentor == '1v1' :
        total=600
    else:
        total=450

    context = {'total':total}
    return render(request, 'cart.html',context)

def card(request):
    return render(request, 'card.html')

@login_required
def update(request):

    
    accounts = Account.objects.get(id__exact=request.user.id)

    if request.method == 'POST':
        form = UpdateForm(request.POST, request.FILES or None, instance=request.user)
        form.actual_user = request.user
        
        print(form.errors)
        
        if form.is_valid():
            print(form.errors)
            form.save()
            #messages.success(request, f'Your account has been updated!')
            return redirect('dashboard')
            
    else:
        form = UpdateForm(instance=request.user)
        
    context = {'media_url':settings.MEDIA_URL,'form':form,'accounts':accounts}
    return render(request,'profile.html', context)
