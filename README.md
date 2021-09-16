
See how to construct Python logger for a module in a program that is part
of the module so that the log level (and formatter etc.) applies only to the
`foo` module (and its sub-modules). This is to avoid getting debug log messages
from third party modules when debug is enabled for the program.

Assumes all the used components use the standard practice of getting the logger
using
```
    logging.getLogger(__name__)
```

The basis for the package was was taken from
https://python-packaging-tutorial.readthedocs.io/en/latest/setup_py.html#exercise-a-small-example-package
