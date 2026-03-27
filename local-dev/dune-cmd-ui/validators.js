// inject validation css
const style = document.createElement("style");
style.textContent = `
.invalid,
.invalid:focus {
  border: 2px solid red !important;
  outline: none !important;
}

.validation-error {
  color: red;
  font-size: 12px;
  margin-top: 4px;
}
`;
document.head.appendChild(style);

const validators = {
  required: value => value.trim() !== "" || "This field is required",

  number: value => {
    if (value.trim() === "") return true;
    return !Number.isNaN(Number(value)) || "Must be a number";
  },

  digit: value => {
    if (value.trim() === "") return true;
    return /^\d+$/.test(value) || "Digits only";
  },

  min: (value, min) => {
    if (value.trim() === "") return true;
    const v = Number(value);
    if (Number.isNaN(v)) return "Must be a number";
    return v >= Number(min) || `Must be >= ${min}`;
  },

  max: (value, max) => {
    if (value.trim() === "") return true;
    const v = Number(value);
    if (Number.isNaN(v)) return "Must be a number";
    return v <= Number(max) || `Must be <= ${max}`;
  },

  range: (value, min, max) => {
    if (value.trim() === "") return true;
    const v = Number(value);
    if (Number.isNaN(v)) return "Must be a number";
    return (v >= Number(min) && v <= Number(max)) || `Must be between ${min} and ${max}`;
  },

  minlen: (value, min) => {
    if (value === "") return true;
    return value.length >= Number(min) || `Minimum length is ${min}`;
  },

  maxlen: (value, max) => {
    if (value === "") return true;
    return value.length <= Number(max) || `Maximum length is ${max}`;
  },
};

function parseRule(rule) {
  const [name, rawArgs] = rule.split(":");
  const args = rawArgs ? rawArgs.split(",").map(s => s.trim()) : [];
  return { name, args };
}

function getErrorElement(el) {
  let err = el.nextElementSibling;
  if (err && err.classList.contains("validation-error")) {
    return err;
  }

  err = document.createElement("div");
  err.className = "validation-error";
  el.insertAdjacentElement("afterend", err);
  return err;
}

function validate(el) {
  const raw = (el.dataset.validate || "").trim();
  const errEl = getErrorElement(el);

  if (!raw) {
    el.classList.remove("invalid");
    errEl.textContent = "";
    return true;
  }

  const rules = raw.split(/\s+/).filter(rule => rule !== "");

  for (const rule of rules) {
    const { name, args } = parseRule(rule);
    const fn = validators[name];

    if (!fn) {
      throw new Error(`Unknown validator: ${name}`);
    }

    const result = fn(el.value, ...args);

    if (result !== true) {
      el.classList.add("invalid");
      errEl.textContent = result;
      return false;
    }
  }

  el.classList.remove("invalid");
  errEl.textContent = "";
  return true;
}

function handleValidateEvent(e) {
  if (!e.target.hasAttribute("data-validate")) return;
  validate(e.target);
}

document.addEventListener("input", handleValidateEvent);
document.addEventListener("change", handleValidateEvent);