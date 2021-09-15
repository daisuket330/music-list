DATABASES = {

    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'music_library_database',
        'USER': 'root',
        'PASSWORD': 'Taco1234',
        'PORT': '3306',
        'HOST': '127.0.0.1',
        'OPTIONS': {
            'autocommit' : True
        }
    }
}

SECRET_KEY = 'django-insecure-=gv8&hne1^xiiv&k-$o+c@7ap+y3(3f3id=a4t7ey_n$lvn2vi'