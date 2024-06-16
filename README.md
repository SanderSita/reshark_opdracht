
## Starting Django backend

##### windows
```bash
cd  backend
python  -m  venv  .venv
.venv\Scripts\activate
pip  install  -r  requirements.txt
python manage.py migrate
python  manage.py  runserver
```

##### macOS
```bash
cd backend
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