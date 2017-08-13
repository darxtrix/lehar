lehar
=====

![Header image](docs/header.png)

![travis_badge](https://travis-ci.org/darxtrix/lehar.svg?branch=master) [![Code Climate](https://codeclimate.com/github/darxtrix/lehar/badges/gpa.svg)](https://codeclimate.com/github/darxtrix/lehar) [![Test Coverage](https://codeclimate.com/github/darxtrix/lehar/badges/coverage.svg)](https://codeclimate.com/github/darxtrix/lehar/coverage) [![Issue Count](https://codeclimate.com/github/darxtrix/lehar/badges/issue_count.svg)](https://codeclimate.com/github/darxtrix/lehar)

Python library to generate sparklines ▁▂▄▅▇█ in your shell based upon relative ordering of data. `lehar` is a [Hindi](https://en.wikipedia.org/wiki/Hindi) word which means wave. `lehar` can be invoked via *commandline* also.

```Bash
# Find commits by authors in a git repo
$ git shortlog -s | cut -f1 | lehar
▇▁▁▁▁▁▁▂▃▁▁█▁▁▂▃▅▁▁▁▂▆▁▁▁▂▁▁▁▁▂▇▁▅▆▁▁▁▄▁▁█▁▁▂▁▂▁
```
[Some cool usage](https://github.com/holman/spark/wiki/Wicked-Cool-Usage)

## Demo

<a href="https://asciinema.org/a/vvtuqfiG5bOkc5ybMvAXf4bsM" target="_blank"><img src="https://asciinema.org/a/vvtuqfiG5bOkc5ybMvAXf4bsM.png" /></a>


## Installation

Using `homebrew`:
```Bash
$ brew install lehar 
```

Using `pip`
```
$ pip install lehar
```

## API

### lehar.draw(numbers,options)

#### numbers
`type` : `list`

#### options
Only supported option is `color`
eg. `color='red'`

#### Basic Usage

```Python

>>> import lehar

# Strings
>>> lehar.draw(["0","1","2","3","4"])
'▁▂▄▆█'

# Numbers
>>> lehar.draw([0,1,2,3,4])
'▁▂▄▆█'

# Negatives
>>> lehar.draw([1,3,-34,12,44,81,0])
'▃▃▁▄▆█▃'

# Missing data
>>> lehar.draw([1,3,-34,'',12,44,'',81,0])
'▃▃▁ ▄▆ █▃'
```

#### Adding colors 

```Python
>>> lehar.draw(["0","1","2","3","4"],color="yellow")

>>> lehar.draw([1,3,-34,'',12,44,'',81,0],color="cyan")

```

## Command line 

```Bash
$ lehar 1 2 3 4 5

$ lehar -c red 1 2 3 4 5

$ echo "-c cyan 1 2 3 4 5" | lehar

$ lehar < input
```

## Support
`lehar` supports both `Python2` & `Python3`.

## Contributing Guide
- Setup
```Bash
$ git clone https://github.com/darxtrix/lehar
$ cd lehar 
$ pip install -r requirements.txt
$ python setup.py develop
$ lehar 
```

- Tests are located at `lehar/tests.py` and covergae tests are located at `.travis.yml`
```Bash
$ python tests.py
```

- While sending a pull request increment the version at [VERSION](https://github.com/darxtrix/lehar/blob/master/lehar/VERSION) and make sure the travis build passes.

## Some feedback please

[![](https://m131jyck4m.execute-api.us-west-2.amazonaws.com/prod/poll/01BQCW33ZE61TN052NM8KQF803/Its%20awesome%2C%20thanks%20!)](https://m131jyck4m.execute-api.us-west-2.amazonaws.com/prod/poll/01BQCW33ZE61TN052NM8KQF803/Its%20awesome%2C%20thanks%20!/vote)
[![](https://m131jyck4m.execute-api.us-west-2.amazonaws.com/prod/poll/01BQCW33ZE61TN052NM8KQF803/Needs%20more%20improvement)](https://m131jyck4m.execute-api.us-west-2.amazonaws.com/prod/poll/01BQCW33ZE61TN052NM8KQF803/Needs%20more%20improvement/vote)

## License

MIT © [Ankush Sharma](http://github.com/darxtrix)
