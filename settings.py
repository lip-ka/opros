from os import environ
import dj_database_url
import os


SESSION_CONFIGS = [
    dict(
        name = 'studtes',
        display_name = "The test of future perception",
        app_sequence = ['studtes'],
        num_demo_participants = 25,
    ),
]

ROOMS = [
    dict(
        name = 'main_test',
        display_name = 'Future perception',
        use_secure_urls = False  # (опционально) если хотите добавить дополнительную безопасность
    ),
]

DATABASES = {
    'default': dj_database_url.config(
        default='postgres://experiment:here_password_of_the_database@localhost/djangodb'
    )
}


# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point = 1.00, participation_fee = 0.00, doc = ""
)

PARTICIPANT_FIELDS = []
SESSION_FIELDS = []

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '6004087896811'
