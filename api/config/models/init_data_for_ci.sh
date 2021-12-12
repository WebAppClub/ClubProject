for filename in ./config/models/*/*.json; do
	set -e
	../venv/bin/python3 manage.py loaddata $filename
done
