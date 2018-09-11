EXTRA_DIST=setup.py foo

all-local:
	python setup.py build

install-exec-local:
	mkdir -p $(DESTDIR)/$(pythondir)/
	PYTHONPATH=$(DESTDIR)/$(pythondir)/ \
	    python setup.py install --prefix=$(DESTDIR)/$(prefix) \
	    $(DEB_PYTHON_INSTALL_ARGS)

clean-local:
	python setup.py clean --all
	-rm -rf build dist foo.egg-info
