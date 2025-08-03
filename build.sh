# # build.sh
# #!/usr/bin/env bash
# python manage.py collectstatic --no-input
# python manage.py migrate
# #!/usr/bin/env bash
# poetry install
#!/usr/bin/env bash
poetry install
poetry run python manage.py collectstatic --no-input
poetry run python manage.py migrate
