#!/bin/bash

# Script to add Google AdSense code to HTML files
# This script will process all files that don't have the AdSense code yet

ADSENSE_CODE='<!-- Google AdSense -->
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-6031811659039199"
     crossorigin="anonymous"></script>'

# List of files to process
files=(
    "./categories/birds.html"
    "./categories/characters/clowns.html"
    "./categories/characters/disney.html"
    "./categories/characters/fairy-tales.html"
    "./categories/characters/fantasy.html"
    "./categories/characters/gaming.html"
    "./categories/characters.html"
    "./categories/educational/geometry.html"
    "./categories/educational/puzzles.html"
    "./categories/educational/stationery.html"
    "./categories/educational.html"
    "./categories/food/apple-viewer.html"
    "./categories/food/cakes.html"
    "./categories/food/candy.html"
    "./categories/food/fast-food.html"
    "./categories/food/fruits.html"
    "./categories/food/ice-cream.html"
    "./categories/food/vegetables.html"
    "./categories/food.html"
    "./categories/holidays/christmas.html"
    "./categories/holidays/halloween/fireworks.html"
    "./categories/holidays/halloween.html"
    "./categories/holidays/summer.html"
    "./categories/holidays/thanksgiving.html"
    "./categories/holidays.html"
    "./categories/insects/bees.html"
    "./categories/insects/butterflies.html"
    "./categories/insects/other-bugs.html"
    "./categories/insects.html"
    "./categories/land-animals/farm-animals.html"
    "./categories/land-animals/wild-animals.html"
    "./categories/land-animals.html"
    "./categories/nature/flowers.html"
    "./categories/nature/natural-elements.html"
    "./categories/nature/trees.html"
    "./categories/nature.html"
    "./categories/ocean-animals/fish.html"
    "./categories/ocean-animals/mammals.html"
    "./categories/ocean-animals/sea-creatures.html"
    "./categories/ocean-animals.html"
    "./categories/sports/activities.html"
    "./categories/sports/index.html"
    "./categories/sports/sports-equipment.html"
    "./categories/sports/toys.html"
    "./categories/sports.html"
    "./categories/vehicles/air.html"
    "./categories/vehicles/airplanes.html"
    "./categories/vehicles/buses.html"
    "./categories/vehicles/cars.html"
    "./categories/vehicles/construction.html"
    "./categories/vehicles/emergency.html"
    "./categories/vehicles/helicopters.html"
    "./categories/vehicles/land.html"
    "./categories/vehicles/rockets.html"
    "./categories/vehicles/sea.html"
    "./categories/vehicles/ships.html"
    "./categories/vehicles/taxi.html"
    "./categories/vehicles/trains.html"
    "./categories/vehicles/trucks.html"
    "./categories/vehicles.html"
    "./color-by-number/animals/index.html"
    "./color-by-number/animals/lion.html"
    "./color-by-number/holidays/index.html"
    "./pdf-detail.html"
)

processed=0
failed=0

for file in "${files[@]}"; do
    if [ -f "$file" ]; then
        # Check if file already has AdSense code
        if grep -q "Google AdSense" "$file"; then
            echo "SKIP: $file already has AdSense code"
        else
            # Use sed to replace the pattern
            if sed -i.bak 's|</script>\n    <meta charset="UTF-8">|</script>\n\n<!-- Google AdSense -->\n<script async src="https:\/\/pagead2.googlesyndication.com\/pagead\/js\/adsbygoogle.js?client=ca-pub-6031811659039199"\n     crossorigin="anonymous\"><\/script>\n    <meta charset="UTF-8">|g' "$file"; then
                echo "SUCCESS: Added AdSense code to $file"
                ((processed++))
                # Remove backup file
                rm -f "$file.bak"
            else
                echo "ERROR: Failed to process $file"
                ((failed++))
            fi
        fi
    else
        echo "ERROR: File $file not found"
        ((failed++))
    fi
done

echo "========================================="
echo "Processing Complete!"
echo "Successfully processed: $processed files"
echo "Failed: $failed files"
echo "Total files in list: ${#files[@]}"
echo "========================================="