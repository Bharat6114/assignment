Prerequisites:
1. Install Python
Install python-3.10.5 and python-pip. Follow the steps from the below reference document based on your Operating System. Reference: https://docs.python-guide.org/starting/installation/

2.Clone git repository
git clone https://github.com/Bharat6114/assignment.git
3.Setup virtual environment
pip install pipenv 
#to active enviroment
pipenv shell

4.Install requirements
pip install -r requirements.txt
5. Run the server
# Run the server
python manage.py runserver

# Make migrations(if required)
python manage.py makemigrations
python manage.py migrate
#for superadmin
urls:localhost:8000/admin/
name:bharat
password:9848826114
