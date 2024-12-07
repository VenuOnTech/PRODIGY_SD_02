# Advanced Number Guessing Game  
An enhanced version of the classic number guessing game with exciting new features like hints, time challenges, streak tracking, and a leaderboard system. This Python program is designed to test your guessing skills while keeping the game fun and competitive!  
  
Features:  
  
🧩 Game Features  
Difficulty Levels:  
Choose from three levels:  
  
Easy: Numbers between 1 and 50  
Medium: Numbers between 1 and 100  
Hard: Numbers between 1 and 200  
Hint System:  
Players can use hint points to get numerical clues, such as how close their guess is to the target number.  
  
Clue System:  
After every three incorrect attempts, the game provides additional clues:  
  
Is the number even or odd?  
Is it divisible by 5?  
Timer Challenge:  
Players must guess the number within a specific time limit:  
  
Easy: 60 seconds  
Medium & Hard: 30 seconds  
Streak Tracking:  
Earn bonus points for consecutive correct guesses.  
  
Leaderboard:  
Tracks players' cumulative scores across games, ensuring a competitive experience.  
  
🛠 Technical Features  
JSON-based Leaderboard:  
The program saves and loads leaderboard data using a local leaderboard.json file.  
  
Scoring System:  
Points are awarded based on:  
  
Difficulty level  
Number of attempts  
Streak count  
Dynamic Gameplay:  
Feedback and clues adjust dynamically based on the player’s guesses.  
