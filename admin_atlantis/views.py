from django.shortcuts import render, redirect
# from django.contrib.auth import views as auth_views
# from django.contrib.auth import logout
# from django.contrib.auth.decorators import login_required

# Pages -- Dashboard
def dashboard(request):
    return render(request, 'index.html')


# Components
def avatars(request):
    return render(request, 'components/avatars.html')

def buttons(request):
    return render(request, 'components/buttons.html')

def flaticons(request):
    return render(request, 'components/flaticons.html')    

def fwicons(request):
    return render(request, 'components/font-awesome-icons.html')    

def gridsystem(request):
    return render(request, 'components/gridsystem.html')  

def panels(request):
    return render(request, 'components/panels.html')

def notifications(request):
    return render(request, 'components/notifications.html')

def sweetalert(request):
    return render(request, 'components/sweetalert.html')

def typography(request):
    return render(request, 'components/typography.html')


# Sidebar layouts
def sidebarone(request):
    return render(request, 'sidebar-style-1.html')

def sidebar_overlay(request):
    return render(request, 'overlay-sidebar.html')

def sidebar_compact(request):
    return render(request, 'compact-sidebar.html')  

def sidebar_static(request):
    return render(request, 'static-sidebar.html')  