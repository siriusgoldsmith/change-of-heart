"""Vercel Python entrypoint for the hosted Change of Heart web build."""
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
os.environ.setdefault("COH_WEB_DEPLOY", "1")
sys.path.insert(0, str(ROOT))

from server import P5RWebHandler  # noqa: E402


class handler(P5RWebHandler):
    """Vercel's Python runtime instantiates this BaseHTTPRequestHandler."""
    pass
