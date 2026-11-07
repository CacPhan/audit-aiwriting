"""
Vercel Python Serverless Function Endpoint: GET & POST /api/audit
Also runnable as a CLI helper for local Vite development middleware.
"""

from http.server import BaseHTTPRequestHandler
import json
from pathlib import Path
import sys
from typing import Any, Dict

_PROJECT_ROOT = str(Path(__file__).resolve().parent.parent)
if _PROJECT_ROOT not in sys.path:
    sys.path.insert(0, _PROJECT_ROOT)

from api.engine.auditor import SAMPLE_THESIS_PAYLOAD, audit_document_sections
from api.engine.lexicon import RULE_METADATA


def evaluate_audit_request(payload: Any) -> Dict[str, Any]:
    """Evaluates a JSON payload containing `{title, sections}` and returns the full audit result."""
    if not isinstance(payload, dict):
        payload = {}
    title = payload.get("title") or SAMPLE_THESIS_PAYLOAD["title"]
    if "sections" in payload and isinstance(payload["sections"], list):
        sections = payload["sections"]
    elif "sections" in payload and payload["sections"] is None:
        sections = []
    else:
        sections = SAMPLE_THESIS_PAYLOAD["sections"]
    return audit_document_sections(title, sections)


class handler(BaseHTTPRequestHandler):
    """Vercel Python Serverless Function HTTP Handler."""

    def _send_json(self, status_code: int, data: Dict[str, Any]) -> None:
        body = json.dumps(data, ensure_ascii=False).encode("utf-8")
        self.send_response(status_code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_OPTIONS(self) -> None:
        self._send_json(200, {"ok": True})

    def do_GET(self) -> None:
        result = evaluate_audit_request(SAMPLE_THESIS_PAYLOAD)
        result["rulesCatalog"] = RULE_METADATA
        self._send_json(200, result)

    def do_POST(self) -> None:
        try:
            content_length = int(self.headers.get("Content-Length", "0"))
            raw_body = self.rfile.read(content_length).decode("utf-8") if content_length > 0 else "{}"
            payload = json.loads(raw_body) if raw_body.strip() else {}
            result = evaluate_audit_request(payload)
            self._send_json(200, result)
        except Exception as exc:
            self._send_json(400, {"error": f"Invalid audit request payload: {str(exc)}"})


if __name__ == "__main__":
    # Supports local Vite dev server bridge via stdin/stdout JSON (UTF-8 safe on Windows & Unix)
    raw_in = sys.stdin.buffer.read().decode("utf-8")
    req_data = json.loads(raw_in) if raw_in.strip() else SAMPLE_THESIS_PAYLOAD
    out = evaluate_audit_request(req_data)
    sys.stdout.buffer.write(json.dumps(out, ensure_ascii=False).encode("utf-8"))
