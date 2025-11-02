<?php
header('Content-Type: application/json');
header('Access-Control-Allow-Origin: *');

$file = isset($_GET['file']) ? $_GET['file'] : '';

// Sanitize the file path to prevent directory traversal
$file = str_replace(['../', '..\\'], '', $file);

if (empty($file) || !file_exists($file)) {
    http_response_code(404);
    echo json_encode(['error' => 'File not found']);
    exit;
}

$lastModified = filemtime($file);

echo json_encode([
    'lastModified' => $lastModified,
    'lastModifiedFormatted' => date('Y-m-d H:i:s', $lastModified)
]);
