# Student Marks Analyzer 📊

A Python-based data analysis project that reads student marks from CSV data, calculates performance metrics, assigns grades, identifies the class topper, and generates visualizations.

## Features

- Reads student data from CSV
- Calculates total marks and percentage
- Assigns grades automatically
- Calculates class average
- Identifies the class topper
- Generates charts for subject averages
- Generates a student percentage chart

## Technologies

- Python
- CSV / File Handling
- Matplotlib
- Basic Data Analysis

## Project Structure

```text
student-marks-analyzer/
├── student_marks_analyzer.py
├── visualize.py
├── students.csv
├── requirements.txt
└── README.md
```

## How to Run

Install the required package:

```bash
pip install -r requirements.txt
```

Run the marks analyzer:

```bash
python student_marks_analyzer.py
```

Generate visualizations:

```bash
python visualize.py
```

The visualization script creates:

- `average_marks_by_subject.png`
- `student_percentages.png`

## Sample Analysis

The project calculates each student's total and percentage, then reports the class average and topper.

## Learning Outcomes

This project helped me practice:

- Python functions
- CSV file handling
- Dictionaries and lists
- Loops and calculations
- Basic data analysis
- Data visualization with Matplotlib

## Future Improvements

- Add more subjects
- Add user input
- Export analyzed results to CSV
- Add more statistical measures
- Build a simple dashboard
