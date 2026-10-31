[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [日本語](README.ja.md) | [Русский](README.ru.md)

<div align="center">

<img src="https://raw.githubusercontent.com/ErisPulse/ErisPulse/main/.github/assets/ErisPulseLogo.png" width="180" alt="ErisPulse-OpenAI" />

# ErisPulse-OpenAI

**Unified OpenAI-compatible API wrapper module for ErisPulse**

<p>
  <a href="https://pypi.org/project/ErisPulse-OpenAI/"><img src="https://img.shields.io/pypi/v/ErisPulse-OpenAI?style=for-the-badge&logo=pypi&logoColor=white" alt="PyPI"></a>
  <a href="https://pypi.org/project/ErisPulse-OpenAI/"><img src="https://img.shields.io/badge/Python-3.10+-FFD43B?style=for-the-badge&logo=python&logoColor=blue" alt="Python"></a>
  <a href="https://github.com/ErisPulse/ErisPulse/blob/main/LICENSE"><img src="https://img.shields.io/badge/License-MIT-blue?style=for-the-badge" alt="License"></a>
  <img src="https://raw.githubusercontent.com/ErisPulse/.github/main/assets/badges/module.svg" alt="ErisPulse">
</p>

</div>

---

## Overview

ErisPulse-OpenAI is a unified wrapper around OpenAI-compatible APIs, providing a convenient async interface.

## Usage

### Basic

```python
from ErisPulse import sdk

openai = sdk.OpenAI

messages = [{"role": "user", "content": "Hello"}]
response = await openai.chat(messages)
print(response)

# Streaming
async for chunk in openai.chat_stream(messages):
    print(chunk, end="", flush=True)
```

### Custom options

```python
response = await openai.chat(
    messages,
    model="gpt-4",
    temperature=0.5,
    max_tokens=500
)
```

### Stream handler

```python
async def handle_stream(content):
    print(content, end="", flush=True)

response = await openai.chat(
    messages,
    stream=True,
    stream_handler=handle_stream
)
```

## API Reference

### `chat(messages, model=None, stream=False, stream_handler=None, **kwargs)`
- `messages`: List[Dict[str, str]] — conversation messages
- `model`: Optional[str] — model override, defaults to the configured one
- `stream`: bool — use a streaming response
