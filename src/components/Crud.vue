// filepath: /c:/project2/sdgs-dashboard/src/components/Crud.vue

<template>
  <div>
    <div class="Title-container">
      <h1>Manage Data</h1>
    </div>
    <!-- Tambahkan container untuk tombol -->
    <div class="button-container">
      <button @click="navigateToAdd" class="primary-button">Add Document</button>
      <button @click="toggleSortOrder" class="sort-button">Sort</button>
    </div>
    <table v-if="documents.length">
      <thead>
        <tr>
          <th>NO</th>
          <th title="Country Name">Country Name</th>
          <th title="Country ISO3">Country ISO3</th>
          <th title="Year">Year</th>
          <th title="Agricultural land (sq. km)">Agri. land (sq. km)</th>
          <th title="Agricultural land (% of land area)">Agri. land (%)</th>
          <th title="Arable land (% of land area)">Arable land (%)</th>
          <th >Actions</th>
        </tr>
      </thead>
      
      <tbody>
        <tr v-for="(document, index) in documents" :key="document._id">
          <td>{{ index + 1 }}</td>
          <td>{{ document["Country Name"] }}</td>
          <td>{{ document["Country ISO3"] }}</td>
          <td>{{ document.Year }}</td>
          <td>{{ formatNumber(document.data["Agricultural land (sq. km)"]) }}</td>
          <td>{{ formatNumber(document.data["Agricultural land (% of land area)"]) }}</td>
          <td>{{ formatNumber(document.data["Arable land (% of land area)"]) }}</td>
          <td class="actions-container">
            <button class="btn-sm warning-button" @click="editDocument(document._id)">Edit</button>
            <button class="btn-sm danger-button" @click="confirmDelete(document._id)">Delete</button>
            <button class="btn-sm primary-button"  @click="viewDetailsWithAlert(document._id)">Detail</button>
          </td>
        </tr>
      </tbody>
    </table>
    <p v-else>No documents found.</p>
  </div>
</template>

<script>
import "@/assets/crud.css"; // Path Crud CSS untuk Crud.vue
import { fetchDocuments, deleteDocument,fetchDocumentById } from "@/api/api.js";
import Swal from 'sweetalert2';
// import axios from "axios";
export default {
  name: "CrudPage",
  data() {
    return {
      documents: [],
      sortOrder: 'desc', // Default sort order
      selectedDocument: null, // Untuk menyimpan dokumen yang dipilih
      showDetailModal: false, // Untuk mengontrol tampilan modal detail
    };
  },

  methods: {
    async loadDocuments() {
      try {
        const response = await fetchDocuments();
        console.log("API Response:", response); // Log the API response
        this.documents = response;
        this.sortDocuments(); // Sort documents after loading
      } catch (error) {
        console.error("Error loading documents:", error);
      }
    },
    sortDocuments() {
      this.documents.sort((a, b) => {
        if (this.sortOrder === 'desc') {
          return b.Year - a.Year;
        } else {
          return a.Year - b.Year;
        }
      });
    },
async viewDetailsWithAlert(documentId) {
  try {
    const response = await fetchDocumentById(documentId);
    console.log("API Response:", response); // Log the API response
    this.selectedDocument = response; // Menyimpan document yang terpilih

    // Buat konten yang ingin ditampilkan di SweetAlert2
    let details = '';
    
    // Loop untuk mengecek semua field dan hanya menampilkan yang bukan undefined
    const fields = [
      "Country Name",
      "Country ISO3",
      "Year",
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
    ];
    
    fields.forEach(field => {
      // Cek apakah nilai field tersebut ada (bukan undefined)
      if (this.selectedDocument[field] !== undefined && this.selectedDocument[field] !== null) {
        details += `<div><strong>${field}:</strong> ${this.selectedDocument[field]}<div/>`;
      }
      else if (this.selectedDocument.data[field] !== undefined && this.selectedDocument.data[field] !== null) {
        details += `<div><strong>${field}:</strong> ${this.selectedDocument.data[field]}<div/>`;
      }
    });

    // Tampilkan detail menggunakan SweetAlert2
    await Swal.fire({
      title: 'Document Details',
      html: details,
      icon: 'info',
      confirmButtonText: 'Close'
    });

    // Setelah menutup alert, load ulang data untuk menampilkan data awal
    this.loadDocuments();
  } catch (error) {
    console.error("Error fetching document details:", error);
    await Swal.fire({
      title: 'Error',
      text: 'Failed to fetch document details. Please try again.',
      icon: 'error',
      confirmButtonText: 'Close'
    });
  }
},

    formatNumber(value) {
      if (typeof value === "number") {
        return value.toFixed(2); // Format angka hingga 2 desimal
      }
      return value;
    },
    toggleSortOrder() {
      // Toggle the sort order between 'asc' and 'desc'
      this.sortOrder = this.sortOrder === 'desc' ? 'asc' : 'desc';
      this.sortDocuments(); // Re-sort documents after toggling
    },
    async deleteDocument(id) {
      try {
        await deleteDocument(id);
        this.loadDocuments(); // Reload documents after deletion
      } catch (error) {
        console.error(`Error deleting document with ID ${id}:`, error);
      }
    },
    confirmDelete(id) {
      if (confirm("Are you sure you want to delete this document?")) {
        this.deleteDocument(id);
      }
    },

    editDocument(id) {
      this.$router.push(`/edit/${id}`); // Navigate to the edit page
    },
    navigateToAdd() {
      this.$router.push('/add'); // Navigate to the add page
    },
    // eslint-disable-next-line no-dupe-keys, vue/no-dupe-keys
    formatNumber(value) {
      if (typeof value === 'number') {
        return value.toFixed(2); // Format number to 2 decimal places
      }
      return value;
    }
  },
  mounted() {
    this.loadDocuments();
  }
  
};
</script>

