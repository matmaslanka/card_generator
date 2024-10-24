# Card Generator
An application based on the Django framework connected with databases and API to generate business card.

## Installation

1. Clone the repository:
   `git clone https://github.com/matmaslanka/card_generator.git`
2. Set up a virtual environment:
   python3 -m venv env <br/>
   source env/bin/activate  # On Windows: env\Scripts\activate
3. Install the dependencies from requirements.txt:
   `pip install -r requirements.txt`
4.  Open a terminal and navigate to the project directory in bash: 
   `cd .\card_generator`
5. Add your own secret key to movie_site/settings.py on line 24.
   Example: "0ne2fxv8vpeisxbd1xtq2kx-vnlv_7bnf%8nwc+jj(bpoe3_@v"
   (Note: The secret key is hidden for security reasons.)
6. Set up the database and run migrations (the application will crash without this step):
   `python manage.py migrate`
