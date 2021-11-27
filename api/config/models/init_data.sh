for filename in ./config/models/*.json; do
	python manage.py loaddata $filename
done
