import React, { useState, useEffect } from 'react';
import axios from 'axios';

const Filter = () => {
  const [phones, setPhones] = useState([]);
  const [filters, setFilters] = useState({
    availability: '',
    storage: '',
    phone_type: '',
    sim: '',
    sort: '', // for price sorting
  });

  const fetchPhones = async () => {
    try {
      const query = new URLSearchParams({
        ...filters,
        ordering: filters.sort === 'asc' ? 'price' : filters.sort === 'desc' ? '-price' : '',
      }).toString();
      const response = await axios.get(`http://localhost:8000/api/phones/?${query}`);
      setPhones(response.data);
    } catch (error) {
      console.error('Error fetching phones:', error);
    }
  };

  useEffect(() => {
    fetchPhones();
  }, [filters]);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFilters((prev) => ({
      ...prev,
      [name]: value,
    }));
  };

  return (
    <div className="max-w-7xl mx-auto p-6 bg-gray-50 min-h-screen">
      <h1 className="text-4xl font-extrabold text-gray-800 mb-8 text-center drop-shadow-sm">
        Phone Marketplace
      </h1>

      {/* Filters */}
      <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-5 gap-5 mb-10">
        {[
          {
            name: 'availability',
            label: 'Availability',
            options: [
              { value: '', label: 'All' },
              { value: 'in_stock', label: 'In Stock' },
              { value: 'online_order', label: 'Online Order' },
              { value: 'pre_order', label: 'Pre Order' },
            ],
          },
          {
            name: 'storage',
            label: 'Storage',
            options: [
              { value: '', label: 'All' },
              { value: '12_128GB', label: '12/128GB' },
              { value: '12_1TB', label: '12/1TB' },
              { value: '12_256GB', label: '12/256GB' },
              { value: '12_512GB', label: '12/512GB' },
              { value: '128GB', label: '128GB' },
            ],
          },
          {
            name: 'phone_type',
            label: 'Type',
            options: [
              { value: '', label: 'All' },
              { value: '4g', label: '4G' },
              { value: 'exynos_5g', label: 'Exynos 5G' },
              { value: 'inactive', label: 'Inactive' },
              { value: 'regular_box', label: 'Regular Box' },
              { value: 'slim_box', label: 'Slim Box' },
            ],
          },
          {
            name: 'sim',
            label: 'SIM',
            options: [
              { value: '', label: 'All' },
              { value: 'dual', label: 'Dual' },
              { value: 'lte', label: 'LTE' },
              { value: 'single', label: 'Single' },
              { value: 'wifi', label: 'Wi-Fi' },
              { value: 'e_sim', label: 'e-Sim' },
            ],
          },
          {
            name: 'sort',
            label: 'Sort by Price',
            options: [
              { value: '', label: 'None' },
              { value: 'asc', label: 'Low to High' },
              { value: 'desc', label: 'High to Low' },
            ],
          },
        ].map(({ name, label, options }) => (
          <select
            key={name}
            name={name}
            onChange={handleChange}
            className="w-full p-3 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-indigo-500 transition"
            value={filters[name]}
          >
            {options.map(({ value, label }) => (
              <option key={value} value={value}>
                {label}
              </option>
            ))}
          </select>
        ))}
      </div>

      {/* Phones Grid */}
      <div className="grid gap-8 sm:grid-cols-1 md:grid-cols-2 lg:grid-cols-3">
        {phones.length === 0 ? (
          <p className="col-span-full text-center text-gray-500 text-lg">No phones found.</p>
        ) : (
          phones.map((phone) => (
            <div
              key={phone.id}
              className="bg-white rounded-lg shadow-md hover:shadow-xl transition-shadow duration-300 overflow-hidden"
            >
              {phone.image ? (
                <img
                  src={`http://localhost:8000${phone.image}`}
                  alt={phone.name}
                  className="w-full h-48 object-cover"
                  loading="lazy"
                />
              ) : (
                <div className="w-full h-48 bg-gray-200 flex items-center justify-center text-gray-400">
                  No Image
                </div>
              )}
              <div className="p-5">
                <h2 className="text-2xl font-semibold mb-2 text-gray-900">{phone.name}</h2>
                <div className="space-y-1 text-gray-700">
                  <p>
                    <span className="font-medium text-indigo-600">Storage:</span> {phone.storage}
                  </p>
                  <p>
                    <span className="font-medium text-indigo-600">Type:</span> {phone.phone_type}
                  </p>
                  <p>
                    <span className="font-medium text-indigo-600">SIM:</span> {phone.sim}
                  </p>
                  <p>
                    <span className="font-medium text-indigo-600">Availability:</span>{' '}
                    {phone.availability.replace('_', ' ')}
                  </p>
                </div>
                <p className="mt-4 text-xl font-bold text-indigo-700">
                  Price: ৳{phone.price.toLocaleString()}
                </p>
              </div>
            </div>
          ))
        )}
      </div>
    </div>
  );
};

export default Filter;
