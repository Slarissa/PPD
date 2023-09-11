// Importa as bibliotecas necessárias
var express = require('express'),

    app = express(),
    server = require('http').createServer(app).listen(4555), // Cria um servidor HTTP e o faz escutar na porta 4555
    io = require('socket.io').listen(server), // Cria uma instância do Socket.io e a conecta ao servidor
    bodyParser = require('body-parser'); // Biblioteca para análise do corpo das requisições
    router = require('./routes'); // Importa o arquivo de rotas
    emitir = require('./middleware')(io); // Passe a instância io como um argumento

// Configura o uso do bodyParser para analisar os corpos das requisições
app.use(bodyParser.urlencoded({
    extended: true
}));
app.use(bodyParser.json());

var port = process.env.PORT || 8080; // Define a porta padrão como 8080 caso não seja fornecida via variável de ambiente

app.use(emitir); // Utiliza o middleware de emissão de notificações
app.use('/api', router); // Define a rota base '/api' para o roteador

// Inicia o servidor na porta definida
app.listen(port);
console.log('Conectado à porta ' + port);