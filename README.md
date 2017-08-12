lehar
=====

![Header image](docs/header.png)

Python library to generate sparklines ▁▂▄▅▇█ in your shell based upon relative ordering of data. `lehar` is a [Hindi](https://en.wikipedia.org/wiki/Hindi) word which means wave. `lehar` can be invoked via *commandline* also.

[Some cool usage](https://github.com/holman/spark/wiki/Wicked-Cool-Usage)

## Demo

<a href="https://asciinema.org/a/vvtuqfiG5bOkc5ybMvAXf4bsM" target="_blank"><img src="https://asciinema.org/a/vvtuqfiG5bOkc5ybMvAXf4bsM.png" /></a>


## Installation



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

## Commandline

```shell 
$ lehar 1 2 3 4 5

$ lehar -c red 1 2 3 4 5
```

## Support
`lehar` supports both `Python2` & `Python3`.

## License

MIT © [Ankush Sharma](http://github.com/darxtrix)
