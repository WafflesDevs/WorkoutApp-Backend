import { Link, useLocation } from "react-router-dom";
import { useAuth } from "../context/AuthContext";

export function Navbar() {
  const { isAuthenticated, logout } = useAuth();
  const location = useLocation();

  return (
    <header className="border-b border-border/60 bg-surface/80 backdrop-blur-md sticky top-0 z-50">
      <div className="max-w-6xl mx-auto px-4 sm:px-6 h-16 flex items-center justify-between">
        <Link to={isAuthenticated ? "/dashboard" : "/"} className="flex items-center gap-3 group">
          <div className="w-9 h-9 rounded-xl bg-accent/15 border border-accent/30 flex items-center justify-center group-hover:bg-accent/25 transition">
            <svg className="w-5 h-5 text-accent" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2}>
              <path strokeLinecap="round" strokeLinejoin="round" d="M3.75 13.5l10.5-11.25L12 10.5h8.25L9.75 21.75 12 13.5H3.75z" />
            </svg>
          </div>
          <span className="font-bold text-lg tracking-tight">Workout Tracker</span>
        </Link>

        <nav className="flex items-center gap-3">
          {!isAuthenticated ? (
            <>
              <Link
                to="/login"
                className={`px-4 py-2 rounded-xl text-sm font-medium transition ${
                  location.pathname === "/login"
                    ? "text-accent"
                    : "text-muted hover:text-white"
                }`}
              >
                Log in
              </Link>
              <Link to="/register" className="btn-primary text-sm py-2 px-4">
                Sign up
              </Link>
            </>
          ) : (
            <>
              <Link
                to="/dashboard"
                className={`px-4 py-2 rounded-xl text-sm font-medium transition ${
                  location.pathname === "/dashboard"
                    ? "text-accent"
                    : "text-muted hover:text-white"
                }`}
              >
                My workouts
              </Link>
              <button onClick={logout} className="btn-secondary text-sm py-2 px-4">
                Log out
              </button>
            </>
          )}
        </nav>
      </div>
    </header>
  );
}
