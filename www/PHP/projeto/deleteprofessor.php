<?php
    $id = $_GET['id'];

    $ch = curl_init();

    curl_setopt($ch, CURLOPT_URL, 'http://127.0.0.1:5000/professor/' . $id);
    curl_setopt($ch, CURLOPT_CUSTOMREQUEST, 'DELETE');

    $response = curl_exec($ch);

    if (curl_errno($ch)) {
        echo 'Erro:' . curl_error($ch);
    }
    else{
        header('Location: users.php');
    }
?>