# Server Setup for File Last-Modified Time

To display the correct last modified time of the Excel file, you need to run a local web server that sends proper file metadata.

## Option 1: Python Server (Recommended)

Run the included Python server that automatically includes Last-Modified headers:

```bash
python3 file-stats.py 8000
```

Then open: `http://localhost:8000/index.html`

## Option 2: PHP Server

If you have PHP installed:

```bash
php -S localhost:8000
```

Then open: `http://localhost:8000/index.html`

## Option 3: Node.js with http-server

Install and run http-server (automatically sends Last-Modified headers):

```bash
npx http-server -p 8000 -c-1
```

Then open: `http://localhost:8000/index.html`

## How It Works

The page will:
1. First try to read the `Last-Modified` header from the HTTP response
2. If that's not available, it will call the `/file-stats` endpoint (Python) or `file-stats.php` (PHP)
3. If neither work, it will fall back to the data in the Excel file

The Python server (`file-stats.py`) automatically adds Last-Modified headers to all file responses, so the page should work without any additional configuration.
