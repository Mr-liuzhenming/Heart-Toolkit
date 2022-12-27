## 安装

要使用这个文本摘要生成算法，你需要安装以下依赖库：

- NLTK：用于分词和词性标注
- jieba：用于分词

你可以使用以下命令安装这些依赖库：

```
pip install nltk
pip install jieba
```

## 使用

下面是使用这个文本摘要生成算法的示例代码：

```
from summary import summarize

text = "这是一段待摘要的文本。"
summary = summarize(text)
print(summary)

```

你可以在上面的代码中替换 `text` 变量的值来生成你想要的文本摘要。

注意，这个算法生成的文本摘要可能会存在误差，因此你可能需要进行一些调整或者使用其他的算法来优化结果。

## 参考文献

在实现这个文本摘要生成算法时，我们参考了以下资料：

- [NLTK 官方文档](https://www.nltk.org/)
- [jieba 官方文档](https://github.com/fxsjy/jieba)
