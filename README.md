# Introduction

The application plays cards with a standard 52 card deck, with suits hearts, spades, diamonds and clubs. The following two games are played:

* Snap [https://en.m.wikipedia.org/wiki/Snap_(card_game)](https://en.m.wikipedia.org/wiki/Snap_(card_game))
* Twenty One [https://en.wikipedia.org/wiki/Blackjack](https://en.wikipedia.org/wiki/Blackjack) and [Example Twenty One](https://www.youtube.com/watch?v=zuZqw12MrVI)


Mocking allows you to test the `CardGame` application completely. It allows you mock user input from the console, as well as files. For this task, you are required to implement several unit tests using the module `unittest.mock` (from the `unittest` library) to mock user input and files.

# Instructions

- Fork this project and make sure your repository is public. Then import the project into your IDE VSCode.
- You cannot change the signature of the provided functions or rename them.
- You cannot interact with your peers: work individually and do your best.
- The unit tests to implement are described through a set of sub-tasks.
- Implement the unit tests one at a time, strictly following the order given by the sub-tasks. Do not read ahead to the following sub-tasks. 
- A sub-task can be considered complete once you are confident that the unit test has been implemented correctly.
- Every time you complete a sub-task, commit and push your code.
- At the end of the assignment, make sure you have pushed the entire project to the public repository.

# Run Tests

python -m unittest discover -v -s ./test/ -p test_*.py

# Sub-tasks

Remember to read and implement the sub-tasks one at a time, following the given order. Do not move on to the next sub-task until the current one has been completed. Implement the required unit tests by working in the `test/test_task.py` file. 

## Sub-task 1 – Mock Console Input Integer

To mock an input from the console.

### Requirement

* Implement unit test `test_get_input_integer` in `test/test_task.py` to mock a method.
* We want to test `ConsoleInOut.get_input_integer` that calls `get_string` to get an input from the console.
* Mock the method `get_string` to return "18"
* The expected output of the unit test, namely the value returned by `ConsoleInOut.get_input_integer`, should be 18 (number, not string).
* Push sub task to GitGub, [Go To GitHub Commit](#github-commit)

## Sub-task 2 – Mock Console Game Info

To mock an input from the console.

### Requirement

* Implement unit test `test_get_game_info` in `test/test_task.py` to mock a method.
* We want to test `Game.get_game_info` that calls `get_input_string` and `get_input_integer` to get an inputs from the console.
* Mock the method `get_string` so that it returns "Derek" on the first call and "3" on the second call. 
* The expected output of the unit test, namely the value returned by `Game.get_game_info`, should be 3 (number, not string). 
* Push sub task to GitGub, [Go To GitHub Commit](#github-commit)

## Sub-task 3 – Verify Mock Call Count
 
To mock an input from the console and verify how many times it was called.
 
### Requirement
 
* Implement unit test `test_get_integer_max_attempts` in `test/test_task.py` to mock a function and verify its usage.
* We want to test `ConsoleInOut.get_integer` (that calls `get_string` to get an input from the console) when the user continually inputs an invalid string. The function ‘ConsoleInOut.get_integer` is supposed to retry 5 times before giving up.
* Mock the `card_game.communication.ConsoleInOut.get_string` function to always return `abc`.
* The expected output of the unit test, namely the value returned by `ConsoleInOut.get_integer`, should be -1.
* Verify that the mocked function, namely `card_game.communication.ConsoleInOut.get_string`, was called exactly 5 times.
* Push sub task to GitGub, [Go To GitHub Commit](#github-commit)

## Sub-task 4 – Mock File Load

To mock the opening of a file.

### Requirement

* Implement unit test `test_get_csv_rows` in `test/test_task.py` to mock the opening of a file. 
* We want to test `LoadCSV.get_csv_rows` that calls `create_csv_reader` to open a file.
* Mock file opening to return the following content: "Derek\nXi". Namely, the mocked file must provide the content `"Derek\nXi"` when read. 
* Call `get_csv_rows` with any file name. The file does not need to exist, because the opening is mocked.
* The mocked content has two lines, so assert that the first value of the second row equals the expected value `Xi`.
* Push sub task to GitGub, [Go To GitHub Commit](#github-commit)

## Sub-task 5 – Verify Mock Call Arguments
To mock a function and verify the arguments passed to it.
### Requirement
* Implement unit test test_play_a_card_from_deck_random in test/test_task.py to mock the random selection of a card.
* We want to test Deck.play_a_card_from_deck, which calls random.randint(0,index) to select a random card when the deck contains more than 8 cards. For a full deck of 52 cards, the upper bound is 51.
* Mock random.randint in card_game.card.entity.Deck to return 0, so that the first card in the deck is selected.
* Create a full deck of 52 cards using create_deck() and record the first card.
* Call play_a_card_from_deck(deck). Since the mock returns 0, assert that the returned card matches the first card in the deck.
* Verify that random.randint was called exactly once with the expected arguments (0, 51) using mock_randint.assert_called_once_with(0, 51).
* Push sub task to GitGub, [Go To GitHub Commit](#github-commit)

# GitHub Commit
* Open VS Code Terminal
* git add *
* git commit -m "sub task x complete"
* git push
