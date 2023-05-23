from .models import CustomUser, Belt, Category, Task, FormQuestion, Progress, MCFormQuestion
from django.shortcuts import render, redirect


"""
# category completed function
task_count = models.Task.objects.filter(category__category_type='Connect', user=request.user).count()
    completed_task_count = models.Task.objects.filter(category__category_type='Connect', completed=True, user=request.user).count()
    for category_id in categories
    if task_count == completed_task_count:
        category = models.Category.objects.get(id=int(category_id))
        category.completed = True
        category.save()
"""

# belt completion function

def belt_completion(category, current_belt, request):
    category_count = Category.objects.filter(belt__belt_colour=current_belt, user=request.user).count()
    comp_category_count = Category.objects.filter(belt__belt_colour=current_belt, completed=True, user=request.user).count()
    belt_id = category.belt.id
    belt = Belt.objects.get(id=belt_id)
    if comp_category_count == category_count:
        belt.completed = True
        belt.save()
        return True
    elif comp_category_count != category_count:
        belt.completed = False
        belt.save()
    return

# category completed function

def category_completion(category_input, category_id, current_belt, request):
    task_count = Task.objects.filter(category__category_type=category_input, belt__belt_colour=current_belt, user=request.user).count()
    comp_task = Task.objects.filter(category__category_type=category_input, belt__belt_colour=current_belt, completed=True, user=request.user).count()
    category = Category.objects.get(id=category_id)
    if task_count == comp_task:
        category.completed = True
        category.save()
    elif task_count != comp_task:
        category.completed = False
        category.save()
    new_belt = belt_completion(category, current_belt, request)
    if new_belt == True:
        return True
    else:
        return

# Returns Users Current Belt

def current_belt(request):

    belts = Belt.objects.filter(user=request.user)
    for belt in belts:
        if belt.completed == False:
            current_belt = belt
            return current_belt


# Calculates total score for user to an integer 0 - 10
def calc_total_score(request):
    totfieldcount = FormQuestion.objects.filter(user=request.user).count()
    truecount = FormQuestion.objects.filter(answer=True, user=request.user).count()

    score = round(truecount / totfieldcount * 10)

    # Build a way for this number to be stored in database while also being able to later reference category and belt?
    # Need to fetch data to track users progress as they go through the program
    # Brainstorm how we want to show data from previous, maybe as a line graph? in this case we can do belts on x axis and score on y axis
    # print(score) # Debugging
    return score

# Calculates score for given user category to an integer 0 - 10
def calc_category_score(usercategory, request):
    categoryfieldcount = FormQuestion.objects.filter(category=usercategory, user=request.user).count() # Multiple Choice >+ MCFormQuestion.objects.filter(category=usercategory, user=request.user).count()
    truecount = (FormQuestion.objects.filter(category=usercategory, answer=True ,user=request.user).count()) # Multiple Choice >+ (MCFormQuestion.objects.filter(answer=1 category=usercategory, user=request.user).count() * 4) + (MCFormQuestion.objects.filter(answer=2 category=usercategory, user=request.user).count() * 3) + (MCFormQuestion.objects.filter(answer=3 category=usercategory, user=request.user).count() * 2) + (MCFormQuestion.objects.filter(answer=4 category=usercategory, user=request.user).count() * 1) 





    userscore = round(truecount / categoryfieldcount * 10)

    
    return userscore


    
        


