# 贡献指南 Contributing Guide

感谢您对AI GitHub Daily Tracker项目的关注！我们欢迎各种形式的贡献。

Thank you for your interest in contributing to AI GitHub Daily Tracker! We welcome all kinds of contributions.

## 🎯 项目目标 Project Goals

为AI开发者、研究者和爱好者提供高质量的GitHub AI项目每日推荐服务。

Provide high-quality daily GitHub AI project recommendations for AI developers, researchers, and enthusiasts.

## 🚀 如何开始贡献 How to Start Contributing

### 1. Fork 和 Clone
```bash
# Fork 项目到你的账户，然后克隆
git clone https://github.com/your-username/GitHubAIDailyRecommendation.git
cd GitHubAIDailyRecommendation

# 添加上游仓库
git remote add upstream https://github.com/snowyowlmia/GitHubAIDailyRecommendation.git
```

### 2. 设置开发环境
```bash
# 创建虚拟环境
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 安装依赖
pip install -r requirements.txt
pip install -r requirements-dev.txt  # 开发依赖（如果存在）
```

### 3. 创建功能分支
```bash
git checkout -b feature/your-feature-name
# 或者
git checkout -b fix/bug-description
```

## 📝 贡献类型 Types of Contributions

### 🐛 Bug 修复
- 修复现有功能的问题
- 提供测试用例验证修复
- 在PR中详细描述问题和解决方案

### ✨ 新功能
- AI项目筛选算法改进
- 新的趋势分析方法
- Discord消息格式优化
- 新的数据源集成

### 📖 文档改进
- README.md 更新
- 代码注释完善
- API文档编写
- 使用教程

### 🧪 测试改进
- 单元测试增加
- 集成测试完善
- 边界条件测试

## 🔍 代码质量要求 Code Quality Requirements

### Python 代码规范
- 遵循 PEP 8 代码风格
- 使用 type hints（类型提示）
- 添加必要的文档字符串
- 保持函数简洁（单一职责原则）

### 示例代码格式
```python
def analyze_project_trend(
    project_data: Dict[str, Any],
    timeframe: str = "lifetime"
) -> float:
    """分析项目趋势分数

    Args:
        project_data: 项目数据字典
        timeframe: 时间框架 ("lifetime", "30days", "7days")

    Returns:
        float: 趋势分数 (0.0-1.0)

    Raises:
        ValueError: 当timeframe参数无效时
    """
    # 实现代码...
```

### 提交消息格式
```
类型: 简短描述

详细描述（可选）

- 具体变更1
- 具体变更2

Closes #issue-number
```

类型包括：
- `feat`: 新功能
- `fix`: 错误修复
- `docs`: 文档更新
- `style`: 代码格式（不影响功能）
- `refactor`: 代码重构
- `test`: 测试相关
- `chore`: 其他（依赖更新等）

## 🔄 Pull Request 流程

### 1. 提交前检查
```bash
# 运行测试
python -m pytest tests/

# 代码格式检查
python -m flake8 ai_tracker.py

# 类型检查
python -m mypy ai_tracker.py
```

### 2. 创建 Pull Request
- 提供清晰的标题和描述
- 关联相关的 Issue
- 添加测试截图（如果是UI相关）
- 说明测试方法

### 3. Code Review 过程
- 至少需要1个维护者的批准
- 所有CI检查必须通过
- 解决所有review意见
- 保持提交历史整洁

## 🧪 测试要求 Testing Requirements

### 必须包含的测试
- 单元测试覆盖核心功能
- API调用的mock测试
- 错误处理测试
- 边界条件测试

### 测试命名规范
```python
def test_analyze_project_trend_with_valid_data():
    """测试有效数据的项目趋势分析"""

def test_analyze_project_trend_with_invalid_timeframe():
    """测试无效时间框架参数的错误处理"""
```

## 🚫 不接受的贡献 Contributions Not Accepted

- 破坏现有功能的更改
- 没有适当测试的新功能
- 不符合项目目标的功能
- 包含恶意代码的提交
- 违反开源许可的内容

## 🎉 贡献者认可 Contributor Recognition

所有贡献者都会在README.md中得到认可，重要贡献者会被添加到项目维护者列表中。

## 📞 联系方式 Contact

- GitHub Issues: 报告问题和功能请求
- Discussions: 一般讨论和问题
- Email: [维护者邮箱]

## 📚 开发资源 Development Resources

- [GitHub API文档](https://docs.github.com/en/rest)
- [Discord Webhook指南](https://discord.com/developers/docs/resources/webhook)
- [Python最佳实践](https://docs.python-guide.org/)

---

再次感谢您的贡献！每一个贡献都让这个项目变得更好。

Thank you again for your contribution! Every contribution makes this project better.