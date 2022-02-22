<h1 align="center">Hi there! Here a Color-Tagged Print
<img src="https://github.com/blackcater/blackcater/raw/main/images/Hi.gif" height="32"/></h1>
<p align="center">
<img src=https://img.shields.io/pypi/v/ctprint.svg?color=%237B1E7A&style=flat-square>
<img src=https://shields-io-visitor-counter.herokuapp.com/badge?page=https://github.com/saner99/ctprint&color=purple&style=flat-square>
<img src=https://img.shields.io/github/repo-size/saner99/ctprint?color=g&style=flat-square>
<img src=https://img.shields.io/github/checks-status/saner99/ctprint/master?color=g&style=flat-square>
<img src=https://img.shields.io/github/last-commit/saner99/ctprint/master?style=flat-square>
<img src=https://img.shields.io/github/license/saner99/ctprint?color=g&style=flat-square>
<img src=https://img.shields.io/pypi/dd/ctprint?label=PyPI%20downloads&style=flat-square>
<img src=https://img.shields.io/github/release-date/saner99/ctprint?style=flat-square>
</p>
<h3 align="center">Cross-platform colorization terminal text using '&lt;tags> embedded in strings' (text markup)</h3>

## Installation

```python
pip install ctprint
```
_or_
```python
poetry add ctprint
```

## Usage

### Initialization

```python
from ctprint import ctp, ctdecode, cterr, ctlog  # callable
```

### ctp.help() -> None

_print colored and some interactive help-message. nothing return_

```python
ctp.help()  # print help message
```

### ctp(*strings: str) -> None

_obj of ctprint. decode `<tags>` in the strings and print it. nothing return_

```python
# decode <tags> and then print the string
ctp('<bw> black text on white background /> default formating')
```

<p align="center">
  <img src="https://user-images.githubusercontent.com/31666804/154970116-1071c2c8-bca0-4da6-8959-0c44259c1803.png" width="100%" title="ctp.help() output"></p>
  
### ctdecode( *strings: str) -> str
_decode `<tags>` in the strings and return it decoded_
```python
# decode <tags> in the strings and return decoded string
string0 = ' background /> default'
string1 = ' formating'
ctdecode('<bw> black text on white', string0, string1)
```
_return string_

### cterr(exception=None, comment='') -> None
_exception required. print colored error message from try/except. nothing return_
```python
try:
    1/0  # any broken line
except Exception as _ex:
    cterr(_ex)
```
<p align="center">
  <img src="https://user-images.githubusercontent.com/31666804/154970120-48464807-9d99-4833-b873-3453eec656f6.png"></p>
  
### ctlog(**vars) -> None
_vars required. print colored message with names $ values of all **vars. nothibg return_

```python
var0 = var1 = 0

def example_ctlog():

    var2 = 'string val'
    var3 = {'ctp_string': '<bg_red><red>red text on red background (NO) >'}

    # out of the function, var0=var2 - nothing problems.
    ctlog(var0=var0, var1=var1, var2=var2, var3=var3)
```
<p align="center">
<img src="https://user-images.githubusercontent.com/31666804/154970137-f07b1ca4-f73b-4ffd-a1a1-d49905e502fa.png" width="100%" title="ctp.help() output"></p>

<h2 align ="center"> ctprint.help()</h2>
<p align="center">
<img src="https://user-images.githubusercontent.com/31666804/154970057-6f710980-c6c1-470b-a5d8-ac1006b04eda.png" width="100%" title="ctp.help() output">
<img src="https://user-images.githubusercontent.com/31666804/154970079-d4f150fe-fa74-466c-8e57-576c6b5cb0ce.png" width="100%" title="ctp.help() output[1]">
<img src="https://user-images.githubusercontent.com/31666804/154970102-ea031f0e-a836-47c8-bf0d-7235a8937f6f.png" width="100%" title="ctp.help() output[2]">
</p>


## Thanks
- [`colorama - wonderfull lib. Makes ANSI escape character sequences work under MS Windows. `](https://pypi.org/project/colorama/)

