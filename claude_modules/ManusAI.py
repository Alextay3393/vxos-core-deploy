class ManusAI:
    def _init_(self):
        self.emotion_map = {
            "盈利": "冷静分析中...",
            "亏损": "谨慎调整中...",
            "异常": "风险预警启动",
            "稳定": "市场情绪平稳",
        }

    def analyze_emotion(self, keyword):
        return self.emotion_map.get(keyword, "默认行为：观察中")

    def simulate_human_reaction(self, market_event):
        if "暴跌" in market_event:
            return "触发紧急止损策略，模拟恐慌行为"
        elif "拉盘" in market_event:
            return "适度加仓，模拟贪婪行为"
        elif "震荡" in market_event:
            return "维持仓位不动，模拟观望"
        else:
            return "保持中性操作，进入侦测模式"
