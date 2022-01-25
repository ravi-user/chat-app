from django.shortcuts import redirect, render
from .models import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

def login(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        
        uid = User.objects.get(username = username)

        if uid:
            if uid.password == password:
                x =uid.username
                u_all = User.objects.exclude(username = x)
                context = {
                    'uid':uid,
                    'u_all':u_all,
                }
                request.session['uname'] = x             
                return render(request,"userapp/index.html",{'context':context})
    
    else:
        return render(request, "userapp/login.html")

@csrf_exempt
def index(request):
    if "uname" in request.session:
        uid = User.objects.get(username = request.session['uname'])
        x =uid.username
        u_all = User.objects.exclude(username = x)
        # print('=======',u_all)
        context = {
            'uid':uid,
            'u_all':u_all,

        }
        return render(request, "userapp/index.html",{'context':context})
    else:
        return redirect('login')

@csrf_exempt
def profile(request):
    if "uname" in request.session:
        uid = User.objects.filter(username = request.session['uname'])
        id = request.POST['id']
        uid = list(uid.values())
        # print("------------->",id)
        # cid = User.objects.filter(id = id)
                
        data=User.objects.filter(id=id)
        data=list(data.values())

        # sid = Detail.objects.filter(sender= uid)
        # sid = list(sid.values())
        # rid = Detail.objects.filter(sender=id, receiver=uid)
        # rid = list(rid.values())
        mess = Detail.objects.all()
        mess = list(mess.values())
        context = {
            'status':"success",
            'data': data,
            'mess': mess,
            'uid':uid,
            # 'rid':rid,
            # 's_mess':sid,
        }

        return JsonResponse({'context':context})

    else:
        return redirect('login')

# @csrf_exempt
# def message(request):
#     if "uname" in request.session:
#         uid = User.objects.get(username = request.session['uname'])

#         rec = request.POST['id']
#         rid = User.objects.get(id = rec)
#         mess = request.POST['mess']
       
#         mid = Detail.objects.create(sender=uid, receiver=rid, value=mess)
#         print(mid)
        
#         m_all = Detail.objects.filter(sender=uid)
#         m_all = list(m_all.values())
#         context = {
#             'mess':mess,
#             'm_all':m_all, 
#         }

#         return JsonResponse({'context':context})

@csrf_exempt
def message(request):
    if "uname" in request.session:
        print('======================')
        uid = User.objects.get(username = request.session['uname'])

        rec = request.POST['id']
        mess = request.POST['mess']
        rid = User.objects.get(id = rec)    
       
        print('====',rid)       
        mid = Detail.objects.create(sender=uid, receiver=rid, value=mess)
        print('====')       
       
        u_sen = User.objects.filter(username = request.session['uname'])
        u_rec = User.objects.filter(id = rec)   
        u_sen = list(u_sen.values())
        u_rec = list(u_rec.values())
        m_all = Detail.objects.all()
        m_all = list(m_all.values())
        context = {
            'uid':u_sen,
            'rid':u_rec,
            'm_all':m_all, 
        }

        return JsonResponse({'context':context})


        