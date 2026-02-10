#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Real Logic for weather skill - Quizhi Project
"""
import sys
import urllib.request
import urllib.parse
import json

def get_weather(location):
    print(f"🔍 正在查询 {location} 的天气... (Searching weather for {location}...)")
    
    # Expanded city to coord map
    coords = {
        "beijing": (39.9042, 116.4074),
        "shanghai": (31.2304, 121.4737),
        "guangzhou": (23.1291, 113.2644),
        "shenzhen": (22.5431, 114.0579),
        "la": (34.0522, -118.2437),
        "los angeles": (34.0522, -118.2437),
        "sydney": (-33.8688, 151.2093),
        "new york": (40.7128, -74.0060),
        "london": (51.5074, -0.1278),
        "tokyo": (35.6895, 139.6917),
        "paris": (48.8566, 2.3522),
        "hong kong": (22.3193, 114.1694)
    }
    
    loc_key = location.lower().strip()
    lat, lon = coords.get(loc_key, (39.9042, 116.4074)) # Default to Beijing
    
    try:
        # Use Xray HTTP Proxy (10809)
        proxy_handler = urllib.request.ProxyHandler({
            'http': 'http://127.0.0.1:10809',
            'https': 'http://127.0.0.1:10809'
        })
        opener = urllib.request.build_opener(proxy_handler)
        urllib.request.install_opener(opener)

        # Use Open-Meteo API (Proven to work via proxy)
        url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
        
        with urllib.request.urlopen(url, timeout=10) as response:
            res_data = json.loads(response.read().decode('utf-8'))
            cw = res_data.get('current_weather', {})
            
            print("\n" + "🌤️" + "="*58)
            print(f"  地点 (Location): {location.upper()}")
            print(f"  气温 (Temp):     {cw.get('temperature')} °C")
            print(f"  风速 (Wind):     {cw.get('windspeed')} km/h")
            print(f"  时间 (Time):     {cw.get('time')}")
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
