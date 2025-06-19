document.addEventListener("DOMContentLoaded", () => {
  fetchEntries();

  const form = document.getElementById("entry-form");
  form.addEventListener("submit", function (e) {
    e.preventDefault(); 
    addEntry();
  });
});


function fetchEntries() {
  fetch("http://127.0.0.1:5000/entries")
    .then(res => res.json())
    .then(data => {
      const container = document.getElementById("entries-container");
      container.innerHTML = "";

      if (data.length === 0) {
        container.textContent = "No journal entries yet.";
        return;
      }

      data.forEach(entry => {
        const div = document.createElement("div");
        div.className = "entry";
        div.innerHTML = `
          <h3>${entry.date}</h3>
          <p><strong>Mood:</strong> ${entry.mood || "N/A"}</p>
          <p>${entry.entry}</p>
          <hr/>
        `;
        container.appendChild(div);
      });
    })
    .catch(err => {
      console.error("Error fetching entries:", err);
    });
}


function addEntry() {
  const date = document.getElementById("date").value;
  const mood = document.getElementById("mood").value;
  const entry = document.getElementById("entry").value;

  if (!date || !entry) {
    alert("Please fill in all fields.");
    return;
  }

  fetch("http://127.0.0.1:5000/entries", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ date, mood, entry })
  }) 
    .then(res => res.json())
    .then(data => {
      console.log("Entry added:", data);
      fetchEntries(); // Refresh the entries list
      document.getElementById("date").value = "";
      document.getElementById("mood").value = "";
      document.getElementById("entry").value = "";
    })
    .catch(err => {
      console.error("Error adding entry:", err);
    });
}