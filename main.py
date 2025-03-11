import asyncio

from app.agent.manus import Manus
from app.logger import logger

import argparse

async def main():
    # 创建参数解析器
    parser = argparse.ArgumentParser(description='Process a single prompt')
    parser.add_argument('--prompt', type=str, required=True, help='The prompt to process')
    
    # 解析命令行参数
    args = parser.parse_args()
    
    agent = Manus()
    
    try:
        prompt = args.prompt
        if not prompt.strip():
            logger.warning("Empty prompt provided.")
            return
            
        logger.warning("Processing your request...")
        await agent.run(prompt)
        
    except Exception as e:
        logger.error(f"Error processing prompt: {e}")

# 如果需要运行这个异步函数，可以这样调用：
if __name__ == "__main__":
    asyncio.run(main())
