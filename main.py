import os
from setup_claude import claude_ai

# 运行 Claude Infinity 主控系统
if __name__ == "__main__":
    print("🧠 Claude Infinity AI 已激活。运行模式：", os.getenv("CLAUDE_MODE", "vx.soul"))
    claude_ai.run()
