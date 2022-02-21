<h1 align="center">Hi there! Here a TagsColoredPrint
<img src="https://github.com/blackcater/blackcater/raw/main/images/Hi.gif" height="32"/></h1>
<h3 align="center">Python script for coloring terminal output using '<tags> embedded in strings' (like a simle text markup language)</h3>
  
![](https://api.visitorbadge.io/api/VisitorHit?user=saner9999f&repo=tcprint&countColor=%237B1E7A)
![](https://img.shields.io/github/repo-size/saner99/tcprint?color=g&style=for-the-badge)
![](https://img.shields.io/github/checks-status/saner99/tcprint/master?color=g&style=for-the-badge)
![](https://img.shields.io/github/last-commit/saner99/tcprint/master?style=for-the-badge)
![](https://img.shields.io/github/release-date/saner99/tcprint?style=for-the-badge)
![](https://img.shields.io/github/stars/saner99/tcprint?style=for-the-badge)
![](https://img.shields.io/github/forks/saner99/tcprint?style=for-the-badge)
  

## Installation 
  ```python
  pip install tcprint
  ```
## Usage

### Initialization 
```python
  from tcprint import tcp, tdecode, terr, tlog # callable 
```

### tcp.help()
_print colored and some interractive help-message. nothing return_
```python
tcp.help() # print help message
```
_output:_

  
  
  
### tcp(string: str)
  _obj of tcprint. decode `<tags>` in the string and print it. nothing return_
  ```python
  tcp('<bw> black text on white background /> default formating') # decode <tags> and then print the string
  ```
<p align="center">
  <img src="https://user-images.githubusercontent.com/31666804/154783032-58888b00-d028-4a17-8d6c-bfe34bb8e604.png" width="100%" title="tcp.help() output">
  
  ### tdecode( *strings: str) -> str
  _decode `<tags>` in the strings and return it decoded_
  ```python
  tdecode('<bw> black text on white background /> default formating') # decode <tags> and then print the string
  ```
  _return string_
  
  ### terr(exception=None, comment='') -> None
  _exception required. print colored error message from try/except. nothing return_
  ```python
  try:
    1/0 #any broken line
  except Exception as _ex:
    terr(_ex)
  ```
<p align="center">
  <img src="https://user-images.githubusercontent.com/31666804/154783196-226b05f0-7401-41a1-8acc-84837140d7a0.png">
  
  ### tlog(**vars) -> None
  _vars required. print colored message with names $ values of all **vars. nothibg return_
  
  ```python
 var0 = var1 = 0

def example_tlog():

    var2 = 'string val'  # out of the try, out of the function, var0=var2 - nothing problems.
    var3 = {'tcp_string': '<bg_red><red>red text on red background (NO) >'}

    tlog(var0=var0, var1=var1, var2=var2, var3=var3)
  ```
<p align="center">
  <img src="https://user-images.githubusercontent.com/31666804/154783320-e90bd588-6d1a-4bef-a8c9-542302e30726.png" width="100%" title="tcp.help() output">
  
  
 
  
<!--   
- [`collide-2d-aabb-aabb`](https://github.com/noffle/collide-2d-aabb-aabb)
- [`goertzel`](https://github.com/noffle/goertzel)
- [`twitter-kv`](https://github.com/noffle/twitter-kv) -->
  
  <h2 align ="center"> tcprint.help()</h2>
<p align="center">
  <img src="https://user-images.githubusercontent.com/31666804/154776452-16a1722a-bd08-4432-af8f-254a5f3d4a41.png" width="100%" title="tcp.help() output">
  <img src="https://user-images.githubusercontent.com/31666804/154778504-3de31e36-4c7b-43fc-820a-727c2a397b20.png" width="100%" title="tcp.help() output[1]">
  <img src="https://user-images.githubusercontent.com/31666804/154778836-3f2168a1-c9ec-4602-ace7-54c429bb4ff5.png" width="100%" title="tcp.help() output[2]">
</p>
