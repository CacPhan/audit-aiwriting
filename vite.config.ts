import { defineConfig } from 'vitest/config';
import react from '@vitejs/plugin-react';
import { spawn } from 'child_process';
import path from 'path';

function pythonAuditApiPlugin() {
  return {
    name: 'python-audit-api-middleware',
    configureServer(server: any) {
      server.middlewares.use('/api/audit', (req: any, res: any) => {
        if (req.method === 'OPTIONS') {
          res.statusCode = 200;
          res.setHeader('Content-Type', 'application/json');
          res.end(JSON.stringify({ ok: true }));
          return;
        }

        const chunks: Buffer[] = [];
        req.on('data', (chunk: Buffer) => chunks.push(chunk));
        req.on('end', () => {
          const bodyStr = Buffer.concat(chunks).toString('utf-8');
          const scriptPath = path.resolve(process.cwd(), 'api', 'audit.py');
          const py = spawn('python', [scriptPath], {
            cwd: process.cwd(),
            env: { ...process.env, PYTHONIOENCODING: 'utf-8' },
          });

          const outChunks: Buffer[] = [];
          const errChunks: Buffer[] = [];

          py.stdout.on('data', (data: Buffer) => outChunks.push(data));
          py.stderr.on('data', (data: Buffer) => errChunks.push(data));

          py.on('close', (code: number) => {
            res.setHeader('Content-Type', 'application/json; charset=utf-8');
            if (code !== 0) {
              res.statusCode = 500;
              res.end(
                JSON.stringify({
                  error: 'Python audit engine execution failed',
                  details: Buffer.concat(errChunks).toString('utf-8'),
                })
              );
              return;
            }
            res.statusCode = 200;
            res.end(Buffer.concat(outChunks).toString('utf-8'));
          });

          if (req.method === 'POST' && bodyStr.trim()) {
            py.stdin.write(bodyStr, 'utf-8');
          }
          py.stdin.end();
        });
      });
    },
  };
}

export default defineConfig({
  plugins: [react() as any, pythonAuditApiPlugin()],
  test: {
    environment: 'jsdom',
    globals: true,
  },
});
