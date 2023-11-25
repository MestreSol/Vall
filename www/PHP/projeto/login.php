<!DOCTYPE html>
<html lang="pt-BR">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>

    <link rel="css" type="text/css" href="../css/login.css">
</head>

<body>
    <div class="container">
        <h2>Login</h2>
        <form>
            <div class="form-group">
                <label for="login">Email:</label>
                <input type="text" id="login" placeholder="Digite seu email">
            </div>
            <div class="form-group">
                <label for="senha">Senha:</label>
                <input type="password" id="senha" placeholder="Digite sua senha">
            </div>
            <div class="btn-container">
                <button type="submit" onclick="logar(); return false">Entrar</button>
            </div>
            <p class="note">Ainda não possui uma conta? <a href="experimente.html">Cadastre-se</a></p>
            <div class="error-message" id="error-message"></div>
        </form>
        <div class="footer">&copy; 2023 Sua Empresa. Todos os direitos reservados.</div>
    </div>

    <script>
        function logar() {
            var login = document.getElementById('login').value;
            var senha = document.getElementById('senha').value;
            var errorMessage = document.getElementById('error-message');

            if (login === "victor" && senha === "victor" ||
                login === "ana" && senha === "ana" ||
                login === "laura" && senha === "laura" ||
                login === "leo" && senha === "leo") {
                alert("Login bem-sucedido! Clique em OK para entrar.");
                location.href = "home.html";
            } else {
                errorMessage.innerHTML = "Usuário ou senha incorretos!";
            }
        }
    </script>
</body>

</html>