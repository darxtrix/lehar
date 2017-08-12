Python packaging/distribution GUIDE  - https://packaging.python.org/tutorials/distributing-packages/

Run the following commands for developing, we are building the wheel package instead of source distribution:

$ python setup.py bdist_wheel 
$ python setup.py develop


# TODO:
fix case when nothing is provided 
Fix help section