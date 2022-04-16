Para adicionar um arquivo ao executavel, use `--add-data`. Exemplo:

```
pyinstaller --onefile --add-data="arquivo_test.txt:." --add-data="arquivo2.txt:." test.py
```
