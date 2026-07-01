import type { Workout } from "../types";

interface WorkoutCardProps {
  workout: Workout;
  onEdit: (workout: Workout) => void;
  onDelete: (id: number) => void;
  deleting?: boolean;
}

const typeColors: Record<string, string> = {
  bench: "from-rose-500/20 to-orange-500/10 border-rose-500/30",
  squat: "from-violet-500/20 to-indigo-500/10 border-violet-500/30",
  deadlift: "from-cyan-500/20 to-teal-500/10 border-cyan-500/30",
  default: "from-accent/20 to-indigo-500/10 border-accent/30",
};

function colorForType(type: string) {
  const key = type.toLowerCase();
  for (const [name, color] of Object.entries(typeColors)) {
    if (key.includes(name)) return color;
  }
  return typeColors.default;
}

export function WorkoutCard({ workout, onEdit, onDelete, deleting }: WorkoutCardProps) {
  const gradient = colorForType(workout.type);

  return (
    <article className={`card bg-gradient-to-br ${gradient} relative overflow-hidden group`}>
      <div className="absolute top-0 right-0 w-32 h-32 bg-accent/5 rounded-full blur-2xl -translate-y-1/2 translate-x-1/2" />

      <div className="relative">
        <div className="flex items-start justify-between gap-4 mb-5">
          <div>
            <p className="text-xs uppercase tracking-widest text-muted mb-1">Exercise</p>
            <h3 className="text-xl font-bold capitalize">{workout.type}</h3>
          </div>
          <span className="text-xs text-muted bg-surface/60 px-2.5 py-1 rounded-lg border border-border">
            #{workout.id}
          </span>
        </div>

        <div className="grid grid-cols-3 gap-3 mb-6">
          <div className="bg-surface/50 rounded-xl p-3 text-center border border-border/50">
            <p className="text-2xl font-bold text-accent">{workout.weight}</p>
            <p className="text-xs text-muted mt-0.5">lbs</p>
          </div>
          <div className="bg-surface/50 rounded-xl p-3 text-center border border-border/50">
            <p className="text-2xl font-bold">{workout.reps}</p>
            <p className="text-xs text-muted mt-0.5">reps</p>
          </div>
          <div className="bg-surface/50 rounded-xl p-3 text-center border border-border/50">
            <p className="text-2xl font-bold">{workout.sets}</p>
            <p className="text-xs text-muted mt-0.5">sets</p>
          </div>
        </div>

        <div className="flex gap-2 opacity-0 group-hover:opacity-100 transition-opacity">
          <button
            onClick={() => onEdit(workout)}
            className="btn-secondary flex-1 text-sm py-2"
          >
            Edit
          </button>
          <button
            onClick={() => onDelete(workout.id)}
            disabled={deleting}
            className="btn-danger flex-1 text-sm py-2 disabled:opacity-50"
          >
            {deleting ? "Deleting…" : "Delete"}
          </button>
        </div>
      </div>
    </article>
  );
}
