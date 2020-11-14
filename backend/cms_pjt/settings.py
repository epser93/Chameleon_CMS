import os
import environ
import boto3

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

env = environ.Env(DEBUG=(bool, False),)
environ.Env.read_env()

SECRET_KEY = env('SECRET_KEY')

DEBUG = env('DEBUG')

ALLOWED_HOSTS = ['*']
DEFAULT_FILE_STORAGE = 'cms_pjt.storages.MediaStorage'
STATICFILES_STORAGE = 'cms_pjt.storages.StaticStorage'
MEDIAFILES_LOCATION = 'media'
STATICFILES_LOCATION = 'static'

# Application definition

INSTALLED_APPS = [
    'django_extensions',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # corsheaders
    'corsheaders',

    # rest_framework
    'rest_framework',
    'rest_framework.authtoken',
    

    # rest_auth
    'rest_auth',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'rest_auth.registration',
    
    # S3 설정
    'storages',

    # my_app
    'accounts',
    'products',
    'services',
]

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'cms_pjt.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'cms_pjt.wsgi.application'


ENGINE = 'django.db.backends.mysql'
init_command = 'SET sql_mode="STRICT_TRANS_TABLES"'

DATABASES = {
    'default': {
        'ENGINE': ENGINE,
        'NAME': env('NAME'),
        'USER': env('DB_USER'),
        'PASSWORD': env('PASSWORD'),
        'HOST': env('HOST'),
        'PORT': env('MASTER_PORT'),
        'OPTIONS': {
            'init_command': init_command
        }
    },
    'master': {
        'ENGINE': ENGINE,
        'NAME': env('NAME'),
        'USER': env('DB_USER'),
        'PASSWORD': env('PASSWORD'),
        'HOST': env('HOST'),
        'PORT': env('MASTER_PORT'),
        'OPTIONS': {
            'init_command': init_command
        }
    },
    'slave': {
        'ENGINE': ENGINE,
        'NAME': env('NAME'),
        'USER': env('DB_USER'),
        'PASSWORD': env('PASSWORD'),
        'HOST': env('HOST'),
        'PORT': 3307,
        'OPTIONS': {
            'init_command': init_command
        }
    },
    # 'master': {
    #     'ENGINE': ENGINE,
    #     'NAME': env('MASTER_NAME'),
    #     'USER': env('MASTER_USER'),
    #     'PASSWORD': env('MASTER_PASSWORD'),
    #     'HOST': env('MASTER_HOST'),
    #     'PORT': env('MASTER_PORT'),
    #     'OPTIONS': {
    #         'init_command': init_command
    #     }
    # },
    # 'slave': {
    #     'ENGINE': ENGINE,
    #     'NAME': env('SLAVE_NAME'),
    #     'USER': env('SLAVE_USER'),
    #     'PASSWORD': env('SLAVE_PASSWORD'),
    #     'HOST': env('SLAVE_HOST'),
    #     'PORT': env('SLAVE_PORT'),
    #     'OPTIONS': {
    #         'init_command': init_command
    #     }
    # }
}

DATABASE_ROUTERS = ['cms_pjt.routers.MasterSlaveRouter']

SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
SESSION_CACHE_ALIAS = 'default'

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": env('LOCATION'),
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "PASSWORD": env('REDIS_PASSWORD'),
        }
    }
}


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


LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'

STATIC_DIR = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [
    STATIC_DIR,
]

# 유저모델은 accounts.의 User로 설정
AUTH_USER_MODEL = 'accounts.User'

# DRF auth settings
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ]
}


CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_ALL_ORIGINS = True

# 이미지 파일 관리
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

CORS_ORIGIN_ALLOW_ALL = True

# 이메일 관련 환경변수
ACCOUNT_EMAIL_REQUIRED = False
ACCOUNT_EMAIL_VERIFICATION = 'none'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = "smtp.gmail.com"
EMAIL_HOST_USER = env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

# 비밀번호 변경시 이전 비밀번호 체크여부
OLD_PASSWORD_FIELD_ENABLED = True

# 이메일 인증
ACCOUNT_ADAPTER = 'accounts.adapter.DefaultAccountAdapterCustom'
URL_FRONT = 'https://i3c205.p.ssafy.io/'


# AWS 관련

AWS_REGION = env('AWS_REGION')
AWS_STORAGE_BUCKET_NAME = env('AWS_STORAGE_BUCKET_NAME')
AWS_ACCESS_KEY_ID = env('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = env('AWS_SECRET_ACCESS_KEY')
AWS_S3_CUSTOM_DOMAIN = '{}.s3.{}.amazonaws.com'.format(AWS_STORAGE_BUCKET_NAME, AWS_REGION)
AWS_DEFAULT_ACL = env('AWS_DEFAULT_ACL')
