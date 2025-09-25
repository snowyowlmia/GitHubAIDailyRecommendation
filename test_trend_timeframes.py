#!/usr/bin/env python3
"""
测试多时间框架趋势分析功能
"""

from ai_tracker import TrendAnalyzer
from datetime import datetime, timedelta
import json

def test_trend_timeframes():
    """测试不同时间框架的趋势分析"""
    analyzer = TrendAnalyzer()

    # 模拟项目数据
    now = datetime.now()
    test_projects = [
        {
            'id': 1,
            'name': '老项目-高人气',
            'stargazers_count': 50000,
            'forks_count': 10000,
            'created_at': (now - timedelta(days=1000)).isoformat(),
            'html_url': 'https://github.com/test/old-popular'
        },
        {
            'id': 2,
            'name': '新项目-高增长',
            'stargazers_count': 1000,
            'forks_count': 200,
            'created_at': (now - timedelta(days=30)).isoformat(),
            'html_url': 'https://github.com/test/new-trending'
        },
        {
            'id': 3,
            'name': '最新项目-快速增长',
            'stargazers_count': 300,
            'forks_count': 50,
            'created_at': (now - timedelta(days=7)).isoformat(),
            'html_url': 'https://github.com/test/newest-fast'
        },
        {
            'id': 4,
            'name': '中等项目',
            'stargazers_count': 5000,
            'forks_count': 1000,
            'created_at': (now - timedelta(days=365)).isoformat(),
            'html_url': 'https://github.com/test/medium'
        }
    ]

    timeframes = ['lifetime', '30days', '7days']

    print("🧪 测试多时间框架趋势分析功能")
    print("=" * 80)

    for timeframe in timeframes:
        print(f"\n📊 {timeframe.upper()} 趋势分析结果:")
        print("-" * 50)

        # 计算每个项目的趋势分数
        for project in test_projects:
            score = analyzer.calculate_trend_score(project, timeframe)
            days_old = (now - datetime.fromisoformat(project['created_at'].replace('Z', ''))).days
            print(f"  {project['name']}")
            print(f"    ⭐ Stars: {project['stargazers_count']:,}")
            print(f"    📅 天数: {days_old}")
            print(f"    📈 趋势分数: {score:.4f}")
            print()

        # 按趋势分数排序
        sorted_projects = analyzer.sort_by_trend_score(test_projects.copy(), timeframe)
        print(f"  🏆 {timeframe} 排名:")
        for i, project in enumerate(sorted_projects, 1):
            print(f"    {i}. {project['name']} (分数: {project['trend_score']:.4f})")
        print()

def test_discord_message_formats():
    """测试不同时间框架的Discord消息格式"""
    from ai_tracker import DiscordNotifier

    print("\n📱 测试Discord消息格式")
    print("=" * 80)

    notifier = DiscordNotifier()

    # 模拟项目数据
    test_projects = [{
        'name': 'test-project',
        'stargazers_count': 1000,
        'forks_count': 200,
        'html_url': 'https://github.com/test/project',
        'language': 'Python',
        'description': 'A test AI project for demonstration'
    }]

    timeframes = ['lifetime', '30days', '7days']

    for timeframe in timeframes:
        embed = notifier.create_discord_embed([], test_projects, timeframe)
        print(f"\n🎯 {timeframe.upper()} 消息格式:")
        print(f"  标题: {embed['embeds'][0]['title']}")
        print(f"  描述: {embed['embeds'][0]['description']}")
        if embed['embeds'][0]['fields']:
            print(f"  字段名: {embed['embeds'][0]['fields'][0]['name']}")
        print()

if __name__ == "__main__":
    test_trend_timeframes()
    test_discord_message_formats()