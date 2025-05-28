1. Project Introduction
What the project is
Why we chose it
Explain Group members and roles

2.0 System Development & Features

## 2.1 System Logic
As stated in the intrdiuction section, this interactive system  participants will play a classic Rock-Paper-Scissors game  against a computer opponent that is programmed to adapt its choices based on the participant’s previous moves. By using a simple pattern-recognition algorithm, the computer will adjust its  responses, creating a dynamic and strategic challenge where players must try to “outsmart” the system or “AI”. The game provides a fun and engaging way to explore basic concepts in prediction and machine learning. For this project or task, we will use “Python” a programming language, accompanied by several libraries to develop this project. Libraries include, cvzone’s  “HandTrackingModule” for object tracking , pygame and cv2 a computer vision library for image processing which includes detecting objects and tracking motion. The system takes the input of the player through a camera and pass it through the library cv2 handtracking module which involves in not invlove in object tracking but classification towards the object has been detected or tracked where the module tracks based on the interjoints of a person's hand and determine the types of gestures that the user has preformed. Moving forward the system, pass it through the output value from the handtracking module which represented or be mapped into 0 and 1 for object detection or  finger detection with 0,0,0,0,0 represented the 5 fingers for a single array with the value of “1” which will be  “Rock”, paper will have an array of 1,1,1,1,1 which will be represent with the variable of  “2”  and 0,1,1,0,0 will be scissors with the variable of  3. Lastly  the system will pass through the output values of the mapping and will pass it through a if else condition or a form of rule based condition. which will be represented as (Figure 1).

<div align="center">
  <img src="figures/figure_1.png" alt="Figure 1: Game Logic Flow"/>
  <p><em>Figure 1: Game Logic Flow</em></p>
</div>

2.2 System features and technology used

For the system's features this project has decided to categorize into 3 enhancements corresponding with the current issues of the rock paper sciorss gameplay which were lack of difficulty variation in certain situation where if hardcore rock paper scissors players wanted to challenge the game they are require to find required a expert players to stay engaged. Next is miminal player feedback, players only provide reaction through facial emotion and basic visual cues, which can lead to boredom and disconnection from the experience and without meaningful feedback or interactive elements, the gameplay can feel repetitive and unengaging. Lastly is limited engagement, such that traditional rock-paper-scissors games offer little beyond the basic gameplay loop, they often lack visual appeal, sound effects, narrative context, or interactive features, thus leading to short-term interest and limited replay value. Therefore to solve the following issues tha we have defined, 3 proposed solutions or enhancement for project was developed through three iterations which were defined as Sprint 1 to Sprint 3, with each iteration focusing on specific areas of improvement in terms of the gameplay experience and visulization for users. Starting from the first iteration which involves in core gameplay mechanics , the system includes or offers three 3 difficulty modes which consist of easy, medium and hard with each using different algorithmic strategies where  easy mode uses a easy uses a deterministic and predictable pattern based on varible roundNumber % 3 thus allowing players to learn and recognize a sequence over time, as for Medium Mode, this mode applies a probabilistic model using Python's random.randint() function to select moves unpredictably, in contrast to hard mode uses a rule-based conditional system where the system selects the exact counter to the player’s move, guaranteeing a win if input is recognized correctly. For the second iteration, we have decided that the system may include a UI using pygame library for user interface and feedback where the UI consist the output of the system  and represent them as 3 images,  rock , paper and scissor. addtionally the system will also display the user's hand and face to provide visual feedback and justification towards the detected hand gestures. Lasltly for the third iteration this project has decided to add features to boost immersion and engagement through including several sound effect such as winning and end phase, thus allowing the players to be more immersive in the game itself, and for further improvement in terms of user engagement, a simple storyline was introduced towards the system as well where players can experince an enhance version of the game rock paper scissor, in consequence transforming it from a basic loop into a more narrative-driven experience, and through storytelling element, it enable increases player interest and adds emotional depth to the gameplay. As a side information in terms of technical specification and the libaray was used for this project development, a webcam was use for receiving the input python core programming language for logic and integration, OpenCV (cv2) for image processing and camera feed input, cvzone for hand gesture tracking and classification, pygame for rendering images, text, and sound in the UI, and lastly tkinter and tkvideo library will be used for displaying post-game video and interface elements.


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

