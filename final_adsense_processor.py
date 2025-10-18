#!/usr/bin/env python3
import os
import re

def add_adsense_to_file(file_path):
    """Add Google AdSense code to HTML file if not already present"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Check if AdSense code already exists
        if 'Google AdSense' in content:
            print(f"SKIP: {file_path} already has AdSense code")
            return False

        # Define the pattern to find and replacement using regex for more flexible matching
        # Look for the closing script tag followed by whitespace and meta charset
        pattern = r'</script>\s*\n\s*<meta charset="UTF-8">'
        replacement = '''</script>

<!-- Google AdSense -->
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-6031811659039199"
     crossorigin="anonymous"></script>
    <meta charset="UTF-8">'''

        # Replace the pattern
        new_content = re.sub(pattern, replacement, content)

        if new_content != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"SUCCESS: Added AdSense code to {file_path}")
            return True
        else:
            print(f"ERROR: Pattern not found in {file_path}")
            return False

    except Exception as e:
        print(f"ERROR processing {file_path}: {str(e)}")
        return False

def get_remaining_files():
    """Get list of HTML files that don't have AdSense code yet"""
    html_files = []
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    if 'Google AdSense' not in content:
                        html_files.append(file_path)
                except:
                    pass
    return html_files

def main():
    print("Starting final Google AdSense insertion process...")
    print("=" * 60)

    # Get all files that still need AdSense code
    files_to_process = get_remaining_files()

    print(f"Found {len(files_to_process)} files that need AdSense code")
    print()

    processed = 0
    failed = 0

    for file_path in files_to_process:
        if add_adsense_to_file(file_path):
            processed += 1
        else:
            failed += 1

        # Progress indicator
        if (processed + failed) % 10 == 0:
            print(f"Progress: {processed + failed}/{len(files_to_process)} files processed")

    print("\n" + "="*60)
    print("Processing Complete!")
    print(f"Successfully processed: {processed} files")
    print(f"Failed: {failed} files")
    print(f"Total files processed: {processed + failed}")
    print("="*60)

    # Final verification
    print("\nRunning final verification...")
    total_html = 0
    with_adsense = 0
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith('.html'):
                total_html += 1
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    if 'Google AdSense' in content:
                        with_adsense += 1
                except:
                    pass

    print(f"Final verification:")
    print(f"Total HTML files: {total_html}")
    print(f"Files with AdSense: {with_adsense}")
    print(f"Files still missing AdSense: {total_html - with_adsense}")

if __name__ == "__main__":
    main()