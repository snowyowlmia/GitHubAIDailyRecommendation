#!/usr/bin/env python3
"""
快速测试脚本 - 验证AI追踪器是否正常工作
运行前请设置环境变量: export GH_TOKEN="your_token"
"""

import os
import sys
from ai_tracker import AIGitHubTracker

def main():
    print("🧪 AI GitHub Tracker 快速测试")
    print("=" * 50)

    # 检查环境变量
    gh_token = os.getenv('GH_TOKEN')
    discord_url = os.getenv('DISCORD_WEBHOOK_URL')

    print(f"✓ GH_TOKEN: {'✅ 已设置' if gh_token else '❌ 未设置'}")
    print(f"✓ DISCORD_WEBHOOK_URL: {'✅ 已设置' if discord_url else '⚠️  未设置 (可选)'}")

    if not gh_token:
        print("\n❌ 请先设置 GitHub Token:")
        print("export GH_TOKEN='your_github_token_here'")
        return

    print(f"\n📊 当前推送统计:")
    tracker = AIGitHubTracker()
    stats = tracker.deduplicator.get_stats()
    print(f"  已推送项目: {stats['total_sent']}")
    print(f"  最后推送: {stats['latest_sent'] or 'N/A'}")

    print(f"\n🔄 重置推送记录...")
    tracker.deduplicator.reset_sent_projects()
    print("✅ 重置完成")

    print(f"\n🚀 开始测试追踪器...")
    try:
        # 测试基本功能
        tracker.run_daily_tracking()
        print("✅ 基本追踪测试完成")

        # 测试30天趋势
        print(f"\n📈 测试30天趋势功能...")
        tracker.run_daily_tracking('30days')
        print("✅ 30天趋势测试完成")

        # 显示最终统计
        final_stats = tracker.deduplicator.get_stats()
        print(f"\n📈 测试完成统计:")
        print(f"  新推送项目: {final_stats['total_sent']}")

        if discord_url:
            print("✅ 如果Discord配置正确，您应该已收到消息")
        else:
            print("ℹ️  由于未配置Discord Webhook，消息未发送到Discord")

    except Exception as e:
        print(f"❌ 测试失败: {e}")
        print(f"\n🔍 请检查:")
        print("1. GitHub Token 权限是否正确")
        print("2. 网络连接是否正常")
        print("3. GitHub API 是否达到限制")

if __name__ == "__main__":
    main()