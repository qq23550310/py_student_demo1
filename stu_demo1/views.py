# Create your views here.
from django.shortcuts import render
from django.shortcuts import redirect

import os


def login(request):
    error_msg = ""
    if request.method == "POST":
        user = request.POST.get('user', None)
        pwd = request.POST.get('pwd', None)

        gender = request.POST.get("gender", "无值")
        favor = request.POST.getlist('favor')
        city = request.POST.get('city')
        op = request.POST.getlist('op')
        file = request.FILES.get('file_v')
        file_path = os.path.join('upload', file.name)
        f = open(file_path, mode='wb')
        for i in file.chunks():
            f.write(i)
        f.close()
        print(file, type(file))
        print(gender)
        print(favor)
        print(city)
        print(op)

        if user == 'root' and pwd == '123456':
            # 去跳转
            return redirect('/login')
        else:
            error_msg = "用户名或密码错误"
    return render(request, 'login.html', {'error_msg': error_msg})


USER_LIST = [
    {'id': 1, 'username': 'alex', 'email': 'asdfasdf', "gender": '男'},
    {'id': 2, 'username': 'eriuc', 'email': 'asdfasdf', "gender": '男'},
    {"id": 3, 'username': 'seven', 'email': 'asdfasdf', "gender": '男'},
    {"id": 4, 'username': 'xiaoYun', 'email': '23230310@qq.com', "gender": '男'},
    {"id": 5, 'username': 'xiaoli', 'email': '1059238964@qq.com', "gender": '女'},
]

USER_DICT = {
    '1': {'name': 'root1', 'email': 'root@live.com'},
    '2': {'name': 'root2', 'email': 'root@live.com'},
    '3': {'name': 'root3', 'email': 'root@live.com'},
    '4': {'name': 'root4', 'email': 'root@live.com'},
    '5': {'name': 'root5', 'email': 'root@live.com'},
}


def home(request):
    print(request.GET.get('nid'))

    if request.method == "POST":
        u = request.POST.get('username')
        e = request.POST.get('email')
        g = request.POST.get('gender')

        temp = {'username': u, 'email': e, "gender": g}
        USER_LIST.append(temp)
    return render(request, 'home.html', {'user_list': USER_LIST})


# def detail(request):
#     nid = request.GET.get('nid')
#     detail_info = USER_DICT[nid]
#     return render(request, 'detail.html', {'detail_info': detail_info})

def detail(request, nid):
    detail_info = USER_DICT[nid]
    return render(request, 'detail.html', {'detail_info': detail_info})
