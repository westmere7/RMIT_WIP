# Configuration Guide

## config.txt

This file contains application settings that you can easily edit.

### Current Settings

```
VERSION=1.0.0
TEAM_NAME=VN Design Team
```

### How to Edit

1. Open `config.txt` in any text editor
2. Change the values after the `=` sign
3. Save the file
4. Reload the website - changes appear immediately!

### Settings Explained

**VERSION**
- Displayed in the footer as "v1.0.0"
- Update this when you make significant changes
- Format: `MAJOR.MINOR.PATCH` (e.g., `1.0.0`, `2.1.3`)

**TEAM_NAME** (Future use)
- Reserved for future feature
- Currently team name comes from Excel file (cell B1)
- May be used for override in future versions

### Examples

**Change version:**
```
VERSION=1.2.0
```

**Update team name (future):**
```
TEAM_NAME=Design Team GCMC
```

### Notes

- One setting per line
- Format: `SETTING_NAME=value`
- No spaces around the `=` sign
- File must be saved as plain text (UTF-8)
