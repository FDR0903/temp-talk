<script setup lang="ts">
import { useSlideContext } from '@slidev/client'
import '../seminar.css'

const { $page } = useSlideContext()
</script>

<template>
  <div class="slidev-layout seminar-slide">
    <slot />
    <div class="seminar-page-number" aria-label="Slide number">{{ $page }} / 25</div>
  </div>
</template>
