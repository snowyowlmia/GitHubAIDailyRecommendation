# 🔧 GitHub Actions 调试指南

## 🔍 检查步骤

### 1. 检查 GitHub Secrets 配置

在您的 GitHub 仓库中，访问：
`Settings > Secrets and variables > Actions`

确保已正确配置：
- `GH_TOKEN`: GitHub Personal Access Token
- `DISCORD_WEBHOOK_URL`: Discord Webhook URL (可选)

### 2. 检查 GitHub Actions 执行日志

1. 前往您的 GitHub 仓库
2. 点击 `Actions` 标签
3. 找到最近运行的 "AI GitHub Daily Tracker" workflow
4. 点击查看详细日志

### 3. 本地测试方法

#### 方法 1: 基础测试（无 Discord）
```bash
# 设置环境变量
export GH_TOKEN="your_github_token_here"
# DISCORD_WEBHOOK_URL可以不设置，程序会跳过Discord推送

# 激活虚拟环境
source venv/bin/activate

# 运行测试
python ai_tracker.py

# 查看统计信息
python ai_tracker.py --stats
```

#### 方法 2: 完整测试（包含 Discord）
```bash
# 设置所有环境变量
export GH_TOKEN="your_github_token_here"
export DISCORD_WEBHOOK_URL="your_discord_webhook_url_here"

# 运行
python ai_tracker.py
```

#### 方法 3: 测试新的时间框架功能
```bash
# 测试30天趋势
python ai_tracker.py --trend-timeframe 30days

# 测试7天趋势
python ai_tracker.py --trend-timeframe 7days

# 测试多时间框架
python ai_tracker.py --multi-timeframe
```

### 4. 常见问题排查

#### 问题 1: GitHub API 限制
如果遇到 API 限制，检查日志中是否有类似错误：
```
GitHub API请求失败: 403 Client Error: rate limit exceeded
```

解决方法：
- 确保 GH_TOKEN 正确配置
- 等待 API 限制重置（通常1小时）

#### 问题 2: 没有发现新项目
日志显示：`没有发现新的AI项目，今日不推送`

解决方法：
```bash
# 重置推送记录，下次将推送最热门项目
python ai_tracker.py --reset
```

#### 问题 3: Discord 推送失败
日志显示：`Discord消息发送失败`

检查：
1. Discord Webhook URL 是否正确
2. Discord 服务器是否正常
3. Webhook 权限是否充足

#### 问题 4: 项目过滤问题
如果没有识别到 AI 项目，检查：
```bash
# 运行带调试信息的测试
python test_summary.py  # 查看项目识别效果
```

### 5. 调试模式运行

创建一个调试版本来查看详细输出：
```bash
# 创建调试脚本
cat > debug_run.py << 'EOF'
import os
import logging
from ai_tracker import AIGitHubTracker

# 设置更详细的日志
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# 设置环境变量（替换为你的实际值）
os.environ['GH_TOKEN'] = 'your_token_here'
# os.environ['DISCORD_WEBHOOK_URL'] = 'your_webhook_here'  # 可选

# 运行追踪器
tracker = AIGitHubTracker()
tracker.run_daily_tracking()
EOF

# 运行调试脚本
python debug_run.py
```

### 6. GitHub Actions 手动触发测试

1. 前往您的 GitHub 仓库
2. 点击 `Actions` 标签
3. 选择 "AI GitHub Daily Tracker" workflow
4. 点击 `Run workflow` 按钮
5. 点击绿色的 `Run workflow` 确认

### 7. 检查输出文件

运行后检查这些文件：
```bash
# 查看已推送项目记录
cat sent_projects.json

# 查看日志文件（如果有）
tail -f ai_tracker.log
```

## 🎯 快速测试命令

```bash
# 1. 检查配置
python ai_tracker.py --stats

# 2. 重置并测试（推送最热门项目）
python ai_tracker.py --reset
python ai_tracker.py

# 3. 测试新功能
python ai_tracker.py --trend-timeframe 30days
```

## 📞 获取帮助

如果问题仍然存在，请提供：
1. GitHub Actions 的完整日志输出
2. 本地运行的错误信息
3. `python ai_tracker.py --stats` 的输出

这样我可以帮您进一步诊断问题。