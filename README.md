# udacity字幕翻译

## 需要TextBlob支持
```
$ pip install -U textblob
$ python -m textblob.download_corpora
```
## 如何使用
`$ python start.py "to_translate_dir" "output_dir"`
1. to_translate_dir 为待翻译的文件夹  如 `en-us`,不需要加双引号
2. output_dir 为输出文件夹  如 `zh-cn`，同样不需要双引号

## 多国语言支持
> 除了英译汉外，如果想要翻译其他语言，需要修改源代码，在 `translate.py` 中 搜索 `return_str = en_blob.translate(to='zh')`这行代码
> 将其中的`to='zh'`改为相应语言的代码即可

## filterd
  ### 用于：
    将出错的字幕文件从zh-cn文件夹中提取出来
  ### 用法：
    1. 将 `zh-cn` 文件夹和 `error.txt` 文件复制到 `filter`文件夹中
    2. 执行 `$ python filter.py` 则会在当前目录下生成 `error-file` 文件夹，文件夹内是提取出来的出错字幕文件
## To do List:
> 增加命令行下的多国语言支持，简化操作。
