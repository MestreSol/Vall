<?php
    header("Access-Control-Allow-Origin: *");
    header("Access-Control-Allow-Methods: GET, POST, PUT, DELETE");
    header("Access-Control-Allow-Headers: Content-Type");
    session_start();
?>
<?php
if($_SERVER['REQUEST_METHOD'] == "POST"){
    $login = isset($_POST['login']) ? $_POST['login'] : '';
    $senha = isset($_POST['senha']) ? $_POST['senha'] : '';

    $errors = [];

    if(empty($login)){
        $errors[] = 'Login é obrigatório.';
    }

    if(empty($senha)){
        $errors[] = 'Senha é obrigatório.';
    }

    if(empty($errors)){
        $data = array(
            'login' => $login,
            'senha' => $senha
        );

        $options = array(
            'http' => array(
                'header'  => "Content-Type: application/json\r\n",
                'method'  => 'GET',
                'content' => json_encode($data)
            )
        );

        $context  = stream_context_create($options);
        $result = file_get_contents('http://localhost:5000/Login/'.$login.'/'.$senha, false, $context);

        if ($result === FALSE) {
            echo "Erro ao logar.";
        }
        else{
            echo $result;
        }

        

}
}
?>
<!DOCTYPE html>
<html lang="pt-BR">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>

    <!-- CSS -->
    <link rel="stylesheet" href="../css/login.css">
</head>

<body>
    <div class="container">
        <h2>Login</h2>
        <form id="loginForm" method="post">
            <div class="form-group">
                <label for="login">Email:</label>
                <input type="text" id="login" name="login" placeholder="Digite seu email">
            </div>
            <div class="form-group">
                <label for="senha">Senha:</label>
                <input type="password" id="senha" name="senha" placeholder="Digite sua senha">
            </div>
            <div class="btn-container">
                <button type="submit" onclick="logar(); return false">Entrar</button>
            </div>
            <div class="error-message" id="error-message"></div>
        </form>
        <p class="note">Ainda não possui uma conta? <a href="MatriculaProfessor.php">Cadastre-se</a></p>
        <div class="footer">&copy; 2023 Sua Empresa. Todos os direitos reservados.</div>
    </div>

    
</body>

</html>