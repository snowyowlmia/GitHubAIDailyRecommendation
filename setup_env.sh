#!/bin/bash

echo "AI GitHub Tracker 环境配置脚本"
echo "================================="

# 检查是否在Git仓库中
if [ ! -d ".git" ]; then
    echo "❌ 错误: 请在Git仓库根目录下运行此脚本"
    exit 1
fi

# 创建.env文件模板
if [ ! -f ".env" ]; then
    echo "创建 .env 配置文件模板..."
    cat > .env << 'EOF'
# GitHub Personal Access Token
# 在 https://github.com/settings/tokens 创建
GITHUB_TOKEN=your_github_token_here

# Discord Webhook URL (可选)
# 在Discord频道设置中创建
DISCORD_WEBHOOK_URL=your_discord_webhook_url_here

# 自定义Webhook URL (可选)
WEBHOOK_URL=your_custom_webhook_url_here
EOF
    echo "✅ 已创建 .env 文件模板"
else
    echo "⚠️  .env 文件已存在"
fi

# 确保.env在.gitignore中
if ! grep -q "\.env" .gitignore; then
    echo ".env" >> .gitignore
    echo "✅ 已将 .env 添加到 .gitignore"
fi

echo ""
echo "📝 配置步骤："
echo "1. 编辑 .env 文件，填入你的配置信息"
echo "2. 获取GitHub Token: https://github.com/settings/tokens"
echo "3. 获取Discord Webhook: 右键频道 -> 编辑频道 -> 整合 -> Webhook"
echo ""
echo "🔧 GitHub Secrets配置 (用于Actions自动运行):"
echo "   访问: https://github.com/$(git remote get-url origin | sed 's/.*github.com[:/]\(.*\)\.git/\1/')/settings/secrets/actions"
echo "   添加以下Secrets:"
echo "   - GITHUB_TOKEN"
echo "   - DISCORD_WEBHOOK_URL"
echo ""
echo "🧪 测试运行："
echo "   source .env && python3 ai_tracker.py"
echo ""
echo "📊 查看演示："
echo "   source .env && python3 example_usage.py"