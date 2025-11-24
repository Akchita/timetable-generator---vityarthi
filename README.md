# timetable-generator---vityarthi
 _**Smart College Timetable Chatbot**_
 
 
 A simple and interactive Python chatbot that helps students create personalized college timetables based on their
 preferences.

 
 **_Features_**

 
 _Personalized Experience_: Greets users by name and creates custom schedules
 _Flexible Configuration_: Supports any number of working days and periods per day
 _Subject Preferences: _Allows you to choose which subject to prioritize for each day
 _Test Day Scheduling_: Automatically reserves the last period on your chosen test day
_ Random Distribution:_ Randomly fills remaining periods with other subjects
_ Clean Output_: Displays timetable in a well-formatted table


**__ Requirements__**

 
 Python 3.x
 No external libraries required (uses only standard Python modules)

 
 _**How to Run**_

 
 1. Save the file as 
aditi.py
 2. Open terminal/command prompt
 3. Navigate to the directory containing the file
 4. Run the command:
 bash
   python aditi.py
   python aditi.py


**_ Usage Guide_**

 
 The chatbot will guide you through the following steps:
 1._ Enter Your Name_: Personalize your experience
 2.__ Set Working Days:_ Specify how many days per week you have classes (e.g., 5 or 6)
 3.__ Set Periods Per Day__: Define how many periods you have each day
 4._ _List Your Subjects_:_ Enter all subjects you're studying this semester
 5._ Choose Preferred Subjects_ :For each day, select which subject you want to prioritize
6. _Select Test Day_: Choose a day for self-assessment (last period will be marked as "TEST")
 Example Output
 ================= FINAL TIMETABLE =================
            
Day         P1             P2             P3             P4             P5             
        
Monday      Math           Physics        Chemistry      English        History        
Tuesday     Physics        Math           English        History        Chemistry      
Wednesday   Chemistry      History        Math           Physics        TEST                
Thursday    English        Chemistry      Physics        Math           History        
Friday      History        English        Math           Chemistry      Physics


_**HOW_IT_WORKS**_

 
 The first period of each day is assigned your preferred subject for that day
 Remaining periods are filled randomly with other subjects
 On your chosen test day, the last period is automatically marked as "TEST"
 Each day's schedule is generated independently for variety


_**Customization_Ideas**_

 
 Add break periods between classes
 Include time slots for each period
 Allow multiple preferred subjects per day
 Save timetable to a file
 Add color-coded output for better visualization


_**Author**_

 
 Created as a simple educational tool to help students organize their study schedules.
_**License**_

 
 Free to use and modify for personal and educational purposes
