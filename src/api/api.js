import axios from "axios";

const API_URL = "http://127.0.0.1:8000"; // Replace with your FastAPI server URL

// Fetch all documents
export const fetchDocuments = async () => {
  try {
    const response = await axios.get(`${API_URL}/documents/`);
    return response.data;
  } catch (error) {
    console.error("Error fetching documents:", error);
    throw error;
  }
};

// Fetch a single document by ID
export const fetchDocumentById = async (id) => {
  try {
    const response = await axios.get(`${API_URL}/documents/${id}`);
    return response.data;
  } catch (error) {
    console.error(`Error fetching document with ID ${id}:`, error);
    throw error;
  }
};

// Create a new document
export const createDocument = async (document) => {
  try {
    const response = await axios.post(`${API_URL}/documents/`, document);
    return response.data;
  } catch (error) {
    console.error("Error creating document:", error);
    throw error;
  }
};

// Update an existing document by ID
export const updateDocumentById = async (id, document) => {
  try {
    const response = await axios.put(`${API_URL}/documents/${id}`, document);
    return response.data;
  } catch (error) {
    console.error(`Error updating document with ID ${id}:`, error);
    throw error;
  }
};

// Delete a document by ID
export const deleteDocument = async (id) => {
  try {
    const response = await axios.delete(`${API_URL}/documents/${id}`);
    return response.data;
  } catch (error) {
    console.error(`Error deleting document with ID ${id}:`, error);
    throw error;
  }
};
