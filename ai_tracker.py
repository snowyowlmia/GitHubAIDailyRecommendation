#!/usr/bin/env python3
"""
AI GitHub Daily Tracker - AI项目每日追踪器
每天自动发现并推送最值得关注的AI开源项目
"""

import os
import json
import time
import logging
from datetime import datetime, timedelta
from typing import List, Dict, Any, Optional
import requests
from dateutil import parser as date_parser

# 加载.env文件中的环境变量（用于本地测试）
try:
    from load_env import load_env
    load_env()
except ImportError:
    pass


class GitHubAPIClient:
    """GitHub API客户端，负责获取项目数据"""

    def __init__(self, token: Optional[str] = None):
        self.token = token or os.getenv('GH_TOKEN')
        self.base_url = 'https://api.github.com'
        self.session = requests.Session()
        if self.token:
            self.session.headers.update({'Authorization': f'token {self.token}'})

        self.logger = logging.getLogger(__name__)

    def search_repositories(self, query: str, sort: str = 'stars', order: str = 'desc', per_page: int = 50) -> List[Dict]:
        """搜索GitHub仓库"""
        url = f'{self.base_url}/search/repositories'
        params = {
            'q': query,
            'sort': sort,
            'order': order,
            'per_page': per_page
        }

        try:
            response = self.session.get(url, params=params)
            response.raise_for_status()
            data = response.json()
            self.logger.info(f"GitHub API请求成功，找到 {data.get('total_count', 0)} 个项目")
            return data.get('items', [])
        except requests.exceptions.RequestException as e:
            self.logger.error(f"GitHub API请求失败: {e}")
            return []

    def get_popular_ai_projects(self) -> List[Dict]:
        """获取最受欢迎的AI项目（按star数排序）"""
        # 分多次查询不同的AI领域，避免查询过长
        queries = [
            'machine learning OR "artificial intelligence" OR "deep learning"',
            'tensorflow OR pytorch OR keras',
            'nlp OR "natural language processing" OR transformer OR gpt',
            '"computer vision" OR opencv OR yolo'
        ]

        all_projects = []
        for query in queries:
            projects = self.search_repositories(query, sort='stars', per_page=25)
            all_projects.extend(projects)
            time.sleep(1)  # 避免API限制

        # 去除重复项目（基于ID）
        seen_ids = set()
        unique_projects = []
        for project in all_projects:
            if project['id'] not in seen_ids:
                seen_ids.add(project['id'])
                unique_projects.append(project)

        return unique_projects

    def get_trending_ai_projects(self) -> List[Dict]:
        """获取趋势AI项目（按更新时间排序）"""
        # 获取最近30天内更新的项目
        date_30_days_ago = (datetime.now() - timedelta(days=30)).strftime('%Y-%m-%d')

        # 分多次查询不同的AI领域
        queries = [
            f'machine learning pushed:>{date_30_days_ago}',
            f'tensorflow OR pytorch pushed:>{date_30_days_ago}',
            f'nlp OR gpt pushed:>{date_30_days_ago}',
            f'"computer vision" pushed:>{date_30_days_ago}'
        ]

        all_projects = []
        for query in queries:
            projects = self.search_repositories(query, sort='updated', per_page=25)
            all_projects.extend(projects)
            time.sleep(1)  # 避免API限制

        # 去除重复项目（基于ID）
        seen_ids = set()
        unique_projects = []
        for project in all_projects:
            if project['id'] not in seen_ids:
                seen_ids.add(project['id'])
                unique_projects.append(project)

        return unique_projects


class AIProjectFilter:
    """AI项目识别和过滤器"""

    AI_KEYWORDS = [
        'artificial intelligence', 'machine learning', 'deep learning', 'neural network',
        'computer vision', 'nlp', 'natural language processing', 'chatbot', 'tensorflow',
        'pytorch', 'llm', 'gpt', 'transformer', 'reinforcement learning', 'data science',
        'ai', 'openai', 'llama', 'bert', 'stable diffusion', 'generative ai', 'langchain',
        'keras', 'scikit-learn', 'pandas', 'numpy', 'opencv', 'yolo', 'cnn', 'rnn',
        'lstm', 'gan', 'vae', 'autoencoder', 'embedding', 'classification', 'regression',
        'clustering', 'recommendation', 'speech recognition', 'text mining', 'sentiment analysis'
    ]

    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def is_ai_project(self, repo: Dict) -> bool:
        """判断项目是否为AI相关项目"""
        # 安全地处理可能为None的字段
        name = repo.get('name') or ''
        description = repo.get('description') or ''
        topics = repo.get('topics') or []

        text_fields = [
            name.lower(),
            description.lower(),
            ' '.join(topics).lower()
        ]

        full_text = ' '.join(text_fields)

        for keyword in self.AI_KEYWORDS:
            if keyword in full_text:
                return True

        return False

    def filter_ai_projects(self, projects: List[Dict]) -> List[Dict]:
        """过滤出AI相关项目"""
        ai_projects = []
        for project in projects:
            if self.is_ai_project(project):
                ai_projects.append(project)

        self.logger.info(f"从 {len(projects)} 个项目中筛选出 {len(ai_projects)} 个AI项目")
        return ai_projects


class CommercialAIProjectFilter:
    """商用实用性AI项目识别和过滤器"""

    COMMERCIAL_KEYWORDS = [
        # 自动化工具和平台
        'automation', 'workflow', 'n8n', 'zapier', 'automate', 'pipeline', 'scheduler',
        'cronjob', 'webhook', 'api automation', 'workflow automation',

        # 社交媒体和内容管理
        'social media', 'instagram', 'twitter', 'linkedin', 'youtube', 'tiktok', 'facebook',
        'xiaohongshu', 'weibo', 'content management', 'social automation', 'post scheduler',
        'social media management', 'content generator', 'social bot', 'mcp',

        # 爬虫和数据采集
        'scraper', 'crawler', 'scraping', 'data extraction', 'web scraping', 'reddit crawler',
        'news crawler', 'price monitor', 'data collection', 'web automation', 'selenium',
        'beautifulsoup', 'scrapy',

        # 电商和业务工具
        'ecommerce', 'shopify', 'amazon', 'product management', 'inventory', 'price tracking',
        'dropshipping', 'affiliate', 'marketing automation', 'email marketing', 'crm',
        'lead generation', 'sales automation',

        # 办公和生产力
        'productivity', 'office automation', 'document processing', 'pdf automation',
        'excel automation', 'report generation', 'business intelligence', 'dashboard',
        'analytics', 'metrics', 'kpi', 'monitoring',

        # 通信和客服
        'chatbot', 'customer service', 'support bot', 'telegram bot', 'discord bot',
        'slack bot', 'whatsapp', 'wechat', 'messaging', 'notification', 'alert',

        # 内容创作和媒体
        'content creation', 'blog automation', 'seo', 'keyword research', 'content generator',
        'video automation', 'image processing', 'thumbnail generator', 'media converter',

        # 金融和交易
        'trading', 'crypto', 'stock', 'financial', 'investment', 'portfolio', 'market data',
        'price alert', 'trading bot', 'arbitrage',

        # 实用工具
        'utility', 'tool', 'helper', 'assistant', 'generator', 'converter', 'validator',
        'formatter', 'calculator', 'manager', 'organizer', 'tracker'
    ]

    BUSINESS_INDICATORS = [
        # 商业模式相关
        'saas', 'api', 'service', 'platform', 'solution', 'enterprise', 'business',
        'commercial', 'professional', 'premium', 'subscription', 'freemium',

        # 实用性指标
        'ready to use', 'production ready', 'plug and play', 'easy setup', 'one click',
        'no code', 'low code', 'drag and drop', 'user friendly', 'gui', 'interface',

        # 部署和集成
        'docker', 'kubernetes', 'cloud', 'aws', 'azure', 'google cloud', 'deployment',
        'hosting', 'server', 'microservice', 'rest api', 'graphql'
    ]

    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def is_commercial_ai_project(self, repo: Dict) -> bool:
        """判断项目是否为商用实用性AI项目"""
        # 首先必须是AI项目
        ai_filter = AIProjectFilter()
        if not ai_filter.is_ai_project(repo):
            return False

        # 安全地处理可能为None的字段
        name = repo.get('name') or ''
        description = repo.get('description') or ''
        topics = repo.get('topics') or []

        # 额外考虑readme内容（如果有的话）
        text_fields = [
            name.lower(),
            description.lower(),
            ' '.join(topics).lower()
        ]

        full_text = ' '.join(text_fields)

        # 检查商用关键词
        commercial_score = 0
        for keyword in self.COMMERCIAL_KEYWORDS:
            if keyword in full_text:
                commercial_score += 2

        # 检查商业指标关键词
        for keyword in self.BUSINESS_INDICATORS:
            if keyword in full_text:
                commercial_score += 1

        # 额外的商用性评估
        stars = repo.get('stargazers_count', 0)
        forks = repo.get('forks_count', 0)

        # 高star数的实用工具更可能是商用项目
        if stars > 1000:
            commercial_score += 1
        if stars > 5000:
            commercial_score += 1

        # 高fork率通常表示实用性
        if forks > 0 and stars > 0:
            fork_ratio = forks / stars
            if fork_ratio > 0.1:  # 10%以上的fork率
                commercial_score += 2

        # 商用性评分阈值
        return commercial_score >= 3

    def filter_commercial_ai_projects(self, projects: List[Dict]) -> List[Dict]:
        """过滤出商用实用性AI项目"""
        commercial_projects = []
        for project in projects:
            if self.is_commercial_ai_project(project):
                commercial_projects.append(project)

        self.logger.info(f"从 {len(projects)} 个项目中筛选出 {len(commercial_projects)} 个商用实用性AI项目")
        return commercial_projects


class ProjectDeduplicator:
    """项目去重器，管理已推送项目记录"""

    def __init__(self, storage_file: str = 'sent_projects.json'):
        self.storage_file = storage_file
        self.logger = logging.getLogger(__name__)
        self.sent_projects = self._load_sent_projects()

    def _load_sent_projects(self) -> Dict:
        """加载已推送项目记录"""
        if os.path.exists(self.storage_file):
            try:
                with open(self.storage_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except (json.JSONDecodeError, IOError) as e:
                self.logger.error(f"读取已推送项目记录失败: {e}")
                return {}
        return {}

    def _save_sent_projects(self):
        """保存已推送项目记录"""
        try:
            with open(self.storage_file, 'w', encoding='utf-8') as f:
                json.dump(self.sent_projects, f, ensure_ascii=False, indent=2)
        except IOError as e:
            self.logger.error(f"保存已推送项目记录失败: {e}")

    def is_project_sent(self, repo_id: str) -> bool:
        """检查项目是否已推送"""
        return str(repo_id) in self.sent_projects

    def mark_project_as_sent(self, repo: Dict):
        """标记项目为已推送"""
        repo_id = str(repo['id'])
        self.sent_projects[repo_id] = {
            'name': repo['name'],
            'full_name': repo['full_name'],
            'sent_date': datetime.now().isoformat(),
            'stars': repo['stargazers_count'],
            'url': repo['html_url']
        }
        self._save_sent_projects()

    def clean_old_records(self, days: int = 30):
        """清理旧记录"""
        cutoff_date = datetime.now() - timedelta(days=days)
        to_remove = []

        for repo_id, project_info in self.sent_projects.items():
            try:
                sent_date = date_parser.parse(project_info['sent_date'])
                if sent_date < cutoff_date:
                    to_remove.append(repo_id)
            except (ValueError, TypeError):
                to_remove.append(repo_id)

        for repo_id in to_remove:
            del self.sent_projects[repo_id]

        if to_remove:
            self._save_sent_projects()
            self.logger.info(f"清理了 {len(to_remove)} 条旧记录")

    def filter_new_projects(self, projects: List[Dict]) -> List[Dict]:
        """过滤出未推送的项目"""
        new_projects = []
        for project in projects:
            if not self.is_project_sent(project['id']):
                new_projects.append(project)

        self.logger.info(f"从 {len(projects)} 个项目中过滤出 {len(new_projects)} 个未推送项目")
        return new_projects

    def reset_sent_projects(self):
        """重置已推送项目记录，清空所有记录"""
        self.sent_projects = {}
        self._save_sent_projects()
        self.logger.info("已重置所有推送记录，下次将推送最热门的项目")

    def get_stats(self) -> Dict:
        """获取推送统计信息"""
        return {
            'total_sent': len(self.sent_projects),
            'latest_sent': max([proj['sent_date'] for proj in self.sent_projects.values()]) if self.sent_projects else None,
            'storage_file': self.storage_file
        }


class ProjectSummarizer:
    """项目总结生成器，生成有说服力的项目介绍"""

    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def generate_summary(self, repo: Dict) -> str:
        """生成项目的智能总结"""
        try:
            name = repo.get('name', '')
            description = repo.get('description', '')
            stars = repo.get('stargazers_count', 0)
            forks = repo.get('forks_count', 0)
            language = repo.get('language', 'Unknown')
            topics = repo.get('topics', [])
            created_at = repo.get('created_at', '')
            updated_at = repo.get('updated_at', '')

            # 计算项目年龄
            try:
                created_date = date_parser.parse(created_at)
                days_since_creation = max((datetime.now().replace(tzinfo=None) -
                                         created_date.replace(tzinfo=None)).days, 1)
                years = days_since_creation / 365.25
            except:
                years = 0

            # 只使用技术亮点和内容描述，避免数字重复
            technical_highlights = self._generate_technical_highlights(name, description, language, topics)

            if technical_highlights:
                return technical_highlights
            else:
                # 如果没有识别到技术亮点，使用项目描述
                return description[:80] + "..." if len(description) > 80 else description

        except Exception as e:
            self.logger.error(f"生成项目总结失败: {e}")
            return repo.get('description', '暂无描述')[:100]

    def _generate_popularity_reason(self, stars: int, forks: int, years: float) -> str:
        """生成受欢迎原因"""
        if stars >= 100000:
            return f"作为GitHub上最受欢迎的项目之一，{stars:,}个star证明了其在开发者社区中的统治地位。"
        elif stars >= 50000:
            return f"凭借{stars:,}个star和{forks:,}个fork，已成为该领域的标杆项目。"
        elif stars >= 20000:
            return f"获得{stars:,}个star，在开发者中享有很高声誉。"
        elif stars >= 5000:
            if years < 1:
                return f"虽然创建不到一年，但已获得{stars:,}个star，展现出强劲的增长势头。"
            else:
                return f"持续获得社区认可，{stars:,}个star体现了其实用价值。"
        elif stars >= 1000:
            if years < 0.5:
                return f"作为新兴项目，{stars:,}个star显示出巨大潜力。"
            else:
                return f"{stars:,}个star表明其在特定领域的影响力。"
        else:
            return f"正在快速发展中的项目，已获得{stars}个star。"

    def _generate_technical_highlights(self, name: str, description: str, language: str, topics: List[str]) -> str:
        """生成技术亮点"""
        name_lower = name.lower()
        desc_lower = description.lower()
        topics_str = ' '.join(topics).lower()
        text = f"{name_lower} {desc_lower} {topics_str}"

        # TensorFlow生态
        if 'tensorflow' in text:
            return "端到端机器学习平台，支持训练到部署的完整工作流"

        # PyTorch生态
        elif 'pytorch' in text:
            return "动态图深度学习框架，提供灵活的模型构建和调试能力"

        # Transformers和Hugging Face
        elif 'transformers' in text or 'huggingface' in text or '🤗' in text:
            return "预训练模型库，包含BERT、GPT等最新NLP模型"

        # 大语言模型推理
        elif any(keyword in text for keyword in ['llm', 'inference', 'vllm', 'serving']):
            return "高性能LLM推理引擎，优化内存使用和推理速度"

        # GPT和对话AI
        elif any(keyword in text for keyword in ['gpt', 'chatgpt', 'chat', 'conversation']):
            return "对话AI工具集，提供高质量的人机交互体验"

        # 计算机视觉
        elif any(keyword in text for keyword in ['opencv', 'yolo', 'detection', 'vision']):
            return "计算机视觉工具包，支持图像处理和目标检测"

        # Scikit-learn
        elif 'scikit' in text or 'sklearn' in text:
            return "经典机器学习库，提供分类、回归、聚类等算法"

        # 数据科学
        elif any(keyword in text for keyword in ['pandas', 'numpy', 'jupyter', 'data']):
            return "数据分析工具链，简化数据处理和可视化流程"

        # AI学习资源
        elif any(keyword in text for keyword in ['tutorial', 'learning', 'course', 'beginner']):
            return "AI学习教程，从基础概念到实践项目的完整指南"

        # 自动化和工具
        elif any(keyword in text for keyword in ['automation', 'tool', 'assistant', 'productivity']):
            return "AI自动化工具，提升开发效率和工作流优化"

        # Awesome系列
        elif 'awesome' in text:
            return "精选资源合集，汇总该领域最佳实践和工具"

        # 通用描述基于项目描述
        else:
            # 从描述中提取关键信息
            if len(description) > 10:
                return description[:70] + "..." if len(description) > 70 else description
            else:
                return f"{language}开发的AI工具，专注解决实际问题"

    def _generate_community_impact(self, stars: int, forks: int, years: float) -> str:
        """生成社区影响描述"""
        fork_ratio = forks / max(stars, 1)

        if fork_ratio > 0.3:
            return "活跃的贡献者社区和丰富的fork数量显示了项目的健康发展态势。"
        elif fork_ratio > 0.15:
            return "良好的社区参与度表明项目具有持续的发展动力。"
        elif stars > 1000:
            return "虽然fork较少，但高star数显示了项目的高质量和实用性。"
        else:
            return "正在建立社区基础，展现出良好的发展前景。"


class TrendAnalyzer:
    """趋势分析器，计算项目趋势分数"""

    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def calculate_trend_score(self, repo: Dict, timeframe: str = 'lifetime') -> float:
        """
        计算项目趋势分数
        timeframe: 'lifetime', '30days', '7days'
        """
        try:
            created_at = date_parser.parse(repo['created_at'])
            # 确保两个datetime都是naive类型
            if created_at.tzinfo is not None:
                created_at = created_at.replace(tzinfo=None)

            stars = repo.get('stargazers_count', 0)
            forks = repo.get('forks_count', 0)

            if timeframe == 'lifetime':
                # 原有逻辑：基于项目整个生命周期
                days_since_creation = max((datetime.now() - created_at).days, 1)
                daily_stars = stars / days_since_creation
                daily_forks = forks / days_since_creation
                trend_score = daily_stars * 0.7 + daily_forks * 0.3

            elif timeframe == '30days':
                # 30天趋势：假设最近30天获得的stars/forks比例更高
                # 使用更激进的增长假设来识别近期热门项目
                days_since_creation = max((datetime.now() - created_at).days, 1)

                # 对于较新的项目（<30天），使用实际天数
                if days_since_creation <= 30:
                    effective_days = days_since_creation
                else:
                    # 对于老项目，假设30%的stars来自最近30天
                    effective_days = 30
                    stars = int(stars * 0.3)  # 估算最近30天的增长
                    forks = int(forks * 0.3)

                daily_stars = stars / effective_days
                daily_forks = forks / effective_days
                trend_score = daily_stars * 0.7 + daily_forks * 0.3

            elif timeframe == '7days':
                # 7天趋势：更激进的近期增长估算
                days_since_creation = max((datetime.now() - created_at).days, 1)

                if days_since_creation <= 7:
                    effective_days = days_since_creation
                else:
                    # 对于老项目，假设15%的stars来自最近7天
                    effective_days = 7
                    stars = int(stars * 0.15)
                    forks = int(forks * 0.15)

                daily_stars = stars / effective_days
                daily_forks = forks / effective_days
                trend_score = daily_stars * 0.7 + daily_forks * 0.3

            else:
                raise ValueError(f"不支持的时间框架: {timeframe}")

            return trend_score
        except Exception as e:
            self.logger.error(f"计算趋势分数失败: {e}")
            return 0.0

    def sort_by_trend_score(self, projects: List[Dict], timeframe: str = 'lifetime') -> List[Dict]:
        """按趋势分数排序项目"""
        for project in projects:
            project['trend_score'] = self.calculate_trend_score(project, timeframe)

        sorted_projects = sorted(projects, key=lambda x: x['trend_score'], reverse=True)
        self.logger.info(f"按{timeframe}趋势分数排序了 {len(sorted_projects)} 个项目")
        return sorted_projects


class DiscordNotifier:
    """Discord消息推送器"""

    def __init__(self, webhook_url: Optional[str] = None, summarizer: Optional['ProjectSummarizer'] = None):
        self.webhook_url = webhook_url or os.getenv('DISCORD_WEBHOOK_URL')
        self.summarizer = summarizer or ProjectSummarizer()
        self.logger = logging.getLogger(__name__)

    def format_project_info(self, repo: Dict, rank: int) -> str:
        """格式化项目信息（包含智能总结）"""
        name = repo['name']
        stars = repo['stargazers_count']
        forks = repo['forks_count']
        url = repo['html_url']
        language = repo.get('language', 'Unknown')

        # 生成智能总结
        summary = self.summarizer.generate_summary(repo)

        # 限制总结长度，确保Discord消息不会太长
        if len(summary) > 120:
            summary = summary[:120] + '...'

        return f"{rank}. **{name}** - ⭐{stars:,} 🍴{forks:,} 📝{language}\n   💡 {summary}\n   [🔗 查看项目]({url})"

    def create_discord_embed(self, popular_projects: List[Dict], trending_projects: List[Dict], trend_timeframe: str = 'lifetime') -> Dict:
        """创建Discord Embed消息"""
        # 根据时间框架生成标题和描述
        timeframe_titles = {
            'lifetime': '最值得关注的AI开源项目',
            '30days': '最近30天上升最快的AI项目',
            '7days': '最近7天上升最快的AI项目'
        }

        trending_field_names = {
            'lifetime': '📈 趋势上升最快的AI项目',
            '30days': '📈 最近30天上升最快的AI项目',
            '7days': '🚀 最近7天上升最快的AI项目'
        }

        embed = {
            "title": "🤖 AI项目日报",
            "description": f"{datetime.now().strftime('%Y年%m月%d日')} {timeframe_titles.get(trend_timeframe, timeframe_titles['lifetime'])}",
            "color": 5814783,  # 蓝色
            "fields": [],
            "timestamp": datetime.now().isoformat()
        }

        # 添加热门项目
        if popular_projects:
            popular_text = "\n\n".join([
                self.format_project_info(repo, i+1)
                for i, repo in enumerate(popular_projects[:2])
            ])
            embed["fields"].append({
                "name": "⭐ 收藏最多的AI项目",
                "value": popular_text,
                "inline": False
            })

        # 添加趋势项目
        if trending_projects:
            trending_text = "\n\n".join([
                self.format_project_info(repo, i+1)
                for i, repo in enumerate(trending_projects[:2])
            ])
            embed["fields"].append({
                "name": trending_field_names.get(trend_timeframe, trending_field_names['lifetime']),
                "value": trending_text,
                "inline": False
            })

        return {"embeds": [embed]}

    def send_notification(self, popular_projects: List[Dict], trending_projects: List[Dict], trend_timeframe: str = 'lifetime') -> bool:
        """发送Discord通知"""
        if not self.webhook_url:
            self.logger.error("Discord Webhook URL未配置")
            return False

        payload = self.create_discord_embed(popular_projects, trending_projects, trend_timeframe)

        try:
            response = requests.post(self.webhook_url, json=payload)
            response.raise_for_status()
            self.logger.info("Discord消息发送成功")
            return True
        except requests.exceptions.RequestException as e:
            self.logger.error(f"Discord消息发送失败: {e}")
            return False

    def create_commercial_discord_embed(self, popular_projects: List[Dict], trending_projects: List[Dict], trend_timeframe: str = 'lifetime') -> Dict:
        """创建商用实用性AI项目的Discord Embed消息"""
        # 根据时间框架生成标题和描述
        timeframe_titles = {
            'lifetime': '最具商用价值的AI开源项目',
            '30days': '最近30天商用热门的AI项目',
            '7days': '最近7天商用爆火的AI项目'
        }

        trending_field_names = {
            'lifetime': '💼 商用趋势上升最快的AI项目',
            '30days': '💼 最近30天商用热门的AI项目',
            '7days': '🚀 最近7天商用爆火的AI项目'
        }

        embed = {
            "title": "💼 商用实用性AI项目日报",
            "description": f"{datetime.now().strftime('%Y年%m月%d日')} {timeframe_titles.get(trend_timeframe, timeframe_titles['lifetime'])}",
            "color": 3447003,  # 深蓝色，更商务感
            "fields": [],
            "timestamp": datetime.now().isoformat()
        }

        # 添加热门商用项目
        if popular_projects:
            popular_text = "\n\n".join([
                self.format_project_info(repo, i+1)
                for i, repo in enumerate(popular_projects[:2])
            ])
            embed["fields"].append({
                "name": "🏆 收藏最多的商用AI项目",
                "value": popular_text,
                "inline": False
            })

        # 添加商用趋势项目
        if trending_projects:
            trending_text = "\n\n".join([
                self.format_project_info(repo, i+1)
                for i, repo in enumerate(trending_projects[:2])
            ])
            embed["fields"].append({
                "name": trending_field_names.get(trend_timeframe, trending_field_names['lifetime']),
                "value": trending_text,
                "inline": False
            })

        # 添加商用价值说明
        embed["fields"].append({
            "name": "💡 商用价值说明",
            "value": "这些项目具有以下特点：\n• 🛠️ 即开即用的实用工具\n• 💰 明确的商业应用场景\n• 🔧 完善的部署和集成方案\n• 📈 活跃的社区和维护团队",
            "inline": False
        })

        return {"embeds": [embed]}

    def send_commercial_notification(self, popular_projects: List[Dict], trending_projects: List[Dict], trend_timeframe: str = 'lifetime') -> bool:
        """发送商用实用性AI项目Discord通知"""
        if not self.webhook_url:
            self.logger.error("Discord Webhook URL未配置")
            return False

        payload = self.create_commercial_discord_embed(popular_projects, trending_projects, trend_timeframe)

        try:
            response = requests.post(self.webhook_url, json=payload)
            response.raise_for_status()
            self.logger.info("商用项目Discord消息发送成功")
            return True
        except requests.exceptions.RequestException as e:
            self.logger.error(f"商用项目Discord消息发送失败: {e}")
            return False


class AIGitHubTracker:
    """AI GitHub追踪器主控制器"""

    def __init__(self):
        self.setup_logging()
        self.github_client = GitHubAPIClient()
        self.ai_filter = AIProjectFilter()
        self.commercial_filter = CommercialAIProjectFilter()
        self.deduplicator = ProjectDeduplicator()
        self.trend_analyzer = TrendAnalyzer()
        self.summarizer = ProjectSummarizer()
        self.notifier = DiscordNotifier(summarizer=self.summarizer)
        self.logger = logging.getLogger(__name__)

    def setup_logging(self):
        """设置日志"""
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            handlers=[
                logging.StreamHandler(),
                logging.FileHandler('ai_tracker.log', encoding='utf-8')
            ]
        )

    def run_daily_tracking(self, trend_timeframe: str = 'lifetime'):
        """
        执行每日追踪任务
        trend_timeframe: 'lifetime', '30days', '7days'
        """
        self.logger.info(f"开始执行AI GitHub项目每日追踪任务（趋势时间框架: {trend_timeframe}）")

        try:
            # 1. 清理旧记录
            self.deduplicator.clean_old_records()

            # 2. 获取项目数据
            self.logger.info("正在获取GitHub项目数据...")
            popular_repos = self.github_client.get_popular_ai_projects()
            trending_repos = self.github_client.get_trending_ai_projects()

            if not popular_repos and not trending_repos:
                self.logger.error("未能获取到任何项目数据")
                return

            # 3. AI项目过滤
            popular_ai_projects = self.ai_filter.filter_ai_projects(popular_repos)
            trending_ai_projects = self.ai_filter.filter_ai_projects(trending_repos)

            # 4. 去重过滤
            new_popular_projects = self.deduplicator.filter_new_projects(popular_ai_projects)
            new_trending_projects = self.deduplicator.filter_new_projects(trending_ai_projects)

            # 5. 趋势分析（使用指定的时间框架）
            trending_sorted = self.trend_analyzer.sort_by_trend_score(new_trending_projects, trend_timeframe)

            # 6. 选择要推送的项目
            selected_popular = new_popular_projects[:2]  # 前2个热门项目
            selected_trending = trending_sorted[:2]      # 前2个趋势项目

            if not selected_popular and not selected_trending:
                self.logger.info("没有发现新的AI项目，今日不推送")
                return

            # 7. 发送通知（传递时间框架信息）
            discord_success = self.notifier.send_notification(selected_popular, selected_trending, trend_timeframe)

            # 8. 标记项目为已推送（无论Discord是否成功）
            for project in selected_popular + selected_trending:
                self.deduplicator.mark_project_as_sent(project)

            if discord_success:
                self.logger.info(f"✅ 成功推送 {len(selected_popular)} 个热门项目和 {len(selected_trending)} 个趋势项目")
            else:
                self.logger.warning(f"⚠️ Discord消息发送失败，但已记录 {len(selected_popular)} 个热门项目和 {len(selected_trending)} 个趋势项目")

        except Exception as e:
            self.logger.error(f"执行追踪任务时发生错误: {e}")
            raise

    def run_multi_timeframe_tracking(self):
        """执行多时间框架追踪，分别推送30天和7天趋势"""
        timeframes = [
            ('30days', '📈 最近30天上升最快的AI项目'),
            ('7days', '🚀 最近7天上升最快的AI项目')
        ]

        for timeframe, description in timeframes:
            self.logger.info(f"执行{description}...")
            try:
                # 获取数据
                popular_repos = self.github_client.get_popular_ai_projects()
                trending_repos = self.github_client.get_trending_ai_projects()

                if not trending_repos:
                    continue

                # 过滤和去重
                trending_ai_projects = self.ai_filter.filter_ai_projects(trending_repos)
                new_trending_projects = self.deduplicator.filter_new_projects(trending_ai_projects)

                # 按指定时间框架排序
                trending_sorted = self.trend_analyzer.sort_by_trend_score(new_trending_projects, timeframe)
                selected_trending = trending_sorted[:2]

                if selected_trending:
                    # 发送通知
                    if self.notifier.send_notification([], selected_trending, timeframe):
                        for project in selected_trending:
                            self.deduplicator.mark_project_as_sent(project)
                        self.logger.info(f"成功推送{timeframe}趋势项目")

            except Exception as e:
                self.logger.error(f"执行{timeframe}追踪时发生错误: {e}")
                continue

    def run_commercial_tracking(self, trend_timeframe: str = 'lifetime'):
        """
        执行商用实用性AI项目追踪任务
        trend_timeframe: 'lifetime', '30days', '7days'
        """
        self.logger.info(f"开始执行商用实用性AI项目追踪任务（趋势时间框架: {trend_timeframe}）")
        try:
            # 1. 清理旧记录
            self.deduplicator.clean_old_records()

            # 2. 获取项目数据
            self.logger.info("正在获取GitHub项目数据...")
            popular_repos = self.github_client.get_popular_ai_projects()
            trending_repos = self.github_client.get_trending_ai_projects()

            if not popular_repos and not trending_repos:
                self.logger.error("未能获取到任何项目数据")
                return

            # 3. 商用实用性AI项目过滤
            popular_commercial_projects = self.commercial_filter.filter_commercial_ai_projects(popular_repos)
            trending_commercial_projects = self.commercial_filter.filter_commercial_ai_projects(trending_repos)

            # 4. 去重过滤
            new_popular_projects = self.deduplicator.filter_new_projects(popular_commercial_projects)
            new_trending_projects = self.deduplicator.filter_new_projects(trending_commercial_projects)

            # 5. 趋势分析（使用指定的时间框架）
            trending_sorted = self.trend_analyzer.sort_by_trend_score(new_trending_projects, trend_timeframe)

            # 6. 选择要推送的项目
            selected_popular = new_popular_projects[:2]  # 前2个热门商用项目
            selected_trending = trending_sorted[:2]      # 前2个商用趋势项目

            if not selected_popular and not selected_trending:
                self.logger.info("没有发现新的商用实用性AI项目，今日不推送")
                return

            # 7. 发送通知（使用商用项目专用格式）
            discord_success = self.notifier.send_commercial_notification(selected_popular, selected_trending, trend_timeframe)

            # 8. 标记项目为已推送（无论Discord是否成功）
            for project in selected_popular + selected_trending:
                self.deduplicator.mark_project_as_sent(project)

            if discord_success:
                self.logger.info(f"✅ 成功推送 {len(selected_popular)} 个热门商用项目和 {len(selected_trending)} 个商用趋势项目")
            else:
                self.logger.warning(f"⚠️ Discord消息发送失败，但已记录 {len(selected_popular)} 个热门商用项目和 {len(selected_trending)} 个商用趋势项目")

        except Exception as e:
            self.logger.error(f"执行商用项目追踪任务时发生错误: {e}")
            raise


def main():
    """主函数"""
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

    args = parser.parse_args()

    tracker = AIGitHubTracker()

    if args.reset:
        print("🔄 重置已推送项目记录...")
        tracker.deduplicator.reset_sent_projects()
        print("✅ 重置完成！下次运行将推送最热门的AI项目。")
        return

    if args.stats:
        stats = tracker.deduplicator.get_stats()
        print("📊 推送统计信息:")
        print(f"  已推送项目总数: {stats['total_sent']}")
        print(f"  最后推送时间: {stats['latest_sent'] or 'N/A'}")
        print(f"  存储文件: {stats['storage_file']}")
        return

    if args.commercial:
        # 执行商用实用性AI项目追踪
        tracker.run_commercial_tracking(args.trend_timeframe)
    elif args.multi_timeframe:
        # 执行多时间框架追踪
        tracker.run_multi_timeframe_tracking()
    else:
        # 执行常规追踪，使用指定的时间框架
        tracker.run_daily_tracking(args.trend_timeframe)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        import traceback
        print(f"❌ 程序执行失败: {e}")
        print("错误详情:")
        traceback.print_exc()
        exit(1)