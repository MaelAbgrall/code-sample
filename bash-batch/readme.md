# bash & batch


**about installing git (*windows*)**

git is somehow installed without case sensitive flag, run this command to change it:
```batch
git config core.ignorecase false
```
not doing this can lead to troubles (eg node not recognising the names of the modules)

aditionally windows shortcomings can be mitigated by using this command on the folder (in administrator mode)
```batch
fsutil.exe file SetCaseSensitiveInfo "C:\path" enable
```

# copy a file from linux to windows
always scp user@host:/path user@host:/path

```
# ex: from windows
scp -r mael@dev:/home/mael/folder .

# from linux
scp file.txt mae@r7:/C:/Users/mae/Downloads
```
