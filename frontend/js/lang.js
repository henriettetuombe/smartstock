const translations = {
  en: {
    hero_title: "Inventory Made Simple",
    hero_description: "SmartStock helps individuals and businesses track stock easily.",
    signup_btn: "Get Started",
    why_title: "Why Choose SmartStock?",
    feature_1: "Simple Tracking",
    feature_1_desc: "Easily monitor what's coming in and going out.",
    feature_2: "Multilingual Support",
    feature_2_desc: "Switch between English, French, and Kinyarwanda.",
    feature_3: "Mobile Ready",
    feature_3_desc: "Works perfectly on all devices.",
    feature_4: "Analytics",
    feature_4_desc: "Visualize your stock trends in real-time.",
    footer_text: "© 2025 SmartStock. All rights reserved.",
  },
  fr: {
    hero_title: "Gestion de Stock Simplifiée",
    hero_description: "SmartStock vous aide à suivre facilement les stocks.",
    signup_btn: "Commencer",
    why_title: "Pourquoi Choisir SmartStock ?",
    feature_1: "Suivi Simple",
    feature_1_desc: "Suivez facilement les entrées et les sorties.",
    feature_2: "Support Multilingue",
    feature_2_desc: "Passez entre l'anglais, le français et le kinyarwanda.",
    feature_3: "Compatible Mobile",
    feature_3_desc: "Fonctionne parfaitement sur tous les appareils.",
    feature_4: "Analytique",
    feature_4_desc: "Visualisez vos tendances de stock en temps réel.",
    footer_text: "© 2025 SmartStock. Tous droits réservés.",
  },
  rw: {
    hero_title: "Gucunga Stokis Byoroshye",
    hero_description: "SmartStock ifasha abantu n’abacuruzi gukurikirana ibicuruzwa.",
    signup_btn: "Tangira",
    why_title: "Impamvu Guhitamo SmartStock",
    feature_1: "Gukurikirana Byoroshye",
    feature_1_desc: "Kurikirana ibyinjiye n’ibyasohotse neza.",
    feature_2: "Indimi nyinshi",
    feature_2_desc: "Hitamo Icyongereza, Igifaransa, cyangwa Ikinyarwanda.",
    feature_3: "Ikoreshwa kuri telefoni",
    feature_3_desc: "Ikoreshwa kuri mudasobwa na telefoni.",
    feature_4: "Ibyegeranyo",
    feature_4_desc: "Reba amakuru ya stokis mu buryo bw’amashusho.",
    footer_text: "© 2025 SmartStock. Uburenganzira bwose burabitswe.",
  },
};

const currentLang = localStorage.getItem("lang") || "en";

function translate(lang) {
  const elements = document.querySelectorAll("[data-i18n]");
  elements.forEach((el) => {
    const key = el.getAttribute("data-i18n");
    if (translations[lang] && translations[lang][key]) {
      el.textContent = translations[lang][key];
    }
  });
  localStorage.setItem("lang", lang);
  document.getElementById("currentLang").textContent =
    lang === "rw" ? "Kinyarwanda" : lang === "fr" ? "Français" : "English";
}

document.addEventListener("DOMContentLoaded", () => {
  translate(currentLang);

  const button = document.getElementById("langButton");
  const dropdown = document.getElementById("langDropdown");

  button.addEventListener("click", () => {
    dropdown.classList.toggle("hidden");
  });

  dropdown.querySelectorAll("li").forEach((item) => {
    item.addEventListener("click", () => {
      const selectedLang = item.getAttribute("data-lang");
      translate(selectedLang);
      dropdown.classList.add("hidden");
    });
  });
});
