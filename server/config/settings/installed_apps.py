INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',
    # 'oauth2_provider',
    # 'social_django',
    # 'rest_framework_social_oauth2',
]

LOCAL_APPS = [
    'apps.test',
    'apps.users',
    'apps.cart',
    'apps.money_accounts',
    'apps.products',
    'apps.drawings',
    'apps.secondary_objects'
]

INSTALLED_APPS += LOCAL_APPS

LOCAL_MIGRATIONS = [app_path.split('.')[1] for app_path in LOCAL_APPS]

MIGRATION_PATH = 'config.migrations.'

MIGRATION_MODULES = {app_name: MIGRATION_PATH + app_name for app_name in LOCAL_MIGRATIONS}
