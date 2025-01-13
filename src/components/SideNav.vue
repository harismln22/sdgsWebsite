<template>
  <div class="h-full w-44 text-sm dark:bg-gray-900">
    <router-link
      to="/"
      class="side-bar-item px-4 py-2 bg-gray-100 dark:bg-gray-600 cursor-pointer"
      :class="{ active: activeButton === 'dashboard' }"
      @click="setActive('dashboard')"
    >
      Dashboard
    </router-link>
    <router-link
      to="/crud"
      class="side-bar-item px-4 py-2 hover:bg-gray-100 hover:dark:bg-gray-800 cursor-pointer"
      :class="{ active: activeButton === 'crud' }"
      @click="setActive('crud')"
    >
      CRUD
    </router-link>
  </div>
</template>

<script>
export default {
  props: {
    activeButton: {
      type: String,
      required: true
    }
  },
  methods: {
    setActive(button) {
      this.$emit('update:activeButton', button);
    }
  }
}
</script>

<style scoped>
/* Add your styles here */
</style>