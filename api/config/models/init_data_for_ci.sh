for filename in ./config/models/*/*.json; do
	../.venv/bin/python3 manage.py loaddata $filename
done
