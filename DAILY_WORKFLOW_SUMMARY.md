# 每日自动推送工作流配置总结

## 🕐 执行时间
- **北京时间**: 每天上午 7:00
- **UTC时间**: 每天 23:00 (前一天)
- **Cron表达式**: `'0 23 * * *'`

## 🔄 6步推送序列

### 普通AI项目 (3步)
1. **1️⃣ 普通AI - Lifetime趋势**
   - 命令: `python ai_tracker.py --trend-timeframe lifetime`
   - 描述: 推送历史最受欢迎的普通AI项目

2. **2️⃣ 普通AI - 30天趋势**
   - 命令: `python ai_tracker.py --trend-timeframe 30days`
   - 描述: 推送最近30天热门的普通AI项目

3. **3️⃣ 普通AI - 7天趋势**
   - 命令: `python ai_tracker.py --trend-timeframe 7days`
   - 描述: 推送最近7天热门的普通AI项目

### 商用AI项目 (3步)
4. **4️⃣ 商用AI - Lifetime趋势**
   - 命令: `python ai_tracker.py --commercial --trend-timeframe lifetime`
   - 描述: 推送历史最受欢迎的商用AI项目

5. **5️⃣ 商用AI - 30天趋势**
   - 命令: `python ai_tracker.py --commercial --trend-timeframe 30days`
   - 描述: 推送最近30天热门的商用AI项目

6. **6️⃣ 商用AI - 7天趋势**
   - 命令: `python ai_tracker.py --commercial --trend-timeframe 7days`
   - 描述: 推送最近7天热门的商用AI项目

## ⏱️ 时间控制
- 每步之间间隔 **30秒**，避免API限制和Discord消息过快
- 总执行时间约 **3-4分钟**（不含实际推送时间）

## 🔐 环境变量需求
- `GH_TOKEN`: GitHub访问令牌
- `DISCORD_WEBHOOK_URL`: Discord Webhook URL（可选）

## 📁 文件自动管理
- 自动更新 `sent_projects.json` 文件
- 自动提交并推送到GitHub仓库
- 提交信息格式: `"Update sent projects - YYYY-MM-DD HH:MM:SS"`

## 🚀 触发方式
1. **自动触发**: 每天北京时间7点自动执行
2. **手动触发**: 在GitHub Actions页面手动运行

## ✅ 配置状态
- [x] 6步推送序列已配置
- [x] 北京时间7点自动执行
- [x] 普通+商用AI双模式覆盖
- [x] 3种时间框架完整覆盖
- [x] API限制和Discord速率控制
- [x] 自动文件管理和提交

## 📋 验证清单
- [ ] GitHub Secrets 已设置 (GH_TOKEN, DISCORD_WEBHOOK_URL)
- [ ] 工作流文件已提交到仓库
- [ ] Discord Webhook 有效且可访问
- [ ] GitHub Actions 权限已正确配置
- [ ] 首次运行手动测试通过

---

**注意**: 此配置确保每天早上7点会推送6条不同类型的AI项目消息到Discord频道，覆盖普通AI和商用AI的全时间框架趋势分析。