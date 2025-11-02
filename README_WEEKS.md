# Adding New Weekly Reports

## Quick Start

### Option 1: Automatic Discovery (Recommended)
The system now **automatically discovers** weekly report files! Just add your files to the `data/` folder with the correct naming format and reload the page.

**File naming format:** `W{week}_{year}.xlsx`

Examples:
- `W45_2025.xlsx` ? Week 45, 2025
- `W46_2025.xlsx` ? Week 46, 2025  
- `W01_2026.xlsx` ? Week 1, 2026

### Option 2: Using the Manifest File (Faster Loading)
For better performance with many files, update the manifest:

1. Add your new weekly report files to the `data/` folder
2. Run the generator script:
   ```bash
   python3 generate_weeks_list.py
   ```
3. Reload the website - your new weeks will appear in the dropdown!

## File Format Requirements

### Excel File Structure
Your weekly report Excel files should follow this structure:

**Row 1 (Metadata):**
- **A1**: Timeline with parentheses, e.g., `(4-11 Nov 2025)`
- **B1**: Team name, e.g., `VN Design Team`
- **C1**: Last updated timestamp, e.g., `Last updated: 11 Nov 2025, 5:00 PM`
- **D1**: Team load percentage, e.g., `85%`

**Row 2 (Headers):**
- Column A: Campaign
- Column B: Task
- Column C: PIC (Person in Charge)
- Column D: Status
- Column E: Details

**Row 3+** (Data rows):
Each row contains one task with the corresponding information.

### Example:
```
| A (Campaign)      | B (Task)          | C (PIC) | D (Status)    | E (Details)              |
|-------------------|-------------------|---------|---------------|--------------------------|
| (4-11 Nov 2025)   | VN Design Team    | Last... | 85%           |                          |
| Campaign          | Task              | PIC     | Status        | Details                  |
| Website Redesign  | Homepage mockup   | Alice   | Done          | Desktop and mobile       |
| Mobile App        | UI components     | Charlie | In Progress   | Button styles complete   |
```

## How It Works

1. **Automatic Discovery**: The system checks for files named `W{week}_{year}.xlsx` in weeks 30-52 of 2025
2. **Manifest Loading**: Loads from `data/weeks.json` if available
3. **Fallback**: Uses default W45 and W46 if nothing else is found

## Status Types

The following status badges are supported:
- **Done** - Completed tasks (green)
- **Review** / **In Review** - Awaiting review (amber)
- **WIP** / **In Progress** - Work in progress (blue)
- **Updating** - Being updated (purple)
- **Blocked** - Cannot proceed (red)
- **On Hold** - Paused (RMIT red)
- **To Do** - Not started (violet)

## Troubleshooting

**Q: I added a new file but it doesn't show up**
- Make sure the filename follows the exact format: `W{week}_{year}.xlsx`
- Run `python3 generate_weeks_list.py` to regenerate the manifest
- Check the browser console (F12) for any errors
- Hard reload the page (Ctrl+Shift+R or Cmd+Shift+R)

**Q: The auto-discovery is slow**
- Run `python3 generate_weeks_list.py` to create a manifest file
- This makes loading instant instead of checking for each week

**Q: I need weeks from a different year**
- Edit the year range in `index.html` around line 942
- Or simply add files and run the generator script

## Need Help?

Check the browser console (F12) for diagnostic messages:
- `Loaded X weekly reports from manifest` - Manifest loaded successfully
- `Auto-discovered X additional weekly reports` - Found extra files
- `weeks.json not found, using fallback list` - No manifest, using defaults
