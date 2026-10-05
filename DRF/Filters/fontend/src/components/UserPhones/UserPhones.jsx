import React, { useEffect, useState } from "react";
import axios from "axios";

export default function UserPhones() {
  const API_URL = "http://localhost:8000/api/phones/";

  const brandOptions = [
    "apple", "samsung", "xiaomi", "oppo", "vivo", "realme", "oneplus",
    "google", "nokia", "motorola", "huawei", "infinix", "tecno", "sony", "asus"
  ];
  const availabilityOptions = ["in_stock", "online_order", "pre_order"];
  const storageOptions = ["12_128", "12_256", "12_512", "12_1tb", "128", "256", "512", "1tb"];
  const typeOptions = ["exynos_5g", "inactive", "regular_box", "slim_box", "snapdragon_5g"];
  const simOptions = ["dual", "lte", "single", "wifi", "e_sim"];

  const [phones, setPhones] = useState([]);
  const [filters, setFilters] = useState({
    search: "",
    brand: "",
    availability: "",
    storage: "",
    type: "",
    sim: "",
    ordering: "",
    min_price: "",
    max_price: ""
  });

  const fetchPhones = async () => {
    const params = {};
    Object.keys(filters).forEach((key) => {
      if (filters[key]) params[key] = filters[key];
    });

    const res = await axios.get(API_URL, { params });
    setPhones(res.data);
  };

  useEffect(() => {
    fetchPhones();
  }, [filters]);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFilters({ ...filters, [name]: value });
  };

  return (
    <div className="p-6 max-w-7xl mx-auto bg-gradient-to-br from-gray-50 to-white min-h-screen">
  <h2 className="text-3xl font-extrabold mb-8 text-indigo-600 flex items-center gap-2">
    📱 Browse Phones
  </h2>

  <div className="grid grid-cols-1 md:grid-cols-4 gap-8">
    {/* Filters Sidebar */}
    <div className="bg-white p-6 shadow-lg rounded-xl border border-gray-200 space-y-5">
      <input
        name="search"
        placeholder="🔍 Search model..."
        value={filters.search}
        onChange={handleChange}
        className="border border-indigo-300 focus:ring-2 focus:ring-indigo-400 focus:outline-none p-2 rounded-lg w-full"
      />

      <select
        name="brand"
        value={filters.brand}
        onChange={handleChange}
        className="border border-indigo-300 focus:ring-2 focus:ring-indigo-400 focus:outline-none p-2 rounded-lg w-full"
      >
        <option value="">All Brands</option>
        {brandOptions.map((b) => (
          <option key={b} value={b}>{b}</option>
        ))}
      </select>

      <select
        name="availability"
        value={filters.availability}
        onChange={handleChange}
        className="border border-indigo-300 focus:ring-2 focus:ring-indigo-400 focus:outline-none p-2 rounded-lg w-full"
      >
        <option value="">Availability</option>
        {availabilityOptions.map((a) => (
          <option key={a} value={a}>{a}</option>
        ))}
      </select>

      <select
        name="storage"
        value={filters.storage}
        onChange={handleChange}
        className="border border-indigo-300 focus:ring-2 focus:ring-indigo-400 focus:outline-none p-2 rounded-lg w-full"
      >
        <option value="">Storage</option>
        {storageOptions.map((s) => (
          <option key={s} value={s}>{s}</option>
        ))}
      </select>

      <select
        name="type"
        value={filters.type}
        onChange={handleChange}
        className="border border-indigo-300 focus:ring-2 focus:ring-indigo-400 focus:outline-none p-2 rounded-lg w-full"
      >
        <option value="">Type</option>
        {typeOptions.map((t) => (
          <option key={t} value={t}>{t}</option>
        ))}
      </select>

      <select
        name="sim"
        value={filters.sim}
        onChange={handleChange}
        className="border border-indigo-300 focus:ring-2 focus:ring-indigo-400 focus:outline-none p-2 rounded-lg w-full"
      >
        <option value="">SIM</option>
        {simOptions.map((s) => (
          <option key={s} value={s}>{s}</option>
        ))}
      </select>

      <div className="space-y-2">
        <input
          name="min_price"
          type="number"
          placeholder="💰 Min Price"
          value={filters.min_price}
          onChange={handleChange}
          className="border border-indigo-300 focus:ring-2 focus:ring-indigo-400 focus:outline-none p-2 rounded-lg w-full"
        />
        <input
          name="max_price"
          type="number"
          placeholder="💸 Max Price"
          value={filters.max_price}
          onChange={handleChange}
          className="border border-indigo-300 focus:ring-2 focus:ring-indigo-400 focus:outline-none p-2 rounded-lg w-full"
        />
      </div>

      <select
        name="ordering"
        value={filters.ordering}
        onChange={handleChange}
        className="border border-indigo-300 focus:ring-2 focus:ring-indigo-400 focus:outline-none p-2 rounded-lg w-full"
      >
        <option value="">Sort By</option>
        <option value="price">Price Asc</option>
        <option value="-price">Price Desc</option>
      </select>
    </div>

    {/* Phones Grid */}
    <div className="md:col-span-3 grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-8">
      {phones.map((phone) => (
        <div
          key={phone.id}
          className="bg-white rounded-2xl shadow-md p-5 hover:shadow-xl transition duration-300 flex flex-col items-center border border-gray-100"
        >
          {phone.image && (
            <img
              src={phone.image}
              alt={phone.model_name}
              className="h-40 object-contain mb-4"
            />
          )}
          <h3 className="font-bold text-xl text-gray-800">{phone.model_name}</h3>
          <p className="text-sm text-gray-500 mb-1">{phone.brand}</p>
          <p className="text-lg font-semibold text-indigo-600">${phone.price}</p>
          <span className="text-xs bg-indigo-100 text-indigo-700 px-3 py-1 rounded-full mt-2 capitalize">
            {phone.availability}
          </span>
        </div>
      ))}
    </div>
  </div>
</div>

  );
}
