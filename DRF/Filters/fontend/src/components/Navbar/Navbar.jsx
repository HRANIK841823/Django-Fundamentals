import { NavLink } from "react-router-dom";

const Navbar = () => {
  const linkStyle = ({ isActive }) =>
    isActive
      ? "text-blue-500 font-semibold border-b-2 border-blue-500"
      : "text-gray-300 hover:text-white transition duration-200";

  return (
    <nav className="bg-gray-800 shadow-md px-6 py-4">
      <div className="max-w-7xl mx-auto flex justify-between items-center">
        {/* Logo or Brand */}
        <div className="text-white text-2xl font-bold tracking-wide">
          MyApp
        </div>

        {/* Navigation Links */}
        <div className="flex space-x-8 text-lg">
         
          <NavLink to="/User" className={linkStyle}>
            Home
          </NavLink>
          <NavLink to="/Admin" className={linkStyle}>
            Admin
          </NavLink>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
