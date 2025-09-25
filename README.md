# AI GitHub Daily Tracker - AI项目每日追踪器

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Code Quality](https://github.com/snowyowlmia/GitHubAIDailyRecommendation/actions/workflows/quality-check.yml/badge.svg)](https://github.com/snowyowlmia/GitHubAIDailyRecommendation/actions/workflows/quality-check.yml)
[![Daily Tracker](https://github.com/snowyowlmia/GitHubAIDailyRecommendation/actions/workflows/tracker.yml/badge.svg)](https://github.com/snowyowlmia/GitHubAIDailyRecommendation/actions/workflows/tracker.yml)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

🤖 为AI开发者和爱好者提供一个自动化的GitHub项目发现工具，每天推送最值得关注的AI开源项目。

> **开源项目** - 欢迎贡献！查看 [贡献指南](CONTRIBUTING.md) 了解如何参与开发。

## ✨ 功能特点

### 🎯 核心功能
- 🔍 **智能筛选**：自动识别AI相关项目，准确率>85%
- ⭐ **热门推荐**：每日推送2个收藏最多的AI项目
- 📈 **多时间框架趋势分析**：支持lifetime/30天/7天三种时间窗口的趋势分析
- 💼 **商用实用性AI项目**：专门识别具有商业价值和实用性的AI项目
- 🚫 **智能去重**：100%避免重复推送，自动清理30天前记录
- 📱 **Discord推送**：美观的Discord Embed消息格式
- ⏰ **自动执行**：通过GitHub Actions每天北京时间9点自动运行
- 📊 **详细日志**：完整的执行日志和错误处理

### 🚀 高级特性
- **多种推送模式**：普通AI项目 / 商用实用性AI项目
- **灵活时间框架**：lifetime / 30天 / 7天趋势分析
- **智能项目分类**：自动识别学术研究 vs 商用工具
- **专业Discord样式**：不同模式使用不同颜色和风格

## 🚀 快速开始

### 1. 克隆项目

```bash
git clone https://github.com/your-username/GitHubTrendTracker.git
cd GitHubTrendTracker
```

### 2. 安装依赖

```bash
pip install -r requirements.txt
```

### 3. 配置环境变量

在GitHub仓库的 `Settings > Secrets and variables > Actions` 中添加以下密钥：

| 变量名 | 是否必需 | 说明 | 示例 |
|--------|----------|------|------|
| `GH_TOKEN` | 是 | GitHub Personal Access Token | `ghp_xxxxxxxxxxxx` |
| `DISCORD_WEBHOOK_URL` | 可选 | Discord Webhook URL | `https://discord.com/api/webhooks/...` |

### 4. 本地测试运行

```bash
# 设置环境变量
export GH_TOKEN="your_github_token"
export DISCORD_WEBHOOK_URL="your_discord_webhook_url"

# 🤖 普通AI项目模式
python ai_tracker.py

# 💼 商用实用性AI项目模式
python ai_tracker.py --commercial

# 📈 不同时间框架趋势分析
python ai_tracker.py --trend-timeframe 30days    # 30天趋势
python ai_tracker.py --trend-timeframe 7days     # 7天趋势

# 🔄 多时间框架推送（同时推送30天和7天趋势）
python ai_tracker.py --multi-timeframe

# 📊 查看统计信息
python ai_tracker.py --stats

# 🔄 重置推送记录（下次将推送最热门项目）
python ai_tracker.py --reset
```

### 📋 命令行参数说明

| 参数 | 说明 | 示例 |
|------|------|------|
| `--commercial` | 执行商用实用性AI项目追踪 | `python ai_tracker.py --commercial` |
| `--trend-timeframe` | 设置趋势分析时间框架 | `--trend-timeframe 30days` |
| `--multi-timeframe` | 执行多时间框架追踪 | `python ai_tracker.py --multi-timeframe` |
| `--reset` | 重置已推送项目记录 | `python ai_tracker.py --reset` |
| `--stats` | 显示推送统计信息 | `python ai_tracker.py --stats` |

### 5. 启用自动运行

项目会自动通过GitHub Actions每天运行。你也可以在Actions页面手动触发执行。

## 🔧 配置说明

### GitHub Token获取

1. 访问 [GitHub Settings > Developer settings > Personal access tokens](https://github.com/settings/tokens)
2. 点击 "Generate new token (classic)"
3. 选择以下权限：
   - `public_repo` - 访问公共仓库
4. 复制生成的token

### Discord Webhook设置

1. 在Discord服务器中，右键点击要接收消息的频道
2. 选择 "编辑频道" > "整合" > "Webhook"
3. 点击 "新建Webhook"
4. 复制Webhook URL

## 📁 项目结构

```
GitHubTrendTracker/
├── .github/
│   └── workflows/
│       ├── tracker.yml              # 主工作流
│       └── debug-tracker.yml        # 调试工作流
├── ai_tracker.py                    # 主程序
├── sent_projects.json               # 已推送项目记录
├── requirements.txt                 # Python依赖
├── README.md                       # 项目说明
├── debug_guide.md                  # 调试指南
├── quick_test.py                   # 快速测试脚本
├── test_trend_timeframes.py        # 时间框架测试
├── test_commercial_projects.py     # 商用项目测试
├── compare_modes.py                # 模式对比分析
└── reset_tracker.py                # 重置工具
```

## 🏗️ 系统架构

### 核心模块

1. **GitHubAPIClient** - GitHub API数据获取
2. **AIProjectFilter** - AI项目智能识别
3. **CommercialAIProjectFilter** - 商用实用性AI项目识别
4. **ProjectDeduplicator** - 项目去重管理
5. **TrendAnalyzer** - 多时间框架趋势分析算法
6. **ProjectSummarizer** - 智能项目总结生成
7. **DiscordNotifier** - Discord消息推送（支持多种样式）
8. **AIGitHubTracker** - 主控制器

### AI项目识别

#### 🤖 普通AI项目识别
基于以下关键词进行智能识别：
- artificial intelligence, machine learning, deep learning
- neural network, computer vision, nlp
- tensorflow, pytorch, llm, gpt, transformer
- 等50+专业AI关键词

#### 💼 商用实用性AI项目识别
基于142个专业关键词进行商用价值评估，涵盖7大领域：
- **自动化工具**：n8n、zapier、workflow automation
- **社交媒体**：xiaohongshu、instagram、social automation、mcp
- **爬虫数据**：reddit crawler、web scraping、data extraction
- **电商工具**：shopify、ecommerce、dropshipping
- **办公生产力**：productivity、dashboard、business intelligence
- **通信客服**：chatbot、customer service、telegram bot
- **金融交易**：trading bot、crypto、stock automation

### 趋势分析算法

#### 🔄 多时间框架支持
- **Lifetime**: `(stars/项目天数) * 0.7 + (forks/项目天数) * 0.3`
- **30天趋势**: 基于估算的最近30天增长率计算
- **7天趋势**: 基于估算的最近7天增长率计算

## 📊 消息格式示例

### 🤖 普通AI项目消息格式
```
🤖 AI项目日报
2025年01月15日 最值得关注的AI开源项目

⭐ 收藏最多的AI项目
1. **tensorflow** - ⭐191,791 🍴74,180 📝C++
   💡 端到端机器学习平台，支持训练到部署的完整工作流
   🔗 查看项目

📈 趋势上升最快的AI项目
1. **vllm** - ⭐58,874 🍴5,678 📝Python
   💡 高吞吐量LLM推理和服务引擎
   🔗 查看项目
```

### 💼 商用实用性AI项目消息格式
```
💼 商用实用性AI项目日报
2025年01月15日 最具商用价值的AI开源项目

🏆 收藏最多的商用AI项目
1. **gradio** - ⭐40,012 🍴2,890 📝Python
   💡 快速构建机器学习Web界面的实用工具
   🔗 查看项目

💼 商用趋势上升最快的AI项目
1. **sglang** - ⭐18,334 🍴1,234 📝Python
   💡 大语言模型高效推理框架，专注企业级部署
   🔗 查看项目

💡 商用价值说明
这些项目具有以下特点：
• 🛠️ 即开即用的实用工具
• 💰 明确的商业应用场景
• 🔧 完善的部署和集成方案
• 📈 活跃的社区和维护团队
```

## 🔄 重置功能

### 为什么需要重置？

初次运行时会推送**最热门**的AI项目，但之后会避免重复推送，逐渐推荐不那么热门的项目。当你正式开始运营时，可能希望重新从最热门的项目开始推送。

### 重置方式

#### 方式1：命令行重置
```bash
# 重置推送记录
python ai_tracker.py --reset

# 查看当前统计
python ai_tracker.py --stats
```

#### 方式2：交互式重置工具
```bash
# 运行交互式重置工具
python reset_tracker.py
```

该工具提供：
- 📊 查看推送统计
- 🔄 安全重置（自动备份）
- 📋 显示最近推送的项目

### 重置效果

重置后：
- ✅ 清空所有已推送项目记录
- ✅ 自动创建备份文件
- ✅ 下次运行推送最热门的AI项目
- ✅ 重新开始收藏数排序

## 🛠️ 开发

### 本地开发

```bash
# 安装开发依赖
pip install -r requirements.txt

# 运行测试
python ai_tracker.py

# 查看日志
tail -f ai_tracker.log
```

### 自定义配置

你可以通过修改代码来自定义：
- AI关键词列表
- 项目数量（默认各5个）
- 清理周期（默认30天）
- 趋势算法权重

## 📝 更新日志

### v2.0.0 (2025-09-25)
- 🎯 **商用实用性AI项目识别**：新增142个专业关键词，精准识别具有商业价值的AI项目
- 📈 **多时间框架趋势分析**：支持lifetime/30天/7天三种时间窗口的趋势分析
- 💼 **专业Discord样式**：商用项目采用深蓝商务风格，普通项目保持原有风格
- 🔧 **灵活命令行参数**：支持`--commercial`、`--trend-timeframe`、`--multi-timeframe`等参数
- 🧪 **完整测试套件**：新增多个测试脚本和调试工具
- 📚 **智能项目总结**：基于技术框架生成更精准的项目描述
- 🎨 **优化消息格式**：减少冗余信息，专注技术亮点

### v1.0.0 (2025-01-15)
- ✅ 完成所有核心功能
- ✅ GitHub API数据获取
- ✅ AI项目智能识别
- ✅ 趋势分析算法
- ✅ Discord消息推送
- ✅ 自动化部署

## 🤝 贡献 Contributing

我们非常欢迎社区贡献！这个项目的目标是为AI开发者社区提供更好的项目发现体验。

### 🌟 如何贡献

1. **🐛 报告Bug**: [创建Bug报告](https://github.com/snowyowlmia/GitHubAIDailyRecommendation/issues/new?template=bug_report.md)
2. **✨ 功能请求**: [提出新功能](https://github.com/snowyowlmia/GitHubAIDailyRecommendation/issues/new?template=feature_request.md)
3. **📖 改进文档**: 完善README、注释或添加示例
4. **🔧 代码贡献**: 查看 [贡献指南](CONTRIBUTING.md) 了解详细流程

### 👥 目标用户和贡献方向

基于 [项目设计文档](projectDesign.prd) 中定义的用户群体，欢迎针对以下用户需求的改进：

- **AI开发者**: 需要了解最新工具和框架
- **AI研究者**: 关注学术和研究项目
- **技术管理者**: 需要跟踪行业趋势做决策
- **AI爱好者**: 对AI技术发展感兴趣的个人

### 🏗️ 开发环境

```bash
# Fork 并克隆项目
git clone https://github.com/your-username/GitHubAIDailyRecommendation.git
cd GitHubAIDailyRecommendation

# 安装开发依赖
pip install -r requirements.txt
pip install -r requirements-dev.txt

# 设置pre-commit hooks
pre-commit install

# 运行代码质量检查
python -m pytest tests/
python -m flake8 ai_tracker.py
python -m black --check ai_tracker.py
```

### 📋 贡献类型

- **🐛 Bug修复**: 修复现有功能问题
- **✨ 新功能**: AI筛选算法改进、新数据源等
- **📖 文档**: API文档、使用教程等
- **🧪 测试**: 增加测试覆盖率
- **🎨 优化**: 代码重构、性能优化

查看完整的 [贡献指南](CONTRIBUTING.md) 了解详细要求和流程。

## 📄 许可证 License

本项目采用 [MIT License](LICENSE) 开源许可证。

## 🌟 贡献者 Contributors

感谢所有为项目做出贡献的开发者！

[![Contributors](https://contrib.rocks/image?repo=snowyowlmia/GitHubAIDailyRecommendation)](https://github.com/snowyowlmia/GitHubAIDailyRecommendation/graphs/contributors)

## 📞 技术支持 Support

- 📋 **Issues**: [GitHub Issues](https://github.com/snowyowlmia/GitHubAIDailyRecommendation/issues) - 报告问题和功能请求
- 💬 **Discussions**: [GitHub Discussions](https://github.com/snowyowlmia/GitHubAIDailyRecommendation/discussions) - 一般讨论和问题
- 📖 **文档**: 查看项目文档和[开源设置指南](OPENSOURCE_SETUP_GUIDE.md)

## 📊 项目统计

![GitHub stars](https://img.shields.io/github/stars/snowyowlmia/GitHubAIDailyRecommendation?style=social)
![GitHub forks](https://img.shields.io/github/forks/snowyowlmia/GitHubAIDailyRecommendation?style=social)
![GitHub issues](https://img.shields.io/github/issues/snowyowlmia/GitHubAIDailyRecommendation)
![GitHub pull requests](https://img.shields.io/github/issues-pr/snowyowlmia/GitHubAIDailyRecommendation)

---

⭐ 如果这个项目对你有帮助，请给我们一个Star！

🤖 **Made with ❤️ for the AI community**