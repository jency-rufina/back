// filepath: f:\newapp\index.js
const { exec } = require('child_process');

exec('python -m uvicorn main:app --reload', (error, stdout, stderr) => {
  if (error) {
    console.error(`Error starting FastAPI: ${error.message}`);
    return;
  }
  if (stderr) {
    console.error(`FastAPI stderr: ${stderr}`);
    return;
  }
  console.log(`FastAPI stdout: ${stdout}`);
});