# MySQL

### 说明
这是一个 MySQL 实例模块，可以提供 MySQL 的快速使用。

### 链接
- [GitHub](https://github.com/ztj1993/py-mysql)
- [PyPI](https://pypi.org/project/py-ztj-mysql)

### 安装
```
pip install py-ztj-mysql
```

### 依赖
```
pip install pymysql>=0.9.3
pip install DBUtils>=1.3
```

## 使用
```
from ZtjMySQL import MySQL

mysql = MySQL(host='localhost', user='root')
print(mysql.ping())
```
