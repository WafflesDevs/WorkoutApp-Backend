from pydantic_settings import BaseSettings
PROJECT_NAME = "FastAPI CRUD App"
VERSION = "1.0.0"
class Settings(BaseSettings):
    secret_key: str
    database_name : str
    database_password : str
    database_port: str
    database_username:str
    database_user:str
    database_hostname : str
    TOKEN_EXPIRE:int
    ALGO:str
    


    class Config:
        env_file = ".env"

settings = Settings()
allowed_roles = ["Admin", "User"]
gym_workouts = {

    # ── Chest ──────────────────────────────────────────────────────
    "chest": {
        "barbell_bench_press":     {"sets": 4, "reps": "6–10",  "rest_sec": 120, "equipment": "barbell"},
        "incline_dumbbell_press":  {"sets": 3, "reps": "8–12",  "rest_sec": 90,  "equipment": "dumbbell"},
        "decline_bench_press":     {"sets": 3, "reps": "8–12",  "rest_sec": 90,  "equipment": "barbell"},
        "cable_fly":               {"sets": 3, "reps": "12–15", "rest_sec": 60,  "equipment": "cable"},
        "dumbbell_fly":            {"sets": 3, "reps": "12–15", "rest_sec": 60,  "equipment": "dumbbell"},
        "push_up":                 {"sets": 3, "reps": "15–20", "rest_sec": 60,  "equipment": "bodyweight"},
        "chest_dip":               {"sets": 3, "reps": "8–12",  "rest_sec": 90,  "equipment": "bodyweight"},
        "pec_deck_machine":        {"sets": 3, "reps": "12–15", "rest_sec": 60,  "equipment": "machine"},
    },

    # ── Back ───────────────────────────────────────────────────────
    "back": {
        "deadlift":                {"sets": 4, "reps": "4–6",   "rest_sec": 180, "equipment": "barbell"},
        "pull_up":                 {"sets": 4, "reps": "6–10",  "rest_sec": 90,  "equipment": "bodyweight"},
        "barbell_row":             {"sets": 4, "reps": "6–10",  "rest_sec": 120, "equipment": "barbell"},
        "seated_cable_row":        {"sets": 3, "reps": "10–12", "rest_sec": 90,  "equipment": "cable"},
        "lat_pulldown":            {"sets": 3, "reps": "10–12", "rest_sec": 90,  "equipment": "cable"},
        "single_arm_dumbbell_row": {"sets": 3, "reps": "10–12", "rest_sec": 75,  "equipment": "dumbbell"},
        "face_pull":               {"sets": 3, "reps": "15–20", "rest_sec": 60,  "equipment": "cable"},
        "hyperextension":          {"sets": 3, "reps": "12–15", "rest_sec": 60,  "equipment": "machine"},
    },

    # ── Shoulders ──────────────────────────────────────────────────
    "shoulders": {
        "overhead_barbell_press":  {"sets": 4, "reps": "6–8",   "rest_sec": 120, "equipment": "barbell"},
        "dumbbell_shoulder_press": {"sets": 3, "reps": "8–12",  "rest_sec": 90,  "equipment": "dumbbell"},
        "lateral_raise":           {"sets": 4, "reps": "12–15", "rest_sec": 60,  "equipment": "dumbbell"},
        "front_raise":             {"sets": 3, "reps": "12–15", "rest_sec": 60,  "equipment": "dumbbell"},
        "rear_delt_fly":           {"sets": 3, "reps": "12–15", "rest_sec": 60,  "equipment": "dumbbell"},
        "cable_lateral_raise":     {"sets": 3, "reps": "12–15", "rest_sec": 60,  "equipment": "cable"},
        "arnold_press":            {"sets": 3, "reps": "10–12", "rest_sec": 90,  "equipment": "dumbbell"},
        "upright_row":             {"sets": 3, "reps": "10–12", "rest_sec": 75,  "equipment": "barbell"},
        "shrug":                   {"sets": 3, "reps": "12–15", "rest_sec": 60,  "equipment": "barbell"},
    },

    # ── Biceps ─────────────────────────────────────────────────────
    "biceps": {
        "barbell_curl":            {"sets": 4, "reps": "8–12",  "rest_sec": 75,  "equipment": "barbell"},
        "dumbbell_curl":           {"sets": 3, "reps": "10–12", "rest_sec": 60,  "equipment": "dumbbell"},
        "hammer_curl":             {"sets": 3, "reps": "10–12", "rest_sec": 60,  "equipment": "dumbbell"},
        "incline_dumbbell_curl":   {"sets": 3, "reps": "10–12", "rest_sec": 60,  "equipment": "dumbbell"},
        "preacher_curl":           {"sets": 3, "reps": "10–12", "rest_sec": 60,  "equipment": "barbell"},
        "concentration_curl":      {"sets": 3, "reps": "12–15", "rest_sec": 60,  "equipment": "dumbbell"},
        "cable_curl":              {"sets": 3, "reps": "12–15", "rest_sec": 60,  "equipment": "cable"},
        "chin_up":                 {"sets": 3, "reps": "6–10",  "rest_sec": 90,  "equipment": "bodyweight"},
    },

    # ── Triceps ────────────────────────────────────────────────────
    "triceps": {
        "close_grip_bench_press":  {"sets": 4, "reps": "6–10",  "rest_sec": 90,  "equipment": "barbell"},
        "skull_crusher":           {"sets": 3, "reps": "10–12", "rest_sec": 75,  "equipment": "barbell"},
        "tricep_pushdown":         {"sets": 3, "reps": "12–15", "rest_sec": 60,  "equipment": "cable"},
        "overhead_tricep_extension":{"sets": 3, "reps": "10–12", "rest_sec": 75,  "equipment": "dumbbell"},
        "diamond_push_up":         {"sets": 3, "reps": "12–15", "rest_sec": 60,  "equipment": "bodyweight"},
        "tricep_dip":              {"sets": 3, "reps": "10–15", "rest_sec": 75,  "equipment": "bodyweight"},
        "kickback":                {"sets": 3, "reps": "12–15", "rest_sec": 60,  "equipment": "dumbbell"},
    },

    # ── Legs ───────────────────────────────────────────────────────
    "legs": {
        "barbell_squat":           {"sets": 4, "reps": "5–8",   "rest_sec": 180, "equipment": "barbell"},
        "romanian_deadlift":       {"sets": 4, "reps": "8–10",  "rest_sec": 120, "equipment": "barbell"},
        "leg_press":               {"sets": 4, "reps": "10–12", "rest_sec": 120, "equipment": "machine"},
        "leg_extension":           {"sets": 3, "reps": "12–15", "rest_sec": 60,  "equipment": "machine"},
        "leg_curl":                {"sets": 3, "reps": "12–15", "rest_sec": 60,  "equipment": "machine"},
        "walking_lunge":           {"sets": 3, "reps": "12–16", "rest_sec": 75,  "equipment": "dumbbell"},
        "bulgarian_split_squat":   {"sets": 3, "reps": "8–12",  "rest_sec": 90,  "equipment": "dumbbell"},
        "hip_thrust":              {"sets": 4, "reps": "10–15", "rest_sec": 90,  "equipment": "barbell"},
        "calf_raise":              {"sets": 4, "reps": "15–20", "rest_sec": 60,  "equipment": "machine"},
        "goblet_squat":            {"sets": 3, "reps": "10–15", "rest_sec": 75,  "equipment": "dumbbell"},
    },

    # ── Core ───────────────────────────────────────────────────────
    "core": {
        "plank":                   {"sets": 3, "reps": "30–60s", "rest_sec": 45,  "equipment": "bodyweight"},
        "cable_crunch":            {"sets": 3, "reps": "12–15", "rest_sec": 60,  "equipment": "cable"},
        "hanging_leg_raise":       {"sets": 3, "reps": "10–15", "rest_sec": 60,  "equipment": "bodyweight"},
        "ab_wheel_rollout":        {"sets": 3, "reps": "8–12",  "rest_sec": 60,  "equipment": "ab wheel"},
        "russian_twist":           {"sets": 3, "reps": "20–30", "rest_sec": 45,  "equipment": "bodyweight"},
        "bicycle_crunch":          {"sets": 3, "reps": "20–30", "rest_sec": 45,  "equipment": "bodyweight"},
        "dead_bug":                {"sets": 3, "reps": "10–12", "rest_sec": 45,  "equipment": "bodyweight"},
        "landmine_twist":          {"sets": 3, "reps": "10–12", "rest_sec": 60,  "equipment": "barbell"},
    },

    # ── Cardio ─────────────────────────────────────────────────────
    "cardio": {
        "treadmill_steady_state":  {"sets": 1, "reps": "30–45 min", "rest_sec": 0,   "equipment": "treadmill"},
        "treadmill_hiit":          {"sets": 8, "reps": "30s sprint", "rest_sec": 90,  "equipment": "treadmill"},
        "rowing_machine":          {"sets": 1, "reps": "20–30 min", "rest_sec": 0,   "equipment": "rower"},
        "stationary_bike":         {"sets": 1, "reps": "30–45 min", "rest_sec": 0,   "equipment": "bike"},
        "stairmaster":             {"sets": 1, "reps": "20–30 min", "rest_sec": 0,   "equipment": "stairmaster"},
        "jump_rope":               {"sets": 5, "reps": "2 min",     "rest_sec": 60,  "equipment": "jump rope"},
        "sled_push":               {"sets": 5, "reps": "20 m",      "rest_sec": 90,  "equipment": "sled"},
        "battle_ropes":            {"sets": 5, "reps": "30s",       "rest_sec": 60,  "equipment": "battle ropes"},
    },

    # ── Forearms & Grip ────────────────────────────────────────────
    "forearms": {
        "wrist_curl":              {"sets": 3, "reps": "15–20", "rest_sec": 45,  "equipment": "barbell"},
        "reverse_wrist_curl":      {"sets": 3, "reps": "15–20", "rest_sec": 45,  "equipment": "barbell"},
        "farmers_carry":           {"sets": 4, "reps": "40 m",   "rest_sec": 90,  "equipment": "dumbbell"},
        "dead_hang":               {"sets": 3, "reps": "20–45s", "rest_sec": 60,  "equipment": "bodyweight"},
        "plate_pinch":             {"sets": 3, "reps": "20–30s", "rest_sec": 60,  "equipment": "plate"},
    },

    # ── Olympic / Power ────────────────────────────────────────────
    "olympic_power": {
        "power_clean":             {"sets": 5, "reps": "3–5",   "rest_sec": 180, "equipment": "barbell"},
        "hang_clean":              {"sets": 4, "reps": "3–5",   "rest_sec": 180, "equipment": "barbell"},
        "snatch":                  {"sets": 5, "reps": "2–3",   "rest_sec": 180, "equipment": "barbell"},
        "push_press":              {"sets": 4, "reps": "4–6",   "rest_sec": 120, "equipment": "barbell"},
        "kettlebell_swing":        {"sets": 4, "reps": "15–20", "rest_sec": 75,  "equipment": "kettlebell"},
        "box_jump":                {"sets": 4, "reps": "5–8",   "rest_sec": 90,  "equipment": "plyobox"},
    },
}