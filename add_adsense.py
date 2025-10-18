#!/usr/bin/env python3
import os
import glob

def add_adsense_to_file(file_path):
    """Add Google AdSense code to HTML file if not already present"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Check if AdSense code already exists
        if 'Google AdSense' in content:
            print(f"SKIP: {file_path} already has AdSense code")
            return False

        # Define the pattern to find and replacement
        old_pattern = '</script>\n    <meta charset="UTF-8">'
        new_pattern = '''</script>

<!-- Google AdSense -->
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-6031811659039199"
     crossorigin="anonymous"></script>
    <meta charset="UTF-8">'''

        # Replace the pattern
        if old_pattern in content:
            new_content = content.replace(old_pattern, new_pattern)

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

def main():
    # List of files that still need AdSense code
    files_to_process = [
        "categories/characters/clowns.html",
        "categories/characters/disney.html",
        "categories/characters/fairy-tales.html",
        "categories/characters/fantasy.html",
        "categories/characters/gaming.html",
        "categories/characters.html",
        "categories/educational/geometry.html",
        "categories/educational/puzzles.html",
        "categories/educational/stationery.html",
        "categories/educational.html",
        "categories/food/apple-viewer.html",
        "categories/food/cakes.html",
        "categories/food/candy.html",
        "categories/food/fast-food.html",
        "categories/food/fruits.html",
        "categories/food/ice-cream.html",
        "categories/food/vegetables.html",
        "categories/food.html",
        "categories/holidays/christmas.html",
        "categories/holidays/halloween/fireworks.html",
        "categories/holidays/halloween.html",
        "categories/holidays/summer.html",
        "categories/holidays/thanksgiving.html",
        "categories/holidays.html",
        "categories/insects/bees.html",
        "categories/insects/butterflies.html",
        "categories/insects/other-bugs.html",
        "categories/insects.html",
        "categories/land-animals/farm-animals.html",
        "categories/land-animals/wild-animals.html",
        "categories/land-animals.html",
        "categories/nature/flowers.html",
        "categories/nature/natural-elements.html",
        "categories/nature/trees.html",
        "categories/nature.html",
        "categories/ocean-animals/fish.html",
        "categories/ocean-animals/mammals.html",
        "categories/ocean-animals/sea-creatures.html",
        "categories/ocean-animals.html",
        "categories/sports/activities.html",
        "categories/sports/index.html",
        "categories/sports/sports-equipment.html",
        "categories/sports/toys.html",
        "categories/sports.html",
        "categories/vehicles/air.html",
        "categories/vehicles/airplanes.html",
        "categories/vehicles/buses.html",
        "categories/vehicles/cars.html",
        "categories/vehicles/construction.html",
        "categories/vehicles/emergency.html",
        "categories/vehicles/helicopters.html",
        "categories/vehicles/land.html",
        "categories/vehicles/rockets.html",
        "categories/vehicles/sea.html",
        "categories/vehicles/ships.html",
        "categories/vehicles/taxi.html",
        "categories/vehicles/trains.html",
        "categories/vehicles/trucks.html",
        "categories/vehicles.html",
        "color-by-number/animals/index.html",
        "color-by-number/animals/lion.html",
        "color-by-number/holidays/index.html",
        "pdf-detail.html"
    ]

    processed = 0
    failed = 0

    for file_path in files_to_process:
        full_path = os.path.join(os.getcwd(), file_path)
        if os.path.exists(full_path):
            if add_adsense_to_file(full_path):
                processed += 1
            else:
                failed += 1
        else:
            print(f"ERROR: File {file_path} not found")
            failed += 1

    print("\n" + "="*50)
    print("Processing Complete!")
    print(f"Successfully processed: {processed} files")
    print(f"Failed: {failed} files")
    print(f"Total files in list: {len(files_to_process)}")
    print("="*50)

if __name__ == "__main__":
    main()