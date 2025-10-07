import json
import os
from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import models
from django.core.validators import MinLengthValidator, RegexValidator, EmailValidator

def startpage(request):
    return render(request, 'startpage.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        first_name = request.POST.get('fullname')
        password = request.POST.get('password')
        if User.objects.filter(username=username).exists():
            if User.objects.filter(email=email).exists():
                if len(username) >=4 and len(username) <=12:
                    user = User.objects.create_user(username=username,email=email,password=password)
                    user.save()
                else:
                    return HttpResponse("Length error")
            else:
                return HttpResponse("Username already taken ❌")
        else:
            return HttpResponse("Username already taken ❌")                    
        return redirect('login')
    else:
        messages.error(request,"Please enter valid details.")
    return render(request,'signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            auth_login(request,user)
            return redirect('home')
        else: 
            return HttpResponse("Invalid username and password!")
            # messages.error(request, "Invalid username and password!")
    return render(request,'login.html')

@login_required(login_url='login')
def home(request):
    json_path = os.path.join(settings.BASE_DIR, 'assets', 'illness.json')
    with open(json_path, 'r', encoding='utf-8') as f:
        diseases = json.load(f)
    return render(request, 'homepage.html', {'diseases': diseases})

def submit_disease(request):
    if request.method == 'POST':
        selected_disease  = request.POST.getlist("disease")
        dishes_form = None
        if "flu".lower() in selected_disease:
            dishes_form = 1
        elif "fever".lower() in selected_disease:
            dishes_form = 1
        elif "allergy".lower() in selected_disease:
            dishes_form = 2
        elif "sugar".lower() in selected_disease:
            dishes_form = 3
        elif "typhoid".lower() in selected_disease:
            dishes_form = 4
        elif "diabetes".lower() in selected_disease:
            dishes_form = 5
        elif "bp".lower() in selected_disease:
            dishes_form = 6
        elif "chronic_kidney_disease".lower() in selected_disease:
            dishes_form = 7
        elif "thyroid_disorder".lower() in selected_disease:
            dishes_form = 8
        elif "chronic_liver_disease".lower() in selected_disease:
            dishes_form = 9
        elif "heart_attack".lower() in selected_disease:
            dishes_form = 10
        fever_breakfast = os.path.join(settings.BASE_DIR, 'assets', 'feverBreakfast.json')
        fever_food = os.path.join(settings.BASE_DIR, 'assets', 'feverfood.json')
        allergy_breakfast = os.path.join(settings.BASE_DIR, 'assets', 'allergyBreakfast.json')
        allergy_food = os.path.join(settings.BASE_DIR, 'assets', 'allergyfood.json')
        sugar_breakfast = os.path.join(settings.BASE_DIR, 'assets', 'sugarBreakfast.json')
        sugar_food = os.path.join(settings.BASE_DIR, 'assets', 'sugarfood.json')
        typhoid_breakfast = os.path.join(settings.BASE_DIR, 'assets', 'typhoidBreakfast.json')
        typhoid_food = os.path.join(settings.BASE_DIR, 'assets', 'typhoidfood.json')
        diabetes_breakfast = os.path.join(settings.BASE_DIR, 'assets', 'diabetesBreakfast.json')
        diabetes_food = os.path.join(settings.BASE_DIR, 'assets', 'diabetesfood.json')
        bp_breakfast = os.path.join(settings.BASE_DIR, 'assets', 'bpBreakfast.json')
        bp_food = os.path.join(settings.BASE_DIR, 'assets', 'bpfood.json')
        Chronic_Kidney_Disease_breakfast = os.path.join(settings.BASE_DIR, 'assets', 'chronic_kidney_diseaseBreakfast.json')
        Chronic_Kidney_Disease_food = os.path.join(settings.BASE_DIR, 'assets', 'chronic_kidney_diseasefood.json')
        thyroid_disorder_breakfast = os.path.join(settings.BASE_DIR, 'assets', 'thyroid_disorderBreakfast.json')
        thyroid_disorder_food = os.path.join(settings.BASE_DIR, 'assets', 'thyroid_disorderfood.json')
        chronic_liver_disease_breakfast = os.path.join(settings.BASE_DIR, 'assets', 'chronic_liver_diseaseBreakfast.json')
        chronic_liver_disease_food = os.path.join(settings.BASE_DIR, 'assets', 'chronic_liver_diseasefood.json')
        heart_attack_breakfast = os.path.join(settings.BASE_DIR, 'assets', 'heart_attackBreakfast.json')
        heart_attack_food = os.path.join(settings.BASE_DIR, 'assets', 'heart_attackfood.json')
        allbreakfast_dir = [
                    fever_breakfast,
                    allergy_breakfast,
                    sugar_breakfast,
                    typhoid_breakfast,
                    diabetes_breakfast,
                    bp_breakfast,
                    Chronic_Kidney_Disease_breakfast,
                    thyroid_disorder_breakfast,
                    chronic_liver_disease_breakfast,
                    heart_attack_breakfast
                    ]
        allfood_dir = [
                    fever_food,
                    allergy_food,
                    sugar_food,
                    typhoid_food,
                    diabetes_food,
                    bp_food,
                    Chronic_Kidney_Disease_food,
                    thyroid_disorder_food,
                    chronic_liver_disease_food,
                    heart_attack_food
                    ]
        for breakfast in allbreakfast_dir:
            with open(breakfast, 'r', encoding='utf-8') as f:
                if breakfast == fever_breakfast:
                    fb = json.load(f)
                elif breakfast == allergy_breakfast:
                    ab = json.load(f)
                elif breakfast == sugar_breakfast:
                    sb = json.load(f)
                elif breakfast == typhoid_breakfast:
                    tb = json.load(f)
                elif breakfast == diabetes_breakfast:
                    db = json.load(f)
                elif breakfast == bp_breakfast:
                    bb = json.load(f)
                elif breakfast == Chronic_Kidney_Disease_breakfast:
                    cb = json.load(f)
                elif breakfast == thyroid_disorder_breakfast:
                    tdb = json.load(f)
                elif breakfast == chronic_liver_disease_breakfast:
                    cldb = json.load(f)
                elif breakfast == heart_attack_breakfast:
                    hab = json.load(f)
        for food in allfood_dir:
            with open(food, 'r', encoding='utf-8') as f:
                if food == fever_food:
                    ff = json.load(f)
                elif food == allergy_food:
                    af = json.load(f)
                elif food == sugar_food:
                    sf = json.load(f)
                elif food == typhoid_food:
                    tf = json.load(f)
                elif food == diabetes_food:
                    df = json.load(f)
                elif food == bp_food:
                    bf = json.load(f)
                elif food == Chronic_Kidney_Disease_food:
                    cf = json.load(f)
                elif food == thyroid_disorder_food:
                    tdf = json.load(f)
                elif food == chronic_liver_disease_food:
                    cldf = json.load(f)
                elif food == heart_attack_food:
                    haf = json.load(f)
        return render(request, 'healthyfood.html',  {"form_to_show": dishes_form, "fb": fb, "ff": ff, "ab": ab,
                                                    "ab": ab, "af": af, "sb": sb, "sf": sf, "tb": tb, "tf": tf,
                                                    "db": db, "df": df, "bb": bb, "bf": bf, "cb": cb, "cf": cf,
                                                    "tdb": tdb, "tdf": tdf, "cldb": cldb, "cldf": cldf, "hab": hab, "haf": haf})

@login_required(login_url='login')
def food_menu(request):
    breakfast_json = os.path.join(settings.BASE_DIR,'assets', 'breakfast.json')
    veg_food_json = os.path.join(settings.BASE_DIR,'assets', 'veg_food.json')
    non_veg_json = os.path.join(settings.BASE_DIR,'assets', 'non_veg.json')
    desserts_json = os.path.join(settings.BASE_DIR,'assets', 'Desserts_Snacks.json')
    food_menu = [
                    breakfast_json,
                    veg_food_json,
                    non_veg_json,
                    desserts_json
                ]
    for food_for_healthy in food_menu:
        with open(food_for_healthy, 'r', encoding='utf-8') as f:
            if food_for_healthy == breakfast_json:
                breakfast_dishes = json.load(f)
            elif food_for_healthy == veg_food_json:
                veg_dishes = json.load(f)
            elif food_for_healthy == non_veg_json:
                non_veg_dishes = json.load(f)
            elif food_for_healthy == desserts_json:
                desserts_dishes = json.load(f)
    return render(request, 'foodmenu.html', {'breakfast': breakfast_dishes,'veg_dish': veg_dishes,'non_veg_dish': non_veg_dishes,'desserts': desserts_dishes})

@login_required(login_url='login')
def selected_menu(request):
    if request.method == 'POST':
        show_selcted_menu = request.POST.getlist("healthyfoods")
        if show_selcted_menu:
            return render(request, 'selectedmenu.html', {'selectedfoodlist': show_selcted_menu})
        return HttpResponse("Food not found !")

@login_required(login_url='login')
def total_selected_list(request):
    if request.method == 'POST':
        order_menu = request.POST.getlist("order_list")
        if order_menu:
            return render(request, 'customerdetails.html')
        return HttpResponse("Menu not found!")

@login_required(login_url='login')
def customer_details(request):
    if request.method == 'POST':
        customerdetails = request.POST.getlist("detail")
        if customerdetails:
            return render(request, 'confirmorder.html')
        return HttpResponse("Details not found!")