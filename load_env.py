#!/usr/bin/env python3
"""
简单的.env文件加载器
"""
import os

def load_env(env_file='.env'):
    """加载.env文件中的环境变量"""
    if not os.path.exists(env_file):
        return

    with open(env_file, 'r') as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#') and '=' in line:
                key, value = line.split('=', 1)
                os.environ[key.strip()] = value.strip()