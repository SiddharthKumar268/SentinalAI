"""
SentinelAI — Module 1: Cognitive Load Profiler (MCP Server)
Assesses driver cognitive/emotional state before trips.
Status: 🚧 In Development
"""
import json
from datetime import datetime

# ── Tool Definition ───────────────────────────────────────
TOOL_DEFINITION = {
    "name": "assess_cognitive_load",
    "description": "Performs a 30-second AI-driven cognitive assessment of the driver before a trip. Analyses responses for linguistic markers of cognitive impairment and returns a risk score from 0-100.",
    "input_schema": {
        "type": "object",
        "properties": {
            "driver_id": {"type": "string", "description": "Unique driver identifier"},
            "sleep_hours": {"type": "number", "description": "Hours of sleep last night"},
            "stress_level": {"type": "string", "enum": ["low", "moderate", "high", "severe"]},
            "last_meal_hours_ago": {"type": "number", "description": "Hours since last meal"},
            "emotional_state": {"type": "string", "description": "Self-reported emotional state"},
        },
        "required": ["driver_id", "sleep_hours", "stress_level"],
    },
}


def compute_cognitive_score(sleep_hours: float, stress: str, meal_gap: float) -> int:
    """Basic cognitive risk scoring — will be replaced with LLM analysis."""
    score = 0
    # Sleep factor
    if sleep_hours < 4:
        score += 40
    elif sleep_hours < 6:
        score += 25
    elif sleep_hours < 7:
        score += 10

    # Stress factor
    stress_map = {"low": 0, "moderate": 15, "high": 30, "severe": 45}
    score += stress_map.get(stress, 15)

    # Meal gap factor
    if meal_gap and meal_gap > 8:
        score += 15
    elif meal_gap and meal_gap > 5:
        score += 8

    return min(score, 100)


def get_recommendation(score: int) -> str:
    if score < 25:
        return "✅ You're in good shape to drive. Stay safe!"
    elif score < 50:
        return "⚠️ Mild risk detected. Consider a short break or coffee before departure."
    elif score < 75:
        return "🟠 Elevated risk. We recommend a 20-minute rest or planning a shorter route."
    else:
        return "🔴 High cognitive load detected. Strongly recommend delaying your trip or using alternative transport."


# ── Placeholder handler ──────────────────────────────────
def handle_request(params: dict) -> dict:
    score = compute_cognitive_score(
        params.get("sleep_hours", 7),
        params.get("stress_level", "low"),
        params.get("last_meal_hours_ago", 3),
    )
    return {
        "driver_id": params["driver_id"],
        "cognitive_risk_score": score,
        "risk_level": "LOW" if score < 25 else "MODERATE" if score < 50 else "HIGH" if score < 75 else "CRITICAL",
        "recommendation": get_recommendation(score),
        "assessed_at": datetime.utcnow().isoformat() + "Z",
    }


if __name__ == "__main__":
    # Quick test
    result = handle_request({
        "driver_id": "driver_001",
        "sleep_hours": 4,
        "stress_level": "high",
        "last_meal_hours_ago": 9,
    })
    print(json.dumps(result, indent=2))
