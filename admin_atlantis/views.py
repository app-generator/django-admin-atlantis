from django.shortcuts import render, redirect
# from django.contrib.auth import views as auth_views
# from django.contrib.auth import logout
# from django.contrib.auth.decorators import login_required

# Pages -- Dashboard
def dashboard(request):
    context = {
        'active_page': 'dashboard' 
    }
    return render(request, 'index.html',context)

def starter_template(request):
    return render(request, 'starter-template.html')

# Components
def avatars(request):
    context = {
        'active_page': 'base' 
    }
    return render(request, 'components/avatars.html',context)

def buttons(request):
    context = {
        'active_page': 'base' 
    }
    return render(request, 'components/buttons.html',context)

def flaticons(request):
    context = {
        'active_page': 'base' 
    }
    return render(request, 'components/flaticons.html',context)    

def fontawesome(request):
    context = {
        'active_page': 'base' 
    }
    return render(request, 'components/font-awesome-icons.html',context)

def simple_line_icons(request):
    context = {
        'active_page': 'base' 
    }
    return render(request, 'components/simple-line-icons.html',context)

def gridsystem(request):
    context = {
        'active_page': 'base' 
    }
    return render(request, 'components/gridsystem.html',context)  

def panels(request):
    context = {
        'active_page': 'base' 
    }
    return render(request, 'components/panels.html',context)

def notifications(request):
    context = {
        'active_page': 'base' 
    }
    return render(request, 'components/notifications.html',context)

def sweetalert(request):
    context = {
        'active_page': 'base' 
    }
    return render(request, 'components/sweetalert.html',context)

def typography(request):
    context = {
        'active_page': 'base' 
    }
    return render(request, 'components/typography.html',context)


# Sidebar layouts
def sidebarone(request):
    context = {
        'active_page': 'sidebar' 
    }
    return render(request, 'sidebar-style-1.html',context)

def sidebar_overlay(request):
    context = {
        'active_page': 'sidebar' 
    }
    return render(request, 'overlay-sidebar.html',context)

def sidebar_compact(request):
    context = {
        'active_page': 'sidebar' 
    }
    return render(request, 'compact-sidebar.html',context)  

def sidebar_static(request):
    context = {
        'active_page': 'sidebar' 
    }
    return render(request, 'static-sidebar.html',context)

def icon_menu(request):
    context = {
        'active_page': 'sidebar' 
    }
    return render(request, 'icon-menu.html',context)


# Forms
def forms(request):
    context = {
        'active_page': 'forms' 
    }
    return render(request, 'forms/forms.html',context)

# Tables    
def datatables(request):
    context = {
        'active_page': 'tables' 
    }
    return render(request, 'tables/datatables.html',context)

def tables(request):
    context = {
        'active_page': 'tables' 
    }
    return render(request, 'tables/tables.html',context)

# Charts  
def charts(request):
    context = {
        'active_page': 'charts' 
    }
    return render(request, 'charts/charts.html',context)

def sparkline(request):
    context = {
        'active_page': 'charts' 
    }
    return render(request, 'charts/sparkline.html',context) 

# Maps
def maps(request):
    context = {
        'active_page': 'maps' 
    }
    return render(request, 'maps/jqvmap.html',context)

# Widgets
def widgets(request):
    context = {
        'active_page': 'widgets' 
    }
    return render(request, 'widgets.html',context)               