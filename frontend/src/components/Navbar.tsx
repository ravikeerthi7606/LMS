import { Link } from "react-router-dom";

const Navbar = () => {
  return (
    <div className="bg-black text-white px-8 py-4 flex justify-between items-center">
      <Link to="/" className="text-2xl font-bold text-purple-500">
        LMS
      </Link>

      <div className="flex gap-6 items-center">
        <input
          type="text"
          placeholder="Search for anything"
          className="px-4 py-2 rounded-md text-black w-96"
        />

        <Link to="/login" className="border px-4 py-2 rounded-md hover:bg-white hover:text-black transition">
          Login
        </Link>
      </div>
    </div>
  );
};

export default Navbar;