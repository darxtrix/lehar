# This is used for bookkeeping of commands/stuff used during development

Python packaging/distribution GUIDE  - https://packaging.python.org/tutorials/distributing-packages/

Run the following commands for developing, we are building the wheel package instead of source distribution:

$ python setup.py bdist_wheel 
$ python setup.py develop

For uploading to PyPi

$ twine upload dist/lehar-0.4*