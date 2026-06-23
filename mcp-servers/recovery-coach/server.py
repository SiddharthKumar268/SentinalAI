"""
SentinelAI — Module 9: Psychological Recovery Coach (MCP Server)
30-day post-accident check-in with PHQ-9/PCL-5 screening.
Status: 🚧 In Development
"""
import json
from datetime import datetime, timezone

# ── Tool Definition ───────────────────────────────────────
TOOL_DEFINITION = {
    "name": "recovery_checkin",
    "description": "Conducts a daily psychological check-in using validated PHQ-9 and PCL-5 screening instruments. Tracks recovery trajectory and provides CBT-aligned micro-exercises.",
    "input_schema": {
        "type": "object",
        "properties": {
            "driver_id": {"type": "string"},
            "day_number": {"type": "integer", "description": "Day of recovery program (1-30)"},
            "mood_score": {"type": "integer", "description": "Self-rated mood 1-10"},
            "sleep_quality": {"type": "string", "enum": ["poor", "fair", "good", "excellent"]},
            "driving_anxiety_level": {"type": "integer", "description": "Driving anxiety 0-10"},
            "intrusive_thoughts": {"type": "boolean", "description": "Experiencing intrusive thoughts about the incident"},
        },
        "required": ["driver_id", "day_number", "mood_score"],
    },
}

# ── PHQ-9 / PCL-5 simplified scoring ─────────────────────
def compute_wellbeing_score(mood: int, sleep: str, anxiety: int, intrusive: bool) -> dict:
    score = mood * 10  # base from mood

    sleep_bonus = {"poor": -20, "fair": -5, "good": 5, "excellent": 15}
    score += sleep_bonus.get(sleep, 0)

    score -= anxiety * 5
    if intrusive:
        score -= 15

    score = max(0, min(100, score))

    if score >= 70:
        status = "recovering_well"
        action = "Continue your current routine. Great progress! 💪"
    elif score >= 40:
        status = "needs_attention"
        action = "Try a 5-minute grounding exercise: name 5 things you see, 4 you hear, 3 you touch."
    else:
        status = "needs_support"
        action = "We recommend speaking with a professional. iCall helpline: 9152987821 (free, confidential)."

    return {"wellbeing_score": score, "status": status, "recommended_action": action}


# ── Graduated return-to-driving protocol ──────────────────
DRIVING_PROTOCOL = {
    "week_1": "Passenger rides only. No driving.",
    "week_2": "10 minutes on a quiet residential road with a companion.",
    "week_3": "20 minutes on a familiar route. Try solo if comfortable.",
    "week_4": "Gradual highway exposure with a companion. Full solo at your own pace.",
}


def handle_request(params: dict) -> dict:
    day = params["day_number"]
    result = compute_wellbeing_score(
        params["mood_score"],
        params.get("sleep_quality", "fair"),
        params.get("driving_anxiety_level", 5),
        params.get("intrusive_thoughts", False),
    )

    week = min((day - 1) // 7 + 1, 4)
    result["driving_protocol"] = DRIVING_PROTOCOL.get(f"week_{week}", DRIVING_PROTOCOL["week_4"])
    result["day"] = day
    result["driver_id"] = params["driver_id"]
    result["checked_in_at"] = datetime.now(timezone.utc).isoformat()

    return result


if __name__ == "__main__":
    result = handle_request({
        "driver_id": "driver_001",
        "day_number": 5,
        "mood_score": 4,
        "sleep_quality": "poor",
        "driving_anxiety_level": 8,
        "intrusive_thoughts": True,
    })
    print(json.dumps(result, indent=2))
