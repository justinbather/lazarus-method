from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, AbstractUser
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


# Create your models here.

class CustomUser(AbstractUser):
    
    EMPOWERED_EXPLORER = "Empowered Explorer"
    TAILORED_TRAILBLAZER = "Tailored Trailblazer"
    PERSONALIZED_PATHFINDER = "Personalized Pathfinder"

    PROGRAMLIST = [
        (EMPOWERED_EXPLORER, _('Empowered Explorer')),
        (TAILORED_TRAILBLAZER, _('Tailored Trailblazer')),
        (PERSONALIZED_PATHFINDER, _('Personalized Pathfinder'))
    ]

    username = None
    program = models.CharField(max_length=28, choices=PROGRAMLIST, unique=False, blank=False)
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(max_length=30, unique=False)
    last_name = models.CharField(max_length=30, unique=False)
    is_admin = models.BooleanField(default=False)
    onboarding_complete = models.BooleanField(default=False)

    # Add new fields as needed

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

class Progress(models.Model):
    NOURISH = 'Nourish'
    MOVE = 'Move'
    REST = 'Rest'
    CONNECT = 'Connect'
    LEARN = 'Learn'
    SPARK = 'Spark'
    CHALLENGE = 'Challenge'

    # Defines Choices
    CATEGORIES = [
        (NOURISH, _('Nourish')),
        (MOVE, _('Move')),
        (REST, _('Rest')),
        (CONNECT, _('Connect')),
        (LEARN, _('Learn')),
        (SPARK, _('Spark')),
        (CHALLENGE, _('Challenge'))
    ]

    WHITE = 'White'
    YELLOW = 'Yellow'
    GREEN = 'Green'
    BLUE = 'Blue'
    ORANGE = 'Orange'
    PURPLE = 'Purple'
    NONE = 'None'

    # Defines Colour Choices in Belt Table
    BELTCOLOURS = [
        (WHITE, _('White')),
        (YELLOW, _('Yellow')),
        (GREEN, _('Green')),
        (BLUE, _('Blue')),
        (ORANGE, _('Orange')),
        (PURPLE, _('Purple')),
        (NONE, _('None'))
    ]

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    belt = models.CharField(max_length=10, choices=BELTCOLOURS)
    category = models.CharField(max_length=15, choices=CATEGORIES)
    score = models.IntegerField()

    def __str__(self):
        return str(self.belt)
    
    # Need a method to return score for queries and redo __Str__ so it returns useful info for admin

class MCFormQuestion(models.Model):
    NOURISH = 'Nourish'
    MOVE = 'Move'
    REST = 'Rest'
    CONNECT = 'Connect'
    LEARN = 'Learn'
    SPARK = 'Spark'
    CHALLENGE = 'Challenge'

    # Defines Choices
    CATEGORIES = [
        (NOURISH, _('Nourish')),
        (MOVE, _('Move')),
        (REST, _('Rest')),
        (CONNECT, _('Connect')),
        (LEARN, _('Learn')),
        (SPARK, _('Spark')),
        (CHALLENGE, _('Challenge'))
    ]

    MC_ANSWERS = [
        (1, _('1')),
        (2, _('2')),
        (3, _('3')),
        (4, _('4'))
    ]

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    question = models.CharField(max_length=100)
    answer = models.IntegerField(choices=MC_ANSWERS, blank=False)
    category = models.CharField(max_length=15, choices=CATEGORIES)

    def __str__(self):
        return self.question


class FormQuestion(models.Model):
    WHITE = 'White'
    YELLOW = 'Yellow'
    GREEN = 'Green'
    BLUE = 'Blue'
    ORANGE = 'Orange'
    PURPLE = 'Purple'

    # Defines Colour Choices in Belt Table
    BELTCOLOURS = [
        (WHITE, _('White')),
        (YELLOW, _('Yellow')),
        (GREEN, _('Green')),
        (BLUE, _('Blue')),
        (ORANGE, _('Orange')),
        (PURPLE, _('Purple'))
    ]

    # Defines Category Types
    NOURISH = 'Nourish'
    MOVE = 'Move'
    REST = 'Rest'
    CONNECT = 'Connect'
    LEARN = 'Learn'
    SPARK = 'Spark'
    CHALLENGE = 'Challenge'

    # Defines Choices
    CATEGORIES = [
        (NOURISH, _('Nourish')),
        (MOVE, _('Move')),
        (REST, _('Rest')),
        (CONNECT, _('Connect')),
        (LEARN, _('Learn')),
        (SPARK, _('Spark')),
        (CHALLENGE, _('Challenge'))
    ]

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    question = models.CharField(max_length=100)
    answer = models.BooleanField(default=False)
    category = models.CharField(max_length=15, choices=CATEGORIES, blank=False)
    
    # belt = models.CharField(max_length=10, choices=BELTCOLOURS, blank=False)

    # Need to add belt choices to this model, give calc category score functions userbelt, build progress page

    def __str__(self):
        return self.question

class UserEntryPatientTest(models.Model):
    MALE = 'Male'
    FEMALE = 'Female'
    GENDERS = [
        (MALE, _('Male')),
        (FEMALE, _('Female'))
    ]

    GRADE = [
        (10, _('10')),
        (7, _('7')),
        (5, _('5')),
        (3, _('3')),
        (1, _('1'))
    ]

    EXAMNUM = [
        (1,_('1')),
        (2, _('2'))
    ]

    patient = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    exam_date = models.DateField(default=timezone.now)
    exam_number = models.IntegerField(choices= EXAMNUM, verbose_name='Exam Number', default=1)
    gender = models.CharField(max_length=10, choices=GENDERS, blank=False)
    weight = models.DecimalField(verbose_name='Weight (lbs)', max_digits=6, decimal_places=2, blank=False)
    age = models.IntegerField(blank=False)
    height = models.IntegerField(verbose_name='Height (inches)', blank=True, null=True)

    #biomarkers
    fasting_glucose = models.IntegerField(verbose_name='Fasting Glucose', blank=False)
    hga1c = models.IntegerField(verbose_name='HgA1c', blank=False)
    cprotein = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='C Reactive Protein', blank=False)
    homocysteine = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Homocysteine', blank=False)
    fasting_insulin = models.IntegerField(verbose_name='Fasting Insulin', blank=False)
    ldl_particle = models.IntegerField(verbose_name='LDL Particle Number', blank=False)
    ldl_size = models.IntegerField(verbose_name='LDL Size', blank=False)
    insulin_resistance = models.DecimalField(max_digits=4, decimal_places=2, verbose_name='Insulin Resistance Score', blank=False)
    testosterone = models.IntegerField(choices=GRADE, verbose_name='Testosterone', blank=False)
    thyroid = models.IntegerField(choices=GRADE, verbose_name='Thyroid Stimulating Hormone', blank=False)
    vitamin_d3 = models.IntegerField(verbose_name='Vitamin D3', blank=False)
    vitamin_b12 = models.IntegerField(verbose_name='Vitamin B12', blank=False)
    zinc_rbc = models.IntegerField(verbose_name='Zinc RBC', blank=False)
    magnesium_rbc = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Magnesium RBC', blank=False)
    omega3_index = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Omega 3 Index', blank=False)



class PatientTest(models.Model):
    # Gender Choices
    MALE = 'Male'
    FEMALE = 'Female'
    GENDERS = [
        (MALE, _('Male')),
        (FEMALE, _('Female'))
    ]

    # Defining grade choices
    """
    5 = '5'
    4 = '4'
    3 = '3'
    2 = '2'
    1 = '1'
    """

    GRADE = [
        (10, _('10')),
        (7, _('7')),
        (5, _('5')),
        (3, _('3')),
        (1, _('1'))
    ]

    EXAMNUM = [
        (1,_('1')),
        (2, _('2'))
    ]
    patient = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    # weight_grade
    exam_date = models.DateField(default=timezone.now)
    exam_number = models.IntegerField(choices= EXAMNUM, verbose_name='Exam Number', default=1)
    gender = models.CharField(max_length=10, choices=GENDERS, blank=False)
    weight = models.DecimalField(verbose_name='Weight (lbs)', max_digits=6, decimal_places=2, blank=False)
    age = models.IntegerField(blank=False)
    height = models.IntegerField(verbose_name='Height (inches)', blank=True, null=True)


    #Nourish biomarkers
    fasting_glucose = models.IntegerField(verbose_name='Fasting Glucose', blank=True)
    hga1c = models.IntegerField(verbose_name='HgA1c', blank=True)
    cprotein = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='C Reactive Protein', blank=True)
    homocysteine = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Homocysteine', blank=True)
    fasting_insulin = models.IntegerField(verbose_name='Fasting Insulin', blank=True)
    ldl_particle = models.IntegerField(verbose_name='LDL Particle Number', blank=True)
    ldl_size = models.IntegerField(verbose_name='LDL Size', blank=True)
    insulin_resistance = models.DecimalField(max_digits=4, decimal_places=2, verbose_name='Insulin Resistance Score', blank=True)
    testosterone = models.IntegerField(choices=GRADE, verbose_name='Testosterone', blank=True)
    thyroid = models.IntegerField(choices=GRADE, verbose_name='Thyroid Stimulating Hormone', blank=True)
    vitamin_d3 = models.IntegerField(verbose_name='Vitamin D3', blank=True)
    vitamin_b12 = models.IntegerField(verbose_name='Vitamin B12', blank=True)
    zinc_rbc = models.IntegerField(verbose_name='Zinc RBC', blank=True)
    magnesium_rbc = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Magnesium RBC', blank=True)
    omega3_index = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Omega 3 Index', blank=True)
    nourish_grade = models.IntegerField(verbose_name='Nourish Grade', choices=GRADE, blank=True, null=True)
    # Come back to nourish_grade not sure if need to have this or not since its self assesment from onboarding form

    # Move Biomarkers
    joint_mobility = models.IntegerField(verbose_name='Joint Mobility', choices=GRADE, blank=True)
    muscle_flexibility = models.IntegerField(verbose_name='Muscle Flexibility', choices=GRADE, blank=True)
    core_strength = models.IntegerField(verbose_name='Core Strength', choices=GRADE, blank=True)
    postural_analysis = models.IntegerField(verbose_name='Postural Analysis', choices=GRADE, blank=True)
    fat_mass = models.IntegerField(verbose_name='Fat Mass', blank=True)
    body_mass_index = models.IntegerField(choices=GRADE, verbose_name='Body Mass Index', blank=True)
    move_grade = models.IntegerField(verbose_name='Move Grade', choices=GRADE, blank=True)
    # Come back to this grade too

    # Rest Biomarkers
    #blood_pressure = models.IntegerField(verbose_name='Blood Pressure', choices=GRADE, blank=True)
    systolic = models.IntegerField(verbose_name='Systolic BP', blank=True)
    diastolic = models.IntegerField(verbose_name='Diastolic BP', blank=True)
    resting_heart_rate = models.IntegerField(verbose_name='Resting Heart Rate', blank=True)
    rest_grade = models.IntegerField(verbose_name='Rest Grade', choices=GRADE, blank=True)
    # Come back to this grade too

    # Connect Biomarkers
    coherence_value = models.DecimalField(max_digits=4, decimal_places=2, verbose_name='Coherence Value', blank=True)
    co2_tolerance = models.IntegerField(verbose_name='CO2 Tolerance', blank=True)
    connect_grade = models.IntegerField(verbose_name='Connect Grade', choices=GRADE, blank=True)
    # Come Back to this grade

    def __str__(self):
        return self.patient.first_name + " " + self.patient.last_name

    #Nourish Calculations

    def calc_fasting_glucose(self):
        if self.fasting_glucose <= 90:
            score = 10
        elif self.fasting_glucose > 90 or self.fasting_glucose <= 99:
            score = 7
        elif self.fasting_glucose > 99 or self.fasting_glucose <= 109:
            score = 5
        elif self.fasting_glucose > 109 or self.fasting_glucose <= 119:
            score = 3
        elif self.fasting_glucose > 119:
            score = 1
        return score
    
    def calc_hga1c(self):
        if self.hga1c <= 5.4:
            score = 10
        elif self.hga1c > 5.4 or self.hga1c <= 5.7:
            score = 7
        elif self.hga1c > 5.7 or self.hga1c <= 6.0:
            score = 5
        elif self.hga1c > 6.0 or self.hga1c <= 6.2:
            score = 3
        elif self.hga1c > 6.2:
            score = 1
        return score
    
    def calc_cprotein(self):
        if self.cprotein <= .5:
            score = 10
        elif self.cprotein > .5 or self.cprotein <= 1.0:
            score = 7
        elif self.cprotein > 1.0 or self.cprotein <= 2.0:
            score = 5
        elif self.cprotein > 2.0 or self.cprotein <= 3.0:
            score = 3
        elif self.cprotein > 3.1:
            score = 1
        return score

    def calc_homocysteine(self):
        if self.homocysteine <= 7:
            score = 10
        elif self.homocysteine > 7 or self.homocysteine <= 9:
            score = 7
        elif self.homocysteine > 9 or self.homocysteine <= 11:
            score = 5
        elif self.homocysteine > 11 or self.homocysteine <= 13:
            score = 3
        elif self.homocysteine > 13:
            score = 1
        return score

    def calc_fasting_insulin(self):
        if self.fasting_insulin <= 4:
            score = 10
        elif self.fasting_insulin > 4 or self.fasting_insulin <= 7:
            score = 7
        elif self.fasting_insulin > 7 or self.fasting_insulin <= 10:
            score = 5
        elif self.fasting_insulin > 10 or self.fasting_insulin <= 20:
            score = 3
        elif self.fasting_insulin > 20:
            score = 1
        return score
    
    def calc_ldl_particle(self):
        if self.ldl_particle <= 999:
            score = 10
        elif self.ldl_particle > 999 or self.ldl_particle <= 1299:
            score = 7
        elif self.ldl_particle > 1299 or self.ldl_particle <= 2000:
            score = 5
        elif self.ldl_particle > 2000 or self.ldl_particle <= 2999:
            score = 3
        elif self.ldl_particle > 3000:
            score = 1
        return score

    def calc_ldl_size(self):
        if self.ldl_size >= 24:
            score = 10
        elif self.ldl_size < 24 or self.ldl_size >= 22:
            score = 7
        elif self.ldl_size < 22 or self.ldl_size >= 20:
            score = 5
        elif self.ldl_size < 20 or self.ldl_size >= 18:
            score = 3
        elif self.ldl_size < 18:
            score = 1
        return score

    def calc_insulin_resistance(self):
        if self.insulin_resistance <= 20:
            score = 10
        elif self.insulin_resistance > 20 or self.insulin_resistance <= 27:
            score = 7
        elif self.insulin_resistance > 27 or self.insulin_resistance <= 45:
            score = 5
        elif self.insulin_resistance > 45 or self.insulin_resistance <= 62:
            score = 3
        elif self.insulin_resistance > 63:
            score = 1
        return score

    def calc_testosterone(self):
        return str(self.testosterone)
    
    def calc_thyroid(self):
        return str(self.thyroid)

    def calc_vitamin_d3(self):
        if self.vitamin_d3 >= 60:
            score = 10
        elif self.vitamin_d3 < 60 or self.vitamin_d3 >= 50:
            score = 7
        elif self.vitamin_d3 < 50 or self.vitamin_d3 >= 40:
            score = 5
        elif self.vitamin_d3 < 40 or self.vitamin_d3 >= 30:
            score = 3
        elif self.vitamin_d3 < 30:
            score = 1
        return score

    def calc_vitamin_b12(self):
        if self.vitamin_b12 >= 1200:
            score = 10
        elif self.vitamin_b12 < 1200 or self.vitamin_b12 >= 900:
            score = 7
        elif self.vitamin_b12 < 900 or self.vitamin_b12 >= 600:
            score = 5
        elif self.vitamin_b12 < 600 or self.vitamin_b12 >= 233:
            score = 3
        elif self.vitamin_b12 < 233:
            score = 1
        return score

    def calc_zinc_rbc(self):
        if self.zinc_rbc >= 1500:
            score = 10
        elif self.zinc_rbc < 1500 or self.zinc_rbc >= 1300:
            score = 7
        elif self.zinc_rbc < 1300 or self.zinc_rbc >= 1000:
            score = 5
        elif self.zinc_rbc < 1000 or self.zinc_rbc >= 879:
            score = 3
        elif self.zinc_rbc < 879:
            score = 1
        return score

    def calc_magnesium_rbc(self):
        if self.magnesium_rbc >= 6.8:
            score = 10
        elif self.magnesium_rbc < 6.8 or self.magnesium_rbc >= 6.0:
            score = 7
        elif self.magnesium_rbc < 6.0 or self.magnesium_rbc >= 5.0:
            score = 5
        elif self.magnesium_rbc < 5.0 or self.magnesium_rbc >= 4.2:
            score = 3
        elif self.magnesium_rbc < 4.2:
            score = 1
        return score

    def calc_omega3_index(self):
        if self.omega3_index >= 8:
            score = 10
        elif self.omega3_index < 8 or self.omega3_index >= 7:
            score = 7
        elif self.omega3_index < 7 or self.omega3_index >= 5:
            score = 5
        elif self.omega3_index < 5 or self.omega3_index >= 3:
            score = 3
        elif self.omega3_index < 3:
            score = 1
        return score

    def calc_nourish_grade(self):
        return str(self.nourish_grade)

    # Move Calculations

    def calc_joint_mobility(self):
        return str(self.joint_mobility)
    
    def calc_muscle_flexibility(self):
        return str(self.muscle_flexibility)

    def calc_core_strength(self):
        return str(self.core_strength)

    def calc_postural_analysis(self):
        return str(self.postural_analysis)

    def calc_fat_mass(self):
        if self.gender == 'Male':
            if self.fat_mass <= 10:
                score = 10
            elif self.fat_mass > 10 or self.fat_mass <= 15:
                score = 7
            elif self.fat_mass > 15 or self.fat_mass <= 20:
                score = 5
            elif self.fat_mass > 20 or self.fat_mass <= 30:
                score = 3
            elif self.fat_mass > 30:
                score = 1
            return score
        
        elif self.gender == 'Female':
            if self.fat_mass <= 16:
                score = 10
            elif self.fat_mass > 16 or self.fat_mass <= 23:
                score = 7
            elif self.fat_mass > 23 or self.fat_mass <= 29:
                score = 5
            elif self.fat_mass > 29 or self.fat_mass <= 40:
                score = 3
            elif self.fat_mass > 40:
                score = 1
            return score

    def calc_body_mass_index(self):
        return str(self.body_mass_index)

    def calc_move_grade(self):
        return str(self.move_grade)
    
    def calc_blood_pressure(self):
        # Calculate systolic / diastolic and run logic
        if self.systolic <= 119 and self.diastolic <= 75:# Use and statements for sys and dia
            score = 10
        elif self.systolic <= 129 or self.systolic > 119 and self.diastolic > 75 or self.diastolic <= 85:
            score = 7
        elif self.systolic <= 135 or self.systolic > 129 and self.diastolic > 85 or self.diastolic <= 90:
            score = 5
        elif self.systolic <= 140 or self.systolic > 135 and self.diastolic > 90 or self.diastolic <= 95:
            score = 3
        elif self.systolic > 140 and self.diastolic > 95:
            score = 1
        return score 
        

    def calc_resting_heart_rate(self):
        if self.resting_heart_rate <= 60:
            score = 10
        elif self.resting_heart_rate > 60 or self.resting_heart_rate <= 80:
            score = 7
        elif self.resting_heart_rate > 80 or self.resting_heart_rate <= 100:
            score = 5
        elif self.resting_heart_rate > 100 or self.resting_heart_rate <= 110:
            score = 3
        elif self.resting_heart_rate > 110:
            score = 1
        return score

    def calc_rest_grade(self):
        return str(self.rest_grade)

    def calc_coherence_value(self):
        if self.coherence_value >= 5:
            score = 10
        elif self.coherence_value < 5 or self.coherence_value >= 3:
            score = 7
        elif self.coherence_value < 3 or self.coherence_value >= 2:
            score = 5
        elif self.coherence_value < 2 or self.coherence_value >= 1:
            score = 3
        elif self.coherence_value < 1:
            score = 1
        return score

    def calc_co2_tolerance(self):
        if self.co2_tolerance >= 80:
            score = 10
        elif self.co2_tolerance < 80 or self.co2_tolerance >= 50:
            score = 7
        elif self.co2_tolerance < 50 or self.co2_tolerance >= 21:
            score = 5
        elif self.co2_tolerance < 21 or self.co2_tolerance >= 10:
            score = 3
        elif self.co2_tolerance < 10:
            score = 1
        return score
    
    def calc_connect_grade(self):
        return str(self.connect_grade)



    """
    Add a belt colour relationship between tasks and the associated belt. This will allow to filter the proper tasks
    for the current belt using a current_belt variable defined by somehow looping through the belts to check which belt has
    completed=false

    Can do this by querying the users belts and looping through, the first one that has completed=False will be current_belt

    I will also need a function to complete belts and categories. Can do this by counting the tasks in each category and
    comparing the int to how many tasks completed=True. if == then category completed=True

    Same logic for finishing a belt. 

    """

class Belt(models.Model):
    # Defines Belt Colours
    WHITE = 'White'
    YELLOW = 'Yellow'
    GREEN = 'Green'
    BLUE = 'Blue'
    ORANGE = 'Orange'
    PURPLE = 'Purple'

    # Defines Colour Choices in Belt Table
    COLOURS = [
        (WHITE, _('White')),
        (YELLOW, _('Yellow')),
        (GREEN, _('Green')),
        (BLUE, _('Blue')),
        (ORANGE, _('Orange')),
        (PURPLE, _('Purple'))
    ]

    belt_colour = models.CharField(max_length=32, choices=COLOURS, default=WHITE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False, blank=True)
    
    def __str__(self):
        return self.belt_colour

class Category(models.Model):

    # Defines Category Types
    NOURISH = 'Nourish'
    MOVE = 'Move'
    REST = 'Rest'
    CONNECT = 'Connect'
    LEARN = 'Learn'
    SPARK = 'Spark'
    CHALLENGE = 'Challenge'

    # Defines Choices
    CATEGORIES = [
        (NOURISH, _('Nourish')),
        (MOVE, _('Move')),
        (REST, _('Rest')),
        (CONNECT, _('Connect')),
        (LEARN, _('Learn')),
        (SPARK, _('Spark')),
        (CHALLENGE, _('Challenge'))
    ]
    
    category_type = models.CharField(max_length=20, choices=CATEGORIES)
    completed = models.BooleanField(default=False, blank=True)
    belt = models.ForeignKey(Belt, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.category_type

class Task(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    task = models.CharField(max_length=200)
    completed = models.BooleanField(default=False, blank=True)
    belt = models.ForeignKey(Belt, on_delete=models.CASCADE)

    def __str__(self):
        return self.task

class AssignedTask(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    task = models.CharField(max_length=200)
    completed = models.BooleanField(default=False, blank=True)
    belt = models.ForeignKey(Belt, on_delete=models.CASCADE)

    def __str__(self):
        return self.task
    
    


