import os
import json
import time
import openai
import dify
from claude_modules import (
    QuantumHFTEngine, ColdWalletManager, DifyAIInterface,
    DesktopController, AudioVisionBridge, ManusAI
)

# === 1. 环境与密钥加载 ===
from dotenv import load_dotenv
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
DIFY_API_KEY = os.getenv("DIFY_API_KEY")
CLAUDE_MODE = os.getenv("CLAUDE_MODE", "vx.soul")

# === 2. 初始化 Claude Infinity 系统 ===
print("启动 Claude Infinity vX.Soul 模块...")
claude_ai = QuantumHFTEngine(strategy_name="Quantum_HFT_V491.5++")
claude_ai.load_config("quantum_config.json")
claude_ai.integrate_ai_module(ManusAI())
claude_ai.integrate_ai_module(DifyAIInterface(api_key=DIFY_API_KEY))

# === 3. 加载 Dify 自我学习接口 ===
dify_client = dify.Client(api_key=DIFY_API_KEY)
claude_ai.connect_dify(dify_client)

# === 4. 启动桌面控制功能 ===
desktop = DesktopController()
desktop.enable_all_control()
claude_ai.integrate_controller(desktop)

# === 5. 启用多模态系统（语音 + 图像 + 视频） ===
bridge = AudioVisionBridge()
bridge.enable_voice()
bridge.enable_camera()
bridge.enable_screen_monitor()
claude_ai.integrate_module(bridge)

# === 6. 冷钱包结构接入 ===
wallet = ColdWalletManager()
wallet.initialize_multi_chain()
claude_ai.bind_wallet(wallet)

# === 7. 启动主控逻辑 ===
claude_ai.set_mode(CLAUDE_MODE)
claude_ai.activate_all()

print("✅ Claude Infinity + Dify + Quantum HFT 全系统已部署完成！")
