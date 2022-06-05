release: python manage.py migrate \
&& python manage.py loaddata products/fixtures/gender.json \
&& python manage.py loaddata products/fixtures/categories.json \
&& python manage.py loaddata products/fixtures/sub_categories.json \
&& python manage.py loaddata products/fixtures/products.json \
web: gunicorn we_glove_boxing.wsgi