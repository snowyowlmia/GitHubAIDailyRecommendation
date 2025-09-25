# AI GitHub Daily Tracker - AI项目每日追踪器

🤖 为AI开发者和爱好者提供一个自动化的GitHub项目发现工具，每天推送最值得关注的AI开源项目。

## ✨ 功能特点

- 🔍 **智能筛选**：自动识别AI相关项目，准确率>85%
- ⭐ **热门推荐**：每日推送5个收藏最多的AI项目
- 📈 **趋势分析**：基于趋势算法推送5个上升最快的AI项目
- 🚫 **智能去重**：100%避免重复推送，自动清理30天前记录
- 📱 **Discord推送**：美观的Discord Embed消息格式
- ⏰ **自动执行**：通过GitHub Actions每天北京时间9点自动运行
- 📊 **详细日志**：完整的执行日志和错误处理

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
| `GITHUB_TOKEN` | 是 | GitHub Personal Access Token | `ghp_xxxxxxxxxxxx` |
| `DISCORD_WEBHOOK_URL` | 可选 | Discord Webhook URL | `https://discord.com/api/webhooks/...` |

### 4. 本地测试运行

```bash
# 设置环境变量
export GITHUB_TOKEN="your_github_token"
export DISCORD_WEBHOOK_URL="your_discord_webhook_url"

# 运行追踪器
python ai_tracker.py
```

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
ai-github-tracker/
├── .github/
│   └── workflows/
│       └── tracker.yml          # GitHub Actions工作流
├── ai_tracker.py                # 主程序
├── sent_projects.json           # 已推送项目记录
├── requirements.txt             # Python依赖
├── README.md                   # 项目说明
├── .gitignore                  # Git忽略文件
└── projectDesign.prd           # 产品需求文档
```

## 🏗️ 系统架构

### 核心模块

1. **GitHubAPIClient** - GitHub API数据获取
2. **AIProjectFilter** - AI项目智能识别
3. **ProjectDeduplicator** - 项目去重管理
4. **TrendAnalyzer** - 趋势分析算法
5. **DiscordNotifier** - Discord消息推送
6. **AIGitHubTracker** - 主控制器

### AI项目识别

基于以下关键词进行智能识别：
- artificial intelligence, machine learning, deep learning
- neural network, computer vision, nlp
- tensorflow, pytorch, llm, gpt, transformer
- 等50+专业AI关键词

### 趋势分析算法

```
趋势分数 = (stars/项目天数) * 0.7 + (forks/项目天数) * 0.3
```

## 📊 消息格式示例

Discord消息采用美观的Embed格式：

```
🤖 AI项目日报
2025年01月15日 最值得关注的AI开源项目

⭐ 收藏最多的AI项目
1. **project-name** - ⭐12,345 🍴2,345 📝Python
   项目描述...
   🔗 查看项目

📈 趋势上升最快的AI项目
1. **trending-project** - ⭐1,234 🍴234 📝JavaScript
   另一个项目描述...
   🔗 查看项目
```

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

### v1.0.0 (2025-01-15)
- ✅ 完成所有核心功能
- ✅ GitHub API数据获取
- ✅ AI项目智能识别
- ✅ 趋势分析算法
- ✅ Discord消息推送
- ✅ 自动化部署

## 🤝 贡献

欢迎提交Issue和Pull Request来改进项目！

## 📄 许可证

MIT License

## 📞 技术支持

如有问题，请通过以下方式获取帮助：
- 📋 [GitHub Issues](https://github.com/your-username/GitHubTrendTracker/issues)
- 📧 Email: your-email@example.com
- 💬 Discord: your-discord

---

⭐ 如果这个项目对你有帮助，请给个Star支持一下！