import { StrictMode } from 'react';
import { createRoot } from 'react-dom/client';
import './index.css';
import App from './App.jsx';
import AdminPhones from './components/AdminPhones/AdminPhones.jsx';
import Error from './components/Error/Error.jsx';
import UserPhones from './components/UserPhones/UserPhones.jsx';
import Details from './components/Details/Details.jsx';
import {createBrowserRouter,RouterProvider} from "react-router-dom";

const router = createBrowserRouter([
  {
    path: '/',
    element: <App />,
    errorElement: <Error />,
    children: [
      {
        path: 'admin',
        element: <AdminPhones />
      },
      {
        path: 'user',
        element: <UserPhones />
      },
      {
        path:'user/:id',
        loader:({params})=>fetch(`http://127.0.0.1:8000/api/phones/${params.id}`),
        element:<Details></Details>
      }
    ]
  },
]);

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <RouterProvider router={router} />
  </StrictMode>
);
