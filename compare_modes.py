#!/usr/bin/env python3
"""
比较不同模式的项目筛选结果
"""

from ai_tracker import AIProjectFilter, CommercialAIProjectFilter

def compare_filters():
    """比较普通AI过滤器和商用AI过滤器的区别"""

    # 模拟项目数据
    test_projects = [
        {
            'id': 1,
            'name': 'tensorflow',
            'description': 'An Open Source Machine Learning Framework for Everyone',
            'stargazers_count': 180000,
            'topics': ['machine-learning', 'deep-learning', 'tensorflow'],
            'language': 'C++'
        },
        {
            'id': 2,
            'name': 'n8n',
            'description': 'Workflow automation tool with AI integration for businesses',
            'stargazers_count': 45000,
            'topics': ['automation', 'workflow', 'business', 'api'],
            'language': 'TypeScript'
        },
        {
            'id': 3,
            'name': 'academic-research-nlp',
            'description': 'Research framework for natural language processing experiments',
            'stargazers_count': 5000,
            'topics': ['nlp', 'research', 'academic', 'experiments'],
            'language': 'Python'
        },
        {
            'id': 4,
            'name': 'chatbot-service',
            'description': 'Production-ready AI chatbot with enterprise features and API',
            'stargazers_count': 12000,
            'topics': ['chatbot', 'enterprise', 'api', 'production'],
            'language': 'Python'
        },
        {
            'id': 5,
            'name': 'social-media-automation',
            'description': 'AI-powered social media posting automation with MCP integration',
            'stargazers_count': 8000,
            'topics': ['social-media', 'automation', 'mcp', 'ai'],
            'language': 'JavaScript'
        },
        {
            'id': 6,
            'name': 'deep-learning-theory',
            'description': 'Theoretical deep learning research implementations',
            'stargazers_count': 3000,
            'topics': ['deep-learning', 'theory', 'research'],
            'language': 'Python'
        }
    ]

    ai_filter = AIProjectFilter()
    commercial_filter = CommercialAIProjectFilter()

    print("🔍 项目筛选对比分析")
    print("=" * 80)

    print("📋 测试项目:")
    for project in test_projects:
        print(f"  • {project['name']} - {project['description'][:50]}...")
    print()

    # 普通AI过滤
    ai_projects = ai_filter.filter_ai_projects(test_projects)
    print("🤖 普通AI模式 (python ai_tracker.py):")
    print(f"  筛选结果: {len(ai_projects)}/{len(test_projects)} 个项目")
    for project in ai_projects:
        print(f"    ✅ {project['name']}")
    print()

    # 商用AI过滤
    commercial_projects = commercial_filter.filter_commercial_ai_projects(test_projects)
    print("💼 商用AI模式 (python ai_tracker.py --commercial):")
    print(f"  筛选结果: {len(commercial_projects)}/{len(test_projects)} 个项目")
    for project in commercial_projects:
        print(f"    ✅ {project['name']}")
    print()

    # 分析差异
    ai_names = {p['name'] for p in ai_projects}
    commercial_names = {p['name'] for p in commercial_projects}

    only_ai = ai_names - commercial_names
    only_commercial = commercial_names - ai_names

    print("📊 筛选差异分析:")
    if only_ai:
        print(f"  🔬 只在普通AI模式中的项目: {', '.join(only_ai)}")
        print("     (通常是学术研究、理论框架类项目)")

    if only_commercial:
        print(f"  💰 只在商用模式中的项目: {', '.join(only_commercial)}")
        print("     (应该不会出现，因为商用是AI的子集)")

    both = ai_names & commercial_names
    if both:
        print(f"  🎯 两种模式都包含的项目: {', '.join(both)}")
        print("     (既有AI技术又有商用价值的项目)")

if __name__ == "__main__":
    compare_filters()