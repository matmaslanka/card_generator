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
6. In \card_gen.view.py add your own url in line 25.
   Example: "https://fake_url/api/"
7. Set up the database and run migrations (the application will crash without this step):
   `python manage.py migrate`

## Running the project
1. Run the Django development server:
   `python manage.py runserver`
2. Access the project in your browser at: http://127.0.0.1:8000/.

## Usage
When the user runs the application, they will see a form to create a card. The user must add their first name, last name, company name, phone number, email address, and photo. By clicking "Next," the user will see a QR code and a URL address that redirects them to the presentation page.

On the presentation page, the user has two options. The first option is to click the "Send Card" button to submit the card to the system. The second option is to enter a phone number into the form field to receive a text message with the contact information from the system.

By choosing the second option, the user must enter their own details—first name, last name, company name, and email address—on the next screen to be added to the system. In the following step, the user will be prompted to enter the date and subject of the phone call. After clicking "Next," the user will see a meme. If the user clicks "OK," the page will redirect to the starting page. If the user clicks "Meme is not OK," the page will reload and display a new meme.

### Admin Access
(Optional) To access the Django admin interface, create a superuser account:
   `python manage.py createsuperuser`
