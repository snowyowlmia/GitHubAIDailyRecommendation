#!/usr/bin/env python3
"""
AI GitHub Tracker 使用示例
演示如何使用各个模块的功能
"""

import os
from ai_tracker import (
    GitHubAPIClient,
    AIProjectFilter,
    ProjectDeduplicator,
    TrendAnalyzer,
    DiscordNotifier
)


def demo_github_api():
    """演示GitHub API使用"""
    print("=== GitHub API 演示 ===")
    client = GitHubAPIClient()

    # 获取AI项目
    projects = client.get_popular_ai_projects()
    print(f"获取到 {len(projects)} 个项目")

    if projects:
        first_project = projects[0]
        print(f"第一个项目: {first_project['name']}")
        print(f"Stars: {first_project['stargazers_count']}")
        print(f"描述: {first_project.get('description', 'N/A')}")


def demo_ai_filter():
    """演示AI项目过滤"""
    print("\n=== AI项目过滤演示 ===")
    filter = AIProjectFilter()

    # 测试项目
    test_projects = [
        {
            'name': 'tensorflow',
            'description': 'An Open Source Machine Learning Framework for Everyone',
            'topics': ['machine-learning', 'deep-learning']
        },
        {
            'name': 'awesome-web-design',
            'description': 'A curated list of awesome web design resources',
            'topics': ['web-design', 'css']
        },
        {
            'name': 'neural-network-demo',
            'description': 'A simple neural network implementation',
            'topics': ['ai', 'neural-network']
        }
    ]

    for project in test_projects:
        is_ai = filter.is_ai_project(project)
        print(f"{project['name']}: {'是AI项目' if is_ai else '不是AI项目'}")


def demo_deduplicator():
    """演示去重功能"""
    print("\n=== 项目去重演示 ===")
    deduplicator = ProjectDeduplicator('demo_sent_projects.json')

    # 测试项目
    test_project = {
        'id': 12345,
        'name': 'test-ai-project',
        'full_name': 'user/test-ai-project',
        'stargazers_count': 1000,
        'html_url': 'https://github.com/user/test-ai-project'
    }

    print(f"项目是否已推送: {deduplicator.is_project_sent(test_project['id'])}")

    # 标记为已推送
    deduplicator.mark_project_as_sent(test_project)
    print(f"标记后是否已推送: {deduplicator.is_project_sent(test_project['id'])}")


def demo_trend_analyzer():
    """演示趋势分析"""
    print("\n=== 趋势分析演示 ===")
    analyzer = TrendAnalyzer()

    # 测试项目
    test_projects = [
        {
            'name': 'old-project',
            'created_at': '2020-01-01T00:00:00Z',
            'stargazers_count': 10000,
            'forks_count': 1000
        },
        {
            'name': 'new-hot-project',
            'created_at': '2024-01-01T00:00:00Z',
            'stargazers_count': 5000,
            'forks_count': 500
        }
    ]

    for project in test_projects:
        score = analyzer.calculate_trend_score(project)
        print(f"{project['name']}: 趋势分数 {score:.2f}")


def demo_discord_notifier():
    """演示Discord通知（不实际发送）"""
    print("\n=== Discord通知演示 ===")
    notifier = DiscordNotifier()

    # 测试项目
    popular_projects = [
        {
            'name': 'tensorflow',
            'description': 'An Open Source Machine Learning Framework for Everyone',
            'stargazers_count': 185000,
            'forks_count': 74000,
            'html_url': 'https://github.com/tensorflow/tensorflow',
            'language': 'C++'
        }
    ]

    trending_projects = [
        {
            'name': 'chatgpt-clone',
            'description': 'A ChatGPT clone built with modern web technologies',
            'stargazers_count': 15000,
            'forks_count': 3000,
            'html_url': 'https://github.com/user/chatgpt-clone',
            'language': 'TypeScript'
        }
    ]

    # 创建消息格式（不发送）
    embed = notifier.create_discord_embed(popular_projects, trending_projects)
    print("Discord消息格式预览：")
    print(f"标题: {embed['embeds'][0]['title']}")
    print(f"描述: {embed['embeds'][0]['description']}")
    print(f"字段数量: {len(embed['embeds'][0]['fields'])}")


if __name__ == "__main__":
    # 设置测试用的环境变量（可选）
    os.environ.setdefault('GITHUB_TOKEN', 'your_token_here')
    os.environ.setdefault('DISCORD_WEBHOOK_URL', 'your_webhook_here')

    print("AI GitHub Tracker 功能演示")
    print("=" * 50)

    try:
        # 如果有GitHub Token，演示API功能
        if os.getenv('GITHUB_TOKEN') and os.getenv('GITHUB_TOKEN') != 'your_token_here':
            demo_github_api()
        else:
            print("跳过GitHub API演示（未配置TOKEN）")

        demo_ai_filter()
        demo_deduplicator()
        demo_trend_analyzer()
        demo_discord_notifier()

    except Exception as e:
        print(f"演示过程中发生错误: {e}")

    print("\n" + "=" * 50)
    print("演示完成！")