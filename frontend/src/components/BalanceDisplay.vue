<script setup>
defineProps({
  balance: {
    type: Number,
    required: true,
  },
});
</script>

<template>
  <div class="balance-display">
    <h3>Your balance</h3>
    <div class="balance-value">{{ balance }}</div>
  </div>
</template>

<style scoped>
.balance-display h3 {
  margin-top: 0;
}

.balance-value {
  font-size: 26px;
  font-weight: bold;
  text-align: center;
}
</style>
