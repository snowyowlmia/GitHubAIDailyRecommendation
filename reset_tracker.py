#!/usr/bin/env python3
"""
AI Tracker Reset Script
快速重置AI追踪器的已推送项目记录
"""

import json
import os
from datetime import datetime

def reset_tracker():
    """重置追踪器记录"""
    storage_file = 'sent_projects.json'

    if not os.path.exists(storage_file):
        print("📝 未找到已推送项目记录文件，无需重置")
        return

    # 备份原有记录
    backup_file = f'sent_projects_backup_{datetime.now().strftime("%Y%m%d_%H%M%S")}.json'
    try:
        with open(storage_file, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # 创建备份
        with open(backup_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

        print(f"📋 已备份 {len(data)} 条记录到: {backup_file}")

        # 重置记录
        with open(storage_file, 'w', encoding='utf-8') as f:
            json.dump({}, f, ensure_ascii=False, indent=2)

        print("🔄 已重置推送记录")
        print("✅ 下次运行将推送最热门的AI项目")
        print(f"📊 原有记录已备份，如需恢复请将 {backup_file} 重命名为 {storage_file}")

    except Exception as e:
        print(f"❌ 重置失败: {e}")

def show_stats():
    """显示统计信息"""
    storage_file = 'sent_projects.json'

    if not os.path.exists(storage_file):
        print("📝 未找到已推送项目记录文件")
        return

    try:
        with open(storage_file, 'r', encoding='utf-8') as f:
            data = json.load(f)

        if not data:
            print("📊 当前没有已推送项目记录")
            return

        print("📊 推送统计信息:")
        print(f"  已推送项目总数: {len(data)}")

        # 找到最新推送时间
        latest_date = None
        latest_project = None
        for project in data.values():
            if 'sent_date' in project:
                if latest_date is None or project['sent_date'] > latest_date:
                    latest_date = project['sent_date']
                    latest_project = project

        if latest_project:
            print(f"  最后推送时间: {latest_date}")
            print(f"  最后推送项目: {latest_project['name']}")

        print(f"  存储文件: {storage_file}")

        # 显示最近5个推送的项目
        print("\n📋 最近推送的项目:")
        sorted_projects = sorted(data.values(),
                               key=lambda x: x.get('sent_date', ''),
                               reverse=True)[:5]

        for i, project in enumerate(sorted_projects, 1):
            stars = project.get('stars', 0)
            print(f"  {i}. {project['name']} - ⭐{stars:,}")

    except Exception as e:
        print(f"❌ 读取统计信息失败: {e}")

def main():
    """主函数"""
    print("AI GitHub Tracker Reset Tool")
    print("=" * 40)

    while True:
        print("\n请选择操作:")
        print("1. 📊 查看推送统计")
        print("2. 🔄 重置推送记录")
        print("3. ❌ 退出")

        choice = input("\n请输入选项 (1-3): ").strip()

        if choice == '1':
            show_stats()
        elif choice == '2':
            confirm = input("⚠️  确定要重置所有推送记录吗？下次将推送最热门项目 (y/N): ").strip().lower()
            if confirm in ['y', 'yes']:
                reset_tracker()
            else:
                print("已取消重置操作")
        elif choice == '3':
            print("再见！")
            break
        else:
            print("无效选项，请重新选择")

if __name__ == "__main__":
    main()