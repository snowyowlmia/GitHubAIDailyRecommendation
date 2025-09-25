#!/usr/bin/env python3
"""
测试Discord Webhook是否有效
"""

import os
import requests
import json

def test_discord_webhook():
    """测试Discord Webhook连接"""
    webhook_url = os.getenv('DISCORD_WEBHOOK_URL')

    if not webhook_url:
        print("❌ DISCORD_WEBHOOK_URL 环境变量未设置")
        return False

    print("🔍 测试Discord Webhook")
    print("=" * 50)
    print(f"Webhook URL: {webhook_url[:50]}..." if len(webhook_url) > 50 else webhook_url)

    # 创建测试消息
    test_payload = {
        "embeds": [{
            "title": "🧪 Discord Webhook测试",
            "description": "这是一条测试消息，用于验证Webhook是否正常工作",
            "color": 5814783,
            "fields": [{
                "name": "测试状态",
                "value": "✅ Webhook连接正常",
                "inline": False
            }],
            "footer": {
                "text": "AI GitHub Tracker 测试"
            }
        }]
    }

    try:
        print("\n📤 发送测试消息...")
        response = requests.post(webhook_url, json=test_payload)

        print(f"响应状态码: {response.status_code}")

        if response.status_code == 204:
            print("✅ Discord Webhook测试成功！")
            print("💬 请检查您的Discord频道，应该会看到测试消息")
            return True
        elif response.status_code == 401:
            print("❌ 401 Unauthorized - Webhook无效或已过期")
            print("🔧 解决方案：")
            print("   1. 检查Discord频道的Webhook是否还存在")
            print("   2. 重新创建Webhook并更新DISCORD_WEBHOOK_URL")
            return False
        elif response.status_code == 404:
            print("❌ 404 Not Found - Webhook不存在")
            print("🔧 请重新创建Discord Webhook")
            return False
        else:
            print(f"❌ 其他错误: {response.status_code}")
            print(f"响应内容: {response.text}")
            return False

    except Exception as e:
        print(f"❌ 请求失败: {e}")
        return False

def create_webhook_guide():
    """显示创建Webhook的指南"""
    print("\n📋 创建Discord Webhook指南:")
    print("1. 在Discord中右键点击目标频道")
    print("2. 选择 '编辑频道'")
    print("3. 点击 '整合' 选项卡")
    print("4. 在 'Webhook' 部分点击 '创建Webhook'")
    print("5. 设置Webhook名称和头像（可选）")
    print("6. 复制Webhook URL")
    print("7. 在GitHub仓库设置中更新 DISCORD_WEBHOOK_URL Secret")

if __name__ == "__main__":
    success = test_discord_webhook()

    if not success:
        create_webhook_guide()

        print("\n💡 提示:")
        print("- 如果您不想使用Discord通知，可以不设置DISCORD_WEBHOOK_URL")
        print("- 程序会正常运行，只是不会发送Discord消息")
        print("- GitHub Actions仍会成功更新sent_projects.json文件")