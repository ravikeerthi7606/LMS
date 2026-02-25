function Footer() {
  return (
    <footer style={{ padding: "30px", background: "#000", marginTop: "40px" }}>
      <h3>About Us</h3>
      <p>This LMS platform provides quality education worldwide.</p>

      <h3>Help & Support</h3>
      <p>Email: support@lms.com</p>

      <p style={{ marginTop: "20px" }}>
        © {new Date().getFullYear()} LMS. All rights reserved.
      </p>
    </footer>
  );
}

export default Footer;