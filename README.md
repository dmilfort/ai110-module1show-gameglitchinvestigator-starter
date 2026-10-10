# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [ ] Describe the game's purpose.
Game Glitch Investigator is a number-guessing game built using Python and Streamlit. The player selects a difficulty level and attempts to guess a randomly generated number within a limited number of attempts. The game provides hints indicating whether the player's guess is too high or too low, while also tracking their score and guess history. The purpose of this project was to identify and repair bugs in an AI-generated game and improve its reliability through debugging, refactoring, and testing.
- [ ] Detail which bugs you found.
During testing, I discovered several issues affecting the game's functionality. The higher and lower hints were reversed, causing the game to give misleading instructions. The secret number was sometimes converted into a string, resulting in incorrect comparisons between guesses and the answer. The New Game button also failed to reset the game status, preventing players from restarting after losing. Other issues included incorrect difficulty ranges, invalid guesses counting as attempts, decimal inputs being accepted, inconsistent scoring, and the attempt counter starting at one instead of zero.
- [ ] Explain what fixes you applied.
I corrected the comparison messages so the game accurately tells players whether to guess higher or lower. I removed the unnecessary string conversion to ensure guesses and secret numbers are compared as integers. I also updated the New Game button to reset the score, attempts, game status, and guess history. Additionally, I fixed the difficulty ranges, improved input validation, corrected the scoring system, and moved the game logic into a separate logic_utils.py file. Finally, I used pytest to test the corrected functions and verify that they returned the expected results.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. Launch the game
2. Enter a guess
3. Follow the hints
4. Win or lose the game
5. Start a new game

## 🧪 Test Results
================================= test session starts =================================
platform darwin -- Python 3.13.1, pytest-9.1.1, pluggy-1.6.0
rootdir: /Users/destinymilfort/ai110-module1show-gameglitchinvestigator-starter
collected 27 items                                                                    

test_logic_utils.py ........................                                    [ 88%]
tests/test_game_logic.py ...                                                    [100%]

================================= 27 passed in 0.01s ==================================
