Organize Settings Module
========================

First, transform the settings.py into a directory containing individual settings files for development, production, and testing. Here's the structure you'll create:

```bash

backend/
backend/
settings/
__init__.py
base.py       # Common settings
development.py  # Development-specific settings
production.py  # Production-specific settings
testing.py     # Testing-specific settings
```

- base.py: Contains settings common to all environments (e.g., INSTALLED_APPS, MIDDLEWARE).
- development.py: Settings for the development environment (e.g., DEBUG = True, database configurations for development).
- production.py: Production-specific settings (e.g., DEBUG = False, security settings, database configurations for production).
- testing.py: Settings used for running tests (e.g., using an in-memory database like SQLite for faster test execution).

### Using the Settings

To use these settings, you'll specify the appropriate settings module when running Django commands. For example:

<br>

#### For development:

```bash

python manage.py runserver --settings=backend.settings.development
```

<br>

#### For production:

```bash
python manage.py collectstatic --settings=backend.settings.production
python manage.py migrate --settings=backend.settings.production
```

<br>

#### For testing:

```bash
python manage.py test --settings=backend.settings.testing
```

<br>

You can also set the DJANGO_SETTINGS_MODULE environment variable in your development, production, or CI/CD environment to point to the correct settings module, simplifying command usage.