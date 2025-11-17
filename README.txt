📊 Demographic Data Analyzer

This project analyzes demographic data extracted from the 1994 U.S. Census Database using Pandas in Python. It is part of the freeCodeCamp Data Analysis with Python certification.

The program reads a dataset (adult.data.csv) and computes various statistics such as race distribution, average age of men, percentage of Bachelor's degree holders, income analysis, and more.

📁 Project Structure
Demographic_Data_Analyser/
│
├── demographic_data_analyzer.py   # Main analysis logic
├── main.py                        # Runs the script and prints results
├── adult.data.csv                 # Dataset file
├── .gitignore                     # Ignored files and folders
└── README.md                      # Project documentation

🧠 What This Project Does

The program uses Pandas to answer the following questions:

How many people of each race are represented?

What is the average age of men?

What percentage of people have a Bachelor's degree?

Among people with advanced education (Bachelors, Masters, Doctorate), what percent earn >50K?

Among people without advanced education, what percent earn >50K?

What is the minimum number of work hours per week?

Among those who work the minimum hours, what percent earn >50K?

Which country has the highest percentage of people earning >50K, and what is that percentage?

What is the most common occupation for >50K earners in India?

All numerical values are rounded to one decimal place, as required by freeCodeCamp.

🧩 How to Run This Project
1. Install Python & Dependencies

Make sure you have Python installed (3.8+ recommended).

Install Pandas:

pip install pandas

2. Clone or Download the Repo
git clone https://github.com/<your-username>/Demographic_Data_Analyser.git
cd Demographic_Data_Analyser

3. Add the Dataset

Place adult.data.csv inside this folder.
The filename must be exactly:

adult.data.csv

4. Run the Script

Use:

python main.py


(or python3 main.py on macOS/Linux)

This will print all computed statistics to your terminal.

🧪 Running Unit Tests (Optional)

If you're using freeCodeCamp's test suite:

python -m pytest -q


Make sure test_module.py is in the same folder.

🧠 Key Technologies Used

Python 3

Pandas

Git / GitHub
