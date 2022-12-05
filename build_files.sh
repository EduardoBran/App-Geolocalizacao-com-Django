# build_files.sh
pip install -r requirements.txt
python 3.9 manage.py makemigrations
python 3.9 manage.py migrate
python3.9 manage.py collectstatic