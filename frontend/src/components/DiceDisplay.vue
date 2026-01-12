<script setup>
import { computed } from 'vue';

const props = defineProps({
  dice: {
    type: Array,
    required: true,
  },
  rolling: {
    type: Boolean,
    default: false,
  },
});

const getDicePattern = (value) => {
  const patterns = {
    1: [4],
    2: [0, 8],
    3: [0, 4, 8],
    4: [0, 2, 6, 8],
    5: [0, 2, 4, 6, 8],
    6: [0, 2, 3, 5, 6, 8],
  };
  return patterns[value] || [];
};
</script>

<template>
  <div class="dice-display">
    <h2>Dice</h2>
    <div class="dice-row">
      <div v-for="(d, i) in dice" :key="i" class="die" :class="{ question: d === '?' }">
        <template v-if="typeof d === 'number'">
          <span v-for="pos in 9" :key="pos" class="dot-position"
            :class="{ dot: getDicePattern(d).includes(pos - 1) }"></span>
        </template>
        <template v-else> ? </template>
      </div>
    </div>
  </div>
</template>

<style scoped>
.dice-display {
  text-align: center;
}

.dice-row {
  display: flex;
  justify-content: center;
  gap: 16px;
  margin-top: 10px;
}

.die {
  width: 60px;
  height: 60px;
  border: 2px solid #222;
  border-radius: 8px;
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  grid-template-rows: repeat(3, 1fr);
  place-items: center;
}

.die.question {
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 28px;
}

.dot-position {
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
}

.dot {
  width: 8px;
  height: 8px;
  background: black;
  border-radius: 50%;
}
</style>
