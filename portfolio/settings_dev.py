from .settings_common import *

SECRET_KEY = 'django-insecure-)ta6_6er#n11^rl))vvkocw4p(rt9h4sjh+%_$cz#54b-m38(4'
DEBUG = True
ALLOWED_HOSTS = []
LOGGING={
    'version':1,
    'disable_existing_loggers':False,

    'loggers':{
        'django':{
        'handlers':['console'],
        'level':'INFO',
        },
        'portfolio':{
            'handlers':['console'],
            'level':'DEBUG',
        },

    },

    'handlers':{
        'console':{
            'level':'DEBUG',
            'class':'logging.StreamHandler',
            'formatter':'dev'
        },
    },

    'formatters':{
        'dev':{
            'format':'\t'.join([
                '%(asctime)s',
                '[%(levelname)s]',
                '%(pathname)s(Line:%(lineno)d)',
                '%(message)s'
            ])
        },
    }
}