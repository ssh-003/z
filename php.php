<?php
function get_input($prompt) {
    echo $prompt;
    return trim(fgets(STDIN));
}

$server_url = get_input("http://192.168.1.3:8080 ~/$ ");

// Check connection
$connect_url = $server_url . '/connect';
$connect_response = file_get_contents($connect_url);
$connect_data = json_decode($connect_response, true);

if ($connect_data['status'] === 'connected') {
    echo "Connected: " . $connect_data['message'] . "\n";
    while (true) {
        $command = get_input("'~/$ ");
        if (strtolower($command) === 'exit') {
            break;
        }
        $url = $server_url . '/' . urlencode($command);
        $response = file_get_contents($url);
        $data = json_decode($response, true);

        echo $data['output'] . "\n";
    }
} else {
    echo "Failed to connect to the server.\n";
}
?>