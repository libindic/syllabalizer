travis:
	python setup.py test --coverage \
		--coverage-package-name=syllabifier
	flake8 --max-complexity 15 --ignore F401 libindic/syllabifier

clean:
	find . -iname "*.pyc" -exec rm -vf {} \;
	find . -iname "__pycache__" -delete
	sudo rm -rf build dist *egg* .tox .coverage .testrepository
