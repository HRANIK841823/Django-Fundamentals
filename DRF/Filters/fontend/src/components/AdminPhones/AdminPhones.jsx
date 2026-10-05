import React, { useState, useEffect } from "react";
import axios from "axios";

export default function AdminPhones() {
  const API_URL = "http://localhost:8000/api/phones/";

  const brandOptions = ["apple", "samsung", "xiaomi", "oppo", "vivo", "realme", "oneplus","google", "nokia", "motorola", "huawei", "infinix", "tecno", "sony", "asus"];
  const availabilityOptions = ["in_stock", "online_order", "pre_order"];
  const storageOptions = ["12_128", "12_256", "12_512", "12_1tb", "128", "256", "512", "1tb"];
  const typeOptions = ["exynos_5g", "inactive", "regular_box", "slim_box", "snapdragon_5g"];
  const simOptions = ["dual", "lte", "single", "wifi", "e_sim"];

  const [phones, setPhones] = useState([]);
  const [imagePreview, setImagePreview] = useState(null);
  const [editId, setEditId] = useState(null);
  // Predefined Form
  const [form, setForm] = useState({
    model_name: "",
    brand: "",
    price: "",
    availability: "",
    storage: "",
    type: "",
    sim: "",
    image: null
  });
  
  // Fetch Phones with function and then called Function in useEffect
  const fetchPhones = async () => {
    const res = await axios.get(API_URL);
    setPhones(res.data);
  };

  useEffect(() => {
    fetchPhones();
  }, []);


  // main product change in input value
  const handleChange = (e) => {
    console.log(e.target);
    const { name, value, files } = e.target;
    if (files) {
      setForm({ ...form, [name]: files[0] });
      setImagePreview(URL.createObjectURL(files[0]));
    } else {
      setForm({ ...form, [name]: value });
    }
  };


  //  when submit button click
  const handleSubmit = async (e) => {
    e.preventDefault();
    const formData = new FormData();

    Object.keys(form).forEach((key) => {
      // Skip appending image if we're editing and no new file is chosen
      if (key === "image" && !form[key]) return;
      formData.append(key, form[key]);
    });

    if (editId) {
      // Partial update with PATCH
      await axios.patch(`${API_URL}${editId}/`, formData, {
        headers: { "Content-Type": "multipart/form-data" }
      });
    } else {
      // Create new phone
      await axios.post(API_URL, formData, {
        headers: { "Content-Type": "multipart/form-data" }
      });
    }

    resetForm();
    fetchPhones();
  };


  // for delete a api
  const handleDelete = async (id) => {
    await axios.delete(`${API_URL}${id}/`);
    fetchPhones();
  };

  const handleEdit = (phone) => {
    setEditId(phone.id);
    setForm({
      model_name: phone.model_name,
      brand: phone.brand,
      price: phone.price,
      availability: phone.availability,
      storage: phone.storage,
      type: phone.type,
      sim: phone.sim,
      image: phone.image // Keep null until a new file is uploaded
    });

    setImagePreview(
      phone.image ? `${phone.image}` : null
    );
  };


  // When submit done this is out Rest Form
  const resetForm = () => {
    setForm({
      model_name: "",
      brand: "",
      price: "",
      availability: "",
      storage: "",
      type: "",
      sim: "",
      image: null
    });
    setImagePreview(null);
    setEditId(null);
  };

  // main Html
  return (
    <div className="p-6 max-w-5xl mx-auto">
      <h2 className="text-2xl font-bold mb-6">
        📱 Admin - {editId ? "Edit Phone" : "Add Phone"}
      </h2>

      {/* Form */}
      <form
        onSubmit={handleSubmit}
        className="grid grid-cols-1 md:grid-cols-2 gap-4 bg-white shadow-lg p-6 rounded-lg mb-8"
      >
        <input
          name="model_name"
          placeholder="Model Name"
          value={form.model_name}
          onChange={handleChange}
          className="border p-2 rounded"
        />
        <select
          name="brand"
          value={form.brand}
          onChange={handleChange}
          className="border p-2 rounded"
        >
          <option value="">Select Brand</option>
          {brandOptions.map((b) => (
            <option key={b} value={b}>{b}</option>
          ))}
        </select>
        <input
          name="price"
          type="number"
          placeholder="Price"
          value={form.price}
          onChange={handleChange}
          className="border p-2 rounded"
        />
        <select
          name="availability"
          value={form.availability}
          onChange={handleChange}
          className="border p-2 rounded"
        >
          <option value="">Select Availability</option>
          {availabilityOptions.map((a) => (
            <option key={a} value={a}>{a}</option>
          ))}
        </select>
        <select
          name="storage"
          value={form.storage}
          onChange={handleChange}
          className="border p-2 rounded"
        >
          <option value="">Select Storage</option>
          {storageOptions.map((s) => (
            <option key={s} value={s}>{s}</option>
          ))}
        </select>
        <select
          name="type"
          value={form.type}
          onChange={handleChange}
          className="border p-2 rounded"
        >
          <option value="">Select Type</option>
          {typeOptions.map((t) => (
            <option key={t} value={t}>{t}</option>
          ))}
        </select>
        <select
          name="sim"
          value={form.sim}
          onChange={handleChange}
          className="border p-2 rounded"
        >
          <option value="">Select SIM</option>
          {simOptions.map((s) => (
            <option key={s} value={s}>{s}</option>
          ))}
        </select>
        <input
          name="image"
          type="file"
          onChange={handleChange}
          className="border p-2 rounded"
        />

        {imagePreview && (
          <div className="col-span-2">
            <img
              src={imagePreview}
              alt="Preview"
              className="h-32 rounded shadow"
            />
          </div>
        )}

        <div className="col-span-2 flex gap-2">
          <button
            type="submit"
            className="bg-blue-600 hover:bg-blue-700 text-white py-2 px-4 rounded"
          >
            {editId ? "Update Phone" : "Add Phone"}
          </button>
          {editId && (
            <button
              type="button"
              onClick={resetForm}
              className="bg-gray-500 hover:bg-gray-600 text-white py-2 px-4 rounded"
            >
              Cancel Edit
            </button>
          )}
        </div>
      </form>

      {/* List */}
      <div className="bg-white shadow-lg p-6 rounded-lg">
        <h3 className="text-xl font-semibold mb-4">📋 Phone List</h3>
        <ul className="divide-y">
          {phones.map((phone) => (
            <li key={phone.id} className="flex justify-between items-center py-3">
              <div className="flex items-center space-x-4">
                {phone.image && (
                  <img
                    src={phone.image}
                    alt={phone.model_name}
                    className="h-12 w-12 object-cover rounded"
                  />
                )}
                <span>{phone.model_name} - {phone.brand} - ${phone.price}</span>
              </div>
              <div className="flex gap-2">
                <button
                  onClick={() => handleEdit(phone)}
                  className="bg-yellow-500 hover:bg-yellow-600 text-white px-3 py-1 rounded"
                >
                  Edit
                </button>
                <button
                  onClick={() => handleDelete(phone.id)}
                  className="bg-red-500 hover:bg-red-600 text-white px-3 py-1 rounded"
                >
                  Delete
                </button>
              </div>
            </li>
          ))}
        </ul>
      </div>
    </div>

  );
}
