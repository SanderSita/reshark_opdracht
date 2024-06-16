
## Starting Django backend

##### windows
```bash
cd  backend
copy env.example .env
python  -m  venv  .venv
.venv\Scripts\activate
pip  install  -r  requirements.txt
python manage.py migrate
python  manage.py  runserver
```

##### macOS
```bash
cd backend
cp env.example .env
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
  
## Starting frontend

```bash
cd  frontend
npm  install
npm  run  dev
```