import { useCallback, useEffect, useState } from "react";
import { api, ApiError } from "../api/client";
import { WorkoutCard } from "../components/WorkoutCard";
import { WorkoutForm } from "../components/WorkoutForm";
import { useAuth } from "../context/AuthContext";
import type { Workout, WorkoutInput } from "../types";

export function DashboardPage() {
  const { token } = useAuth();
  const [workouts, setWorkouts] = useState<Workout[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");
  const [showForm, setShowForm] = useState(false);
  const [editing, setEditing] = useState<Workout | null>(null);
  const [deletingId, setDeletingId] = useState<number | null>(null);

  const loadWorkouts = useCallback(async () => {
    if (!token) return;
    setLoading(true);
    setError("");
    try {
      const data = await api.getWorkouts(token);
      setWorkouts(data);
    } catch (err) {
      if (err instanceof ApiError && err.status === 404) {
        setWorkouts([]);
      } else {
        setError(err instanceof Error ? err.message : "Failed to load workouts");
      }
    } finally {
      setLoading(false);
    }
  }, [token]);

  useEffect(() => {
    loadWorkouts();
  }, [loadWorkouts]);

  async function handleCreate(data: WorkoutInput) {
    if (!token) return;
    await api.createWorkout(token, data);
    await loadWorkouts();
  }

  async function handleUpdate(data: WorkoutInput) {
    if (!token || !editing) return;
    await api.updateWorkout(token, editing.id, data);
    setEditing(null);
    await loadWorkouts();
  }

  async function handleDelete(id: number) {
    if (!token) return;
    setDeletingId(id);
    try {
      await api.deleteWorkout(token, id);
      setWorkouts((prev) => prev.filter((w) => w.id !== id));
    } catch (err) {
      setError(err instanceof Error ? err.message : "Failed to delete workout");
    } finally {
      setDeletingId(null);
    }
  }

  const totalVolume = workouts.reduce(
    (sum, w) => sum + w.weight * w.reps * w.sets,
    0,
  );

  return (
    <main className="max-w-6xl mx-auto px-4 sm:px-6 py-10">
      <div className="flex flex-col sm:flex-row sm:items-end justify-between gap-4 mb-10">
        <div>
          <h1 className="text-3xl font-bold mb-1">My Workouts</h1>
          <p className="text-muted">
            {workouts.length === 0
              ? "No workouts yet — log your first session."
              : `${workouts.length} session${workouts.length === 1 ? "" : "s"} logged`}
          </p>
        </div>
        <button
          onClick={() => {
            setEditing(null);
            setShowForm(true);
          }}
          className="btn-primary shrink-0"
        >
          + Log workout
        </button>
      </div>

      {!loading && workouts.length > 0 && (
        <div className="grid sm:grid-cols-3 gap-4 mb-10">
          <div className="card text-center">
            <p className="text-3xl font-bold text-accent">{workouts.length}</p>
            <p className="text-sm text-muted mt-1">Total sessions</p>
          </div>
          <div className="card text-center">
            <p className="text-3xl font-bold">
              {Math.max(...workouts.map((w) => w.weight))}
            </p>
            <p className="text-sm text-muted mt-1">Heaviest lift (lbs)</p>
          </div>
          <div className="card text-center">
            <p className="text-3xl font-bold">{totalVolume.toLocaleString()}</p>
            <p className="text-sm text-muted mt-1">Total volume (lbs)</p>
          </div>
        </div>
      )}

      {error && (
        <div className="mb-6 rounded-xl border border-danger/30 bg-danger/10 px-4 py-3 text-sm text-danger">
          {error}
        </div>
      )}

      {loading ? (
        <div className="grid sm:grid-cols-2 lg:grid-cols-3 gap-5">
          {[1, 2, 3].map((i) => (
            <div key={i} className="card animate-pulse h-48 bg-surface-hover" />
          ))}
        </div>
      ) : workouts.length === 0 ? (
        <div className="card text-center py-16">
          <div className="w-16 h-16 rounded-2xl bg-accent/10 border border-accent/20 flex items-center justify-center mx-auto mb-4">
            <svg className="w-8 h-8 text-accent" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={1.5}>
              <path strokeLinecap="round" strokeLinejoin="round" d="M12 4.5v15m7.5-7.5h-15" />
            </svg>
          </div>
          <h2 className="text-xl font-semibold mb-2">No workouts yet</h2>
          <p className="text-muted mb-6 max-w-sm mx-auto">
            Hit the button above to log your first exercise and start building your history.
          </p>
          <button onClick={() => setShowForm(true)} className="btn-primary">
            Log your first workout
          </button>
        </div>
      ) : (
        <div className="grid sm:grid-cols-2 lg:grid-cols-3 gap-5">
          {workouts.map((workout) => (
            <WorkoutCard
              key={workout.id}
              workout={workout}
              onEdit={(w) => {
                setEditing(w);
                setShowForm(true);
              }}
              onDelete={handleDelete}
              deleting={deletingId === workout.id}
            />
          ))}
        </div>
      )}

      {showForm && (
        <WorkoutForm
          initial={editing}
          onSubmit={editing ? handleUpdate : handleCreate}
          onCancel={() => {
            setShowForm(false);
            setEditing(null);
          }}
        />
      )}
    </main>
  );
}
