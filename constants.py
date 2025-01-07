TEMPLATE_QFMT = "<h1 >{{Header}}</h1>\n{{Front}}"

TEMPLATE_AFMT = '{{FrontSide}}<hr id="answer">{{Back}}'

CSS_STYLE = """
.card {
  font-family: 'Arial', sans-serif; /* Use a clean, modern font */
  font-size: 10px; /* Increase readability */
  color: #333; /* Slightly softer black for better contrast */
  background-color: #f9f9f9; /* Light gray for a softer look */
  border-radius: 10px; /* Rounded corners */
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); /* Subtle shadow for depth */
  padding: 20px; /* Add inner spacing */
  margin: 10px auto; /* Center the card and add space between them */
  max-width: 400px; /* Constrain the card width */
  line-height: 1.5; /* Improve text readability */
  transition: transform 0.2s ease, box-shadow 0.2s ease; /* Smooth animations */
}

pre{
  white-space: pre-wrap;
}

.card h1, .card h2, .card h3 {
  color: #0073e6; /* Accent color for headings */
  margin-bottom: 10px; /* Spacing below headings */
}

.card p {
  color: #555; /* Softer text color for paragraphs */
  margin-bottom: 10px; /* Spacing between paragraphs */
}

.card a {
  color: #0073e6; /* Link color */
  text-decoration: none; /* Remove underline */
  font-weight: bold; /* Make links stand out */
}

.card a:hover {
  text-decoration: underline; /* Add underline on hover */
}
"""
