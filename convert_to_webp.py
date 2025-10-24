#!/usr/bin/env python3
"""
图片转WebP格式转换脚本
需要安装: pip install Pillow
使用方法: python convert_to_webp.py
"""

import os
import sys
from pathlib import Path
from PIL import Image

def convert_to_webp(input_path, output_path=None, quality=85):
    """
    将图片转换为WebP格式

    Args:
        input_path: 输入图片路径
        output_path: 输出路径（可选，默认为输入路径.webp）
        quality: WebP质量 (0-100，默认85)
    """
    try:
        if output_path is None:
            output_path = str(Path(input_path).with_suffix('.webp'))

        # 打开图片
        with Image.open(input_path) as img:
            # 转换为RGB模式（如果需要）
            if img.mode in ('RGBA', 'LA', 'P'):
                # 如果有透明通道，保持RGBA
                if img.mode == 'P' and 'transparency' in img.info:
                    img = img.convert('RGBA')
                else:
                    img = img.convert('RGB')

            # 保存为WebP
            img.save(output_path, 'WEBP', quality=quality, optimize=True)
            print(f"✅ 转换成功: {input_path} -> {output_path}")

            # 显示文件大小对比
            original_size = os.path.getsize(input_path)
            webp_size = os.path.getsize(output_path)
            reduction = (1 - webp_size / original_size) * 100
            print(f"📊 文件大小减少: {reduction:.1f}% ({original_size:,} -> {webp_size:,} bytes)")

    except Exception as e:
        print(f"❌ 转换失败: {input_path} - 错误: {e}")

def find_images_to_convert(directory):
    """
    查找目录中需要转换的图片文件

    Args:
        directory: 要搜索的目录

    Returns:
        list: 图片文件路径列表
    """
    image_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.tiff')
    image_files = []

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(image_extensions):
                file_path = os.path.join(root, file)
                # 检查是否已经有对应的WebP文件
                webp_path = str(Path(file_path).with_suffix('.webp'))
                if not os.path.exists(webp_path):
                    image_files.append(file_path)

    return image_files

def main():
    print("🎨 图片转WebP格式转换工具")
    print("=" * 40)

    # 检查当前目录中的图片
    current_dir = os.getcwd()

    # 查找博客配图文件夹
    blog_images_dir = os.path.join(current_dir, "blog配图")

    if os.path.exists(blog_images_dir):
        print(f"📁 搜索目录: {blog_images_dir}")
        image_files = []

        # 递归搜索所有子目录
        for root, dirs, files in os.walk(blog_images_dir):
            for file in files:
                if file.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp', '.tiff')):
                    file_path = os.path.join(root, file)
                    # 检查是否已经有对应的WebP文件
                    webp_path = str(Path(file_path).with_suffix('.webp'))
                    if not os.path.exists(webp_path):
                        image_files.append(file_path)

        if image_files:
            print(f"🖼️  找到 {len(image_files)} 个需要转换的图片:")
            for img in image_files:
                print(f"   - {os.path.relpath(img, blog_images_dir)}")

            # 询问是否继续
            response = input("\n是否开始转换? (y/n): ").lower().strip()
            if response in ['y', 'yes', '是']:
                print("\n🚀 开始转换...")
                for img_path in image_files:
                    convert_to_webp(img_path)
                print("\n✅ 所有转换完成!")
            else:
                print("❌ 取消转换")
        else:
            print("✅ 没有找到需要转换的图片")
    else:
        print(f"❌ 目录不存在: {blog_images_dir}")
        print("请确保在项目根目录运行此脚本")

    print("\n" + "=" * 40)
    print("💡 提示:")
    print("- 转换后的WebP文件将与原文件在同一目录")
    print("- 建议在上传到R2之前先转换图片")
    print("- 可以使用 quality 参数调整图片质量")

if __name__ == "__main__":
    main()