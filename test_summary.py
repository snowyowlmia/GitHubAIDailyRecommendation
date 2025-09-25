#!/usr/bin/env python3
"""
测试项目总结生成功能
"""

from ai_tracker import ProjectSummarizer, DiscordNotifier

def test_project_summaries():
    """测试项目总结生成"""
    summarizer = ProjectSummarizer()

    # 测试项目数据
    test_projects = [
        {
            'name': 'tensorflow',
            'description': 'An Open Source Machine Learning Framework for Everyone',
            'stargazers_count': 185000,
            'forks_count': 74000,
            'language': 'C++',
            'topics': ['machine-learning', 'deep-learning', 'neural-network'],
            'created_at': '2015-11-07T01:05:27Z',
            'updated_at': '2023-12-01T10:30:00Z',
            'html_url': 'https://github.com/tensorflow/tensorflow'
        },
        {
            'name': 'transformers',
            'description': '🤗 Transformers: State-of-the-art Machine Learning for Pytorch, TensorFlow, and JAX.',
            'stargazers_count': 150000,
            'forks_count': 30000,
            'language': 'Python',
            'topics': ['transformers', 'bert', 'gpt', 'nlp', 'pytorch'],
            'created_at': '2018-10-29T13:56:00Z',
            'updated_at': '2023-12-01T15:20:00Z',
            'html_url': 'https://github.com/huggingface/transformers'
        },
        {
            'name': 'awesome-chatgpt-prompts',
            'description': 'This repo includes ChatGPT prompt curation to use ChatGPT better.',
            'stargazers_count': 95000,
            'forks_count': 12000,
            'language': 'None',
            'topics': ['chatgpt', 'prompts', 'ai'],
            'created_at': '2022-12-05T10:30:00Z',
            'updated_at': '2023-12-01T08:45:00Z',
            'html_url': 'https://github.com/f/awesome-chatgpt-prompts'
        },
        {
            'name': 'cursor-free-vip',
            'description': 'A new experimental project for cursor editor.',
            'stargazers_count': 35756,
            'forks_count': 2500,
            'language': 'TypeScript',
            'topics': ['editor', 'ai', 'tool'],
            'created_at': '2024-08-15T14:20:00Z',
            'updated_at': '2023-12-01T12:10:00Z',
            'html_url': 'https://github.com/yeongpin/cursor-free-vip'
        },
        {
            'name': 'NewAIProject',
            'description': 'A brand new AI innovation that just launched.',
            'stargazers_count': 850,
            'forks_count': 120,
            'language': 'Python',
            'topics': ['ai', 'innovation'],
            'created_at': '2024-11-01T09:00:00Z',
            'updated_at': '2023-12-01T16:30:00Z',
            'html_url': 'https://github.com/test/newaiproject'
        }
    ]

    print("🧪 测试项目总结生成功能")
    print("=" * 80)

    for i, project in enumerate(test_projects, 1):
        print(f"\n{i}. 项目: {project['name']}")
        print(f"   Star数: {project['stargazers_count']:,}")
        print(f"   语言: {project['language']}")
        print(f"   原描述: {project['description']}")

        summary = summarizer.generate_summary(project)
        print(f"   🤖 智能总结: {summary}")
        print("-" * 80)

def test_discord_format():
    """测试Discord消息格式"""
    print("\n📱 测试Discord消息格式")
    print("=" * 80)

    summarizer = ProjectSummarizer()
    notifier = DiscordNotifier(summarizer=summarizer)

    test_project = {
        'name': 'pytorch',
        'description': 'Tensors and Dynamic neural networks in Python with strong GPU acceleration',
        'stargazers_count': 93000,
        'forks_count': 25000,
        'language': 'C++',
        'topics': ['pytorch', 'deep-learning', 'machine-learning'],
        'created_at': '2016-08-13T07:45:00Z',
        'updated_at': '2023-12-01T14:20:00Z',
        'html_url': 'https://github.com/pytorch/pytorch'
    }

    formatted = notifier.format_project_info(test_project, 1)
    print("Discord格式化结果:")
    print(formatted)

    # 测试完整embed
    embed = notifier.create_discord_embed([test_project], [test_project])
    print(f"\nEmbed标题: {embed['embeds'][0]['title']}")
    print(f"字段数量: {len(embed['embeds'][0]['fields'])}")

def test_different_project_types():
    """测试不同类型项目的总结"""
    print("\n🔍 测试不同类型项目的总结生成")
    print("=" * 80)

    summarizer = ProjectSummarizer()

    project_types = [
        ("热门老项目", {
            'name': 'scikit-learn', 'description': 'machine learning in Python',
            'stargazers_count': 58000, 'forks_count': 25000, 'language': 'Python',
            'topics': ['machine-learning', 'data-science'], 'created_at': '2010-08-17T09:43:33Z'
        }),
        ("新兴项目", {
            'name': 'vllm', 'description': 'A high-throughput and memory-efficient inference and serving engine for LLMs',
            'stargazers_count': 25000, 'forks_count': 3500, 'language': 'Python',
            'topics': ['llm', 'inference'], 'created_at': '2023-02-14T18:11:12Z'
        }),
        ("学习资源", {
            'name': 'ML-For-Beginners', 'description': '12 weeks, 26 lessons, 52 quizzes, classic Machine Learning for all',
            'stargazers_count': 77000, 'forks_count': 15000, 'language': 'Jupyter Notebook',
            'topics': ['machine-learning', 'beginner', 'course'], 'created_at': '2021-03-01T21:11:42Z'
        })
    ]

    for type_name, project in project_types:
        summary = summarizer.generate_summary(project)
        print(f"{type_name}: {project['name']}")
        print(f"  💡 {summary}\n")

if __name__ == "__main__":
    test_project_summaries()
    test_discord_format()
    test_different_project_types()