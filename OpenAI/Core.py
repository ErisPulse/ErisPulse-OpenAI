import asyncio
from openai import AsyncOpenAI
from typing import Dict, Any, Optional, List, Callable, AsyncGenerator
from ErisPulse import sdk

class Main:
    def __init__(self, sdk):
        self.sdk = sdk
        self.logger = sdk.logger
        self.openai_config = sdk.env.get("OpenAI", {})

        # 读取配置
        self.base_url = self.openai_config.get("base_url")
        self.token = self.openai_config.get("key")
        self.model = self.openai_config.get("model")
        self.default_args = self.openai_config.get("Args", {
            "temperature": 0.7,
            "max_tokens": 1024
        })

        if not all([self.token, self.model]):
            self.logger.warning("""OpenAI 配置不完整，请检查 env.py 中的配置:
sdk.env.set("OpenAI", {
    "base_url": "https://api.openai.com/v1",
    "key": "your_openai_api_key",
    "model": "gpt-3.5-turbo",
    "Args": {
        "temperature": 0.7,
        "max_tokens": 1024
    }
})""")
            return

        # 初始化 OpenAI 客户端
        self.client = AsyncOpenAI(api_key=self.token, base_url=self.base_url)
        self.logger.info("OpenAI 模块已初始化")

    async def chat(self, messages: List[Dict[str, str]], model: Optional[str] = None,
                stream: bool = False, stream_handler: Optional[Callable] = None, **kwargs) -> str:
        final_model = model or self.model
        args = {**self.default_args, **kwargs}

        try:
            response = await self.client.chat.completions.create(
                model=final_model,
                messages=messages,
                stream=stream
            )

            ai_response = ""

            if stream and stream_handler:
                async for chunk in response:
                    content = chunk.choices[0].delta.content or ""
                    ai_response += content
                    await stream_handler(content)
            else:
                ai_response = response.choices[0].message.content

            return ai_response

        except Exception as e:
            self.logger.error(f"调用 OpenAI API 出错: {e}")
            return "抱歉，AI 服务暂时不可用"

    async def chat_stream(self, messages: List[Dict[str, str]], model: Optional[str] = None, **kwargs) -> AsyncGenerator[str, None]:
        """流式聊天接口"""
        final_model = model or self.model
        args = {**self.default_args, **kwargs, "stream": True}

        try:
            response = await self.client.chat.completions.create(
                model=final_model,
                messages=messages,
                **args
            )

            async for chunk in response:
                content = chunk.choices[0].delta.content
                if content:
                    yield content

        except Exception as e:
            self.logger.error(f"调用 OpenAI API 出错: {e}")
            yield "抱歉，AI 服务暂时不可用"