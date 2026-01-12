<script setup>
import { computed } from 'vue';

const props = defineProps({
  bet: {
    type: Number,
    required: true,
  },
  rolling: {
    type: Boolean,
    default: false,
  },
  balance: {
    type: Number,
    required: true,
  },
});

const emit = defineEmits(['update:bet', 'roll']);

const canRoll = computed(() => {
  return !props.rolling && props.bet > 0 && props.bet <= props.balance;
});

const updateBet = (value) => {
  emit('update:bet', value);
};

const handleRoll = () => {
  if (canRoll.value) {
    emit('roll');
  }
};
</script>

<template>
  <div class="bet-controls">
    <h3>Bet</h3>
    <div class="bet-row">
      <input type="number" :value="bet" @input="updateBet(Number($event.target.value))" min="1" :max="balance" />
      <button @click="handleRoll" :disabled="!canRoll">
        {{ rolling ? "Rolling..." : "ROLL" }}
      </button>
    </div>
  </div>
</template>

<style scoped>
.bet-controls h3 {
  margin-top: 0;
}

.bet-row {
  display: flex;
  gap: 10px;
}

.bet-row input {
  width: 80px;
  padding: 6px;
  font-size: 16px;
}

.bet-row button {
  padding: 6px 18px;
  font-size: 16px;
  background: linear-gradient(#f6c1b8, #d88);
  border: none;
  border-radius: 6px;
  cursor: pointer;
}

.bet-row button:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}
</style>
