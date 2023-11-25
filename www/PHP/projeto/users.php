<?php
$ch = curl_init();

curl_setopt($ch, CURLOPT_URL, 'http://127.0.0.1:5000/professor');
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);

$response = curl_exec($ch);

if (curl_errno($ch)) {
    echo 'Erro:' . curl_error($ch);
}

curl_close($ch);

$users = json_decode($response, true);
#echo $response;
?>
<html>
    <head>
        <title>Admin</title>
        <link rel="stylesheet" href="../css/bootstrap/css/bootstrap.css">
    </head>
    <body>
        <div class="container">
            <h1>Professores</h1>
            <table class="table table-striped">
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>Nome</th>
                        <th>Instituição</th>
                        <th>Action</th>
                    </tr>
                </thead>
                <tbody>
                    <?php foreach ($users as $user): ?>
                        <tr>
                            <td><?php echo $user['id_professor']; ?></td>
                            <td><?php echo $user['nome']; ?></td>
                            <td><?php echo $user['instituicao']; ?></td>
                            <td>
                                <a href="editprofessor.php?id=<?php echo $user['id_professor']; ?>" class="btn btn-primary">Editar</a>
                                <a href="deleteprofessor.php?id=<?php echo $user['id_professor']; ?>" class="btn btn-danger">Excluir</a>
                            </td>
                        </tr>
                    <?php endforeach; ?>
                </tbody>
            </table>
        </div>
    </body>
</html>