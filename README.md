# Coding Competition Platform Django App

This is a Django app for hosting a coding contest with a judge.

Two types of questions can be made : 
1. Questions with description and sample Input/Output followed by test input. User must paste the correct output to the problem
set.
2. Multiple Choice Questions

There is a timer that ticks off the moment user logs in for the first time. After a certain period, no submissions
can be made from a particular user.

A scoreboard feature (only accessible to admin) has been made to view all teams in order of their ranks and scores on /scoreboard/.

To create a user, a user must be first made on Django admin and a corresponding user profile object must also be made.

@chiragjn (http://github.com/chiragjn) and I had developed this for the screening round of a coding competition held 
in our college by our college's ACM student chapter. I hope this turns out to be useful for other colleges trying 
to hold similar competitions in their colleges.

## Demo Images

### Login Screen
![alt tag](https://github.com/monikkinom/CodingContestDjango/blob/master/loginscreen.png)

### Participant View
![alt tag](https://github.com/monikkinom/CodingContestDjango/blob/master/homeview.png)

### Coding Problem View
![alt tag](https://github.com/monikkinom/CodingContestDjango/blob/master/questionview.png)

### MCQ View
![alt tag](https://github.com/monikkinom/CodingContestDjango/blob/master/mcqview.png)

### Scoreboard View
![alt tag](https://github.com/monikkinom/CodingContestDjango/blob/master/scoreboard.png)



