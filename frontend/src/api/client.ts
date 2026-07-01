import type {
  AuthCredentials,
  TokenResponse,
  User,
  Workout,
  WorkoutInput,
} from "../types";

const API_BASE = import.meta.env.VITE_API_URL ?? "/api";

class ApiError extends Error {
  status: number;

  constructor(status: number, message: string) {
    super(message);
    this.status = status;
  }
}

async function request<T>(
  path: string,
  options: RequestInit = {},
  token?: string | null,
): Promise<T> {
  const headers = new Headers(options.headers);
  headers.set("Content-Type", "application/json");
  if (token) {
    headers.set("Authorization", `Bearer ${token}`);
  }

  const response = await fetch(`${API_BASE}${path}`, {
    ...options,
    headers,
  });

  if (response.status === 204) {
    return undefined as T;
  }

  const data = await response.json().catch(() => null);

  if (!response.ok) {
    const message =
      typeof data?.detail === "string"
        ? data.detail
        : `Request failed (${response.status})`;
    throw new ApiError(response.status, message);
  }

  return data as T;
}

export const api = {
  register(credentials: AuthCredentials) {
    return request<User>("/users/create_user", {
      method: "POST",
      body: JSON.stringify(credentials),
    });
  },

  login(credentials: AuthCredentials) {
    return request<TokenResponse>("/login", {
      method: "POST",
      body: JSON.stringify(credentials),
    });
  },

  getWorkouts(token: string) {
    return request<Workout[]>("/users/user/workouts", {}, token);
  },

  createWorkout(token: string, workout: WorkoutInput) {
    return request<Workout>("/workout", {
      method: "POST",
      body: JSON.stringify(workout),
    }, token);
  },

  updateWorkout(token: string, id: number, workout: WorkoutInput) {
    return request<Workout>(`/workout/${id}`, {
      method: "PUT",
      body: JSON.stringify(workout),
    }, token);
  },

  deleteWorkout(token: string, id: number) {
    return request<void>(`/workout/${id}`, { method: "DELETE" }, token);
  },
};

export { ApiError };
