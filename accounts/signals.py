from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CustomUser, Belt, Category, Task, FormQuestion, MCFormQuestion
# Need to import final version of models for forms.

#Intake form creation
@receiver(post_save, sender=CustomUser)
def create_onboarding_form(sender, instance, created, **kwargs):
    if created:
        # Boolean Choice Questions
        FormQuestion.objects.create(user=instance, question="Do you know your Basal Metabolic Rate (BMR)?", answer=False, category='Nourish')
        FormQuestion.objects.create(user=instance, question="Do you regularly sleep for 7-8 hours?", answer=False, category='Rest')
        FormQuestion.objects.create(user=instance, question="Do you spend time in nature for over 15 minutes at least 2 times per week?", answer=False, category='Connect')
        FormQuestion.objects.create(user=instance, question="Do you read any subjects that interest or inspire you daily?", answer=False, category='Learn')
        FormQuestion.objects.create(user=instance, question="Is spirituality important to you?", answer=False, category='Spark')
        FormQuestion.objects.create(user=instance, question="Do you set daily or weekly challanges for yourself?", answer=False, category='Challenge')
        FormQuestion.objects.create(user=instance, question="Do you know what the 3 pillars of movement are?", answer=False, category='Move')
        FormQuestion.objects.create(user=instance, question="Do you know what your optimal Macronutrient balance is?", answer=False, category='Nourish')
        FormQuestion.objects.create(user=instance, question="Do you know your primary chronotype?", answer=False, category='Rest')
        FormQuestion.objects.create(user=instance, question="Do you have a location anywhere outdoors that you visit regularly for reflection or perspective?", answer=False, category='Connect')
        FormQuestion.objects.create(user=instance, question="Do you listen to any podcasts that discuss health, performance or motivation?", answer=False, category='Learn')
        FormQuestion.objects.create(user=instance, question="Do you know the differenece between your Ego vs. your Soul?", answer=False, category='Spark')
        FormQuestion.objects.create(user=instance, question="Are you motivated most of the time?", answer=False, category='Challenge')
        FormQuestion.objects.create(user=instance, question="Do you have a stretching or foam roller routine?", answer=False, category='Move')
        FormQuestion.objects.create(user=instance, question="Do you know what phytonutrients are?", answer=False, category='Nourish')
        FormQuestion.objects.create(user=instance, question="Do you stop eating or consuming alcohol at least 3 hours before you sleep?", answer=False, category='Rest')
        FormQuestion.objects.create(user=instance, question="Do you meditate regularly", answer=False, category='Connect')
        FormQuestion.objects.create(user=instance, question="Do you travel to new places every year?", answer=False, category='Learn')
        FormQuestion.objects.create(user=instance, question="Do you use a Gratitude journal regularly?", answer=False, category='Spark')
        FormQuestion.objects.create(user=instance, question="Do you set short term and long term goals for yourself?", answer=False, category='Challenge')
        FormQuestion.objects.create(user=instance, question="Do you stregthen your core at least 3 times per week?", answer=False, category='Move')
        FormQuestion.objects.create(user=instance, question="Do you stick to a healthy diet without fast or processed foods?", answer=False, category='Nourish')
        FormQuestion.objects.create(user=instance, question="Do you stop consuming caffeine after noon?", answer=False, category='Rest')
        FormQuestion.objects.create(user=instance, question="Do you use any daily mantras, intentions, or manifesting strategies?", answer=False, category='Connect')
        FormQuestion.objects.create(user=instance, question="Do you discuss relevant topics with your family, friends or community?", answer=False, category='Learn')
        FormQuestion.objects.create(user=instance, question="Do you feel you know your life's purpose?", answer=False, category='Spark')
        FormQuestion.objects.create(user=instance, question="Are you comfortable with being uncomfortable?", answer=False, category='Challenge')
        FormQuestion.objects.create(user=instance, question="Do you practice yoga, dance or participate in any recreational activity at all during the week?", answer=False, category='Move')
        FormQuestion.objects.create(user=instance, question="Do you eat fermented food or cultured foods at least 3 times a week?", answer=False, category='Nourish')
        FormQuestion.objects.create(user=instance, question="Do you go to bed between 8:00-11:00pm?", answer=False, category='Rest')
        FormQuestion.objects.create(user=instance, question="Do you journal or write down your thoughts, emotions, or ideas?", answer=False, category='Connect')
        FormQuestion.objects.create(user=instance, question="Do you know if you have a growth mindset?", answer=False, category='Learn')
        FormQuestion.objects.create(user=instance, question="Do you feel you live a life that's in alignment with your true value & beliefs?", answer=False, category='Spark')
        FormQuestion.objects.create(user=instance, question="Do you plan weekly activities that aren't part of your normal routine? ", answer=False, category='Challenge')
        FormQuestion.objects.create(user=instance, question="Do you use resitance or lift weights at least 3 times per week?", answer=False, category='Move')
        FormQuestion.objects.create(user=instance, question="Do you stay away from overeating or binge eating?", answer=False, category='Nourish')
        FormQuestion.objects.create(user=instance, question="Do you sleep without waking up more than once per night on average?", answer=False, category='Rest')
        FormQuestion.objects.create(user=instance, question="Do you have a sit spot or a place that you sit still in silence?", answer=False, category='Connect')
        FormQuestion.objects.create(user=instance, question="Are you familiar with the Flow State?", answer=False, category='Learn')
        FormQuestion.objects.create(user=instance, question="Do you have a clear life philosophy that governs your daily decisions?", answer=False, category='Spark')
        FormQuestion.objects.create(user=instance, question="Do you practice any breathwork techniques?", answer=False, category='Challenge')
        FormQuestion.objects.create(user=instance, question="Do you have a diversity of different exercises that exceeds 20 minutes at least 3 times per week?", answer=False, category='Move')
        FormQuestion.objects.create(user=instance, question="Do you know what your protein threshold is?", answer=False, category='Nourish')
        FormQuestion.objects.create(user=instance, question="Do you stop using your devices an hour before bed?", answer=False, category='Rest')
        FormQuestion.objects.create(user=instance, question="Do you communicate effectively with your partner, spouse, or family?", answer=False, category='Connect')
        FormQuestion.objects.create(user=instance, question="Do you watch educational documentaries or subscribe to Gaia Network?", answer=False, category='Learn')
        FormQuestion.objects.create(user=instance, question="Do you know your Ikigai?", answer=False, category='Spark')
        FormQuestion.objects.create(user=instance, question="Do you take cold showers or use the cold regularly?", answer=False, category='Challenge')
        FormQuestion.objects.create(user=instance, question="Are you familiar with Zone 2 Training?", answer=False, category='Move')
        FormQuestion.objects.create(user=instance, question="Do you intermittent fast at least 3 times per week?", answer=False, category='Nourish')
        FormQuestion.objects.create(user=instance, question="Do you stop working after dinner?", answer=False, category='Rest')
        FormQuestion.objects.create(user=instance, question="Do you have an inspiring and productive support system?", answer=False, category='Connect')
        FormQuestion.objects.create(user=instance, question="Do you know what Neuroplasticity is and how to achieve it?", answer=False, category='Learn')
        FormQuestion.objects.create(user=instance, question="Would you consider yourself enlightened?", answer=False, category='Spark')
        FormQuestion.objects.create(user=instance, question="Have you ever fasted for 24 hours or longer on purpose?", answer=False, category='Challenge')
        FormQuestion.objects.create(user=instance, question="Do you sit for less than 4 hours at work daily?", answer=False, category='Move')
        FormQuestion.objects.create(user=instance, question="Do you drink more than 4 glasses of water per day?", answer=False, category='Nourish')
        FormQuestion.objects.create(user=instance, question="Do you take any breaks during the day to rest your mind?", answer=False, category='Rest')
        FormQuestion.objects.create(user=instance, question="Are there any unresolved issues with your familty and/or friends?", answer=False, category='Connect')
        FormQuestion.objects.create(user=instance, question="Do you try new hobbies or develop new skills that are not work related?", answer=False, category='Learn')
        FormQuestion.objects.create(user=instance, question="Do you use a regular routine to remind you to be proactive and not reactive?", answer=False, category='Spark')
        FormQuestion.objects.create(user=instance, question="Do you currently have an event or competition that you're working towards?", answer=False, category='Challenge')
        FormQuestion.objects.create(user=instance, question="Do you have an injury or physcial impairment that prevents you from exercising?", answer=False, category='Move')
        FormQuestion.objects.create(user=instance, question="Do you take any supplements?", answer=False, category='Nourish')
        FormQuestion.objects.create(user=instance, question="Do you have 'chill time' during your day?", answer=False, category='Rest')
        FormQuestion.objects.create(user=instance, question="Do you feel like you're a productive part of your community?", answer=False, category='Connect')
        FormQuestion.objects.create(user=instance, question="Do you have a coach or mentor that you work with regularly?", answer=False, category='Learn')
        FormQuestion.objects.create(user=instance, question="Are you excited about your life and the next phases of your life?", answer=False, category='Spark')
        FormQuestion.objects.create(user=instance, question="Do you agree that if it doesn't challenge you, it doesn't change you?", answer=False, category='Challenge')
        FormQuestion.objects.create(user=instance, question="Do you hike or go for walks at least 3 times daily?", answer=False, category='Move')
        #Multiple Choice Questions
        MCFormQuestion.objects.create(user=instance, question="How often do you stick to 1 task at a time and commit to one thing?", answer=1, category='Learn')
        MCFormQuestion.objects.create(user=instance, question="Do you currently have a lot of responsibilities on your plate?", answer=1, category='Rest')
        MCFormQuestion.objects.create(user=instance, question="How clear are you about how to create your ideal life?", answer=1, category='Spark')
        MCFormQuestion.objects.create(user=instance, question="How difficult is it for you to turn work mode off?", answer=1, category='Connect')
        MCFormQuestion.objects.create(user=instance, question="Do you try activities that are outside of your comfort level?", answer=1, category='Challenge')
        MCFormQuestion.objects.create(user=instance, question="How overworked are you?", answer=1, category='Rest')
        MCFormQuestion.objects.create(user=instance, question="Do you prioritize and organize your time, or do you figure it out on the fly?", answer=1, category='Connect')
        MCFormQuestion.objects.create(user=instance, question="Do you know your ideal way to acquire knowledge and wisdom", answer=1, category='Learn')
        MCFormQuestion.objects.create(user=instance, question="Do you invole youtself in different groups other than friends, family, or colleagues?", answer=1, category='Challenge')
        MCFormQuestion.objects.create(user=instance, question="Would you consider yourself to be curious and interested in new topics or concepts?", answer=1, category='Learn')
        MCFormQuestion.objects.create(user=instance, question="Have you purposefully addressed any of your fears?", answer=1, category='Challenge')
        MCFormQuestion.objects.create(user=instance, question="Do you currently have a high level of excitement and motivation?", answer=1, category='Spark')
"""
@receiver(post_save, sender=CustomUser)
def create_user_tasks(sender, instance, created, **kwargs):
    if created:
        Belt.objects.create(belt_colour='White', completed=False, user=instance)
        Belt.objects.create(belt_colour='Yellow', completed=False, user=instance)
        Belt.objects.create(belt_colour='Green', completed=False, user=instance)
        Belt.objects.create(belt_colour='Blue', completed=False, user=instance)
        Belt.objects.create(belt_colour='Orange', completed=False, user=instance)
        Belt.objects.create(belt_colour='Purple', completed=False, user=instance)

        belts = Belt.objects.filter(user=instance)
        for belt in belts:
            Category.objects.create(category_type='Nourish', completed=False, belt=belt, user=instance)
            Category.objects.create(category_type='Move', completed=False, belt=belt, user=instance)
            Category.objects.create(category_type='Rest', completed=False, belt=belt, user=instance)
            Category.objects.create(category_type='Connect', completed=False, belt=belt, user=instance)
            Category.objects.create(category_type='Learn', completed=False, belt=belt, user=instance)
            Category.objects.create(category_type='Spark', completed=False, belt=belt, user=instance)
            Category.objects.create(category_type='Challenge', completed=False, belt=belt, user=instance)
        
        # White belt

        user_belt = Belt.objects.get(belt_colour='White', user=instance)

        user_category = Category.objects.get(category_type='Nourish', belt=user_belt, user=instance)
        Task.objects.create(category=user_category, belt=user_belt, completed=False, task='Access the Carb Manager App and enter your goals', user=instance)
       
        user_category = Category.objects.get(category_type='Move', belt=user_belt, user=instance)
        Task.objects.create(category=user_category, belt=user_belt, completed=False, task='Access the TrueCoach App', user=instance)
        
        user_category = Category.objects.get(category_type='Rest', belt=user_belt, user=instance)
        Task.objects.create(category=user_category, belt=user_belt, completed=False, task='Access the Waking Up App', user=instance)
        
        user_category = Category.objects.get(category_type='Connect', belt=user_belt, user=instance)
        Task.objects.create(category=user_category, belt=user_belt, completed=False, task='Read Spirituality Guide & Write down your definition of falling awake', user=instance)

        user_category = Category.objects.get(category_type='Learn', belt=user_belt, user=instance)
        Task.objects.create(category=user_category, belt=user_belt, completed=False, task='Read Wellness Manifesto', user=instance)

        user_category = Category.objects.get(category_type='Spark', belt=user_belt, user=instance)
        Task.objects.create(category=user_category, belt=user_belt, completed=False, task='Read or Listen to the Biology of Belief, write down the most profound concept and relate it to your life', user=instance)

        user_category = Category.objects.get(category_type='Challenge', belt=user_belt, user=instance)
        Task.objects.create(category=user_category, belt=user_belt, completed=False, task='Complete the Values Form', user=instance)

        # Yellow Belt

        user_belt = Belt.objects.get(belt_colour='Yellow', user=instance)

        user_category = Category.objects.get(category_type='Nourish', belt=user_belt, user=instance)
        Task.objects.create(category=user_category, belt=user_belt, completed=False, task='Read Nutrition Chapter', user=instance)
        Task.objects.create(category=user_category, belt=user_belt, completed=False, task='Review & Apply the Personalized Food Plan', user=instance)

        user_category = Category.objects.get(category_type='Move', belt=user_belt, user=instance)
        Task.objects.create(category=user_category, belt=user_belt, completed=False, task='Begin Personalized Corrective Exercises', user=instance)
        Task.objects.create(category=user_category, belt=user_belt, completed=False, task='Perform TrueCoach Sessions', user=instance)

        user_category = Category.objects.get(category_type='Rest', belt=user_belt, user=instance)
        Task.objects.create(category=user_category, belt=user_belt, completed=False, task='Complete the Initial 5 Lessons in Waking Up', user=instance)
        Task.objects.create(category=user_category, belt=user_belt, completed=False, task='Read the Sleep Chapter', user=instance)

        user_category = Category.objects.get(category_type='Connect', belt=user_belt, user=instance)
        Task.objects.create(category=user_category, belt=user_belt, completed=False, task='Read & Perform the Visualization Process', user=instance)
        Task.objects.create(category=user_category, belt=user_belt, completed=False, task='Select 5 of the Intentions', user=instance)

        user_category = Category.objects.get(category_type='Learn', belt=user_belt, user=instance)
        Task.objects.create(category=user_category, belt=user_belt, completed=False, task='Read the Science of Longevity', user=instance)
        Task.objects.create(category=user_category, belt=user_belt, completed=False, task='Select and Listen to Podcast', user=instance)

        user_category = Category.objects.get(category_type='Spark', belt=user_belt, user=instance)
        Task.objects.create(category=user_category, belt=user_belt, completed=False, task='Post Visualization Anchor on Mirror & Screensaver', user=instance)

        user_category = Category.objects.get(category_type='Challenge', belt=user_belt, user=instance)
        Task.objects.create(category=user_category, belt=user_belt, completed=False, task='Use 3 of the 6 SAVERS Daily', user=instance)
        Task.objects.create(category=user_category, belt=user_belt, completed=False, task='Register for a Health Event', user=instance)

        # Green Belt

        user_belt = Belt.objects.get(belt_colour='Green', user=instance)

        user_category = Category.objects.get(category_type='Nourish', belt=user_belt, user=instance)
        Task.objects.create(category=user_category, belt=user_belt, completed=False, task='Perform the Warrior Eradication & Pantry Purge', user=instance)
        Task.objects.create(category=user_category, belt=user_belt, completed=False, task='Select and apply at least 2 of the XYZ Axis', user=instance)

        user_category = Category.objects.get(category_type='Move', belt=user_belt, user=instance)
        Task.objects.create(category=user_category, belt=user_belt, completed=False, task='Indentify a local hiking trail and map a route (Strava or All Trails', user=instance)
        Task.objects.create(category=user_category, belt=user_belt, completed=False, task='Time or video your Flexibility, Mobility, and Stability Routine', user=instance)

        user_category = Category.objects.get(category_type='Rest', belt=user_belt, user=instance)
        Task.objects.create(category=user_category, belt=user_belt, completed=False, task='Write down your optimal Sleep Ritual with steps and timeframe', user=instance)
        Task.objects.create(category=user_category, belt=user_belt, completed=False, task='Perform Mind training at least 4 days for a week', user=instance)

        user_category = Category.objects.get(category_type='Connect', belt=user_belt, user=instance)
        Task.objects.create(category=user_category, belt=user_belt, completed=False, task='Identify your Sit Spot and apply for at least 10 minutes', user=instance)
        Task.objects.create(category=user_category, belt=user_belt, completed=False, task='Perform all 6 SAVERS tasks two days in a row', user=instance)

        user_category = Category.objects.get(category_type='Learn', belt=user_belt, user=instance)
        Task.objects.create(category=user_category, belt=user_belt, completed=False, task='Listen to the Sleep Podcast by Matthew Walker', user=instance)
        Task.objects.create(category=user_category, belt=user_belt, completed=False, task='Read at least one chapter of a personalized recommended book', user=instance)

        user_category = Category.objects.get(category_type='Spark', belt=user_belt, user=instance)
        Task.objects.create(category=user_category, belt=user_belt, completed=False, task='Complete a Life Purpose Insight', user=instance)

        user_category = Category.objects.get(category_type='Challenge', belt=user_belt, user=instance)
        Task.objects.create(category=user_category, belt=user_belt, completed=False, task='Begin Burpee/Pushup/Plank 30 Day Challenge', user=instance)
        Task.objects.create(category=user_category, belt=user_belt, completed=False, task='Remove all unproductive Apps on your phone', user=instance)

        # Blue Belt

        user_belt = Belt.objects.get(belt_colour='Blue', user=instance)

        user_category = Category.objects.get(category_type='Nourish', belt=user_belt, user=instance)
        Task.objects.create(category=user_category, belt=user_belt, completed=False, task='Read the Wellness Warrior Keto Jumpstart Guide', user=instance)
        Task.objects.create(category=user_category, belt=user_belt, completed=False, task='Prep all Grab & Go snacks for an entire week', user=instance)

        user_category = Category.objects.get(category_type='Move', belt=user_belt, user=instance)
        Task.objects.create(category=user_category, belt=user_belt, completed=False, task='Perform a zone 2 activity for at least one hour', user=instance)
        Task.objects.create(category=user_category, belt=user_belt, completed=False, task='Create, practice, and record your mobility flow using stretching foam roller and stability', user=instance)

        user_category = Category.objects.get(category_type='Rest', belt=user_belt, user=instance)
        Task.objects.create(category=user_category, belt=user_belt, completed=False, task='Watch the YouTube video on NSDR', user=instance)
        Task.objects.create(category=user_category, belt=user_belt, completed=False, task='Perform all 4 steps in 10-3-2-1 Technique for Optimal Sleep', user=instance)

        user_category = Category.objects.get(category_type='Connect', belt=user_belt, user=instance)
        Task.objects.create(category=user_category, belt=user_belt, completed=False, task='Practice Meditation for at least 20 minutes', user=instance)
        Task.objects.create(category=user_category, belt=user_belt, completed=False, task='Use the Chakra sheet to identify your current energy balance', user=instance)

        user_category = Category.objects.get(category_type='Learn', belt=user_belt, user=instance)
        Task.objects.create(category=user_category, belt=user_belt, completed=False, task="Review your Ikigai and brainstorm potential mentors that you know in a skill you're skilled in.", user=instance)
        Task.objects.create(category=user_category, belt=user_belt, completed=False, task="Select and write down any experience you're interested in that you're currently not doing. Just do it for at least 15 minutes", user=instance)

        user_category = Category.objects.get(category_type='Spark', belt=user_belt, user=instance)
        Task.objects.create(category=user_category, belt=user_belt, completed=False, task='Read or Listen to the Biology of Belief and write down the most profound concept and relate it to your life', user=instance)

        user_category = Category.objects.get(category_type='Challenge', belt=user_belt, user=instance)
        Task.objects.create(category=user_category, belt=user_belt, completed=False, task='Select a 4 hour eating window for 3 days straight', user=instance)
        Task.objects.create(category=user_category, belt=user_belt, completed=False, task='Begin the Guided Breathing Challenge in the Wim Hof App', user=instance)

        # Orange Belt

        user_belt = Belt.objects.get(belt_colour='Orange', user=instance)

        user_category = Category.objects.get(category_type='Nourish', belt=user_belt, user=instance)
        Task.objects.create(category=user_category, belt=user_belt, completed=False, task='Eat all 10 Wellness Warrior Power Foods', user=instance)
        Task.objects.create(category=user_category, belt=user_belt, completed=False, task='Remove all gluten, seed oils, and processed food', user=instance)

        user_category = Category.objects.get(category_type='Move', belt=user_belt, user=instance)
        Task.objects.create(category=user_category, belt=user_belt, completed=False, task='Find Dynamic Neuromuscular Stabilization on YouTube and select 3 movements to add to your routine', user=instance)
        Task.objects.create(category=user_category, belt=user_belt, completed=False, task='Select, write down, and perform all 3 Pillars of Movement', user=instance)

        user_category = Category.objects.get(category_type='Rest', belt=user_belt, user=instance)
        Task.objects.create(category=user_category, belt=user_belt, completed=False, task='Perform 2 of the 4 steps in the 10-3-2-1 Technique for Optimal Sleep', user=instance)
        Task.objects.create(category=user_category, belt=user_belt, completed=False, task='Rest your mind for 5 minutes each day by performing the Take 5 Breathing Technique', user=instance)

        user_category = Category.objects.get(category_type='Connect', belt=user_belt, user=instance)
        Task.objects.create(category=user_category, belt=user_belt, completed=False, task='Bring full attention to a redundant chore, like washing the dished or folding your clothes, instead of striving for a quick completion', user=instance)
        Task.objects.create(category=user_category, belt=user_belt, completed=False, task="Use a Gratitude Journal and write down 2 things you're grateful for right before bed", user=instance)

        user_category = Category.objects.get(category_type='Learn', belt=user_belt, user=instance)
        Task.objects.create(category=user_category, belt=user_belt, completed=False, task='Read the Neurohacking Guide & select size mind hacks to implement', user=instance)
        Task.objects.create(category=user_category, belt=user_belt, completed=False, task='Select a new hobby or topic that interests you and take one step to pursue it', user=instance)

        user_category = Category.objects.get(category_type='Spark', belt=user_belt, user=instance)
        Task.objects.create(category=user_category, belt=user_belt, completed=False, task='Take 15 minutes to review your SAVERS journaling and write down the 3 top thoughts, ideas, epiphanies, or worries', user=instance)

        user_category = Category.objects.get(category_type='Challenge', belt=user_belt, user=instance)
        Task.objects.create(category=user_category, belt=user_belt, completed=False, task='Do not eat for 16 straight hours', user=instance)
        Task.objects.create(category=user_category, belt=user_belt, completed=False, task='Finish a shower with 30 seconds of cold water on your head & shoulders', user=instance)

        # Purple Belt

        user_belt = Belt.objects.get(belt_colour='Purple', user=instance)

        user_category = Category.objects.get(category_type='Nourish', belt=user_belt, user=instance)
        Task.objects.create(category=user_category, belt=user_belt, completed=False, task='Review the Nutrition Recommendations from your genetic report and follow it exactly for an entire week', user=instance)
        Task.objects.create(category=user_category, belt=user_belt, completed=False, task='Follow all 3 factors in XYZ Guide from your Prescribed Foodplan for an entire week', user=instance)

        user_category = Category.objects.get(category_type='Move', belt=user_belt, user=instance)
        Task.objects.create(category=user_category, belt=user_belt, completed=False, task='Complete at least 6 intense sessions in Purple Belt TrueCoach Rx & Comment', user=instance)
        Task.objects.create(category=user_category, belt=user_belt, completed=False, task="Write down your PR's in Squat, Deadlift, Pushup and be prepared to share", user=instance)

        user_category = Category.objects.get(category_type='Rest', belt=user_belt, user=instance)
        Task.objects.create(category=user_category, belt=user_belt, completed=False, task='Find your circadian rhythm by going to bed and waking up at the same time for an entire week', user=instance)
        Task.objects.create(category=user_category, belt=user_belt, completed=False, task='Meditate for 10 minutes within the first 30 minutes of waking, between 12-2, and 30 minutes before bed', user=instance)

        user_category = Category.objects.get(category_type='Connect', belt=user_belt, user=instance)
        Task.objects.create(category=user_category, belt=user_belt, completed=False, task="Write down 3 things you're grateful for for an entire week and be prepared to share", user=instance)
        Task.objects.create(category=user_category, belt=user_belt, completed=False, task='Write a note to anybody in your life that you have unresolved tension with or have grown distant from', user=instance)

        user_category = Category.objects.get(category_type='Learn', belt=user_belt, user=instance)
        Task.objects.create(category=user_category, belt=user_belt, completed=False, task="Become the teacher and discuss any interesting health or performance concept you've learned with a friend or family member", user=instance)
        Task.objects.create(category=user_category, belt=user_belt, completed=False, task="Listen to 3 of your favorite health Podcasts and write down one simple concept you'd like to apply", user=instance)

        user_category = Category.objects.get(category_type='Spark', belt=user_belt, user=instance)
        Task.objects.create(category=user_category, belt=user_belt, completed=False, task='Write down your new definition of falling awake and make artwork out of it in anyway you feel comfortable', user=instance)

        user_category = Category.objects.get(category_type='Challenge', belt=user_belt, user=instance)
        Task.objects.create(category=user_category, belt=user_belt, completed=False, task='Use one day with the clear intention of sending good vibes to every person you come in contact with including strangers', user=instance)
        Task.objects.create(category=user_category, belt=user_belt, completed=False, task='Identify a day to attempt to fast for the entire day', user=instance)
"""

@receiver(post_save, sender=CustomUser)
def create_belts_and_categories(sender, instance, created, **kwargs):
    if created:
        Belt.objects.create(belt_colour='White', completed=False, user=instance)
        Belt.objects.create(belt_colour='Yellow', completed=False, user=instance)
        Belt.objects.create(belt_colour='Green', completed=False, user=instance)
        Belt.objects.create(belt_colour='Blue', completed=False, user=instance)
        Belt.objects.create(belt_colour='Orange', completed=False, user=instance)
        Belt.objects.create(belt_colour='Purple', completed=False, user=instance)

        belts = Belt.objects.filter(user=instance)
        for belt in belts:
            Category.objects.create(category_type='Nourish', completed=False, belt=belt, user=instance)
            Category.objects.create(category_type='Move', completed=False, belt=belt, user=instance)
            Category.objects.create(category_type='Rest', completed=False, belt=belt, user=instance)
            Category.objects.create(category_type='Connect', completed=False, belt=belt, user=instance)
            Category.objects.create(category_type='Learn', completed=False, belt=belt, user=instance)
            Category.objects.create(category_type='Spark', completed=False, belt=belt, user=instance)
            Category.objects.create(category_type='Challenge', completed=False, belt=belt, user=instance)

@receiver(post_save, sender=CustomUser)
def assign_tasks(sender, instance, created, **kwargs):
    if created:
        belt_list = Belt.objects.filter(user=instance)
        category_list = Category.objects.filter(user=instance)
        for belt_type in belt_list:
            for category_type in category_list:
                tasks = AssignedTask.objects.filter(category=category_type, belt=belt_type)
                for item in tasks:
                    Task.objects.create(category=category_type, belt=belt_type, completed=False, user=instance, task=item)