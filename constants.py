TEMPLATE_QFMT = """<h1>{{Header}}</h1>
<textarea id="userInput" rows="4" cols="50" placeholder="在这里写下你的思路..."></textarea>
{{Front}}

<!-- Clear previous input value when loading the front page -->
<script>
  // Clear any previously stored answer when the front side loads
  localStorage.removeItem("ankiUserAnswer");

  // Save new input value when the user types
  document.addEventListener("input", () => {
    const textarea = document.getElementById("userInput");
    if (textarea) {
      localStorage.setItem("ankiUserAnswer", textarea.value);
    }
  });

</script>

"""

TEMPLATE_AFMT = """<h1>{{Header}}</h1>{{Front}}
<hr id="answer" />
{{Back}}
<hr />
<p class="user-input">
  <strong>你的思路:</strong>
  <strong id="userInputValue"></strong>
</p>

<script>
document.getElementById('userInputValue').innerHTML = localStorage.getItem("ankiUserAnswer")?.replace(/\n/g, "<p/>") || "空";

</script>"""

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

textarea{
	box-sizing: border-box;
    width: 100%; /* Full width of the container */
    padding: 10px; /* Inner spacing for better readability */
    font-size: 12px; /* Larger font size for clarity */
    font-family: Arial, sans-serif; /* Clean and readable font */
    border: 1px solid #ccc; /* Subtle border for structure */
    border-radius: 5px; /* Rounded corners for a modern look */
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); /* Soft shadow for depth */
    outline: none; /* Remove default focus outline */
    resize: vertical; /* Allow vertical resizing only */
 }

.user-input {
  font-size: 12px;
  line-height: 1.5;
  color: #333;
  font-family: Arial, sans-serif;
}

.user-input #userInputValue, .user-input p {
  color: #007BFF;
  font-weight: bold;
}

"""
