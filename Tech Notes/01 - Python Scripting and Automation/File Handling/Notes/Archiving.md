
```python
import zipfile

with zipfile.ZipFile('data.zip', 'r') as zipobj:
    bar_info = zipobj.getinfo('sub_dir/bar.py')
    print(bar_info.file_size)
```

```bash title:output ln:False
15277
```

## Script to List the Properties of contents of a Zip file

- note that `*` lists out the contents of the tuple as `args` for `datetime`

```python
import zipfile
from datetime import datetime

with zipfile.ZipFile('DM_240709_150431.sdocx', 'r') as zipobj:
    print(f'{zipobj.filename}:')
    print(f'{"NAME":15} {"DATE":20} {"FILE SIZE":10} {"COMPRESS SIZE":10}')
    
    for filename in zipobj.namelist():
	    fileinfo = zipobj.getinfo(filename)
	    
	    filename = fileinfo.filename
	    filename = (filename[:11] + "...") if len(filename) >= 15 else filename
	    
	    time = datetime(*fileinfo.date_time).strftime('%d %b %Y')
	    filesize = str(fileinfo.file_size)
	    filecsize = str(fileinfo.compress_size)
	    
	    print(f'{filename:15} {time:20} {filesize:10} {filecsize:10}')
```

```bash title:output ln:False
DM_240709_150431.sdocx:
NAME            DATE                 FILE SIZE  COMPRESS SIZE
pageIdInfo.dat  11 Jul 2024          564        436
7b4650e0-e7...  11 Jul 2024          4839752    1542139
7b46613e-e7...  11 Jul 2024          3211905    1025652
dea6de50-e7...  11 Jul 2024          1350038    431739
4b1f6826-e8...  11 Jul 2024          336        263
6bb9b6dc-e8...  11 Jul 2024          336        261
media/media...  11 Jul 2024          883        486
```


---

## Extracting ZIP Archives

using `.extract()` and `.extractall()`

```python ln:False
>>> import zipfile
>>> import os

>>> os.listdir('.')
['data.zip']

>>> data_zip = zipfile.ZipFile('data.zip', 'r')

>>> # Extract a single file to current directory
>>> data_zip.extract('file1.py')
'/home/terra/test/dir1/zip_extract/file1.py'

>>> os.listdir('.')
['file1.py', 'data.zip']

>>> # Extract all files into a different directory
>>> data_zip.extractall(path='extract_dir/')

>>> os.listdir('.')
['file1.py', 'extract_dir', 'data.zip']

>>> os.listdir('extract_dir')
['file1.py', 'file3.py', 'file2.py', 'sub_dir']

>>> data_zip.close()
```

---

## Opening TAR Archives

```python
import tarfile

with tarfile.open('example.tar', 'r') as tar_file:
    print(tar_file.getnames())
```

| Mode    | Action                                                 |
| ------- | ------------------------------------------------------ |
| `r`     | Opens archive for reading with transparent compression |
| `r:gz`  | Opens archive for reading with gzip compression        |
| `r:bz2` | Opens archive for reading with bzip2 compression       |
| `r:xz`  | Opens archive for reading with lzma compression        |
| `w`     | Opens archive for uncompressed writing                 |
| `w:gz`  | Opens archive for gzip compressed writing              |
| `w:xz`  | Opens archive for lzma compressed writing              |
| `a`     | Opens archive for appending with no compression        |
### Obtaining Metadata of TAR Archives

```python ln:False
>>> for entry in tar.getmembers():
...     print(entry.name)
...     print(' Modified:', time.ctime(entry.mtime))
...     print(' Size    :', entry.size, 'bytes')
...     print()
CONTRIBUTING.rst
 Modified: Sat Nov  1 09:09:51 2018
 Size    : 402 bytes

README.md
 Modified: Sat Nov  3 07:29:40 2018
 Size    : 5426 bytes

app.py
 Modified: Sat Nov  3 07:29:13 2018
 Size    : 6218 bytes
```

---
## Extracting TAR Archives

- to extract single file from tar
```python ln:False
>>> tar.extract('README.md')
>>> os.listdir('.')
['README.md', 'example.tar']
```

- To unpack or extract everything from the archive
```python ln:False
>>> tar.extractall(path="extracted/")
>>> tar.close()
```

> [!note] 
> Opened archives should always be closed after they have been read or written to.

---

## Creating new TAR Archive

- setting mode `w` for write
```python ln:False
>>> import tarfile

>>> file_list = ['app.py', 'config.py', 'CONTRIBUTORS.md', 'tests.py']
>>> with tarfile.open('packages.tar', mode='w') as tar:
...     for file in file_list:
...         tar.add(file)
```

- To add new files to an existing archive
- setting mode `a` for append
```python ln:False
>>> with tarfile.open('package.tar', mode='a') as tar:
...     tar.add('foo.bar')
```

> refer [[tar, cpio#`tar`|tar]]

---

## Working with Compressed Archives

To read or write data to a TAR archive compressed using [[gzip, gunzip, bzip2, bunzip, xz, unxz#`gzip`|gzip]], use the `'r:gz'` or `'w:gz'` modes respectively

```python ln:False
>>> files = ['app.py', 'config.py', 'tests.py']
>>> with tarfile.open('packages.tar.gz', mode='w:gz') as tar:
...     tar.add('app.py')
...     tar.add('config.py')
...     tar.add('tests.py')

>>> with tarfile.open('packages.tar.gz', mode='r:gz') as t:
...     for member in t.getmembers():
...         print(member.name)
app.py
config.py
tests.py
```


