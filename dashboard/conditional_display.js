// Conditional Display Engine

function parseDisplayRule(rule) {
  const [fieldId, expected] = rule.split(":");
  return { fieldId, expected };
}

function getFieldValue(field) {
  if (!field) return null;

  if (field.type === "checkbox") {
    return field.checked ? "checked" : "unchecked";
  }

  if (field.type === "radio") {
    const group = document.querySelectorAll(`input[name="${field.name}"]`);
    const checked = Array.from(group).find(r => r.checked);
    return checked ? checked.value : null;
  }

  return field.value;
}

function checkCondition(field, expected) {
  const actual = getFieldValue(field);
  return actual === expected;
}

function getDisplayContainer(el) {
  return el.parentElement;
}

function evaluateDisplay(el) {
  // Obtains data-display value
  const raw = (el.dataset.display || "").trim();

  if (!raw) return;

  const rules = raw.split(/\s+/).filter(r => r !== "");

  for (const rule of rules) {
    const { fieldId, expected } = parseDisplayRule(rule);
    const field = document.getElementById(fieldId);

    if (!checkCondition(field, expected)) {
      const container = getDisplayContainer(el);
      if (container) {
        container.style.display = "none"
      };
      
      return;
    }
  }
  
  const container = getDisplayContainer(el);
  if (container) {
    container.style.display = "";
  }
}

function evaluateAllDisplays() {
  const elements = document.querySelectorAll("[data-display]");
  elements.forEach(evaluateDisplay);
}

function handleDisplayEvent(e) {
  // Only react if the changed element could affect conditions
  if (!e.target.id && !e.target.name) return;
  evaluateAllDisplays();
}

// Event delegation
document.addEventListener("change", handleDisplayEvent);
document.addEventListener("input", handleDisplayEvent);

// Initial evaluation on page load
document.addEventListener("DOMContentLoaded", evaluateAllDisplays);