import { useEffect, useState } from "react";
import { Link } from "react-router-dom";

const dummyCourses = [
  { id: 1, title: "React for Beginners", instructor: "John Doe" },
  { id: 2, title: "Python Complete Course", instructor: "Jane Smith" },
  { id: 3, title: "MongoDB Mastery", instructor: "Alex Johnson" },
];

function Home() {
  const [isLoggedIn, setIsLoggedIn] = useState(false);

  useEffect(() => {
    const token = localStorage.getItem("access_token");
    setIsLoggedIn(!!token);
  }, []);

  return (
    <div>
      {/* Navbar */}
      <nav className="navbar">
        <h2 className="logo">LMS</h2>

        <input
          type="text"
          placeholder="Search for courses..."
          className="search-bar"
        />

        <div>
          {!isLoggedIn ? (
            <>
              <Link to="/login">Login</Link> |{" "}
              <Link to="/register">Sign Up</Link>
            </>
          ) : (
            <span className="user-icon">👤</span>
          )}
        </div>
      </nav>

      {/* Popular Courses */}
      <section className="popular">
        <h2>🔥 Popular Courses</h2>
        <div className="course-grid">
          {dummyCourses.map((course) => (
            <div key={course.id} className="course-card">
              <h3>{course.title}</h3>
              <p>{course.instructor}</p>
              <button>View Course</button>
            </div>
          ))}
        </div>
      </section>
    </div>
  );
}

export default Home;