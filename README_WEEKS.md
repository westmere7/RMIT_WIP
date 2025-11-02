# Adding New Weekly Reports

## Quick Start - Maximum Speed (Instant Loading!)

### Simple Workflow
**Every time you add a new file:**

1. Add `WXX_YYYY.xlsx` to the `data/reports/` folder
2. Run the generator script:
   ```bash
   python3 generate_weeks_list.py
   ```
3. Reload the website - file appears instantly!

**File naming format:** `WXX_YYYY.xlsx` (week with 2 digits, year with 4 digits)

Examples:
- `W45_2025.xlsx`
- `W46_2025.xlsx`
- `W01_2026.xlsx`
- `W48_2026.xlsx`

### Why This Approach?

**Instant loading:**
- No file searching at all
- Just loads JSON manifest (milliseconds)
- Works for any year
- 100% reliable

**Previous approaches:**
- ? Check all years: 693 files = slow
- ? Check 2025 only: 99 files = faster but still searches
- ? **No searching: 0 files checked = instant!**

### Trade-off
- **Speed**: Maximum possible (instant)
- **Automation**: One script run per file
- **Worth it**: Yes! Page loads instantly every time

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

## Status Types

The following status badges are supported:
- **Done** - Completed tasks (green)
- **Review** / **In Review** - Awaiting review (amber)
- **WIP** / **In Progress** - Work in progress (blue)
- **Updating** - Being updated (purple)
- **Blocked** - Cannot proceed (red)
- **On Hold** - Paused (RMIT red)
- **To Do** - Not started (violet)

## File Structure

```
data/
??? reports/           # Put weekly report files here
?   ??? W47_2025.xlsx
?   ??? W48_2025.xlsx
?   ??? W48_2026.xlsx
??? weeks.json         # Generated manifest (don't edit manually)
??? RMIT_logo_white.svg
```

## Troubleshooting

**Q: I added a new file but it doesn't show up**
- Did you put it in `data/reports/` folder?
- Did you run `python3 generate_weeks_list.py`?
- Make sure the filename follows the exact format: `WXX_YYYY.xlsx`
- Check the browser console (F12) for any errors
- Hard reload the page (Ctrl+Shift+R or Cmd+Shift+R)

**Q: The page loads slowly**
- This shouldn't happen! The page loads instantly from manifest
- Check browser console for errors
- Make sure `data/weeks.json` exists

**Q: Can I add files without running the script?**
- No - for maximum speed, auto-discovery is disabled
- Running the script takes 1 second and ensures instant page loads

## Need Help?

Check the browser console (F12) for diagnostic messages:
- `Loaded X weeks from manifest` - Success!
- `To add new files, run: python3 generate_weeks_list.py` - Reminder message
