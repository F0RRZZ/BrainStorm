import os
import pathlib

from django.utils.translation import gettext_lazy as _
import environ

BASE_DIR = pathlib.Path(__file__).resolve().parent.parent

environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

env = environ.Env(
    ALLOWED_HOSTS=(list, ['*']),
    DEBUG=(bool, True),
    EMAIL_ADDRESS=(str, 'example@example.com'),
    EMAIL_PASSWORD=(str, 'password'),
    GITHUB_CLIENT_ID=(str, 'client_id'),
    GITHUB_SECRET_KEY=(str, 'secret_key'),
    SECRET_KEY=(str, 'dummy-key'),
    USERS_AUTOACTIVATE=(bool, True),
)

ALLOWED_HOSTS = env('ALLOWED_HOSTS')
DEBUG = env('DEBUG')
EMAIL = env('EMAIL_ADDRESS')

SECRET_KEY = env('SECRET_KEY')

USERS_AUTOACTIVATE = env('USERS_AUTOACTIVATE')

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.github',
    'allauth.socialaccount.providers.google',
    'django_cleanup.apps.CleanupConfig',
    'sorl.thumbnail',
    'about.apps.AboutConfig',
    'core.apps.CoreConfig',
    'collaboration_request.apps.CollaborationRequestConfig',
    'comments.apps.CommentsConfig',
    'feedback.apps.FeedbackConfig',
    'feeds.apps.FeedsConfig',
    'projects.apps.ProjectsConfig',
    'rating.apps.RatingConfig',
    'tags.apps.TagsConfig',
    'users.apps.UsersConfig',
]

if DEBUG:
    INSTALLED_APPS += [
        'debug_toolbar',
    ]

INTERNAL_IPS = [
    '127.0.0.1',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
if DEBUG:
    MIDDLEWARE += [
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    ]

ROOT_URLCONF = 'brainstorm.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates',
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

WSGI_APPLICATION = 'brainstorm.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': (
            'django.contrib.auth.password_validation.'
            'UserAttributeSimilarityValidator'
        ),
    },
    {
        'NAME': (
            'django.contrib.auth.password_validation.MinimumLengthValidator'
        ),
    },
    {
        'NAME': (
            'django.contrib.auth.password_validation.CommonPasswordValidator'
        ),
    },
    {
        'NAME': (
            'django.contrib.auth.password_validation.NumericPasswordValidator'
        ),
    },
]

LANGUAGE_CODE = 'en'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static_dev',
]

DEFAULT_USER_IMAGE_PATH = 'images/user_default.jpg'

THUMBNAIL_DEBUG = True

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = '/media/'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_FILE_PATH = BASE_DIR / 'sent_emails'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = EMAIL
EMAIL_HOST_PASSWORD = env('EMAIL_PASSWORD')
EMAIL_PORT = 587
EMAIL_USE_TLS = True

LOGIN_URL = '/auth/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'


AUTH_USER_MODEL = 'users.User'
AUTHENTICATION_BACKENDS = [
    'users.backend.NormalizedEmailAuthBackend',
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

SITE_ID = 1

SOCIALACCOUNT_PROVIDERS = {
    'github': {
        'APP': {
            'client_id': env('GITHUB_CLIENT_ID'),
            'secret': env('GITHUB_SECRET_KEY'),
            'key': '',
        }
    },
}

LANGUAGES = (
    ('en', _('English')),
    ('ru', _('Russian')),
    ('de', _('Deutsche')),
)

LOCALE_PATHS = [
    BASE_DIR / 'locale',
]

REDIS_HOST = '0.0.0.0'
REDIS_PORT = '6379'
CELERY_BROKER_URL = ''.join(['redis://', REDIS_HOST, ':', REDIS_PORT, '/0'])
CELERY_BROKER_TRANSPORT_OPTIONS = {'visibility_timeout': 3600}
CELERY_RESULT_BACKEND = ''.join(
    ['redis://', REDIS_HOST, ':', REDIS_PORT, '/0']
)
