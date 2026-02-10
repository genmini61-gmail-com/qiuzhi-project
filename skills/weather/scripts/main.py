#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Real Logic for weather skill - Quizhi Project
"""
import sys
import urllib.request
import urllib.parse

def get_weather(location):
    print(f"🔍 正在查询 {location} 的天气... (Searching weather for {location}...)")
    try:
        # Use wttr.in for real weather data (no API key needed)
        # ?format=3 for single line or ?m for metric
        safe_location = urllib.parse.quote(location)
        url = f"https://wttr.in/{safe_location}?m&lang=zh-cn"
        
        # We'll get the full ASCII art version for the "wow" factor
        headers = {'User-Agent': 'curl/7.64.1'}
        req = urllib.request.Request(url, headers=headers)
        
        with urllib.request.urlopen(req, timeout=10) as response:
            data = response.read().decode('utf-8')
            print("\n" + "="*60)
            print(data)
            print("="*60)
            print("\n✅ 查询完成！ (Query complete!)")
    except Exception as e:
        print(f"\n❌ 查询失败 (Query failed): {e}")

if __name__ == "__main__":
    loc = "Beijing"
    if len(sys.argv) > 1:
        loc = sys.argv[1]
    
    print("🌤️  秋芝天气助手 (Quizhi Weather Assistant)")
    get_weather(loc)
