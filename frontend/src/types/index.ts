export interface User {
  user_id: number;
  email: string;
  created_at: string;
}

export interface Workout {
  id: number;
  owner_id: number;
  type: string;
  weight: number;
  reps: number;
  sets: number;
}

export interface WorkoutInput {
  type: string;
  reps: number;
  weight: number;
  sets?: number;
}

export interface TokenResponse {
  access_token: string;
  token_type: string;
}

export interface AuthCredentials {
  email: string;
  password: string;
}
