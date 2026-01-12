import { ref } from "vue";

const API_URL = import.meta.env.VITE_API_URL || "http://127.0.0.1:8000";

export function useGameApi() {
  const loading = ref(false);
  const error = ref(null);

  const handleRequest = async (requestFn) => {
    loading.value = true;
    error.value = null;

    try {
      const response = await requestFn();

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      return await response.json();
    } catch (err) {
      error.value = err.message;
      console.error("API Error:", err);
      throw err;
    } finally {
      loading.value = false;
    }
  };

  const initGame = async () => {
    return handleRequest(() => fetch(`${API_URL}/init`, { method: "POST" }));
  };

  const rollDice = async (betAmount) => {
    return handleRequest(() =>
      fetch(`${API_URL}/roll`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ bet: Number(betAmount) }),
      })
    );
  };

  return {
    loading,
    error,
    initGame,
    rollDice,
  };
}
