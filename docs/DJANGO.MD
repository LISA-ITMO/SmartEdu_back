## Requirements

- [ ] Python >= 3.11

## Local development

#### 🐍 Create venv

 ```bash
 python3.11 -m venv .venv
 ```

#### 🚀 Activate venv

 ```bash
 source .venv/bin/activate
 ```

#### 📦 Install requirements

 ```bash
 pip install -r django_core/requirements.txt
 ```

#### 📁 Collect staticfiles

 ```bash
 python django_core/manage.py collectstatic --noinput
 ```

#### 🐘 Run postgresql in docker-compose or other database

 ```bash
 docker compose --file local-docker-compose.yml up -d
 ```

#### 🗃️ Run migrations

 ```bash
 python django_core/manage.py migrate
 ```

#### 👑 Create superuser

```bash
python django_core/manage.py createsuperuser
```

#### 🚀 Run server

```bash
python django_core/manage.py runserver
```

## Swagger Docs

📖 Go to http://127.0.0.1:8000/api/swagger after running server

## Docker and Docker compose

🐳 Refer to: https://docs.docker.com/engine/install/

## Development

During development, use Black formatter, Pylint and Flake8.

## Git

### Sructure
- main
  - feature/...
  - fix/...

### Branches

❌ Do not push directly to `main` branch.

Use the following branch naming rules:

- `feature/<name>` for new features
- `bugfix/<name>` for bug fixes
- `hotfix/<name>` for hotfixes
- `release/<name>` for releases

Use the `kebab-case` branch naming rules for `name`.

### Pull requests

🔀 Squash commits before merging to `main` branch.

### Commit messages

Use standard commit naming rules: [conventionalcommits.org](https://www.conventionalcommits.org/en/v1.0.0/)
