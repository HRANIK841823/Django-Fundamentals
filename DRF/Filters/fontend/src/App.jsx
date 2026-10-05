import { Outlet, Link } from "react-router-dom";
import Navbar from "./components/Navbar/Navbar";
import Filter from "./components/Filter/Filter";
const App = () => {
  return (
    <div>
     
      <Navbar ></Navbar>
      <Outlet /> {/* Renders child components */}
      {/* <Filter></Filter> */}
    </div>
  );
};

export default App;
