import numpy
from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from main.forms import RegisterUserForm, LoginUserForm, PostForm
from main.models import Post, Results
from PIL import Image

import tensorflow as tf
from tensorflow import keras
import numpy as np
import pickle

import logging

logging.basicConfig(level=logging.INFO, filename="py_log.log",filemode="w",
                    format="%(asctime)s %(levelname)s %(message)s")
emotions={
    0:'Angry',
    1:'Disgust',
    2:'Fear',
    3:'Happy',
    4:'Sad',
    5:'Surprise',
    6:'Neutral'
}

def init():
    logging.info('Method "init()" was called')
    global model
    model = tf.keras.models.load_model('model_on_augmentation72')
    logging.info("Model is downloaded")

def mainpage(request):
    logging.info('Method "mainpage" was called')
    return render(request, 'main/main.html')

def aboutuser(request):
    logging.info('Method "aboutuser" was called')
    calc=len(Results.objects.filter(userid=userid))
    name=User.objects.get(id=userid).first_name
    surname = User.objects.get(id=userid).last_name
    email = User.objects.get(id=userid).email
    context={
        'name':name,
        'surname':surname,
        'email':email,
        'calc':calc,
    }
    return render(request,'main/aboutuser.html',context)

def toautho(request):
    logging.info('Method "toautho" was called')
    return render(request,'main/authopage.html')

def exit(request):
    logging.info('Method "exit" was called')
    logout(request)
    return redirect('authopage')

def addtofile(request):
    logging.info('Method "addtofile" was called')
    form = PostForm(request.POST, request.FILES)
    with open("result_file",'a') as file:
        file.write(f"{number} ({emotion}) : {im}\n")
    context = {
        'im': im,
        'form': form,
        'emotion': emotion,
        'saved':True,
    }
    return render(request, 'main/main.html',context=context)


def addimage(request):
    global number,emotion,im
    logging.info('Method "addimage" was called')
    if request.method == 'POST':
        logging.info('request.method="post"')

        form = PostForm(request.POST, request.FILES)
        form.save()
        logging.info("Form was saved into DB")

        post = Post.objects.latest('id')

        im=post.image
        logging.info(f"Image: {post.image}")
        img = Image.open(im)
        image48 = img.resize((48, 48))
        image48=image48.convert('L')
        pix = numpy.array(image48.getdata()).reshape(48, 48)
        pix=pix.astype(float)

        if 'model' not in globals():
            init()

        y = model.predict(tf.expand_dims(pix, axis=0))
        y = y.tolist()
        y = y[0]
        number= y.index(max(y))
        emotion=emotions[number]

        result=Results.objects.create(emotion=emotion,imagename=post.image,userid=userid)
        result.save()

        logging.info(f"Result of prediction: {emotion}")
        context = {
            'im': im,
            'form': form,
            'emotion':emotion,
        }
        return render(request, 'main/main.html', context=context)
    else:
        logging.info('request.method != "post"')
        form = PostForm()
    return render(request, 'main/main.html',{'form':form})





class RegisterUser(CreateView):

    form_class = RegisterUserForm
    template_name = 'main/register.html'
    success_url = 'authopage'

    def form_valid(self, form):
        logging.info('Method "form_valid" was called')
        user=form.save()
        logging.info('Form was saved into DB')
        global userid
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        me = User.objects.get(username=username)
        userid = me.id
        login(self.request,user)
        return redirect('main')


class LoginUser(LoginView):
    form_class=LoginUserForm
    template_name = 'main/authopage.html'

    def get_success_url(self):
        logging.info('Method "get_success_url" was called')
        return 'mainpage'

    def form_valid(self, form):
        logging.info('Method "form_valid" was called')
        global userid
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        logging.info('Method "form_valid" was called')
        me = User.objects.get(username=username)
        logging.info(' me = User.objects.get(username=username)')
        userid=me.id
        logging.info(f'{userid}')
        return HttpResponseRedirect(self.get_success_url())

class PostFormMain(CreateView):
    form_class = PostForm
    template_name = 'main/main.html'


