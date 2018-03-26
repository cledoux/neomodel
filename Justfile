clean:
	rm -rf ./dist ./build ./*.spec

# Build for PyPi
build: clean
	python2 ./setup.py sdist

# Upload to PyPi
upload: build
	twine upload ./dist/*

