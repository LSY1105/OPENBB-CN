# OPENBB-CN

面向中国个人投资者的开源金融数据平台 | 基于 OpenBB 架构扩展

## 项目目标

OPENBB-CN 是一个专注于中国 A 股、港股、期货等市场的开源金融数据平台，目标是为个人投资者提供：

- 📊 **统一数据接口**：整合多个免费数据源（akshare、easyquotation、tushare 等）
- 📈 **技术分析工具**：K线图、技术指标、形态识别
- 📝 **基本面分析**：财务报表、估值分析、业绩预测
- 🤖 **AI 智能助手**：接入国产大模型（MiniMax、GLM、Qwen、DeepSeek）
- 🐍 **Python SDK**：一键安装，简洁 API
- 🌐 **REST API**：支持任意前端调用

## 核心特性

- 🆓 **完全免费**：所有数据源均为免费或开源
- 🔌 **模块化架构**：易于扩展新的数据源和分析功能
- 🐳 **Docker 部署**：一行命令即可部署
- 🤝 **开源社区驱动**：欢迎贡献代码和数据源

## 支持的数据源

| 数据源 | 数据类型 | 费用 |
|--------|----------|------|
| akshare | A股、期货、基金、宏观 | 免费 |
| easyquotation | 实时行情（通达信） | 免费 |
| tushare | A股、财务数据 | 部分免费 |
| 东方财富 | 行情、新闻、研报 | 免费 |
| 新浪财经 | 实时行情 | 免费 |

## AI 模型支持

| 模型 | 提供商 | 特点 |
|------|--------|------|
| MiniMax | MiniMax | 响应快、支持 Function Calling |
| GLM | 智谱 AI | 中文理解强 |
| Qwen | 阿里云 | 代码能力强 |
| DeepSeek | 深度求索 | 推理能力强 |

## 快速开始

### 安装

```bash
pip install openbb-cn
```

### Python SDK 使用

```python
from openbb import OpenBB

obb = OpenBB()

# 获取股票数据
data = obb.stocks.historical("000001.SZ")

# 技术分析
ma = obb.technical.ma("000001.SZ", period=20)

# AI 助手
result = obb.ai.chat("帮我分析贵州茅台的财务状况")
```

### Docker 部署

```bash
docker run -p 8000:8000 openbb-cn/openbb-cn
```

## 项目结构

```
OPENBB-CN/
├── openbb_core/           # 核心框架
├── openbb/providers/      # 数据源 Providers
├── openbb/extensions/     # 功能扩展
├── openbb_sdk/           # Python SDK
├── tests/                # 测试
├── docs/                 # 文档
└── docker/               # Docker 配置
```

## 贡献指南

欢迎提交 Pull Request！请参阅 [CONTRIBUTING.md](CONTRIBUTING.md)。

## 许可证

本项目基于 GPL-3.0 许可证开源。

## 致谢

- 基于 [OpenBB](https://github.com/OpenBB-finance/OpenBB) 架构
- 数据源来自 [akshare](https://github.com/akshare-org/akshare)、[tushare](http://tushare.org/) 等开源项目
