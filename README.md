# Advent of Code 2025 solutions

## Prerequisites
- Python 3.12+

## Running a solution
1. Create input as text file in the `inputs` folder
2. Run the solution file
    ```sh
    python day1.py ./inputs/day1.txt # run day 1
    ```

There are also some pre-configured VSCode tasks that can be used to quickly run files:
1. *run day script* runs `python {current file} ./inputs/{current file name without .py}.txt`
2. *run day script ex1* runs `python {current file} ./inputs/{current file name without .py}-ex1.txt` (good for running examples given by AoC)
3. *run day script with custom input file* prompts for a file name then run `python {current file} {file name from prompt}`