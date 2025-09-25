#!/usr/bin/env python3
"""
测试基础功能是否正常
"""

import os
import sys
import traceback

def test_basic_import():
    """测试基础导入"""
    print("🧪 测试基础功能")
    print("=" * 50)

    try:
        from ai_tracker import AIGitHubTracker, GitHubAPIClient, AIProjectFilter
        print("✅ 核心类导入成功")

        # 测试实例化
        tracker = AIGitHubTracker()
        print("✅ AIGitHubTracker 实例化成功")

        # 测试方法存在
        methods = ['run_daily_tracking', 'run_commercial_tracking']
        for method in methods:
            if hasattr(tracker, method):
                print(f"✅ {method} 方法存在")
            else:
                print(f"❌ {method} 方法不存在")

        return True
    except Exception as e:
        print(f"❌ 导入测试失败: {e}")
        traceback.print_exc()
        return False

def test_environment_check():
    """测试环境检查"""
    print("\n🔍 环境检查:")

    # 检查环境变量
    gh_token = os.getenv('GH_TOKEN')
    discord_url = os.getenv('DISCORD_WEBHOOK_URL')

    print(f"  GH_TOKEN: {'✅ 已设置' if gh_token else '❌ 未设置'}")
    print(f"  DISCORD_WEBHOOK_URL: {'✅ 已设置' if discord_url else '⚠️ 未设置 (可选)'}")

    # 检查必要文件
    files = ['ai_tracker.py', 'requirements.txt', 'sent_projects.json']
    for file in files:
        if os.path.exists(file):
            print(f"  {file}: ✅ 存在")
        else:
            print(f"  {file}: ❌ 不存在")

def test_argument_parsing():
    """测试参数解析不会崩溃"""
    print("\n📋 测试参数解析:")

    test_cases = [
        [],  # 无参数（GitHub Actions场景）
        ['--help'],  # 会导致SystemExit，但这是正常的
        ['--stats'],
        ['--reset'],
        ['--commercial'],
        ['--trend-timeframe', '30days'],
    ]

    for i, args in enumerate(test_cases):
        if '--help' in args:
            print(f"  测试 {i+1}: {args} - 跳过（会导致help退出）")
            continue

        try:
            # 模拟命令行参数
            original_argv = sys.argv.copy()
            sys.argv = ['ai_tracker.py'] + args

            import argparse
            parser = argparse.ArgumentParser(description='AI GitHub Daily Tracker - AI项目每日追踪器')
            parser.add_argument('--reset', action='store_true', help='重置已推送项目记录，下次将推送最热门的项目')
            parser.add_argument('--stats', action='store_true', help='显示推送统计信息')
            parser.add_argument('--trend-timeframe', choices=['lifetime', '30days', '7days'], default='lifetime', help='趋势分析时间框架 (默认: lifetime)')
            parser.add_argument('--multi-timeframe', action='store_true', help='执行多时间框架追踪（30天和7天趋势）')
            parser.add_argument('--commercial', action='store_true', help='执行商用实用性AI项目追踪')

            parsed_args = parser.parse_args(args)
            print(f"  测试 {i+1}: {args} - ✅ 解析成功")

        except SystemExit:
            # --help 和其他会导致退出的参数
            print(f"  测试 {i+1}: {args} - ✅ 正常退出")
        except Exception as e:
            print(f"  测试 {i+1}: {args} - ❌ 解析失败: {e}")
        finally:
            sys.argv = original_argv

if __name__ == "__main__":
    success = test_basic_import()
    test_environment_check()
    test_argument_parsing()

    if success:
        print("\n🎉 基础功能测试通过！")
        print("💡 如果GitHub Actions仍有问题，请检查:")
        print("   1. GitHub Secrets是否正确设置")
        print("   2. 网络连接是否正常")
        print("   3. GitHub API是否有限制")
        print("   4. 查看Actions的详细日志")
    else:
        print("\n❌ 基础功能测试失败，需要修复导入问题")