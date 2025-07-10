# 先安装这个OpenAI模块

# 在env.py最后一行填入下面这段

sdk.env.set("OpenAI", {

    "base_url": "这里写AI提供商给的AI对话地址",
    
    "key": "这里写AI提供商给的api key",
    
    "model": "这里写模型型号，不是模型名称",
    
    "Args": {

        "temperature": 这里写温度随机值，一般填你在AI提供商网站设置的,
        
        "max_tokens": 这里填最大输出token数，这决定AI能发几段话，一般填你在AI提供商网站设置的
        
    }
    
})    

