document.addEventListener("DOMContentLoaded", function () {
  const form = document.querySelector(".add-item-form");
  const tableBody = document.querySelector("table tbody");
  const searchInput = document.querySelector(".search-input");

  // Handle form submission
  form.addEventListener("submit", function (e) {
    e.preventDefault();

    const inputs = form.querySelectorAll("input, select");
    const [itemName, date, category, quantity, status] = inputs;

    if (!itemName.value || !date.value || !category.value || !quantity.value || !status.value) {
      alert("Please fill all fields.");
      return;
    }

    const row = document.createElement("tr");
    row.innerHTML = `
      <td><input type="checkbox" /></td>
      <td>${itemName.value}</td>
      <td>${new Date(date.value).toLocaleDateString('en-GB')}</td>
      <td>${category.value}</td>
      <td>${quantity.value}</td>
      <td>${status.value}</td>
    `;

    tableBody.appendChild(row);
    form.reset();
  });

  // Handle live search
  searchInput.addEventListener("keyup", function () {
    const searchTerm = searchInput.value.toLowerCase();
    const rows = tableBody.querySelectorAll("tr");

    rows.forEach(row => {
      const rowText = row.textContent.toLowerCase();
      row.style.display = rowText.includes(searchTerm) ? "" : "none";
    });
  });
});
