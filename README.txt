1. Project Introduction
What the project is
Why we chose it
Explain Group members and roles

2.0 System Development & Features

2.1 System Logic
For  this interactive system , participants will play a classic Rock-Paper-Scissors game  against a computer opponent that is programmed to adapt its choices based on the participant’s previous moves. By using a simple pattern-recognition algorithm, the computer will adjust its  responses, creating a dynamic and strategic challenge where players must try to “outsmart” the system or “AI”. The game provides a fun and engaging way to explore basic concepts in prediction and machine learning. For this project or task, we will use “Python” a programming language, accompanied by several libraries to develop this project. Libraries include, cvzone’s  “HandTrackingModule” for object tracking , pygame and cv2 a computer vision library for image processing which includes detecting objects and tracking motion. The system takes the input of the player through a camera and pass it through the library cv2 handtracking module which involves in not invlove in object tracking but classification towards the object has been detected or tracked where the module tracks based on the interjoints of a person's hand and determine the types of gestures that the user has preformed. Moving forward the system, pass it through the output value from the handtracking module which represented or be mapped into 0 and 1 for object detection or  finger detection 
with 0,0,0,0,0 represented the 5 fingers for a single array with the value of “1” which will be  “Rock”, paper will have an array of 1,1,1,1,1 which will be represent with the variable of  “2”  and 0,1,1,0,0 will be scissors with the variable of  3. Lastly  the system will pass through the output values of the mapping and will pass it through a if else condition or a form of rule based condition. which will be represented as (Figure 1).

![Figure 1: Game Logic Flow](https://www.google.com/imgres?q=hand%20tracking%20module%20involved%20in%20classification%20cv2&imgurl=https%3A%2F%2Fmiro.medium.com%2Fv2%2Fresize%3Afit%3A1118%2F1*UaoJR_TxWrvAV4fQ8VZ8JQ.gif&imgrefurl=https%3A%2F%2Fmedium.com%2F%40Nivitus.%2Fhand-tracking-module-with-fps-using-opencv-4c9e8928a096&docid=tXANdFIoBm3tQM&tbnid=t_WA7SFbEkMFAM&vet=12ahUKEwjoyIfYycKNAxXATWwGHdAPI8QQM3oECBsQAA..i&w=559&h=459&hcb=2&ved=2ahUKEwjoyIfYycKNAxXATWwGHdAPI8QQM3oECBsQAA)



3. Scrum/Agile Implementation
Product Backlog which we will explain the tasks planned at the start
Sprint 1 / 2 / 3 Backlogs (tasks done in each iteration)
Kanban board screenshots showing task progress
how the tasks were distributed in our group

4. Version Control
Explain GitHub repository used
Screenshots of commits, branches, tags
Explanation of how we used the version control

5. User Manual
How to run the project
How to interact with it

6. Reflection & Conclusion
Challenges our  group faced 
What we have learned
Improvements

![My Image](images/testImage.png)
