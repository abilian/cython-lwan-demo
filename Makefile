.PHONY:
all: build-module

.PHONY:
build-lwan:
	mkdir -p vendor/lwan/build
	cd vendor/lwan/build && cmake .. -DCMAKE_BUILD_TYPE=Release
	cd vendor/lwan/build && make

.PHONY:
build-module:
	python3 setup.py build_ext --inplace

.PHONY:
run: build-module
	./run.py

.PHONY:
clean:
	rm -rf vendor/lwan/build
	rm -f src/*.c
	rm -f *.so
	python setup.py clean


.PHONY:
push:
	rsync -e ssh -avz ./ puer:cython-lwan/
