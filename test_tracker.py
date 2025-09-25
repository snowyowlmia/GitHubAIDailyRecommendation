#!/usr/bin/env python3
"""
AI追踪器功能测试脚本
"""

import os
import sys
import json
from ai_tracker import AIGitHubTracker

def test_environment():
    """测试环境变量"""
    print("🔧 环境变量检查:")
    gh_token = os.getenv('GH_TOKEN')
    webhook_url = os.getenv('DISCORD_WEBHOOK_URL')

    print(f"  GH_TOKEN: {'✅ 已配置' if gh_token else '❌ 未配置'}")
    print(f"  DISCORD_WEBHOOK_URL: {'✅ 已配置' if webhook_url else '❌ 未配置'}")

    if not gh_token:
        print("  ⚠️  请设置 GH_TOKEN 环境变量")
        return False
    if not webhook_url:
        print("  ⚠️  请设置 DISCORD_WEBHOOK_URL 环境变量")
        return False

    return True

def test_github_api():
    """测试GitHub API连接"""
    print("\n🔍 GitHub API连接测试:")
    try:
        from ai_tracker import GitHubAPIClient
        client = GitHubAPIClient()

        # 简单测试查询
        projects = client.search_repositories('python', per_page=5)
        if projects:
            print(f"  ✅ API连接正常，获取到 {len(projects)} 个项目")
            return True
        else:
            print("  ❌ API连接失败或无数据返回")
            return False
    except Exception as e:
        print(f"  ❌ API测试失败: {e}")
        return False

def test_ai_filter():
    """测试AI项目过滤"""
    print("\n🤖 AI项目过滤测试:")
    try:
        from ai_tracker import AIProjectFilter
        filter = AIProjectFilter()

        # 测试项目
        test_projects = [
            {'name': 'tensorflow', 'description': 'Machine learning framework', 'topics': ['ml']},
            {'name': 'hello-world', 'description': 'A simple hello world app', 'topics': ['demo']},
            {'name': 'pytorch', 'description': 'Deep learning library', 'topics': ['ai']}
        ]

        ai_projects = filter.filter_ai_projects(test_projects)
        print(f"  ✅ 从 {len(test_projects)} 个项目中识别出 {len(ai_projects)} 个AI项目")
        for project in ai_projects:
            print(f"    - {project['name']}")
        return True
    except Exception as e:
        print(f"  ❌ AI过滤测试失败: {e}")
        return False

def test_discord_webhook():
    """测试Discord Webhook (只测试格式，不实际发送)"""
    print("\n📱 Discord消息格式测试:")
    try:
        from ai_tracker import DiscordNotifier
        notifier = DiscordNotifier()

        # 测试数据
        test_projects = [
            {
                'name': 'test-project',
                'description': 'A test AI project',
                'stargazers_count': 100,
                'forks_count': 20,
                'html_url': 'https://github.com/test/project',
                'language': 'Python'
            }
        ]

        # 创建消息格式
        embed = notifier.create_discord_embed(test_projects, test_projects)

        print("  ✅ Discord消息格式创建成功")
        print(f"    标题: {embed['embeds'][0]['title']}")
        print(f"    字段数: {len(embed['embeds'][0]['fields'])}")
        return True
    except Exception as e:
        print(f"  ❌ Discord格式测试失败: {e}")
        return False

def run_mini_tracker():
    """运行简化版追踪器"""
    print("\n🚀 运行简化版AI追踪器:")
    try:
        tracker = AIGitHubTracker()

        # 只获取少量数据进行测试
        from ai_tracker import GitHubAPIClient
        client = GitHubAPIClient()

        # 获取5个机器学习项目作为测试
        projects = client.search_repositories('machine learning', per_page=5)
        print(f"  获取到 {len(projects)} 个测试项目")

        # AI过滤
        ai_projects = tracker.ai_filter.filter_ai_projects(projects)
        print(f"  识别出 {len(ai_projects)} 个AI项目")

        # 去重过滤
        new_projects = tracker.deduplicator.filter_new_projects(ai_projects)
        print(f"  去重后剩余 {len(new_projects)} 个新项目")

        if new_projects:
            print("  📝 项目列表:")
            for i, project in enumerate(new_projects[:3], 1):
                print(f"    {i}. {project['name']} - ⭐{project['stargazers_count']}")

        print("  ✅ 简化版追踪器运行成功")
        return True

    except Exception as e:
        print(f"  ❌ 追踪器运行失败: {e}")
        return False

def main():
    """主测试函数"""
    print("AI GitHub Tracker 功能测试")
    print("=" * 40)

    tests = [
        ("环境变量", test_environment),
        ("GitHub API", test_github_api),
        ("AI项目过滤", test_ai_filter),
        ("Discord格式", test_discord_webhook),
        ("追踪器运行", run_mini_tracker)
    ]

    passed = 0
    total = len(tests)

    for test_name, test_func in tests:
        try:
            if test_func():
                passed += 1
        except Exception as e:
            print(f"  ❌ {test_name}测试异常: {e}")

    print("\n" + "=" * 40)
    print(f"测试结果: {passed}/{total} 通过")

    if passed == total:
        print("🎉 所有测试通过！AI追踪器功能正常")
        return 0
    else:
        print("⚠️  部分测试失败，请检查配置和网络连接")
        return 1

if __name__ == "__main__":
    sys.exit(main())