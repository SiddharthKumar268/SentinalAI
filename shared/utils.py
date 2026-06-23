"""
SentinelAI — Shared utilities and configuration.
"""
import os
import hashlib
import json
from datetime import datetime, timezone
from dotenv import load_dotenv

load_dotenv()


def get_env(key: str, default: str = None) -> str:
    """Get environment variable or raise error if required and missing."""
    value = os.getenv(key, default)
    if value is None:
        raise EnvironmentError(f"Required environment variable '{key}' is not set.")
    return value


def sha256_hash(data: str) -> str:
    """Generate SHA-256 hash for data integrity / immutable timestamping."""
    return hashlib.sha256(data.encode("utf-8")).hexdigest()


def create_timestamped_record(data: dict) -> dict:
    """
    Wraps any data dict with a UTC ISO timestamp and SHA-256 integrity hash.
    Used by Crash Context Recorder and Witness Statement AI for evidentiary records.
    """
    timestamp = datetime.now(timezone.utc).isoformat()
    payload = json.dumps(data, sort_keys=True, default=str)
    return {
        "timestamp_utc": timestamp,
        "data": data,
        "integrity_hash": sha256_hash(f"{timestamp}:{payload}"),
    }


def risk_level_label(score: float) -> str:
    """Convert a 0-100 risk score to a human-readable label."""
    if score < 25:
        return "LOW"
    elif score < 50:
        return "MODERATE"
    elif score < 75:
        return "HIGH"
    else:
        return "CRITICAL"


# ── Constants ─────────────────────────────────────────────
ANTHROPIC_MODEL = os.getenv("ANTHROPIC_MODEL", "claude-sonnet-4-20250514")
OPENWEATHERMAP_BASE = "https://api.openweathermap.org/data/2.5"
GOOGLE_MAPS_GEOCODE = "https://maps.googleapis.com/maps/api/geocode/json"
