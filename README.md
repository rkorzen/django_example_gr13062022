# Instalacja Django

    pip install django

# Utworzenie projektu

    django-admin startproject <nazwa>

# Uruchomienie projektu

    cd <nazwa>  # jesli tam nie jestes
    python manage.py runserver

jak nie pamietamy nazwy polecenia

    python manage.py

# Uzycie pomocy dla polecenia

    python manage.py help <nazwa polecenia>

# W pliku <nazwa>/urls.py znajduje sie glowne narzedzie routingu

# Dodanie aplikacji

    python manage.py startapp <nazwa aplikacji>

# Po dodaniu aplikacji

- dodanie do INSTALLED_APPS 
    np. 'maths' albo korzystajcac apps.py 'maths.apps.MathsConfig'
- dodanie routingu - utworzenie pliku urls.py


# przydatne polecenia

- python manage.py diffsettings --all   # pokazuje różnice miedzy naszym settings a wartosciami domyslnymi
- python manage.py runserver
- python manage.py shell

- python manage.py makemigrations
- python manage.py migrate

- python manage.py showmigrations

- python manage.py createsuperuser

# przydatne rozszerzenia

- ipython: pip install ipython
- django-extensions: https://django-extensions.readthedocs.io