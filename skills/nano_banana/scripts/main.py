#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Real AI Logic for nano banana skill - Quizhi Project
"""
import os
import sys
import time
from datetime import datetime

def generate_banana_pic(prompt):
    print(f"🎨 正在为您创作 '{prompt}'... (Creating your art: {prompt}...)")
    
    # Check for API Key
    api_key = os.getenv("GOOGLE_API_KEY") or os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("\n⚠️  错误: 未找到 API Key。 (Error: API Key not found.)")
        print("请在终端运行: export GOOGLE_API_KEY='您的KEY'")
        return

    try:
        from google import genai
        from google.genai import types
    except ImportError:
        print("\n❌ 错误: 未安装 google-genai 库。 (Error: google-genai not installed.)")
        print("请运行: pip install google-genai")
        return

    print("🧠 正在启动 Gemini 图像引擎... (Starting Gemini Image Engine...)")
    client = genai.Client(api_key=api_key)
    
    # Enrich the prompt with the "Nano Banana" theme
    full_prompt = f"A futuristic, tech-heavy 'Nano Banana' art piece. {prompt}. Hyper-realistic, 8k resolution, cinematic lighting, 3D render style, neon accents, tropical cyberpunk vibe."
    
    # Create output directory
    # We want it in the project root's output folder
    script_dir = os.path.dirname(os.path.abspath(__file__))
    root_dir = os.path.abspath(os.path.join(script_dir, "../../../"))
    output_dir = os.path.join(root_dir, "output")
    os.makedirs(output_dir, exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"nano_banana_{timestamp}.png"
    output_path = os.path.join(output_dir, filename)

    try:
        print("🚀 正在生成高科技图像 (这可能需要 30-60 秒)...")
        print(f"📝 Prompt: {full_prompt[:100]}...")
        
        # Call the real Image Generation API
        # Using imagen-3.0-generate-001 (standard for Imagen 3)
        response = client.models.generate_image(
            model='imagen-3.0-generate-001',
            prompt=full_prompt,
            config=types.GenerateImageConfig(
                number_of_images=1,
                include_rai_reasoning=True,
                output_mime_type='image/png'
            )
        )
        
        # Save the image
        for i, generated_image in enumerate(response.generated_images):
            with open(output_path, "wb") as f:
                f.write(generated_image.image.image_bytes)
        
        print(f"\n✨ 创作成功！ (Creation success!)")
        print(f"🖼️  图像已保存为: output/{filename}")
        print(f"🔗 完整路径: {output_path}")
        
    except Exception as e:
        print(f"\n❌ AI 创作中断 (AI failed): {e}")
        if "429" in str(e):
            print("💡 提示: API 额度已用完，请稍后再试或更换 API Key。")

if __name__ == "__main__":
    p = "Tropical Tech Fusion"
    if len(sys.argv) > 1:
        p = sys.argv[1]
    
    print("\n" + "═"*60)
    print("🍌 秋芝纳米香蕉艺术中心 (Quizhi Nano Banana Art Center) - V2.0")
    print("═"*60)
    generate_banana_pic(p)
