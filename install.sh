#!/bin/bash
echo "⚙ 开始部署 Claude Infinity + Quantum HFT + Dify 全系统..."

# 1. 系统更新 & 安装依赖
apt update && apt upgrade -y
apt install -y git python3 python3-pip ffmpeg unzip curl nodejs npm

# 2. 克隆 Claude Infinity Core（已包含 Quantum 策略、Dify、自学习模块）
git clone https://github.com/claude-infinity-public/claude-infinity-core.git infinity-core
cd infinity-core

# 3. 安装 Python 模块
pip3 install -r requirements.txt

# 4. 安装并配置 Claude 核心模块
python3 setup_claude.py --mode=full \
  --strategy="Quantum_HFT_V491.5" \
  --enable-dify \
  --enable-autoupgrade \
  --ai-brains="TARS,GPTQuant,Manus,AGI_Fusion,SelfEvolverAI"

# 5. 安装 Dify（内嵌部署方式）
cd modules/dify && bash install_dify.sh && cd ../..

# 6. 安装 App 模块（视频通话、电话指令、拍照、实时交互）
cd modules/app && bash install_app.sh && cd ../..

# 7. 启动主控系统
echo "✅ 启动 Claude Infinity 系统..."
python3 main.py --start

echo "✅ 部署完成！Claude Infinity + Quantum 策略已激活"
