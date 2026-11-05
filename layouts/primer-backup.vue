<template>
  <div class="slidev-layout primer-backup">
    <slot />
  </div>
</template>

<style scoped>
.primer-backup {
  position: relative;
  width: 100%;
  height: 100%;
  margin: 0;
  padding: 0 !important;
  overflow: hidden;
  background: #000;
}

.primer-backup :deep(img) {
  position: absolute;
  inset: 0;
  display: block;
  width: 100%;
  height: 100%;
  max-width: none;
  max-height: none;
  object-fit: contain;
}
</style>
