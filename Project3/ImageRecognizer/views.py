from django.shortcuts import render, redirect
from .models import History, Models
from django.contrib.sessions.models import Session
from django.contrib import messages
import base64
import re
from .model.predict_image import *
from sys import getsizeof
from os.path import exists
import datetime
import pytz

# Create your views here.


def image_recognizer(image):
    print('Call recognizer function')
    return predict_image(image)

def clear_history(request):
    if request.session.session_key:
        history = History.objects.filter(session=Session.objects.filter(pk=request.session.session_key).get()).delete()
    return redirect('index')


def clear_expired():
    sessions = Session.objects.filter(expire_date__lte=pytz.utc.localize(datetime.datetime.now()))
    for session_ in sessions:
        History.objects.filter(session=session_).delete()

def get_history(session_key):
    history = None
    current_session = Session.objects.filter(pk=session_key)
    if current_session:
        history = History.objects.filter(session=current_session.get()).order_by('-id').all()
        for raw in history:
            image = base64.b64encode(raw.body)
            image = image.decode('utf8')
            raw.body = image
    return history


def get_file_type(file_name):
    file_type = re.search('\.[a-zA-Z]+$', file_name).group(0)[1:]
    return file_type


def index(request):
    history = None
    print('request.session.session_key: ', request.session.session_key)
    if not request.session.session_key:
        request.session.create()
    clear_expired()
    if not Session.objects.filter(pk=request.session.session_key):
        request.session.delete()
        request.session.create()
    try:
        if request.method == 'POST':
            file = dict(request.__dict__['_files'])
            if file != {}:
                file = file['project_files'][0]
                file_type = get_file_type(file.name)
                assert (file_type in ['png', 'jpeg', 'jpg', 'gif']), 'Incorrect file type, file should be an image'
                assert (getsizeof(file.read()) < 15000000), 'File to big, please resize image'
                file.seek(0)
                response = image_recognizer(file)
                file.seek(0)
                raw = History(session=Session.objects.filter(pk=request.session.session_key).get(),
                              name=file.name,
                              type=file_type,
                              response=response,
                              body=file.read()
                              )
                raw.save()
            else:
                messages.add_message(request, messages.WARNING, "Didn't find file to upload")
    except Exception as e:
        print(e)
        messages.add_message(request, messages.WARNING, str(e))
    history = get_history(request.session.session_key)
    return render(request,
                  'index.html',
                  context={'history': history},
                 )

