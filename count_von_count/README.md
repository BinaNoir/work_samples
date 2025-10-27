# Count von Count
*Version 2.2.0* </br>
by *Bina Schmütsch*

## Description

In this interactive Python game you will be greeted by The Count, a friendly (and slightly dramatic) character who loves numbers. He will challenge you to a fun guessing game where you must guess a randomly chosen number between 1 and 100.

## Installation
1. Download Python 3.3.17 (or later) from https://www.python.org/ and install it.
2. Open your terminal:<br>
Linux: `[strg] + [alt] + [t]`<br>
Windows: `[win] + [X]` → `wt` → `[Enter]`
3. Clone this repository:   
```bash
git clone https://github.com/BinaNoir/workSamples/tree/main/count_von_count
```
4. Change directory to the repository:
```bash
cd count_von_count
```

## Play the game
Run the main programm:
```bash
python -m count_von_count.__main__
```

## Unittests
Run all unittests: 
```bash
python -m unittest count_von_count.tests
```
Test a specific module: 
```bash
python -m unittest count_von_count.MODULNAME
```

## Updates
### v2.2.0
- Refactored code style for PEP 8 compliance
- Modularized codebase
- Added unittests
- Improved README.md

### Planned Updates
- Add language selection
- Improve interactive dialogue
- Add randomized test coverage
- Define key variables as globals for easier configuration