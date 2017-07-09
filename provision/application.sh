[ -d "environment" ] && rm -rf environment

pyvenv-3.5 environment
source environment/bin/activate

pip3.5 install --upgrade pip
pip3.5 install -r hastatakip/requirements.txt

cd hastatakip/src

python3.5 manage.py collectstatic --no-input
python3.5 manage.py makemigrations
python3.5 manage.py migrate
