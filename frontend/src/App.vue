<script setup>
import { ref, onMounted } from "vue";
import { useGameApi } from "./composables/useGameApi.js";
import DiceDisplay from "./components/DiceDisplay.vue";
import PriceList from "./components/PriceList.vue";
import BetControls from "./components/BetControls.vue";
import BalanceDisplay from "./components/BalanceDisplay.vue";
import { PRICES, DEFAULT_BET, DICE_COUNT, ROLL_ANIMATION_DURATION } from "./constants/gameConfig.js";

const { initGame, rollDice, error } = useGameApi();

const balance = ref(0);
const bet = ref(DEFAULT_BET);
const dice = ref(Array(DICE_COUNT).fill("?"));
const combination = ref(null);
const win = ref(0);
const rolling = ref(false);

onMounted(async () => {
  try {
    const data = await initGame();
    balance.value = data.balance;
  } catch (err) {
    console.error("Failed to initialize game:", err);
    balance.value = 100;
  }
});

async function roll() {
  if (rolling.value) return;

  rolling.value = true;
  combination.value = null;
  win.value = 0;

  dice.value = Array(DICE_COUNT).fill("?");

  await new Promise((resolve) => setTimeout(resolve, ROLL_ANIMATION_DURATION));

  try {
    const data = await rollDice(bet.value);

    dice.value = data.dice;
    combination.value = data.combination;
    win.value = data.win;
    balance.value = data.balance;
  } catch (err) {
    console.error("Failed to roll dice:", err);
    dice.value = Array(DICE_COUNT).fill("?");
  } finally {
    rolling.value = false;
  }
}
</script>

<template>
  <div class="page">
    <div class="card dice-card">
      <DiceDisplay :dice="dice" :rolling="rolling" />
    </div>

    <div class="bottom">
      <div class="card prices">
        <PriceList :prices="PRICES" :activeCombination="combination" />
      </div>

      <div class="right">
        <div class="card bet">
          <BetControls v-model:bet="bet" :rolling="rolling" :balance="balance" @roll="roll" />
        </div>

        <div class="card balance">
          <BalanceDisplay :balance="balance" />
        </div>
      </div>
    </div>
  </div>
</template>

<style>
body {
  margin: 0;
  background: #f3f3f3;
  color: black;
}

.page {
  max-width: 800px;
  margin: 40px auto;
  font-family: sans-serif;
}

.card {
  background: white;
  border-radius: 12px;
  padding: 20px;
  box-shadow: 0 6px 14px rgba(0, 0, 0, 0.12);
}

.dice-card {
  text-align: center;
}

.bottom {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 30px;
  margin-top: 30px;
}

.right {
  display: flex;
  flex-direction: column;
  gap: 20px;
}
</style>
