#!/usr/bin/env python3
"""
调试GitHub Actions问题
模拟GitHub Actions环境运行
"""

import sys
import traceback
import logging

def test_basic_run():
    """测试基本运行，模拟GitHub Actions"""
    print("🔍 调试GitHub Actions问题")
    print("=" * 50)

    print("📋 测试各种运行模式:")

    # 测试1: 模拟GitHub Actions的默认运行
    print("\n1. 🤖 默认模式 (模拟GitHub Actions):")
    print("   命令: python ai_tracker.py")
    try:
        # 模拟命令行参数
        original_argv = sys.argv.copy()
        sys.argv = ['ai_tracker.py']  # 只有程序名，没有其他参数

        from ai_tracker import main
        main()
        print("   ✅ 默认模式运行成功")

    except Exception as e:
        print(f"   ❌ 默认模式运行失败: {e}")
        print(f"   错误详情:")
        traceback.print_exc()
    finally:
        sys.argv = original_argv

    # 测试2: 显式指定参数
    print("\n2. 📈 显式参数模式:")
    print("   命令: python ai_tracker.py --trend-timeframe lifetime")
    try:
        original_argv = sys.argv.copy()
        sys.argv = ['ai_tracker.py', '--trend-timeframe', 'lifetime']

        from ai_tracker import main
        main()
        print("   ✅ 显式参数模式运行成功")

    except Exception as e:
        print(f"   ❌ 显式参数模式运行失败: {e}")
        print(f"   错误详情:")
        traceback.print_exc()
    finally:
        sys.argv = original_argv

def test_imports():
    """测试导入是否有问题"""
    print("\n🔍 测试模块导入:")

    try:
        from ai_tracker import AIGitHubTracker
        print("   ✅ AIGitHubTracker导入成功")

        tracker = AIGitHubTracker()
        print("   ✅ AIGitHubTracker实例化成功")

        # 测试方法存在
        if hasattr(tracker, 'run_daily_tracking'):
            print("   ✅ run_daily_tracking方法存在")
        else:
            print("   ❌ run_daily_tracking方法不存在")

        if hasattr(tracker, 'run_commercial_tracking'):
            print("   ✅ run_commercial_tracking方法存在")
        else:
            print("   ❌ run_commercial_tracking方法不存在")

    except Exception as e:
        print(f"   ❌ 导入失败: {e}")
        traceback.print_exc()

def test_argument_parsing():
    """测试参数解析"""
    print("\n🔍 测试参数解析:")

    try:
        import argparse

        parser = argparse.ArgumentParser(description='AI GitHub Daily Tracker - AI项目每日追踪器')
        parser.add_argument('--reset', action='store_true',
                           help='重置已推送项目记录，下次将推送最热门的项目')
        parser.add_argument('--stats', action='store_true',
                           help='显示推送统计信息')
        parser.add_argument('--trend-timeframe', choices=['lifetime', '30days', '7days'],
                           default='lifetime',
                           help='趋势分析时间框架 (默认: lifetime)')
        parser.add_argument('--multi-timeframe', action='store_true',
                           help='执行多时间框架追踪（30天和7天趋势）')
        parser.add_argument('--commercial', action='store_true',
                           help='执行商用实用性AI项目追踪')

        # 测试无参数（GitHub Actions场景）
        args = parser.parse_args([])
        print(f"   ✅ 无参数解析成功:")
        print(f"      reset: {args.reset}")
        print(f"      stats: {args.stats}")
        print(f"      trend_timeframe: {args.trend_timeframe}")
        print(f"      multi_timeframe: {args.multi_timeframe}")
        print(f"      commercial: {args.commercial}")

    except Exception as e:
        print(f"   ❌ 参数解析失败: {e}")
        traceback.print_exc()

if __name__ == "__main__":
    test_imports()
    test_argument_parsing()
    # test_basic_run()  # 注释掉避免实际运行网络请求

    print("\n💡 GitHub Actions调试提示:")
    print("1. 检查是否有任何导入错误")
    print("2. 检查参数解析是否正常")
    print("3. 检查环境变量是否设置(GH_TOKEN)")
    print("4. 检查网络连接是否正常")
    print("5. 检查GitHub API限制")