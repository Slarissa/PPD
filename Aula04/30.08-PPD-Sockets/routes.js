var express = require('express');
var router = express.Router();

// Rota para receber notificações
router.route('/notificar')
    .get(function (req, res) {
        // Responde com uma mensagem JSON
        res.json({
            message: "testando essa rota"
        });
    });

module.exports = router;

