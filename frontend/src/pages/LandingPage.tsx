import { Link } from "react-router-dom";

export function LandingPage() {
  return (
    <main className="max-w-6xl mx-auto px-4 sm:px-6 py-16 sm:py-24">
      <div className="grid lg:grid-cols-2 gap-12 items-center">
        <div>
          <div className="inline-flex items-center gap-2 rounded-full border border-accent/30 bg-accent/10 px-4 py-1.5 text-sm text-accent mb-6">
            <span className="w-2 h-2 rounded-full bg-accent animate-pulse" />
            Powered by your FastAPI backend
          </div>

          <h1 className="text-4xl sm:text-5xl lg:text-6xl font-extrabold tracking-tight leading-[1.1] mb-6">
            Track every rep.
            <span className="block text-accent">Crush every set.</span>
          </h1>

          <p className="text-lg text-muted max-w-lg mb-8 leading-relaxed">
            Log workouts, monitor progress, and manage your training — all connected
            to your existing workout API.
          </p>

          <div className="flex flex-wrap gap-4">
            <Link to="/register" className="btn-primary">
              Get started free
            </Link>
            <Link to="/login" className="btn-secondary">
              I have an account
            </Link>
          </div>
        </div>

        <div className="relative">
          <div className="card bg-gradient-to-br from-accent/10 to-indigo-500/5 border-accent/20 p-8">
            <div className="space-y-4">
              {[
                { type: "Bench Press", weight: 185, reps: 8, sets: 4 },
                { type: "Squat", weight: 225, reps: 5, sets: 3 },
                { type: "Deadlift", weight: 315, reps: 3, sets: 3 },
              ].map((w) => (
                <div
                  key={w.type}
                  className="flex items-center justify-between bg-surface/60 rounded-xl px-5 py-4 border border-border/50"
                >
                  <div>
                    <p className="font-semibold">{w.type}</p>
                    <p className="text-sm text-muted">
                      {w.sets} sets × {w.reps} reps
                    </p>
                  </div>
                  <span className="text-xl font-bold text-accent">{w.weight} lbs</span>
                </div>
              ))}
            </div>
          </div>
          <div className="absolute -z-10 inset-0 bg-accent/10 blur-3xl rounded-full scale-75" />
        </div>
      </div>
    </main>
  );
}
