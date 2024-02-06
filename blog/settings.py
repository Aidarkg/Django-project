from pathlib import Path

# Base directory of the project
BASE_DIR = Path(__file__).resolve().parent.parent

# Secret key - Django will use this to encrypt and sign things
SECRET_KEY = 'django-insecure-jps1*!j$q%&w5nki3#o0+)4f96z@1qv2^nsb*c6f)7v3i$y)es'

# Debug mode - True means we're in development
DEBUG = True

# Allowed hosts - Django will only serve requests from these hosts
ALLOWED_HOSTS = []

# Application definition
INSTALLED_APPS = [
    # installed apps
    'django.contrib.admin',  # Django's admin site
    'django.contrib.auth',  # Django's authentication framework
    'django.contrib.contenttypes',  # Django's content types framework
    'django.contrib.sessions',  # Django's session framework
    'django.contrib.messages',  # Django's messaging framework (for errors, etc.)
    'django.contrib.staticfiles',  # Django's static file framework

    # my apps
    'post',

    # third-party apps
]

# Middleware - code that runs before and after views are called
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',  # Security middleware
    'django.contrib.sessions.middleware.SessionMiddleware',  # Session middleware
    'django.middleware.common.CommonMiddleware',  # Common middleware
    'django.middleware.csrf.CsrfViewMiddleware',  # CSRF middleware
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # Authentication middleware
    'django.contrib.messages.middleware.MessageMiddleware',  # Message middleware
    'django.middleware.clickjacking.XFrameOptionsMiddleware',  # Clickjacking middleware
]

# root URL configuration - tells Django where to find the root URL configuration module
ROOT_URLCONF = 'blog.urls'

# Template configuration - tells Django how to load templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / "templates",  # Tells Django to look for templates in the templates/ directory
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# WSGI application - tells Django where your WSGI application is
WSGI_APPLICATION = 'blog.wsgi.application'

# Database - tells Django how to connect to your database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Tells Django which database engine to use
        'NAME': BASE_DIR / 'db.sqlite3',  # Tells Django the name of your database file
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Asia/Bishkek'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
