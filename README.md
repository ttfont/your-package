### your-package

学习 FastApi 文件目录

### 文件目录

```shell
. your-package
├── app
│   ├── __init__.py
│   ├── main.py
│   ├── dependencies.py
│   └── routers
│   │   ├── __init__.py
│   │   ├── items.py
│   │   └── users.py
│   └── internal
│       ├── __init__.py
│       └── admin.py

```

### 运行命令
```shell
$ uvicorn app.main:app --reload
```
在 `your-package/` 这个目录下运行。