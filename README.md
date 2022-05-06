# Telus_Data_Science
Data Science solution 


Pre-Requisite:

Python Version: Python 3.9.5

One need to install some required packages to run this code. The step to perform the installation is:

**pip3 install pandas**

**pip3 install wikipedia-api**

**pip3 install beautifulsoup4**

1. ## telus_task1_submission.py:  
This file contains the solution for Task1. To run this program one need to run the following command through terminal:

**python3 telus_task1_submission.py**

Output: The output of this file will be stored in the same location as the script named: 'Canadian_Company_Details-%Y-%m-%d-%H-%M-%S.csv'.


2. ## telus_task2_submission.py:
This file contains the solution for Task2. To run the program one need to pass two argument: filepath generated by task1 and the list of words. Please see below for the required command:

**python3 telus_task2_submission.py 'Canadian_Company_Details-%Y-%m-%d-%H-%M-%S.csv.csv' "[Manulife,Royal]"**

Please replace the filename with the original filepath while running the actual code. The third argument is the list of words which will be passed in this format: "[word_1,word_2,word_3,...,word_n]". The code will parse this format and take each word and find the most closest matched company name using fuzzy search algorithm.

Output: The output of this program will be saved in a csv file (same location as the script) has two columns. One is the user inputted word, another is the closest matched company name. The name of the csv file will be 'Task2_Output--%Y-%m-%d-%H-%M-%S.csv'.
