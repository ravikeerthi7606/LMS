interface Course {
  title: string;
  price: number;
  thumbnail: string;
}

const CourseCard = ({ course }: { course: Course }) => {
  return (
    <div className="bg-white shadow-md rounded-lg overflow-hidden hover:shadow-xl transition">
      <img
        src={course.thumbnail}
        alt={course.title}
        className="w-full h-40 object-cover"
      />
      <div className="p-4">
        <h3 className="font-semibold text-lg">{course.title}</h3>
        <p className="text-purple-600 font-bold mt-2">₹{course.price}</p>
        <button className="mt-4 w-full bg-purple-600 text-white py-2 rounded-md hover:bg-purple-700">
          Enroll Now
        </button>
      </div>
    </div>
  );
};

export default CourseCard;