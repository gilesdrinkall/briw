# briw

Create a round of drinks using pre-defined lists of team members and drinks.

## Requirements

You will need to have Python3 installed.

## Setup

The application will attempt to read in both a list of team members and a list of available drinks found in files called `people.txt` and 'drinks.txt' respectively. These files are stored at the top-level directory of this project.
The round you create is presisted to a file called 'round.txt'
These files needs to be defined before using the applications and never committed to source control for privacy reasons.

Example `people.txt`:

```
1, John
2, Chris
3, Andrew
4, Claire
```
Example 'drinks.txt:

```

1, Coffee
2, Tea
3, Coke
4, Water
```

## Running

Invoke the application with

```
python3 round.py
```

The application will generate a new winner on page refresh, not when the "GO" button is pressed. Thus, to pick a different winner, refresh the page and press the "GO" button to run the animation again.

## Contributing

If you wish to contribute to the `briw`, fork this repo and submit a pull request with any changes you've made.

In order for your pull request to be approved, your fork should pass the automated checks. Run `pytest` at the top-level directory and if no warnings or errors are printed, it's good to go!