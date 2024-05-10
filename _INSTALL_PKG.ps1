pipenv run python setup.py install #python setup.py sdist bdist_wheel; pip install -e
pipenv run python setup.py sdist
#pipenv run python setup.py develop
python setup.py register
python setup.py sdist upload