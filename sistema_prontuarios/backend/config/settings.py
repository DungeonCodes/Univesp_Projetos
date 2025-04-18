"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 5.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see,
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
<<<<<<< HEAD
import os
import dj_database_url
from dotenv import load_dotenv
=======
from decouple import config
import os
import dj_database_url
# from dotenv import load_dotenv > com o uso do decouple, nao e necessario essa biblioteca 
>>>>>>> bd

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY", "django-insecure-7ptpp97=ku&afe$97cr__u04w3l6b1jyt-7r=q)9zky(dnc2%&")

<<<<<<< HEAD
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv("DEBUG", "False").lower() == "true"

# Permitir apenas os hosts específicos
=======
# SECURITY WARNING: do not run with debug turned on in production!
DEBUG = os.getenv("DEBUG", "False").lower() == "true"

# Permitir apenas os hosts especificos
>>>>>>> bd
ALLOWED_HOSTS = [
    "univespprojetos-production.up.railway.app",
    "127.0.0.1",
    "localhost"
]

# CSRF Configuration
CSRF_TRUSTED_ORIGINS = [
    "https://univespprojetos-production.up.railway.app"
]

<<<<<<< HEAD
CSRF_COOKIE_SECURE = True  # Garantir cookies seguros em produção
=======
CSRF_COOKIE_SECURE = True  # Garantir cookies seguros em producao
>>>>>>> bd

# Adicionar suporte a Proxy para HTTPS no Railway
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

# Application definition
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
<<<<<<< HEAD
    "prontuarios",  # Certifique-se de que essa linha está aqui
=======
    "prontuarios",  # Certifique-se de que essa linha esta aqui
>>>>>>> bd
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

<<<<<<< HEAD
# Carregar variáveis do .env
load_dotenv(dotenv_path=os.path.join(BASE_DIR, ".env"))

# Configuração do Banco de Dados
DATABASES = {
    "default": dj_database_url.config(
        default=os.getenv("DATABASE_URL"),
=======
# Carregar variaveis do .env - config() (decouple) carrega automaticamente 
# as variaveis do arquivo .env se estiver na raiz do projeto
# load_dotenv(dotenv_path=os.path.join(BASE_DIR, ".env"))

# Configuracao do Banco de Dados
DATABASES = {
    "default": dj_database_url.config(
        default=config("DATABASE_URL"),
>>>>>>> bd
        conn_max_age=600,
        ssl_require=config("DATABASE_SSL_REQUIRE", default=False, cast=bool)
    )
}

# Desativar prepared statements para suportar o Transaction Pooler
DATABASES["default"]["DISABLE_SERVER_SIDE_CURSORS"] = True

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

<<<<<<< HEAD
# Configuração para arquivos estáticos no Railway
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

# Default primary key field type
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
=======
# Configuracao de hora
DATE_INPUT_FORMATS = ['%d/%m/%Y %H:%M']

# Configuracao para arquivos estaticos no Railway
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

AUTH_USER_MODEL = 'prontuarios.SisUser'
>>>>>>> bd
