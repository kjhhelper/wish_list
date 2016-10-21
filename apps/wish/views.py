from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Log


def index(request):
    print('index here')
    if not "errors" in request.session:
        request.session['errors']=[]
    return render (request, 'wish/index.html')

def register(request):
    # print('aaaa********************')
    if request.POST['thing'] == 'Register' :
        result = Log.logMgr.validate(request.POST['name'], request.POST['email'], request.POST['pwd'], request.POST['confirmpwd'])
        # print('**********bbbb**********')
        if result[0]: #result[0] is true
            print('v-r-t')
            request.session['result'] = result[1].name
            if 'errors' in request.session:
                request.session.pop('errors')  #this was the error brian found though i still dont get it
            return redirect('/dashboard')

        else: #result[0] is false
            print('v-r-f')
            request.session['errors'] = result[1]
            # print (request.session['errors'])
            return redirect ('/')


    else: #if request.method is not POST
        return redirect ('/')

def dashboard(request):
    logs = Log.logMgr.all()
    context = {
        'all_logs': logs,
        'your_log':Log.logMgr.all().latest('created_at')
    }
    return render(request,'wish/dashboard.html', context)

def itemprocess(request):
    return render(request,'wish/item.html')

def item(request):
    if request.method=="POST":
    # if request.POST['thing'] == 'Add':
        result= Log.logMgr.vali(request.POST['item'])
        if result[0]:
            print('v-i-t')
            request.session['result'] = result[1].item

            if 'errors' in request.session:
                request.session.pop('errors')  #this was the error brian found though i still dont get it
            return redirect('/dashboard')

        else: #result[0] is false
            print('v-i-f')
            request.session['errors'] = result[1]
            # print (request.session['errors'])
            return render(request,'wish/item.html')

    else: #if request.method is not POST
        return redirect ('/')

def wishlistprocess(request):
    return render(request,'wish/wishlist.html')

def wishlist(request):
    return render(request,'wish/wishlist.html')
