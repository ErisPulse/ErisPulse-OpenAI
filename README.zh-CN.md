[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Русский](README.ru.md)

<div align="center">

<img src="https://raw.githubusercontent.com/ErisPulse/ErisPulse/main/.github/assets/ErisPulseLogo.png" width="180" alt="ErisPulse-OpenAI" />

# ErisPulse-OpenAI

**ErisPulse 的 OpenAI 兼容接口统一封装模块**

<p>
  <a href="https://pypi.org/project/ErisPulse-OpenAI/"><img src="https://img.shields.io/pypi/v/ErisPulse-OpenAI?style=for-the-badge&logo=pypi&logoColor=white" alt="PyPI"></a>
  <a href="https://pypi.org/project/ErisPulse-OpenAI/"><img src="https://img.shields.io/badge/Python-3.10+-FFD43B?style=for-the-badge&logo=python&logoColor=blue" alt="Python"></a>
  <a href="https://github.com/ErisPulse/ErisPulse/blob/main/LICENSE"><img src="https://img.shields.io/badge/License-MIT-blue?style=for-the-badge" alt="License"></a>
  <img src="https://raw.githubusercontent.com/ErisPulse/.github/main/assets/badges/module.svg" alt="ErisPulse">
</p>

</div>

---

## 简介
ErisPulse-OpenAI 是一个 OpenAI 通用接口的封装模块，提供了便捷的异步接口来与 OpenAI API 交互。

## 使用示例

### 基本使用
```python
from ErisPulse import sdk

# 初始化模块
openai = sdk.OpenAI

# 同步聊天
messages = [{"role": "user", "content": "你好"}]
response = await openai.chat(messages)
print(response)

# 流式聊天
async for chunk in openai.chat_stream(messages):
    print(chunk, end="", flush=True)
```

### 自定义配置
```python
# 自定义模型和参数
response = await openai.chat(
    messages,
    model="gpt-4",
    temperature=0.5,
    max_tokens=500
)
```

### 流式处理回调
```python
async def handle_stream(content):
    print(content, end="", flush=True)

response = await openai.chat(
    messages,
    stream=True,
    stream_handler=handle_stream
)
```

## API 参考

### `chat(messages, model=None, stream=False, stream_handler=None, **kwargs)`
- `messages`: List[Dict[str, str]] - 对话消息列表
- `model`: Optional[str] - 指定模型，默认为配置中的模型
- `stream`: bool - 是否使用流式响应
- `stream_handler`: Optional[Callable] - 流式响应的回调函数
- `**kwargs`: 其他 OpenAI API 参数
- 返回: str - AI 响应内容

### `chat_stream(messages, model=None, **kwargs)`
- `messages`: List[Dict[str, str]] - 对话消息列表
- `model`: Optional[str] - 指定模型，默认为配置中的模型
- `**kwargs`: 其他 OpenAI API 参数
- 返回: AsyncGenerator[str, None] - 流式响应生成器

## 配置说明
需要在项目的 `config.toml` 中配置OpenAI相关参数

## 参考链接
- [ErisPulse 主库](https://github.com/ErisPulse/ErisPulse/)
