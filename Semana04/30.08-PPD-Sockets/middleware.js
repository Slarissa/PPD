var emitir = function (io) { // Recebe io como um argumento
// Middleware para emitir notificações via Socket.io
    return function (req, res, next) {
        var notificar = req.query.notificacao || '';
        if (notificar != '') {
            io.emit('notificacao', notificar); // Emite uma notificação via Socket.io
            next(); // Passa para o próximo middleware
        } else {
            next(); // Passa para o próximo middleware
        }
    }
}
module.exports = emitir;