# Text Utilities


Text Utilities is a simple Django web application that allows users to analyze and manipulate text in various ways. It provides multiple text processing features with an easy-to-use web interface.

## Features

- **Remove Punctuation:** Eliminate all punctuation from the input text.
- **Convert to Uppercase:** Change all letters in the text to uppercase.
- **Remove New Lines:** Remove all newline characters from the text.
- **Remove Extra Spaces:** Remove extra spaces between words.
- **Count Characters:** Display the total number of characters in the text.


## Tech Stack

- **Backend:** Django 6
- **Frontend:** HTML, CSS, Bootstrap 5
- **Language:** Python 3.13

## Installation

1. Clone the repository:

```bash
git clone https://github.com/minahil-azaz/text-utilities.git
Navigate into the project folder:

cd text-utilities
Create a virtual environment:

python -m venv venv
Activate the virtual environment:

Mac/Linux:

source venv/bin/activate
Windows:

venv\Scripts\activate
Install dependencies:

pip install django
Run migrations:

python manage.py migrate
Start the development server:

python manage.py runserver
Open your browser and go to http://127.0.0.1:8000

Usage
Enter your text in the textarea.

Select the desired text processing options.

Click Analyze Text to view the result.

