#!/usr/bin/env python3
"""
Auto-generate weeks.json manifest for available weekly reports
Scans data directory for WXX_YYYY.xlsx files (any week 1-99, any year)

Usage:
    python3 generate_weeks_list.py

After adding new weekly report files, run this script to update data/weeks.json
The website will automatically load the updated list on next page load.

Note: The website can auto-discover files on its own, but using this script
provides instant loading instead of checking each possible filename.
"""
import os
import re
import json

# Scan data directory for weekly report files
data_dir = 'data'
week_pattern = re.compile(r'W(\d{2})_(\d{4})\.xlsx')

available_weeks = []
for filename in sorted(os.listdir(data_dir)):
    match = week_pattern.match(filename)
    if match:
        week_num = int(match.group(1))
        year = int(match.group(2))
        available_weeks.append({
            'file': filename,
            'week': week_num,
            'year': year
        })

# Sort by year and week
available_weeks.sort(key=lambda x: (x['year'], x['week']))

if len(available_weeks) == 0:
    print("??  No weekly report files found!")
    print("   Add files with format: W{week}_{year}.xlsx")
    print("   Example: W45_2025.xlsx")
    exit(1)

print(f"? Found {len(available_weeks)} weekly report files:")
for w in available_weeks:
    print(f"   - {w['file']} (Week {w['week']}, {w['year']})")

# Save as JSON manifest
output_file = 'data/weeks.json'
with open(output_file, 'w') as f:
    json.dump(available_weeks, f, indent=2)

print(f"\n? Saved to {output_file}")
print(f"   The website will automatically load these {len(available_weeks)} weeks on next page refresh.")
print("\n?? Tip: Run this script whenever you add new weekly report files!")
