# settings.py

# Other settings...

DEBUG = True  # Enable debug mode for development

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']  # Allow local connections

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # Leave empty
        'APP_DIRS': True,  # Enables finding templates within your apps
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

# Add this line to define the URL configuration module
ROOT_URLCONF = 'SamEducation' 

# Other settings...
