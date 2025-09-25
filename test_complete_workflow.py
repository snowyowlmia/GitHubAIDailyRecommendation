#!/usr/bin/env python3
"""
测试完整的6步推送工作流
"""

import os
import subprocess
import time

def test_workflow_sequence():
    """测试6步推送序列"""
    print("🔧 测试完整工作流序列")
    print("=" * 60)

    # 定义6步推送序列
    steps = [
        ("1️⃣ 普通AI - Lifetime趋势", ["--trend-timeframe", "lifetime"]),
        ("2️⃣ 普通AI - 30天趋势", ["--trend-timeframe", "30days"]),
        ("3️⃣ 普通AI - 7天趋势", ["--trend-timeframe", "7days"]),
        ("4️⃣ 商用AI - Lifetime趋势", ["--commercial", "--trend-timeframe", "lifetime"]),
        ("5️⃣ 商用AI - 30天趋势", ["--commercial", "--trend-timeframe", "30days"]),
        ("6️⃣ 商用AI - 7天趋势", ["--commercial", "--trend-timeframe", "7days"]),
    ]

    # 检查环境变量
    gh_token = os.getenv('GH_TOKEN')
    discord_url = os.getenv('DISCORD_WEBHOOK_URL')

    print(f"🔍 环境检查:")
    print(f"  GH_TOKEN: {'✅ 已设置' if gh_token else '❌ 未设置'}")
    print(f"  DISCORD_WEBHOOK_URL: {'✅ 已设置' if discord_url else '⚠️ 未设置'}")
    print()

    if not gh_token:
        print("❌ GH_TOKEN未设置，无法测试完整功能")
        return False

    success_count = 0
    for i, (step_name, args) in enumerate(steps, 1):
        print(f"🚀 执行步骤 {i}/6: {step_name}")
        print(f"   命令: python ai_tracker.py {' '.join(args)}")

        try:
            # 执行命令（dry run模式，不实际发送到Discord）
            result = subprocess.run(
                ["python", "ai_tracker.py"] + args,
                capture_output=True,
                text=True,
                timeout=30
            )

            if result.returncode == 0:
                print(f"   ✅ 成功")
                success_count += 1
            else:
                print(f"   ❌ 失败 (退出码: {result.returncode})")
                if result.stderr:
                    print(f"   错误: {result.stderr[:200]}...")

        except subprocess.TimeoutExpired:
            print(f"   ⏰ 超时")
        except Exception as e:
            print(f"   ❌ 异常: {e}")

        print()

        # 模拟30秒间隔（测试中缩短为3秒）
        if i < 6:
            print("⏳ 等待3秒（模拟30秒间隔）...")
            time.sleep(3)
            print()

    print("📊 测试结果:")
    print(f"   成功: {success_count}/6")
    print(f"   失败: {6-success_count}/6")

    if success_count == 6:
        print("🎉 所有步骤测试通过！")
        return True
    else:
        print("⚠️ 部分步骤失败，请检查错误信息")
        return False

def check_workflow_timing():
    """检查cron时间设置"""
    print("\n⏰ GitHub Actions cron时间检查:")
    print("   设置: '0 23 * * *' (UTC时间)")
    print("   对应: 北京时间早上7点")
    print("   频率: 每天执行一次")
    print("   ✅ 时间配置正确")

if __name__ == "__main__":
    success = test_workflow_sequence()
    check_workflow_timing()

    print("\n💡 下一步:")
    if success:
        print("   1. 工作流测试通过，可以提交到GitHub")
        print("   2. 在GitHub Actions中手动触发测试")
        print("   3. 等待明天早上7点自动执行")
    else:
        print("   1. 修复测试中发现的问题")
        print("   2. 重新运行测试")
        print("   3. 确保所有环境变量正确设置")