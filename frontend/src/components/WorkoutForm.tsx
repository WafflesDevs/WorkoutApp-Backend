import { useEffect, useState, type FormEvent } from "react";
import type { Workout, WorkoutInput } from "../types";

interface WorkoutFormProps {
  initial?: Workout | null;
  onSubmit: (data: WorkoutInput) => Promise<void>;
  onCancel: () => void;
}

const emptyForm: WorkoutInput = {
  type: "",
  weight: 0,
  reps: 0,
  sets: 3,
};

export function WorkoutForm({ initial, onSubmit, onCancel }: WorkoutFormProps) {
  const [form, setForm] = useState<WorkoutInput>(emptyForm);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  useEffect(() => {
    if (initial) {
      setForm({
        type: initial.type,
        weight: initial.weight,
        reps: initial.reps,
        sets: initial.sets,
      });
    } else {
      setForm(emptyForm);
    }
  }, [initial]);

  async function handleSubmit(e: FormEvent) {
    e.preventDefault();
    setError("");
    setLoading(true);
    try {
      await onSubmit(form);
      onCancel();
    } catch (err) {
      setError(err instanceof Error ? err.message : "Something went wrong");
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4">
      <div
        className="absolute inset-0 bg-black/60 backdrop-blur-sm"
        onClick={onCancel}
      />
      <form
        onSubmit={handleSubmit}
        className="card relative w-full max-w-md shadow-2xl shadow-black/40"
      >
        <h2 className="text-xl font-bold mb-1">
          {initial ? "Edit workout" : "Log a workout"}
        </h2>
        <p className="text-sm text-muted mb-6">
          Track your sets, reps, and weight for any exercise.
        </p>

        {error && (
          <div className="mb-4 rounded-xl border border-danger/30 bg-danger/10 px-4 py-3 text-sm text-danger">
            {error}
          </div>
        )}

        <div className="space-y-4">
          <div>
            <label className="block text-sm font-medium text-muted mb-1.5">
              Exercise type
            </label>
            <input
              required
              value={form.type}
              onChange={(e) => setForm({ ...form, type: e.target.value })}
              placeholder="e.g. Bench press, Squat, Deadlift"
              className="w-full"
            />
          </div>

          <div className="grid grid-cols-3 gap-3">
            <div>
              <label className="block text-sm font-medium text-muted mb-1.5">
                Weight
              </label>
              <input
                required
                type="number"
                min={0}
                value={form.weight || ""}
                onChange={(e) =>
                  setForm({ ...form, weight: Number(e.target.value) })
                }
                placeholder="135"
                className="w-full"
              />
            </div>
            <div>
              <label className="block text-sm font-medium text-muted mb-1.5">
                Reps
              </label>
              <input
                required
                type="number"
                min={1}
                value={form.reps || ""}
                onChange={(e) =>
                  setForm({ ...form, reps: Number(e.target.value) })
                }
                placeholder="8"
                className="w-full"
              />
            </div>
            <div>
              <label className="block text-sm font-medium text-muted mb-1.5">
                Sets
              </label>
              <input
                type="number"
                min={1}
                value={form.sets ?? ""}
                onChange={(e) =>
                  setForm({ ...form, sets: Number(e.target.value) || undefined })
                }
                placeholder="3"
                className="w-full"
              />
            </div>
          </div>
        </div>

        <div className="flex gap-3 mt-6">
          <button type="button" onClick={onCancel} className="btn-secondary flex-1">
            Cancel
          </button>
          <button type="submit" disabled={loading} className="btn-primary flex-1">
            {loading ? "Saving…" : initial ? "Update" : "Add workout"}
          </button>
        </div>
      </form>
    </div>
  );
}
