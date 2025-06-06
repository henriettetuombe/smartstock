function loadLanguage(langCode) {
  fetch(`../lang/${langCode}.json`)
    .then(response => {
      if (!response.ok) {
        throw new Error(`Language file not found: ${langCode}`);
      }
      return response.json();
    })
    .then(data => {
      document.querySelectorAll("[data-i18n]").forEach(el => {
        const key = el.getAttribute("data-i18n");
        if (data[key]) {
          // Use innerText for better accessibility; fallback to textContent if needed
          el.innerText = data[key];
        } else {
          console.warn(`Missing translation for key: "${key}" in ${langCode}`);
        }
      });
      localStorage.setItem("selectedLanguage", langCode);
    })
    .catch(error => {
      console.error("Language loading error:", error);
      alert("Sorry, this language file could not be loaded. Defaulting to English.");
      if (langCode !== "en") loadLanguage("en");
    });
}

// Load saved language preference or fallback to 'en'
document.addEventListener("DOMContentLoaded", () => {
  const langSelector = document.getElementById("lang-select");
  const savedLang = localStorage.getItem("selectedLanguage") || "en";
  
  if (langSelector) {
    langSelector.value = savedLang;
    langSelector.addEventListener("change", function () {
      loadLanguage(this.value);
    });
  }

  loadLanguage(savedLang);
});
