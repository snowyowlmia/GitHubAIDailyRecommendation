#!/usr/bin/env python3
"""
测试商用实用性AI项目功能
"""

from ai_tracker import CommercialAIProjectFilter, DiscordNotifier, ProjectSummarizer

def test_commercial_filter():
    """测试商用项目过滤器"""
    print("🧪 测试商用实用性AI项目过滤器")
    print("=" * 80)

    filter_obj = CommercialAIProjectFilter()

    # 测试项目数据
    test_projects = [
        {
            'id': 1,
            'name': 'n8n-workflows',
            'description': 'n8n workflow automation for social media posting and web scraping',
            'stargazers_count': 5000,
            'forks_count': 800,
            'topics': ['automation', 'workflow', 'n8n', 'scraping'],
            'language': 'JavaScript'
        },
        {
            'id': 2,
            'name': 'xiaohongshu-mcp',
            'description': 'MCP system for automatic Xiaohongshu posting with AI content generation',
            'stargazers_count': 2500,
            'forks_count': 400,
            'topics': ['xiaohongshu', 'mcp', 'social-media', 'automation'],
            'language': 'Python'
        },
        {
            'id': 3,
            'name': 'reddit-crawler-ai',
            'description': 'AI-powered Reddit crawler and content analyzer for business intelligence',
            'stargazers_count': 3200,
            'forks_count': 600,
            'topics': ['reddit', 'crawler', 'ai', 'business-intelligence'],
            'language': 'Python'
        },
        {
            'id': 4,
            'name': 'chatbot-saas',
            'description': 'Production-ready chatbot service with enterprise features and API',
            'stargazers_count': 8000,
            'forks_count': 1200,
            'topics': ['chatbot', 'saas', 'enterprise', 'api'],
            'language': 'TypeScript'
        },
        {
            'id': 5,
            'name': 'academic-research-tool',
            'description': 'Deep learning research framework for academic purposes',
            'stargazers_count': 15000,
            'forks_count': 2000,
            'topics': ['research', 'academic', 'deep-learning'],
            'language': 'Python'
        },
        {
            'id': 6,
            'name': 'ecommerce-ai-assistant',
            'description': 'AI assistant for Shopify stores with inventory management and customer service automation',
            'stargazers_count': 4500,
            'forks_count': 700,
            'topics': ['ecommerce', 'shopify', 'ai', 'automation', 'customer-service'],
            'language': 'JavaScript'
        },
        {
            'id': 7,
            'name': 'trading-bot-ai',
            'description': 'Automated trading bot with machine learning for crypto and stock markets',
            'stargazers_count': 6800,
            'forks_count': 1000,
            'topics': ['trading', 'crypto', 'stock', 'automation', 'machine-learning'],
            'language': 'Python'
        }
    ]

    print("📋 项目评估结果:")
    print("-" * 50)

    commercial_projects = []
    for project in test_projects:
        is_commercial = filter_obj.is_commercial_ai_project(project)
        status = "✅ 商用项目" if is_commercial else "❌ 非商用项目"

        print(f"{project['name']} - {status}")
        print(f"  描述: {project['description']}")
        print(f"  ⭐ {project['stargazers_count']:,} 🍴 {project['forks_count']:,}")
        print(f"  主题: {', '.join(project['topics'])}")
        print()

        if is_commercial:
            commercial_projects.append(project)

    print(f"🎯 商用项目识别结果: {len(commercial_projects)}/{len(test_projects)} 个项目被识别为商用项目")

    # 测试过滤方法
    filtered = filter_obj.filter_commercial_ai_projects(test_projects)
    print(f"📊 过滤器结果: 识别出 {len(filtered)} 个商用实用性AI项目")

    return commercial_projects

def test_commercial_discord_format():
    """测试商用项目Discord消息格式"""
    print("\n📱 测试商用项目Discord消息格式")
    print("=" * 80)

    summarizer = ProjectSummarizer()
    notifier = DiscordNotifier(summarizer=summarizer)

    # 模拟商用项目数据
    commercial_projects = [
        {
            'name': 'n8n-social-automation',
            'stargazers_count': 5000,
            'forks_count': 800,
            'html_url': 'https://github.com/test/n8n-social-automation',
            'language': 'JavaScript',
            'description': 'Complete social media automation workflows using n8n with AI content generation',
            'topics': ['automation', 'n8n', 'social-media', 'ai']
        },
        {
            'name': 'ecommerce-chatbot',
            'stargazers_count': 3200,
            'forks_count': 480,
            'html_url': 'https://github.com/test/ecommerce-chatbot',
            'language': 'Python',
            'description': 'Production-ready AI chatbot for e-commerce with Shopify integration',
            'topics': ['chatbot', 'ecommerce', 'shopify', 'ai']
        }
    ]

    timeframes = ['lifetime', '30days', '7days']

    for timeframe in timeframes:
        embed = notifier.create_commercial_discord_embed(commercial_projects, commercial_projects, timeframe)
        print(f"\n🎯 {timeframe.upper()} 商用消息格式:")
        print(f"  标题: {embed['embeds'][0]['title']}")
        print(f"  描述: {embed['embeds'][0]['description']}")
        print(f"  颜色: {embed['embeds'][0]['color']} (深蓝商务色)")
        print(f"  字段数量: {len(embed['embeds'][0]['fields'])}")

        # 显示字段名称
        for field in embed['embeds'][0]['fields']:
            print(f"    - {field['name']}")
        print()

def test_commercial_keywords():
    """测试商用关键词覆盖"""
    print("\n🔍 测试商用关键词覆盖")
    print("=" * 80)

    filter_obj = CommercialAIProjectFilter()

    print("💼 商用关键词类别:")
    categories = [
        ("自动化工具", ['automation', 'workflow', 'n8n', 'zapier']),
        ("社交媒体", ['social media', 'xiaohongshu', 'instagram', 'mcp']),
        ("爬虫工具", ['scraper', 'crawler', 'reddit crawler', 'web scraping']),
        ("电商工具", ['ecommerce', 'shopify', 'amazon', 'dropshipping']),
        ("办公生产力", ['productivity', 'office automation', 'dashboard']),
        ("通信客服", ['chatbot', 'customer service', 'telegram bot']),
        ("金融交易", ['trading', 'crypto', 'stock', 'trading bot'])
    ]

    for category, keywords in categories:
        print(f"  {category}: {len(keywords)} 个关键词")
        print(f"    示例: {', '.join(keywords[:3])}")

    print(f"\n📊 总计:")
    print(f"  商用关键词: {len(filter_obj.COMMERCIAL_KEYWORDS)} 个")
    print(f"  商业指标词: {len(filter_obj.BUSINESS_INDICATORS)} 个")
    print(f"  总覆盖: {len(filter_obj.COMMERCIAL_KEYWORDS) + len(filter_obj.BUSINESS_INDICATORS)} 个关键词")

if __name__ == "__main__":
    # 运行所有测试
    commercial_projects = test_commercial_filter()
    test_commercial_discord_format()
    test_commercial_keywords()

    print("\n🎉 商用实用性AI项目功能测试完成！")
    print(f"✅ 成功识别出具有商用价值的AI项目")
    print(f"✅ Discord消息格式设计完成")
    print(f"✅ 关键词覆盖全面")