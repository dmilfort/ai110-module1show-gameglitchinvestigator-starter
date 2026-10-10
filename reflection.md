# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
---
  when I first started the game it lloked like a normal guessing game however while I was playing I realized that the guesses were backwards and one of my guesses even ended up being a negative number. Another issue I noticed is that the game wouldnt reset when i pressed new game. 

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

I guessed 9 when the secret was -25, Game should have said go lower but instead the game incorrectly said go higher. No console error was displayed.

I clicked new game after losing, the game should have restarted but it didn't and the game remained in the game over state. No console error was displayed. 

Entered an invalid guess for example I put in a word instead of a number guess. The invalid input should display an error without using up an attempt but the original code counted that invalid input as an attempt. Input validation message displayed. 


## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.

---
I used both Claude and ChatGPT as a teammate to help identify bugs,understand the code, and figure out how to correct the issues I ran into. One helpful suggestion was to reset "st.session_state.status to "playing" when starting a new game which addressed the major problem of the game not being able to restart. One suggestion I modified was the approach to testing check_guess() since the original assertions compared the entire returned tuple to a single strong; I changed them to use result 0 and verified the correction by running pytest. 

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---
To determine whether a bug was fixed, I reviewed the corrected code and used pytest to check whether the functions returned the expected results. When I first ran the tests, 24 passed and 3 failed, specifically the tests checking winning guesses and guesses that were too high or too low. I discovered that the tests were comparing tuples to strings, and after correcting the assertions and saving the file, the tests passed. This showed me that sometimes problems occur outside of the main program.

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---
I learned that Streamlit reruns the Python script whenever a user interacts with certain elements, such as buttons or inputs. Session state allows the program to remember information between these reruns, including the secret number, remaining attempts, score, and whether the game is still active. Without session state, important game information could reset every time the script runs again.

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

---
One habit I want to continue using in future projects is running tests after making changes instead of assuming that the code works correctly. I also learned the importance of checking whether files are saved before running tests, since I initially had three failing tests even after correcting the assertions in VS Code.