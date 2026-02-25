import { useEffect, useState } from "react";
import API from "./src/services/api";
import CourseCard from "./src/components/CourseCard";

interface Course {
  title: string;
  price: number;
  thumbnail: string;
}

const Home = () => {
  const [courses, setCourses] = useState<Course[]>([]);

  useEffect(() => {
    API.get("/courses")
      .then((res) => setCourses(res.data))
      .catch((err) => console.log(err));
  }, []);

  return (
    <>
      <div className="bg-gradient-to-r from-purple-700 to-pink-500 text-white p-20 text-center">
        <h1 className="text-5xl font-bold mb-4">Learn Without Limits</h1>
        <p className="text-xl">Build skills with top instructors</p>
      </div>

      <div className="grid grid-cols-4 gap-8 p-12 bg-gray-100">
        {courses.map((course, index) => (
          <CourseCard key={index} course={course} />
        ))}
      </div>
    </>
  );
};

export default Home;