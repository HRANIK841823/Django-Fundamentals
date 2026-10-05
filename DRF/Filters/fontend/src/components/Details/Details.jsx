import { useEffect, useState } from "react";
import { useLoaderData, Link } from "react-router-dom";

const Details = () => {
  const loader = useLoaderData();
  const [phone, setPhone] = useState(null);

  useEffect(() => {
    setPhone(loader);
  }, [loader]);

  if (!phone) {
    return <div className="text-center mt-20 text-gray-600 text-lg">Loading...</div>;
  }

  return (
    <div className="max-w-3xl mx-auto mt-12 p-8 bg-white rounded-2xl shadow-lg text-gray-900 font-sans">
      <Link 
        to="/user"
        className="inline-block mb-6 px-5 py-2 text-blue-600 border border-blue-600 rounded-full hover:bg-blue-600 hover:text-white transition"
      >
        &larr; Back to list
      </Link>

      <h1 className="text-4xl font-extrabold mb-6">{phone.name}</h1>

      <div className="flex justify-center mb-6">
        <img 
          src={phone.image} 
          alt={phone.name} 
          className="w-full max-w-md rounded-xl shadow-md object-cover"
          loading="lazy"
        />
      </div>

      <p className="mb-6 text-lg leading-relaxed text-gray-700">{phone.description}</p>

      <ul className="grid grid-cols-2 gap-y-3 gap-x-6 text-gray-800 font-medium">
        <li>
          <span className="font-semibold">Price:</span> ${phone.price}
        </li>
        <li>
          <span className="font-semibold">Storage:</span> {phone.storage} GB
        </li>
      
        <li>
          <span className="font-semibold">SIM Type:</span> {phone.sim}
        </li>
        <li className="col-span-2">
          <span className="font-semibold">Availability:</span>{" "}
          <span className={`inline-block px-3 py-1 rounded-full text-sm font-semibold ${
            phone.isAvailable ? "bg-green-200 text-green-800" : "bg-red-200 text-red-800"
          }`}>
            {phone.isAvailable ? "In Stock" : "Out of Stock"}
          </span>
        </li>
      </ul>
    </div>
  );
};

export default Details;

