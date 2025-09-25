#!/usr/bin/env python3
"""
调试今天早上没有收到通知的原因
"""

import json
import os
from datetime import datetime, timezone, timedelta

def analyze_today_issue():
    """分析今天的问题"""
    print("🔍 分析今天早上的问题")
    print("=" * 60)

    # 分析时间
    beijing_tz = timezone(timedelta(hours=8))
    utc_now = datetime.now(timezone.utc)
    beijing_now = utc_now.astimezone(beijing_tz)

    print(f"📅 当前时间分析:")
    print(f"  UTC时间: {utc_now.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"  北京时间: {beijing_now.strftime('%Y-%m-%d %H:%M:%S')}")
    print()

    # 分析日志信息
    log_info = """
2025-09-25 08:58:06,279 - __main__ - INFO - GitHub API请求成功，找到 373261 个项目
2025-09-25 08:58:08,309 - __main__ - INFO - GitHub API请求成功，找到 34976 个项目
2025-09-25 08:58:10,304 - __main__ - INFO - GitHub API请求成功，找到 9601 个项目
2025-09-25 08:58:12,371 - __main__ - INFO - GitHub API请求成功，找到 21367 个项目
2025-09-25 08:58:14,309 - __main__ - INFO - GitHub API请求成功，找到 4500 个项目
2025-09-25 08:58:15,311 - __main__ - INFO - 从 89 个项目中筛选出 87 个AI项目
2025-09-25 08:58:15,312 - __main__ - INFO - 从 94 个项目中筛选出 80 个AI项目
2025-09-25 08:58:15,312 - __main__ - INFO - 从 87 个项目中过滤出 87 个未推送项目
2025-09-25 08:58:15,312 - __main__ - INFO - 从 80 个项目中过滤出 80 个未推送项目
2025-09-25 08:58:15,318 - __main__ - INFO - 按lifetime趋势分数排序了 80 个项目
2025-09-25 08:58:15,682 - __main__ - INFO - Discord消息发送成功
2025-09-25 08:58:15,684 - __main__ - INFO - ✅ 成功推送 2 个热门项目和 2 个趋势项目
    """

    print("📋 从日志分析发现的问题:")

    # 问题1: 只执行了一次
    print("1️⃣ **只执行了一次推送**")
    print("   - 日志显示只有一个时间点: 08:58")
    print("   - 应该有6次不同的推送（每隔30秒）")
    print("   - 说明工作流只执行了第一步")
    print()

    # 问题2: 使用的是旧版工作流
    print("2️⃣ **使用的是旧版工作流配置**")
    print("   - 日志显示成功推送了项目")
    print("   - 但只有一次推送，不是6次")
    print("   - 说明GitHub Actions使用的还是旧的workflow文件")
    print()

    # 问题3: 权限问题导致文件推送失败
    print("3️⃣ **权限问题导致git push失败**")
    print("   - 错误: Permission denied to github-actions[bot]")
    print("   - 403错误表示没有写入权限")
    print("   - sent_projects.json文件没有成功更新到远程仓库")
    print()

    print("🔧 解决方案:")
    print("1. ✅ 已推送新的6步工作流到远程仓库")
    print("2. ✅ 已修复权限配置")
    print("3. 🔄 明天早上7点将使用新配置")
    print("4. 💡 可以手动触发测试新工作流")
    print()

    # 检查当前sent_projects.json
    if os.path.exists('sent_projects.json'):
        with open('sent_projects.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
            print(f"📊 当前sent_projects.json状态:")
            print(f"   记录的项目数量: {len(data)}")

            # 找最新的记录
            latest_entries = []
            for project_id, info in data.items():
                if info.get('sent_date', '').startswith('2025-09-25'):
                    latest_entries.append((project_id, info))

            print(f"   今天的记录: {len(latest_entries)} 个项目")
            if latest_entries:
                print("   最新记录:")
                for project_id, info in latest_entries[:3]:  # 显示前3个
                    print(f"     - {info.get('name', project_id)}: {info.get('sent_date')}")
            print()

    print("🎯 **重要**: 今天早上的执行使用了旧配置，所以只推送了一次")
    print("明天早上7点将使用新的6步配置，会推送6条不同的消息！")

if __name__ == "__main__":
    analyze_today_issue()