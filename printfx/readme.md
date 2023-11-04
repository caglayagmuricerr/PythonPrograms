# PrintFX

PrintFX is a Python package for text output in CLI Apps. It provides print effects, including a three-dot animation and a classic typewriter effect, adding a touch of dynamism to console applications.

## Installation

You can install PrintFX using pip:
#### without the version number 
```bash
pip install printfx
```
#### with the version number
```bash
pip install printfx==1.0.0
```
## Usage

### Type Writer Effect

This will print a string gradually. You can change the delay time if its too fast or slow.

```bash
from printfx import type_writer_effect

text = "Hello, PrintFX!"
type_writer_effect(text, delay=0.05)
```

### Three Dots Effect

This will print 3 dots according to the delay time you specify.

```bash
from printfx import three_dots

three_dots(delay=1)
```

### Examples

will add example usage

## Licence
[MIT LICENCE](https://github.com/caglayagmuricerr/PythonPrograms/blob/master/LICENSE)

