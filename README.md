![img1](https://raw.githubusercontent.com/mimseyedi/dlbar/master/docs/dlbar-poster.gif)
 
## Table of contents:
* [Introduction](#intro)
* [Installation](#install)
* [How to use dlbar?](#use)
* [Customize the download bar](#customize)
* [Contribution](#cont)


## Introduction <a class="anchor" id="intro"></a>
dlbar is a simple terminal progress bar for downloading and displaying download progress.

You can use this module to download files and display the download progress bar in your Python projects.
## Installation <a class="anchor" id="install"></a>
You can use pip to install:
```
python3 -m pip install dlbar
```
## How to use dlbar? <a class="anchor" id="use"></a>
To use the dlbar module, you must import it:
```python
from dlbar import DownloadBar

download_bar = DownloadBar()

download_bar.download(
    url='https://url',
    dest='/a/b/c/downloaded_file.suffix',
    title='Downloading downloaded_file.suffix'
)
```

Output:
```
Downloading downloaded_file.suffix
43% █████████████████████----------------------------- 197.777 MB/450.327 MB
```

## Customize the download bar <a class="anchor" id="customize"></a>
You have many options to customize your download bar. 

Pay attention to the following example on how to change the characters of the download bar:
```python
from dlbar import DownloadBar

download_bar = DownloadBar(
    empty_char='.',
    filled_char='>'
)

download_bar.download(
    url='https://url',
    dest='/a/b/c/downloaded_file.suffix',
    title='Downloading downloaded_file.suffix'
)
```

Output:
```
Downloading downloaded_file.suffix
63% >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>................... 284.590 MB/450.327 MB
```

You can even use ANSI codes to color the download bar characters:
```python
from dlbar import DownloadBar

download_bar = DownloadBar(
    empty_char=f"\033[31m{chr(9472)}\033[0m",
    filled_char=f"\033[32m{chr(9472)}\033[0m"
)

download_bar.download(
    url='https://url',
    dest='/a/b/c/downloaded_file.suffix',
    title='Downloading downloaded_file.suffix'
)
```

Output:
![img1](https://raw.githubusercontent.com/mimseyedi/dlbar/master/docs/ANSI-char.png)

You can also change the width of the download bar (any number greater than or equal to 10 is valid):
```python
from dlbar import DownloadBar

download_bar = DownloadBar(width=35)

download_bar.download(
    url='https://url',
    dest='/a/b/c/downloaded_file.suffix',
    title='Downloading downloaded_file.suffix'
)
```

Output:
```
Downloading downloaded_file.suffix
12% ████------------------------------- 54.512 MB/450.327 MB
```

You can even hide the percentage or progress status of the download:
```python
from dlbar import DownloadBar

download_bar = DownloadBar(percent=False)

download_bar.download(
    url='https://url',
    dest='/a/b/c/downloaded_file.suffix',
    title='Downloading downloaded_file.suffix'
)
```

Output:
```
Downloading downloaded_file.suffix
█████████████████████----------------------------- 197.777 MB/450.327 MB
```

You can also deal with attributes in the form of properties and change their values after creating an instance:
```python
from dlbar import DownloadBar

download_bar = DownloadBar()

download_bar.status = False
download_bar.filled_char = '#'

download_bar.download(
    url='https://url',
    dest='/a/b/c/downloaded_file.suffix',
    title='Downloading downloaded_file.suffix'
)
```

Output:
```
Downloading downloaded_file.suffix
43% #####################-----------------------------
```

## Contribution <a class="anchor" id="cont"></a>
dlbar is a free and open source project under the MIT license. You can easily use dlbar and contribute if you have an idea for development.

Thank you