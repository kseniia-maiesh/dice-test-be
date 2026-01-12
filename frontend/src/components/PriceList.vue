<script setup>
defineProps({
  prices: {
    type: Array,
    required: true,
  },
  activeCombination: {
    type: String,
    default: null,
  },
});
</script>

<template>
  <div class="price-list">
    <h3>Prices</h3>
    <div
      v-for="p in prices"
      :key="p.name"
      class="price-row"
      :class="{ active: activeCombination === p.name }"
    >
      <span>{{ p.name }}</span>
      <strong>x{{ p.mult }}</strong>
    </div>
  </div>
</template>

<style scoped>
.price-list h3 {
  margin-top: 0;
}

.price-row {
  display: flex;
  justify-content: space-between;
  padding: 6px 0;
}

.price-row.active {
  color: #d64545;
  font-weight: bold;
}
</style>
