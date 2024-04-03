
pythhon3 -m venv .env

. .env/bin/activate

pip install -r requarement.txt

./manage.py makemigrations

./manage.py migrate

./manage.py createsuperuser

