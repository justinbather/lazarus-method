from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.template import loader
from django.core.exceptions import ObjectDoesNotExist

from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic

from . import models
from . import forms
from .logic import category_completion, current_belt, calc_total_score, belt_completion, calc_category_score

# Create your views here.
def signup(request):
    if request.method == "POST":
        form = forms.CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=raw_password)
            login(request, user)
            return redirect('welcome')

    else:
        form = forms.CustomUserCreationForm()

    return render(request, 'signup/signup_page.html', {'form': form})



def login_request(request):
    user = request.user

    if request.POST:
        
        form = forms.UserForm(request.POST)
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(email=email, password=password)
        if user:
            login(request, user)
            messages.success(request, 'Logged in')
            if user.onboarding_complete == False:
                return redirect('welcome')
            return redirect('home')
        else:
            messages.error(request, 'Invalid credentials')
            return render(request, 'login/login_page.html', {'form': form})
    else:
        form = forms.UserForm()
        return render(request, 'login/login_page.html', {'form': form})



def logout_request(request): 
    logout(request)
    messages.success(request, 'Logged Out')
    return redirect('../login')



@login_required(login_url='../login/')
def home(request):
    user_belt = current_belt(request)
    context = {"first_name":request.user.first_name, 'user_belt': user_belt}
    return render(request, 'home/home_page.html', context)



@login_required
def progress(request):
    print(request.user.program)
    # For chart.js
    labels_none = []
    data_none = []
    labels_white = []
    data_white = []
    labels_yellow = []
    data_yellow = []
    labels_green = []
    data_green = []
    labels_blue = []
    data_blue = []
    labels_orange = []
    data_orange = []
    labels_purple = []
    data_purple = []
    labels_finalpurple = []
    data_finalpurple = []
    labels_baseline = []
    data_baseline = []
    labels_final = []
    data_final = []
    
    
    # Chart data is updated via the Onboarding Form View and Afterbeltform View
    # Gets all scores for user categorys and renders into a chart in progress.html

    # Patient Test Data input by Admin
    if request.user.program == 'Personalized Pathfinder':

        queryset_initial = models.Progress.objects.filter(user=request.user, belt='None').order_by('category')
        for entry in queryset_initial:
            labels_none.append(entry.category)
            data_none.append(entry.score)
        try:
            object_test1 = models.PatientTest.objects.get(patient=request.user, exam_number='1')

            # Stores scores from patient test into variables
            fasting_glucose = models.PatientTest.calc_fasting_glucose(object_test1)
            hga1c = models.PatientTest.calc_hga1c(object_test1)
            cprotein = models.PatientTest.calc_cprotein(object_test1)
            homocysteine = models.PatientTest.calc_homocysteine(object_test1)
            fasting_insulin = models.PatientTest.calc_fasting_insulin(object_test1)
            ldl_particle = models.PatientTest.calc_ldl_particle(object_test1)
            ldl_size = models.PatientTest.calc_ldl_size(object_test1)
            insulin_resistance = models.PatientTest.calc_insulin_resistance(object_test1)
            testosterone = models.PatientTest.calc_testosterone(object_test1)
            thyroid = models.PatientTest.calc_thyroid(object_test1)
            vitamin_d3 = models.PatientTest.calc_vitamin_d3(object_test1)
            vitamin_b12 = models.PatientTest.calc_vitamin_b12(object_test1)
            zinc_rbc = models.PatientTest.calc_zinc_rbc(object_test1)
            magnesium_rbc = models.PatientTest.calc_magnesium_rbc(object_test1)
            omega3_index = models.PatientTest.calc_omega3_index(object_test1)
            nourish_grade = models.PatientTest.calc_nourish_grade(object_test1)
            

            joint_mobility = models.PatientTest.calc_joint_mobility(object_test1)
            muscle_flexibility = models.PatientTest.calc_joint_mobility(object_test1)
            core_strength = models.PatientTest.calc_core_strength(object_test1)
            postural_analysis = models.PatientTest.calc_postural_analysis(object_test1)
            fat_mass = models.PatientTest.calc_fat_mass(object_test1)
            body_mass_index = models.PatientTest.calc_body_mass_index(object_test1)
            move_grade = models.PatientTest.calc_move_grade(object_test1)

            blood_pressure = models.PatientTest.calc_blood_pressure(object_test1)
            resting_heart_rate = models.PatientTest.calc_resting_heart_rate(object_test1)
            rest_grade = models.PatientTest.calc_rest_grade(object_test1)

            coherence_value = models.PatientTest.calc_coherence_value(object_test1)
            co2_tolerance = models.PatientTest.calc_co2_tolerance(object_test1)
            connect_grade = models.PatientTest.calc_connect_grade(object_test1)

            # Stores above data into category lists then gets average and sends to chart
            nourishdata = [ int(fasting_glucose), int(hga1c), int(cprotein), int(homocysteine), int(fasting_insulin), int(ldl_particle),
            int(ldl_size), int(insulin_resistance), int(testosterone), int(thyroid), int(vitamin_d3), int(vitamin_b12), 
            int(zinc_rbc), int(magnesium_rbc), int(omega3_index), int(nourish_grade), data_none[4] ]
            nourish_average = sum(nourishdata) / len(nourishdata)

            movedata = [int(joint_mobility), int(muscle_flexibility), int(core_strength), int(postural_analysis), int(fat_mass),
            int(body_mass_index), int(move_grade), data_none[3]]
            move_average = sum(movedata) / len(movedata)

            restdata = [int(blood_pressure), int(resting_heart_rate), int(rest_grade), data_none[5]]
            rest_average = sum(restdata) / len(restdata)

            connectdata = [ int(coherence_value), int(co2_tolerance), int(connect_grade), data_none[1]]
            connect_average = sum(connectdata) / len(connectdata)

            data_baseline = [data_none[0], round(connect_average), data_none[2], round(move_average), round(nourish_average), round(rest_average), data_none[6]]
            labels_baseline = ['Challenge', 'Connect', 'Learn', 'Move', 'Nourish', 'Rest', 'Spark']
        except ObjectDoesNotExist: # Error Handling
            data_baseline = [data_none[0], data_none[1], data_none[2], data_none[3], data_none[4], data_none[5], data_none[6]]
            labels_baseline = ['Challenge', 'Connect', 'Learn', 'Move', 'Nourish', 'Rest', 'Spark']

        belt_obj = models.Belt.objects.get(user=request.user, belt_colour='Purple')
        if belt_obj.completed == True:

            queryset_final = models.Progress.objects.filter(user=request.user, belt='Purple').order_by('category')
            for entry in queryset_final:
                labels_finalpurple.append(entry.category)
                data_finalpurple.append(entry.score)
                
            try:
                object_test2 = models.PatientTest.objects.get(patient=request.user, exam_number='2')

                # Stores scores from patient test into variables
                fasting_glucose = models.PatientTest.calc_fasting_glucose(object_test2)
                hga1c = models.PatientTest.calc_hga1c(object_test2)
                cprotein = models.PatientTest.calc_cprotein(object_test2)
                homocysteine = models.PatientTest.calc_homocysteine(object_test2)
                fasting_insulin = models.PatientTest.calc_fasting_insulin(object_test2)
                ldl_particle = models.PatientTest.calc_ldl_particle(object_test2)
                ldl_size = models.PatientTest.calc_ldl_size(object_test2)
                insulin_resistance = models.PatientTest.calc_insulin_resistance(object_test2)
                testosterone = models.PatientTest.calc_testosterone(object_test2)
                thyroid = models.PatientTest.calc_thyroid(object_test2)
                vitamin_d3 = models.PatientTest.calc_vitamin_d3(object_test2)
                vitamin_b12 = models.PatientTest.calc_vitamin_b12(object_test2)
                zinc_rbc = models.PatientTest.calc_zinc_rbc(object_test2)
                magnesium_rbc = models.PatientTest.calc_magnesium_rbc(object_test2)
                omega3_index = models.PatientTest.calc_omega3_index(object_test2)
                nourish_grade = models.PatientTest.calc_nourish_grade(object_test2)
                

                joint_mobility = models.PatientTest.calc_joint_mobility(object_test2)
                muscle_flexibility = models.PatientTest.calc_joint_mobility(object_test2)
                core_strength = models.PatientTest.calc_core_strength(object_test2)
                postural_analysis = models.PatientTest.calc_postural_analysis(object_test2)
                fat_mass = models.PatientTest.calc_fat_mass(object_test2)
                body_mass_index = models.PatientTest.calc_body_mass_index(object_test2)
                move_grade = models.PatientTest.calc_move_grade(object_test2)

                blood_pressure = models.PatientTest.calc_blood_pressure(object_test2)
                resting_heart_rate = models.PatientTest.calc_resting_heart_rate(object_test2)
                rest_grade = models.PatientTest.calc_rest_grade(object_test2)

                coherence_value = models.PatientTest.calc_coherence_value(object_test2)
                co2_tolerance = models.PatientTest.calc_co2_tolerance(object_test2)
                connect_grade = models.PatientTest.calc_connect_grade(object_test2)

                # Stores above data into category lists then gets average and sends to chart
                nourishdata = [ int(fasting_glucose), int(hga1c), int(cprotein), int(homocysteine), int(fasting_insulin), int(ldl_particle),
                int(ldl_size), int(insulin_resistance), int(testosterone), int(thyroid), int(vitamin_d3), int(vitamin_b12), 
                int(zinc_rbc), int(magnesium_rbc), int(omega3_index), int(nourish_grade), data_finalpurple[4]]
                nourish_average = sum(nourishdata) / len(nourishdata)

                movedata = [int(joint_mobility), int(muscle_flexibility), int(core_strength), int(postural_analysis), int(fat_mass),
                int(body_mass_index), int(move_grade), data_finalpurple[3]]
                move_average = sum(movedata) / len(movedata)

                restdata = [int(blood_pressure), int(resting_heart_rate), int(rest_grade), data_finalpurple[5]]
                rest_average = sum(restdata) / len(restdata)

                connectdata = [ int(coherence_value), int(co2_tolerance), int(connect_grade), data_finalpurple[1]]
                connect_average = sum(connectdata) / len(connectdata)

                data_final = [data_finalpurple[0], round(connect_average), data_finalpurple[2], round(move_average), round(nourish_average), round(rest_average), data_finalpurple[6]]
                labels_final = ['Challenge', 'Connect', 'Learn', 'Move', 'Nourish', 'Rest', 'Spark']
            except ObjectDoesNotExist: # Error Handling
            # getting list out of index error because purple belt hasnt been finished yet. come back to this. 
                data_final = [data_finalpurple[0], data_finalpurple[1], data_finalpurple[2], data_finalpurple[3], data_finalpurple[4], data_finalpurple[5], data_finalpurple[6]]
                labels_final = ['Challenge', 'Connect', 'Learn', 'Move', 'Nourish', 'Rest', 'Spark']

        else:
            data_final = [0, 0, 0, 0, 0, 0, 0]
            labels_final = ['Challenge', 'Connect', 'Learn', 'Move', 'Nourish', 'Rest', 'Spark']

        # User Input Data
        '''
        queryset_initial = models.Progress.objects.filter(user=request.user, belt='None').order_by('category')
        for entry in queryset_initial:
            labels_none.append(entry.category)
            print(labels_none)
            data_none.append(entry.score)
            print(sum(data_none)) # add
        '''
        # move queryset_initial above test scoring listed above and incorporate this data into the categories before they are averaged out,
        # if objectdoesnot exist, queryset_initial becomes only source of data. this mitigates the difference in values from the test only
        # having 4 catagories and error tests at the same time. BAM
        queryset_white = models.Progress.objects.filter(user=request.user, belt='White').order_by('category')
        for entry in queryset_white:
            labels_white.append(entry.category)
            data_white.append(entry.score)
        queryset_yellow = models.Progress.objects.filter(user=request.user, belt='Yellow').order_by('category')
        for entry in queryset_yellow:
            labels_yellow.append(entry.category)
            data_yellow.append(entry.score)
        queryset_green = models.Progress.objects.filter(user=request.user, belt='Green').order_by('category')
        for entry in queryset_green:
            labels_green.append(entry.category)
            data_green.append(entry.score)
        queryset_blue = models.Progress.objects.filter(user=request.user, belt='Blue').order_by('category')
        for entry in queryset_blue:
            labels_blue.append(entry.category)
            data_blue.append(entry.score)
        queryset_orange = models.Progress.objects.filter(user=request.user, belt='Orange').order_by('category')
        for entry in queryset_orange:
            labels_orange.append(entry.category)
            data_orange.append(entry.score)
        queryset_purple = models.Progress.objects.filter(user=request.user, belt='Purple').order_by('category')
        for entry in queryset_purple:
            labels_purple.append(entry.category)
            data_purple.append(entry.score)
        
        

        chartdata = {
            'labels_white': labels_white,
            'data_white': data_white,
            'labels_yellow': labels_yellow,
            'data_yellow': data_yellow,
            'labels_green': labels_green,
            'data_green': data_green,
            'labels_blue': labels_blue,
            'data_blue': data_blue,
            'labels_orange': labels_orange,
            'data_orange': data_orange,
            'labels_purple': labels_purple,
            'data_purple': data_purple,
            'labels_baseline': labels_baseline,
            'data_baseline': data_baseline,
            'labels_final': labels_final,
            'data_final': data_final
        }
        
        print(data_white)
        return render(request, 'progress/progress.html', chartdata)

    elif request.user.program == 'Tailored Trailblazer':

        queryset_initial = models.Progress.objects.filter(user=request.user, belt='None').order_by('category')
        for entry in queryset_initial:
            labels_none.append(entry.category)
            data_none.append(entry.score)

        try:
            object_test1 = models.UserEntryPatientTest.objects.get(patient=request.user, exam_number='1')

            # Stores scores from patient test into variables
            fasting_glucose = models.PatientTest.calc_fasting_glucose(object_test1)
            hga1c = models.PatientTest.calc_hga1c(object_test1)
            cprotein = models.PatientTest.calc_cprotein(object_test1)
            homocysteine = models.PatientTest.calc_homocysteine(object_test1)
            fasting_insulin = models.PatientTest.calc_fasting_insulin(object_test1)
            ldl_particle = models.PatientTest.calc_ldl_particle(object_test1)
            ldl_size = models.PatientTest.calc_ldl_size(object_test1)
            insulin_resistance = models.PatientTest.calc_insulin_resistance(object_test1)
            testosterone = models.PatientTest.calc_testosterone(object_test1)
            thyroid = models.PatientTest.calc_thyroid(object_test1)
            vitamin_d3 = models.PatientTest.calc_vitamin_d3(object_test1)
            vitamin_b12 = models.PatientTest.calc_vitamin_b12(object_test1)
            zinc_rbc = models.PatientTest.calc_zinc_rbc(object_test1)
            magnesium_rbc = models.PatientTest.calc_magnesium_rbc(object_test1)
            omega3_index = models.PatientTest.calc_omega3_index(object_test1)
            

            # Stores above data into category lists then gets average and sends to chart
            nourishdata = [ int(fasting_glucose), int(hga1c), int(cprotein), int(homocysteine), int(fasting_insulin), int(ldl_particle),
            int(ldl_size), int(insulin_resistance), int(testosterone), int(thyroid), int(vitamin_d3), int(vitamin_b12), 
            int(zinc_rbc), int(magnesium_rbc), int(omega3_index), data_none[4]]
            nourish_average = sum(nourishdata) / len(nourishdata)

            data_baseline = [data_none[0], data_none[1], data_none[2], data_none[3], round(nourish_average), data_none[5] ,data_none[6]]
            labels_baseline = ['Challenge', 'Connect', 'Learn', 'Move', 'Nourish', 'Rest', 'Spark']
        except ObjectDoesNotExist: # Error Handling
            data_baseline = [data_none[0], data_none[1], data_none[2], data_none[3], data_none[4], data_none[5] ,data_none[6]]
            labels_baseline = ['Challenge', 'Connect', 'Learn', 'Move', 'Nourish', 'Rest', 'Spark']
            
        belt_obj = models.Belt.objects.get(user=request.user, belt_colour='Purple')
        if belt_obj.completed == True:

            queryset_final = models.Progress.objects.filter(user=request.user, belt='Purple').order_by('category')
            for entry in queryset_final:
                labels_finalpurple.append(entry.category)
                data_finalpurple.append(entry.score)

            try:
                object_test2 = models.UserEntryPatientTest.objects.get(patient=request.user, exam_number='2')

                # Stores scores from patient test into variables
                fasting_glucose = models.PatientTest.calc_fasting_glucose(object_test2)
                hga1c = models.PatientTest.calc_hga1c(object_test2)
                cprotein = models.PatientTest.calc_cprotein(object_test2)
                homocysteine = models.PatientTest.calc_homocysteine(object_test2)
                fasting_insulin = models.PatientTest.calc_fasting_insulin(object_test2)
                ldl_particle = models.PatientTest.calc_ldl_particle(object_test2)
                ldl_size = models.PatientTest.calc_ldl_size(object_test2)
                insulin_resistance = models.PatientTest.calc_insulin_resistance(object_test2)
                testosterone = models.PatientTest.calc_testosterone(object_test2)
                thyroid = models.PatientTest.calc_thyroid(object_test2)
                vitamin_d3 = models.PatientTest.calc_vitamin_d3(object_test2)
                vitamin_b12 = models.PatientTest.calc_vitamin_b12(object_test2)
                zinc_rbc = models.PatientTest.calc_zinc_rbc(object_test2)
                magnesium_rbc = models.PatientTest.calc_magnesium_rbc(object_test2)
                omega3_index = models.PatientTest.calc_omega3_index(object_test2)
                nourish_grade = models.PatientTest.calc_nourish_grade(object_test2)
                


                # Stores above data into category lists then gets average and sends to chart
                nourishdata = [ int(fasting_glucose), int(hga1c), int(cprotein), int(homocysteine), int(fasting_insulin), int(ldl_particle),
                int(ldl_size), int(insulin_resistance), int(testosterone), int(thyroid), int(vitamin_d3), int(vitamin_b12), 
                int(zinc_rbc), int(magnesium_rbc), int(omega3_index), data_finalpurple[4]]
                nourish_average = sum(nourishdata) / len(nourishdata)

                # personalized pathfinder lab result only tests for nourish
                data_final = [data_finalpurple[0], data_finalpurple[1], data_finalpurple[2], data_finalpurple[3], round(nourish_average), data_finalpurple[5] ,data_finalpurple[6]]
                labels_final = ['Challenge', 'Connect', 'Learn', 'Move', 'Nourish', 'Rest', 'Spark']

            except ObjectDoesNotExist: # Error Handling
                data_final = [data_finalpurple[0], data_finalpurple[1], data_finalpurple[2], data_finalpurple[3], data_finalpurple[4], data_finalpurple[5] ,data_finalpurple[6]]
                labels_final = ['Challenge', 'Connect', 'Learn', 'Move', 'Nourish', 'Rest', 'Spark']
        else:
            data_final = [0, 0, 0, 0, 0, 0 ,0]
            labels_final = ['Challenge', 'Connect', 'Learn', 'Move', 'Nourish', 'Rest', 'Spark']

        # User Input Data

        
        
        queryset_white = models.Progress.objects.filter(user=request.user, belt='White').order_by('category')
        for entry in queryset_white:
            labels_white.append(entry.category)
            data_white.append(entry.score)

        queryset_yellow = models.Progress.objects.filter(user=request.user, belt='Yellow').order_by('category')
        for entry in queryset_yellow:
            labels_yellow.append(entry.category)
            data_yellow.append(entry.score)

        queryset_green = models.Progress.objects.filter(user=request.user, belt='Green').order_by('category')
        for entry in queryset_green:
            labels_green.append(entry.category)
            data_green.append(entry.score)

        queryset_blue = models.Progress.objects.filter(user=request.user, belt='Blue').order_by('category')
        for entry in queryset_blue:
            labels_blue.append(entry.category)
            data_blue.append(entry.score)

        queryset_orange = models.Progress.objects.filter(user=request.user, belt='Orange').order_by('category')
        for entry in queryset_orange:
            labels_orange.append(entry.category)
            data_orange.append(entry.score)

        queryset_purple = models.Progress.objects.filter(user=request.user, belt='Purple').order_by('category')
        for entry in queryset_purple:
            labels_purple.append(entry.category)
            data_purple.append(entry.score)

        chartdata = {
            'labels_white': labels_white,
            'data_white': data_white,
            'labels_yellow': labels_yellow,
            'data_yellow': data_yellow,
            'labels_green': labels_green,
            'data_green': data_green,
            'labels_blue': labels_blue,
            'data_blue': data_blue,
            'labels_orange': labels_orange,
            'data_orange': data_orange,
            'labels_purple': labels_purple,
            'data_purple': data_purple,
            'labels_baseline': labels_baseline,
            'data_baseline': data_baseline,
            'labels_final': labels_final,
            'data_final': data_final
        }
        return render(request, 'progress/progress.html', chartdata)

    elif request.user.program == "Empowered Explorer":

        queryset_none = models.Progress.objects.filter(user=request.user, belt='None').order_by('category')
        for entry in queryset_none:
            labels_baseline.append(entry.category)
            data_baseline.append(entry.score)
        queryset_white = models.Progress.objects.filter(user=request.user, belt='White').order_by('category')
        for entry in queryset_white:
            labels_white.append(entry.category)
            data_white.append(entry.score)
        queryset_yellow = models.Progress.objects.filter(user=request.user, belt='Yellow').order_by('category')
        for entry in queryset_yellow:
            labels_yellow.append(entry.category)
            data_yellow.append(entry.score)
        queryset_green = models.Progress.objects.filter(user=request.user, belt='Green').order_by('category')
        for entry in queryset_green:
            labels_green.append(entry.category)
            data_green.append(entry.score)
        queryset_blue = models.Progress.objects.filter(user=request.user, belt='Blue').order_by('category')
        for entry in queryset_blue:
            labels_blue.append(entry.category)
            data_blue.append(entry.score)
        queryset_orange = models.Progress.objects.filter(user=request.user, belt='Orange').order_by('category')
        for entry in queryset_orange:
            labels_orange.append(entry.category)
            data_orange.append(entry.score)
        queryset_purple = models.Progress.objects.filter(user=request.user, belt='Purple').order_by('category')
        for entry in queryset_purple:
            labels_purple.append(entry.category)
            data_purple.append(entry.score)
            labels_final.append(entry.category)
            data_final.append(entry.score)
            
        chartdata = {
            'labels_baseline': labels_baseline,
            'data_baseline': data_baseline,
            'labels_white': labels_white,
            'data_white': data_white,
            'labels_yellow': labels_yellow,
            'data_yellow': data_yellow,
            'labels_green': labels_green,
            'data_green': data_green,
            'labels_blue': labels_blue,
            'data_blue': data_blue,
            'labels_orange': labels_orange,
            'data_orange': data_orange,
            'labels_purple': labels_purple,
            'data_purple': data_purple,
            'data_final': data_final,
            'labels_final': labels_final
        }
        
        return render(request, 'progress/progress.html', chartdata)



@login_required #Not being used
def testresults(request):
    try:
        object = models.PatientTest.objects.get(patient=request.user)
    except ObjectDoesNotExist:
        return render(request, 'testresults/testresults.html')
         # Fix does not exist error

        
    # Stores scores from patient test into variables
    # refactor into logic
    fasting_glucose = models.PatientTest.calc_fasting_glucose(object)
    hga1c = models.PatientTest.calc_hga1c(object)
    cprotein = models.PatientTest.calc_cprotein(object)
    homocysteine = models.PatientTest.calc_homocysteine(object)
    fasting_insulin = models.PatientTest.calc_fasting_insulin(object)
    ldl_particle = models.PatientTest.calc_ldl_particle(object)
    ldl_size = models.PatientTest.calc_ldl_size(object)
    insulin_resistance = models.PatientTest.calc_insulin_resistance(object)
    testosterone = models.PatientTest.calc_testosterone(object)
    thyroid = models.PatientTest.calc_thyroid(object)
    vitamin_d3 = models.PatientTest.calc_vitamin_d3(object)
    vitamin_b12 = models.PatientTest.calc_vitamin_b12(object)
    zinc_rbc = models.PatientTest.calc_zinc_rbc(object)
    magnesium_rbc = models.PatientTest.calc_magnesium_rbc(object)
    omega3_index = models.PatientTest.calc_omega3_index(object)
    nourish_grade = models.PatientTest.calc_nourish_grade(object)
    

    joint_mobility = models.PatientTest.calc_joint_mobility(object)
    muscle_flexibility = models.PatientTest.calc_joint_mobility(object)
    core_strength = models.PatientTest.calc_core_strength(object)
    postural_analysis = models.PatientTest.calc_postural_analysis(object)
    fat_mass = models.PatientTest.calc_fat_mass(object)
    body_mass_index = models.PatientTest.calc_body_mass_index(object)
    move_grade = models.PatientTest.calc_move_grade(object)

    blood_pressure = models.PatientTest.calc_blood_pressure(object)
    print(blood_pressure)
    resting_heart_rate = models.PatientTest.calc_resting_heart_rate(object)
    rest_grade = models.PatientTest.calc_rest_grade(object)

    coherence_value = models.PatientTest.calc_coherence_value(object)
    co2_tolerance = models.PatientTest.calc_co2_tolerance(object)
    connect_grade = models.PatientTest.calc_connect_grade(object)

    # Stores above data into category lists then gets average and sends to chart
    nourishdata = [ int(fasting_glucose), int(hga1c), int(cprotein), int(homocysteine), int(fasting_insulin), int(ldl_particle),
    int(ldl_size), int(insulin_resistance), int(testosterone), int(thyroid), int(vitamin_d3), int(vitamin_b12), 
    int(zinc_rbc), int(magnesium_rbc), int(omega3_index), int(nourish_grade) ]
    nourish_average = sum(nourishdata) / len(nourishdata)

    movedata = [int(joint_mobility), int(muscle_flexibility), int(core_strength), int(postural_analysis), int(fat_mass),
    int(body_mass_index), int(move_grade)]
    move_average = sum(movedata) / len(movedata)

    restdata = [int(blood_pressure), int(resting_heart_rate), int(rest_grade)]
    rest_average = sum(restdata) / len(movedata)

    connectdata = [ int(coherence_value), int(co2_tolerance), int(connect_grade)]
    connect_average = sum(connectdata) / len(connectdata)


    data = [nourish_average, move_average, rest_average, connect_average]
    labels = ['Nourish: Metabolic Fitness', 'Move: Physical Fitness', 'Rest: Mental Fitness', 'Connect: Emotional Fitness']



    # print(fasting_glucose)
    context = {
        'fasting_glucose': fasting_glucose, 'hga1c': hga1c,
        'cprotein': cprotein, 'homocysteine': homocysteine,
        'fasting_insulin': fasting_insulin, 'ldl_particle': ldl_particle,
        'ldl_size': ldl_size, 'insulin_resistance': insulin_resistance,
        'testosterone': testosterone, 'thyroid': thyroid,
        'vitamin_d3': vitamin_d3, 'vitamin_b12': vitamin_b12,
        'zinc_rbc': zinc_rbc, 'magnesium_rbc': magnesium_rbc,
        'omega3_index': omega3_index, 'nourish_grade': nourish_grade,
        'joint_mobility': joint_mobility, 'muscle_flexibility': muscle_flexibility,
        'core_strength': core_strength, 'postural_analysis': postural_analysis,
        'fat_mass': fat_mass, 'body_mass_index': body_mass_index,
        'move_grade': move_grade, 'blood_pressure': blood_pressure,
        'resting_heart_rate': resting_heart_rate, 'rest_grade': rest_grade,
        'coherence_value': coherence_value, 'co2_tolerance': co2_tolerance,
        'connect_grade': connect_grade, 'labels':labels, 'data':data
    }
            
    return render(request, 'testresults/testresults.html', context)


# Need to add a check for people typing in the url and resubmitting, creates extra categories.


@login_required(login_url='../login/')
def onboarding(request):
    # Stores questions for user made in signals.py from user creation
    question_list = models.FormQuestion.objects.filter(user=request.user)

    if request.POST:
        checked_questions = request.POST.getlist("question_true")

        for question_id in checked_questions:
            question = models.FormQuestion.objects.get(id=int(question_id))
            question.answer = True
            question.save()

        # After question answers are saved, we calculate and store the users score from the intake form in Progress
        usercategories = ['Connect', 'Nourish', 'Challenge', 'Spark', 'Learn', 'Move', 'Rest']
        
        for category in usercategories:
            category_score = calc_category_score(category, request)
            models.Progress.objects.create(category=category, score=category_score, belt='None', user=request.user)
        
        return redirect('onboarding2')

    return render(request, 'onboarding/onboarding.html', {"question_list":question_list})

@login_required(login_url='../login/')
def onboarding2(request):
    # Stores questions for user made in signals.py from user creation
    question_list = models.FormQuestion.objects.filter(user=request.user)

    if request.POST:
        checked_questions = request.POST.getlist("question_true")

        for question_id in checked_questions:
            question = models.FormQuestion.objects.get(id=int(question_id))
            question.answer = True
            question.save()

        # After question answers are saved, we calculate and store the users score from the intake form in Progress
        usercategories = ['Connect', 'Nourish', 'Challenge', 'Spark', 'Learn', 'Move', 'Rest']
        
        for category in usercategories:
            category_score = calc_category_score(category, request)
            obj = models.Progress.objects.get(category=category, belt='None', user=request.user)
            obj.score = category_score
            obj.save()
        
        return redirect('onboarding3')

    return render(request, 'onboarding/onboarding2.html', {"question_list":question_list})

@login_required(login_url='../login/')
def onboarding3(request):
    # Stores questions for user made in signals.py from user creation
    question_list = models.FormQuestion.objects.filter(user=request.user)

    if request.POST:
        checked_questions = request.POST.getlist("question_true")

        for question_id in checked_questions:
            question = models.FormQuestion.objects.get(id=int(question_id))
            question.answer = True
            question.save()

        # After question answers are saved, we calculate and store the users score from the intake form in Progress
        usercategories = ['Connect', 'Nourish', 'Challenge', 'Spark', 'Learn', 'Move', 'Rest']
        
        for category in usercategories:
            category_score = calc_category_score(category, request)
            obj = models.Progress.objects.get(category=category, belt='None', user=request.user)
            obj.score = category_score
            obj.save()

        return redirect('onboarding4')

    return render(request, 'onboarding/onboarding3.html', {"question_list":question_list})



@login_required(login_url='../login/')
def onboarding4(request):
    # Stores questions for user made in signals.py from user creation
    question_list = models.FormQuestion.objects.filter(user=request.user)

    if request.POST:
        checked_questions = request.POST.getlist("question_true")

        for question_id in checked_questions:
            question = models.FormQuestion.objects.get(id=int(question_id))
            question.answer = True
            question.save()

        # After question answers are saved, we calculate and store the users score from the intake form in Progress
        usercategories = ['Connect', 'Nourish', 'Challenge', 'Spark', 'Learn', 'Move', 'Rest']
        
        for category in usercategories:
            category_score = calc_category_score(category, request)
            obj = models.Progress.objects.get(category=category, belt='None', user=request.user)
            obj.score = category_score
            obj.save()

        return redirect('onboarding5')

    return render(request, 'onboarding/onboarding4.html', {"question_list":question_list})



@login_required(login_url='../login/')
def onboarding5(request):
    # Stores questions for user made in signals.py from user creation
    question_list = models.FormQuestion.objects.filter(user=request.user)

    if request.POST:
        checked_questions = request.POST.getlist("question_true")

        for question_id in checked_questions:
            question = models.FormQuestion.objects.get(id=int(question_id))
            question.answer = True
            question.save()

        # After question answers are saved, we calculate and store the users score from the intake form in Progress
        usercategories = ['Connect', 'Nourish', 'Challenge', 'Spark', 'Learn', 'Move', 'Rest']
        
        for category in usercategories:
            category_score = calc_category_score(category, request)
            obj = models.Progress.objects.get(category=category, belt='None', user=request.user)
            obj.score = category_score
            obj.save()

        return redirect('onboarding6')

    return render(request, 'onboarding/onboarding5.html', {"question_list":question_list})



@login_required(login_url='../login/')
def onboarding6(request):
    # Stores questions for user made in signals.py from user creation
    question_list = models.FormQuestion.objects.filter(user=request.user)

    if request.POST:
        checked_questions = request.POST.getlist("question_true")

        for question_id in checked_questions:
            question = models.FormQuestion.objects.get(id=int(question_id))
            question.answer = True
            question.save()

        # After question answers are saved, we calculate and store the users score from the intake form in Progress
        usercategories = ['Connect', 'Nourish', 'Challenge', 'Spark', 'Learn', 'Move', 'Rest']
        
        for category in usercategories:
            category_score = calc_category_score(category, request)
            obj = models.Progress.objects.get(category=category, belt='None', user=request.user)
            obj.score = category_score
            obj.save()

        return redirect('onboarding7')

    return render(request, 'onboarding/onboarding6.html', {"question_list":question_list})


@login_required(login_url='../login/')
def onboarding7(request):
    # Stores questions for user made in signals.py from user creation
    question_list = models.FormQuestion.objects.filter(user=request.user)

    if request.POST:
        checked_questions = request.POST.getlist("question_true")

        for question_id in checked_questions:
            question = models.FormQuestion.objects.get(id=int(question_id))
            question.answer = True
            question.save()

        # After question answers are saved, we calculate and store the users score from the intake form in Progress
        usercategories = ['Connect', 'Nourish', 'Challenge', 'Spark', 'Learn', 'Move', 'Rest']
        
        for category in usercategories:
            category_score = calc_category_score(category, request)
            obj = models.Progress.objects.get(category=category, belt='None', user=request.user)
            obj.score = category_score
            obj.save()
        
        user = request.user
        user.onboarding_complete = True
        user.save()

        
        return redirect('onboarding_results')

    return render(request, 'onboarding/onboarding7.html', {"question_list":question_list})

@login_required
def onboarding_results(request):
    data_none = []
    labels_none = []

    queryset_initial = models.Progress.objects.filter(user=request.user, belt='None').order_by('category')
    for entry in queryset_initial:
        labels_none.append(entry.category)
        data_none.append(entry.score)
    
    context = {'data_none': data_none, 'labels_none': labels_none}
    #query onboarding score
    #create context from query similar to progress view
    if request.POST:
        return ('home')

    return render(request, 'onboarding/onboarding_results.html', context)

@login_required
def biomarker_entry(request):
    user = request.user
    if user.program != 'Tailored Trailblazer':
        return redirect('home')

    if request.POST:
        form = forms.TestForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.patient=request.user.id
            form.save()
            return redirect('home')
    else:
        form = forms.TestForm(initial={'patient':request.user.id})

    return render(request, 'biomarker/user_entry.html', {"form":form})




@login_required(login_url='../login/')
def afterbeltform(request):
    
    question_list = models.FormQuestion.objects.filter(answer=False, user=request.user)
    new_belt = current_belt(request)
    if request.POST:
        # Will need to change this to a certain amount of questions else will show too many
        belts = models.Belt.objects.filter(user=request.user).order_by('id')
        print(belts)
        counter = 0
        for belt in belts:
            if belt.completed == True:
                counter += 1
        previous_belt = belts[counter - 1]

        checked_questions = request.POST.getlist("question_true")
        for question_id in checked_questions:
            question = models.FormQuestion.objects.get(id=int(question_id))
            question.answer = True
            question.save()

        # Stores Progress instance and updates the new score from user completing intermediate form
        
        usercategories = ['Connect', 'Nourish', 'Challenge', 'Spark', 'Learn', 'Move', 'Rest']
        for category in usercategories:
            category_score = calc_category_score(category, request)
            object = models.Progress.objects.create(score=category_score, belt=previous_belt, category=category, user=request.user)
            
        return redirect('home')
    return render(request, 'afterbeltform/afterbeltform.html', {"question_list":question_list})



@login_required(login_url='../login/')
def welcome(request):
    return render(request, 'welcome/welcome.html')

def wlkthru_spark(request):
    return render(request, 'walkthrough/spark.html')

def wlkthru_rest(request):
    return render(request, 'walkthrough/rest.html')

def wlkthru_nourish(request):
    return render(request, 'walkthrough/nourish.html')

def wlkthru_move(request):
    return render(request, 'walkthrough/move.html')

def wlkthru_learn(request):
    return render(request, 'walkthrough/learn.html')

def wlkthru_connect(request):
    return render(request, 'walkthrough/connect.html')

def wlkthru_challenge(request):
    return render(request, 'walkthrough/challenge.html')

def wlkthru_continue(request):
    return render(request, 'walkthrough/continue.html')

def wlkthru_start(request):
    return render(request, 'walkthrough/start.html')



@login_required
def wlkthru_home(request):
    if request.POST:
        return redirect('wlkthrough_task')
    return render(request, 'walkthrough/home.html')

@login_required
def wlkthru_task(request):
    
    user_belt = current_belt(request)
    task_list = models.Task.objects.filter(category__category_type='Spark',belt__belt_colour=user_belt, user=request.user)
    
    
    if request.POST:

        #Stores task ids that were selected in html checkboxes
        checked_tasks = request.POST.getlist("task_complete")

        for task_id in checked_tasks:
            task = models.Task.objects.get(id=int(task_id))
            task.completed = True
            task.save()
         
        #Allows users do undo task completion
        #Opposite to above logic
        unchecked_tasks = request.POST.getlist("task_incomplete")

        for task_id in unchecked_tasks:
            task = models.Task.objects.get(id=int(task_id))
            task.completed = False
            task.save()
            
        return redirect('wlkthru_task')

    return render(request, 'walkthrough/task.html', {'task_list': task_list})

@login_required
def wlkthru_progress(request):
    if request.POST:
        return redirect('wlkthru_complete')
    return render(request,'walkthrough/progress.html')

def wlkthru_complete(request):
    # undoing any tasks marked complete in walkthrough
    user_belt = current_belt(request)
    task_list = models.Task.objects.filter(category__category_type='Spark',belt__belt_colour=user_belt, user=request.user, completed=True)
    for task in task_list:
        task.completed = False
        task.save()

    if request.POST:
        return redirect('home')

    return render(request,'walkthrough/complete.html')


@login_required
def connect(request):
    #current_belt = current_belt(request)
    #Stores all tasks in associated category for context
    
    user_belt = current_belt(request)
    task_list = models.Task.objects.filter(category__category_type='Connect',belt__belt_colour=user_belt, user=request.user)
    
    
    if request.POST:

        #Stores task ids that were selected in html checkboxes
        checked_tasks = request.POST.getlist("task_complete")

        for task_id in checked_tasks:
            task = models.Task.objects.get(id=int(task_id))
            task.completed = True
            task.save()
            #Function in logic.py to update category completion
            # Saves into variable new_belt, returns True if user unlocks new belt, returns None if not
            new_belt = category_completion('Connect', task.category.id, user_belt, request)
            # print(new_belt) # Debugging
            # if user is on new belt, prompts user to answer some additional questions from intake form
            # scores update upon form completion, tracking their progress
            if new_belt == True:
                return redirect('afterbeltform')
        #Allows users do undo task completion
        #Opposite to above logic
        unchecked_tasks = request.POST.getlist("task_incomplete")

        for task_id in unchecked_tasks:
            task = models.Task.objects.get(id=int(task_id))
            task.completed = False
            task.save()
            category_completion('Connect', task.category.id, user_belt, request)
        return redirect('connect')
    
    return render(request, 'task_categories/connect/connect.html', {"task_list":task_list})

    
@login_required
def move(request):
    user_belt = current_belt(request)
    task_list = models.Task.objects.filter(category__category_type='Move', belt__belt_colour=user_belt, user=request.user)
    
    if request.POST:

        checked_tasks = request.POST.getlist("task_complete")

        for task_id in checked_tasks:
            #task = models.Task.objects.get(request, "task_complete")
            task = models.Task.objects.get(id=int(task_id))
            task.completed = True
            task.save()
            new_belt = category_completion('Move', task.category.id, user_belt, request)
            if new_belt == True:
                return redirect('afterbeltform')
        
        #Allows users do undo task
        unchecked_tasks = request.POST.getlist("task_incomplete")

        for task_id in unchecked_tasks:
            task = models.Task.objects.get(id=int(task_id))
            task.completed = False
            task.save()
            category_completion('Move', task.category.id, user_belt, request)

        return redirect('move')

    return render(request, 'task_categories/move/move.html', {"task_list":task_list})


@login_required
def rest(request):
    user_belt = current_belt(request)
    task_list = models.Task.objects.filter(category__category_type='Rest', belt__belt_colour=user_belt, user=request.user)
    
    if request.POST:

        checked_tasks = request.POST.getlist("task_complete")

        for task_id in checked_tasks:
            #task = models.Task.objects.get(request, "task_complete")
            task = models.Task.objects.get(id=int(task_id))
            task.completed = True
            task.save()
            new_belt = category_completion('Rest', task.category.id, user_belt, request)
            if new_belt == True:
                return redirect('afterbeltform')        
        #Allows users do undo task
        unchecked_tasks = request.POST.getlist("task_incomplete")

        for task_id in unchecked_tasks:
            task = models.Task.objects.get(id=int(task_id))
            task.completed = False
            task.save()
            category_completion('Rest', task.category.id, user_belt, request)
        return redirect('rest')

    return render(request, 'task_categories/rest/rest.html', {"task_list":task_list})


@login_required
def nourish(request):
    user_belt = current_belt(request)
    task_list = models.Task.objects.filter(category__category_type='Nourish', belt__belt_colour=user_belt, user=request.user)
    
    if request.POST:
        checked_tasks = request.POST.getlist("task_complete")
        for task_id in checked_tasks:
            #task = models.Task.objects.get(request, "task_complete")
            task = models.Task.objects.get(id=int(task_id))
            task.completed = True
            task.save()
            new_belt = category_completion('Nourish', task.category.id, user_belt, request)
            if new_belt == True:
                return redirect('afterbeltform')
        #Allows users do undo task
        unchecked_tasks = request.POST.getlist("task_incomplete")

        for task_id in unchecked_tasks:
            task = models.Task.objects.get(id=int(task_id))
            task.completed = False
            task.save()
            category_completion('Nourish', task.category.id, user_belt, request)
        return redirect('nourish')

    return render(request, 'task_categories/nourish/nourish.html', {"task_list":task_list})


@login_required
def challenge(request):
    user_belt = current_belt(request)
    task_list = models.Task.objects.filter(category__category_type='Challenge', belt__belt_colour=user_belt, user=request.user)
    
    if request.POST:

        checked_tasks = request.POST.getlist("task_complete")

        for task_id in checked_tasks:
            #task = models.Task.objects.get(request, "task_complete")
            task = models.Task.objects.get(id=int(task_id))
            task.completed = True
            task.save()
            new_belt = category_completion('Challenge', task.category.id, user_belt, request)
            if new_belt == True:
                return redirect('afterbeltform')
        #Allows users do undo task
        unchecked_tasks = request.POST.getlist("task_incomplete")

        for task_id in unchecked_tasks:
            task = models.Task.objects.get(id=int(task_id))
            task.completed = False
            task.save()
            category_completion('Challenge', task.category.id, user_belt, request)

        return redirect('challenge')

    return render(request, 'task_categories/challenge/challenge.html', {"task_list":task_list})


@login_required
def spark(request):
    user_belt = current_belt(request)
    task_list = models.Task.objects.filter(category__category_type='Spark', belt__belt_colour=user_belt, user=request.user)
    
    if request.POST:
        checked_tasks = request.POST.getlist("task_complete")
        for task_id in checked_tasks:
            task = models.Task.objects.get(id=int(task_id))
            task.completed = True
            task.save()
            new_belt = category_completion('Spark', task.category.id, user_belt, request)
            if new_belt == True:
                return redirect('afterbeltform')

        #Allows users do undo task
        unchecked_tasks = request.POST.getlist("task_incomplete")

        for task_id in unchecked_tasks:
            task = models.Task.objects.get(id=int(task_id))
            task.completed = False
            task.save()
            category_completion('Spark', task.category.id, user_belt, request)
        return redirect('spark')

    return render(request, 'task_categories/spark/spark.html', {"task_list":task_list})


@login_required
def learn(request):
    user_belt = current_belt(request)
    task_list = models.Task.objects.filter(category__category_type='Learn', belt__belt_colour=user_belt, user=request.user)
    
    if request.POST:

        checked_tasks = request.POST.getlist("task_complete")

        for task_id in checked_tasks:
            task = models.Task.objects.get(id=int(task_id))
            task.completed = True
            task.save()
            new_belt = category_completion('Learn', task.category.id, user_belt, request)
            if new_belt == True:
                return redirect('afterbeltform')

        #Allows users do undo task
        unchecked_tasks = request.POST.getlist("task_incomplete")

        for task_id in unchecked_tasks:
            task = models.Task.objects.get(id=int(task_id))
            task.completed = False
            task.save()
            category_completion('Learn', task.category.id, user_belt, request)

        return redirect('learn')

    return render(request, 'task_categories/learn/learn.html', {"task_list":task_list})
    


                
        