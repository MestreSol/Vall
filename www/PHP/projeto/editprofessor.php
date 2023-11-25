<?php
    if($_SERVER['REQUEST_METHOD'] === 'POST'){
        $id = $_GET['id'];

        $nome = $_POST['nome'];
        $telefone = $_POST['telefone'];
        $email = $_POST['email'];
        $CPF = $_POST['CPF'];
        $CEP = $_POST['CEP'];

        $data = array(
            'nome' => $nome,
            'telefone' => $telefone,
            'email' => $email,
            'cpf' => $CPF,
            'cep' => $CEP
        );
        
        $options = array(
            'http' => array(
                'header'  => "Content-Type: application/json\r\n",
                'method'  => 'PUT',
                'content' => json_encode($data)
            )
        );

        $ch = curl_init();

        $context  = stream_context_create($options);
        $result = file_get_contents('http://127.0.0.1:5000/professor/' . $id, false, $context);


        if($result === FALSE){
            echo 'Erro ao editar.';
        }
        else{
            header('Location: users.php');
        }
    }
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="../css/bootstrap/css/bootstrap.css">
    <title>Document</title>
</head>
<body>
    <div class="container">

        <?php
            $ch = curl_init();
    
            curl_setopt($ch, CURLOPT_URL, 'http://127.0.0.1:5000/professor/'.$_GET['id']);
            curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
    
            $response = curl_exec($ch);
    
            if (curl_errno($ch)) {
                echo 'Erro:' . curl_error($ch);
            }
    
            curl_close($ch);
    
            $professor = json_decode($response, true);
            echo '
                <form method="post">
                    <div class="mb-3">
                        <label for="nome" class="form-label">Nome</label>
                        <input type="text" class="form-control" id="nome" name="nome" value="' . $professor['nome'] . '">
                    </div>
                    <div>
                        <label for="telefone" class="form-label">Telefone</label>
                        <input type="text" id="nome" class="form-control" name="telefone" value="' . $professor['telefone'] . '">
                    </div>
                    <div>
                        <label for="email" class="form-label">Email</label>
                        <input type="text" name="email" class="form-control" value="' . $professor['email'] . '">
                    </div>
                    <div>
                        <label for="CPF" class="form-label">CPF</label>
                        <input type="text" name="CPF" class="form-control" value="' . $professor['cpf'] . '">
                    </div>
                    <div>
                        <label for="CEP" class="form-label">CEP</label>
                        <input type="text" name="CEP" class="form-control" value="' . $professor['cep'] . '">
                    </div>
                    <input class="form-control btn btn-primary" type="submit" value="Enviar">
                </form>
            ';
        ?>
</body>
</html>
</div>