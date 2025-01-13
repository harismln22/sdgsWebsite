<template>
  <!-- Navigation Bar -->
  <nav
    class="bg-white dark:bg-gray-900 border-gray-200 rounded px-4 py-2 flex justify-between items-center"
  >
    <span class="font-semibold whitespace-nowrap py-2">
      <i class="bi bi-pie-chart"></i>
      SDGs
    </span>

    <!-- <div class="mr-4">
      <label for="purchaseMethod">Purchase method: </label>
      <select id="purchaseMethod" class="dark:bg-gray-700">
        <option value="All">All</option>
        <option value="Drama">Drama</option>
      </select>
    </div> -->

    <div class="flex">
      <button id="btn-dark-mode">
        <i id="icon-dark-mode" class="bi bi-moon-fill"></i>
      </button>
    </div>
  </nav>

  <!-- Dashboard Page -->
  <div id="dashboard-page" class="h-full flex">
    <!-- Side Nav -->
    <div class="h-full w-44 text-sm dark:bg-gray-900">
      <div
        class="side-bar-item px-4 py-2 bg-gray-100 dark:bg-gray-600 cursor-pointer"
        :class="{ active: activeButton === 'DashboardPage' }"
        @click="navigate('DashboardPage')"
      >
        Dashboard
      </div>
      <div
        class="side-bar-item px-4 py-2 hover:bg-gray-100 hover:dark:bg-gray-800 cursor-pointer"
        :class="{ active: activeButton === 'CrudPage' }"
        @click="navigate('CrudPage')"
      >
        CRUD
      </div>
    </div>

    <!-- Dashboard Content -->
    <main class="h-full grow">
      <router-view />
    </main>
  </div>
</template>

<script>
export default {
  name: "HelloWorld",
  props: {
    msg: String,
  },
  data() {
    return {
      activeButton: "DashboardPage",
    };
  },
  methods: {
    setActive(button) {
      this.activeButton = button;
    },
    navigate(route) {
      this.setActive(route);
      this.$router.push({ name: route });
    },
  },
  mounted() {
    const darkModeBtn = document.getElementById("btn-dark-mode");
    darkModeBtn.addEventListener("click", toggleDarkMode);
  },
};

const toggleDarkMode = async () => {
  // Toggle dark mode icon
  const darkModeIcon = document.getElementById("icon-dark-mode");
  darkModeIcon.classList.toggle("bi-moon-fill");
  darkModeIcon.classList.toggle("bi-sun-fill");

  // Toggle dark mode for ALL tailwind components
  document.documentElement.classList.toggle("dark");
};

/**
 * END
 */
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.active {
  background-color: #4a5568; /* Tailwind dark background color */
  color: white;
}
</style>
