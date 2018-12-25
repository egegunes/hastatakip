HOME=/home/hastatakip
CODEDIR=$(HOME)/hastatakip

build:
	sudo docker build -t hastatakip .
run:
	sudo docker run --rm --name hastatakip -p 8080:8000 -v $(shell pwd)/db.sqlite3:/app/db.sqlite3 hastatakip
run-it:
	sudo docker run --rm -it --name hastatakip -p 8080:8000 -v $(shell pwd)/db.sqlite3:/app/db.sqlite3 hastatakip
shell:
	sudo docker exec -it hastatakip /bin/sh
django-shell:
	sudo docker exec -it hastatakip python manage.py shell
requirements:
	test -d $(HOME)/environment && source $(HOME)/environment/bin/activate || python3 -m venv $(HOME)/environment
	pip install --upgrade pip setuptools wheel
	pip install -r $(CODEDIR)/requirements.txt
	chown -R hastatakip:hastatakip $(HOME)/environment
scripts:
	ln -s $(CODEDIR)/utils $(HOME)/bin
	chown -R hastatakip:hastatakip $(HOME)/bin
crontab:
	crontab -u hastatakip < crontab/crontab
folders:
	mkdir -p $(HOME)/logs
	mkdir -p $(HOME)/db
	mkdir -p $(HOME)/static
	mkdir -p $(HOME)/media
	chown -R hastatakip:hastatakip $(HOME)/logs $(HOME)/db $(HOME)/static $(HOME)/media
staticfiles:
	source $(HOME)/environment/bin/activate
	cd $(CODEDIR)/src
	python manage.py collectstatic --noinput
	chown -R hastatakip:hastatakip $(HOME)/static
nginx:
	ln -s $(CODEDIR)/nginx/hastatakip.conf /etc/nginx/conf.d/hastatakip.conf
	ln -s $(CODEDIR)/nginx/hastatakip-ssl.conf /etc/nginx/conf.d/hastatakip-ssl.conf
nginx-ubuntu:
	ln -s $(CODEDIR)/nginx/hastatakip.conf /etc/nginx/sites-enabled/hastatakip.conf
	ln -s $(CODEDIR)/nginx/hastatakip-ssl.conf /etc/nginx/sites-enabled/hastatakip-ssl.conf
systemd:
	ln -s $(CODEDIR)/systemd/hastatakip.service /etc/systemd/system/hastatakip.service
	systemctl daemon-reload
	systemctl start hastatakip
	systemctl enable hastatakip
install: requirements scripts crontab folders staticfiles systemd
