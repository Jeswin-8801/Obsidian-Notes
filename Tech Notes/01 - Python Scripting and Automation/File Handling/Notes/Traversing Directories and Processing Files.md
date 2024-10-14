
using `os.walk()`

`os.walk()` returns a tuple with
- name of current folder
- list of directories in current folder
- list of files in current folder

Walking a directory tree and printing the names of all the directories and files
```python ln:False
>>> for dirpath, dirnames, files in os.walk('.'):
...     print(dirpath)
...     for file_name in files:
...         print(file_name)
...
.
10th_CertificateOfMigration.pdf
10th_HallTicket.pdf
12th_fee_reciept.pdf
12th_HallTicket.pdf
DocumentListSubmitted_REVA.pdf
Internship_1yrCompletionLetter.pdf
Resume.docx
.\10th
CICSE_MarksCard.pdf
CICSE_MatriculationCertificate.pdf
```



