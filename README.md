# logrolling

Like log-rolling in real life, logrolling takes an awkward activity,
(using logging), and attempts to make it seem effortless.

An encapsulation of python logging to make using it easier and more
pythonic.

## Use

You only need to use logrolling in the top module.
```
logger = logrolling.LogWrapper(
    __name__,
    [
        "imported_module1",
        "imported_module2",
        "imported_module3",
    ],
    use_console=True,
)
logger.add_filehandler("log.txt")
logger.debug("Starting logging")
```

Then, in the imported modules, you can use logging.  The following would be at
the top of `imported_module1` for example:
```
import logging

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())
```
