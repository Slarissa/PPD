
const { Worker, isMainThread, parentPort, workerData } = require('worker_threads');

function executarTarefa(tarefaId) {
 
  const tempo = Math.random() * 2000 + 1000;
  console.log(`Thread ${tarefaId} Iniciou a tarefa...`);
  setTimeout(() => {
    console.log(`Thread ${tarefaId} Tarefa Concluida!`);
    parentPort.postMessage({ tarefaId, tempo });
  }, tempo);
}

if (isMainThread) {
  const numThreads = 4;

  const resultado = [];

  function handleWorkerMessage(message) {
    resultado.push(message);

    if (resultado.length === numThreads) {
      console.log('\nTempo de conclusão das Threads:');
      resultado.sort((a, b) => a.tarefaId - b.tarefaId);
      resultado.forEach(result => {
        console.log(`\nThread ${result.tarefaId} - Tempo: ${result.tempo.toFixed(2)}ms`);
      });
    }
  }

  for (let i = 0; i < numThreads; i++) {
    const worker = new Worker(__filename, { workerData: i });
    worker.on('message', handleWorkerMessage);
  }
} else {
  const tarefaId = workerData;
  executarTarefa(tarefaId);
}