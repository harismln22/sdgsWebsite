<template>
  <div class="max-w-2xl mx-auto p-4">
    <h1 class="text-2xl font-bold mb-4">Edit Document</h1>
    <form @submit.prevent="updateDocument" class="space-y-4">
      <div class="form-group">
        <label for="countryName" class="block text-sm font-medium   ">Country Name</label>
        <input
          type="text"
          class="mt-1 input-colored block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
          id="countryName"
          v-model="document['Country Name']"
        />
      </div>
      <div class="form-group">
        <label for="countryISO3" class="block text-sm font-medium   ">Country ISO3</label>
        <input
          type="text"
          class="mt-1 input-colored block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
          id="countryISO3"
          v-model="document['Country ISO3']"
        />
      </div>
      <div class="form-group">
        <label for="year" class="block text-sm font-medium   ">Year</label>
        <input
          type="number"
          class="mt-1 block input-colored  w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
          id="year"
          v-model.number="document.Year"
        />
      </div>
      <div v-for="key in allFields" :key="key" class="form-group">
        <label :for="key" class="block text-sm font-medium   ">{{ key }}</label>
        <input
          type="text"
          class="mt-1 block input-colored w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
          :id="key"
          v-model.number="document.data[key]"
        />
      </div>
      <div class="flex space-x-4">
        <button type="submit" class="btn btn-primary bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
          Save
        </button>
        <button type="button" class="btn btn-secondary bg-gray-500 hover:bg-gray-700 text-white font-bold py-2 px-4 rounded" @click="cancelEdit">
          Cancel
        </button>
      </div>
    </form>
  </div>
</template>

<script>
import { fetchDocumentById, updateDocumentById } from "@/api/api.js";

export default {
  name: "EditDocument",
  data() {
    return {
      document: {
        'Country Name': '',
        'Country ISO3': '',
        Year: null,
        data: {}
      },
      allFields: [
        "Agricultural land (sq. km)",
        "Agricultural land (% of land area)",
        "Arable land (% of land area)",
        "Rural land area where elevation is below 5 meters (sq. km)",
        "Rural land area where elevation is below 5 meters (% of total land area)",
        "Urban land area where elevation is below 5 meters (sq. km)",
        "Urban land area where elevation is below 5 meters (% of total land area)",
        "Land area where elevation is below 5 meters (% of total land area)",
        "Forest area (sq. km)",
        "Forest area (% of land area)",
        "Average precipitation in depth (mm per year)",
        "Cereal yield (kg per hectare)",
        "Access to electricity (% of population)",
        "Renewable energy consumption (% of total final energy consumption)",
        "Disaster risk reduction progress score (1-5 scale; 5=best)",
        "Rural population living in areas where elevation is below 5 meters (% of total population)",
        "Urban population living in areas where elevation is below 5 meters (% of total population)",
        "Population living in areas where elevation is below 5 meters (% of total population)",
        "Population in urban agglomerations of more than 1 million (% of total population)",
        "Terrestrial protected areas (% of total land area)",
        "Marine protected areas (% of territorial waters)",
        "Terrestrial and marine protected areas (% of total territorial area)",
        "Ease of doing business rank (1=most business-friendly regulations)",
        "CPIA public sector management and institutions cluster average (1=low to 6=high)",
        "Poverty headcount ratio at $2.15 a day (2017 PPP) (% of population)",
        "Population growth (annual %)",
        "Urban population growth (annual %)",
        "Urban population",
        "Urban population (% of total population)"
      ]
    };
  },
  methods: {
    async loadDocument() {
      try {
        const response = await fetchDocumentById(this.$route.params.id);
        this.document = response;
        // Ensure all fields are present in the document data
        this.allFields.forEach(field => {
          if (!Object.prototype.hasOwnProperty.call(this.document.data, field)) {
            this.document.data[field] = "";
          }
        });
      } catch (error) {
        console.error("Error loading document:", error);
      }
    },
    async updateDocument() {
      try {
        console.log("Updating document:", this.document); // Debugging log
        // Filter out empty fields
        const filteredDocument = {
          'Country Name': this.document['Country Name'],
          'Country ISO3': this.document['Country ISO3'],
          Year: this.document.Year,
          data: {}
        };
        for (const key in this.document.data) {
          if (this.document.data[key]) {
            filteredDocument.data[key] = this.document.data[key];
          }
        }
        await updateDocumentById(this.document._id, filteredDocument);
        console.log("Document updated successfully"); // Debugging log
        this.$router.push("/crud"); // Redirect to the main page after saving
      } catch (error) {
        console.error("Error updating document:", error);
      }
    },
    cancelEdit() {
      this.$router.push("/crud"); // Redirect to the main page without saving
    }
  },
  mounted() {
    this.loadDocument();
  }
};
</script>

<style scoped>

.input-colored {
  color: black; /* Warna font */
}

.dark body {
  color: white;
}
.form-group {
  margin-bottom: 15px;
}
.form-control {

  color: white;
  background-color: white;
  width: 100%;
  padding: 8px;
  box-sizing: border-box;
}
.btn {
  margin-right: 10px;
}
</style>