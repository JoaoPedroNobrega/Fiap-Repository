const preview = document.getElementById("preview");
const cssCode = document.getElementById("cssCode");
const resetBtn = document.getElementById("resetBtn");
 
const filters = {
  brightness: {
    input: document.getElementById("brightness"),
    value: document.getElementById("brightnessValue"),
    unit: "%",
    css: "brightness"
  },
  contrast: {
    input: document.getElementById("contrast"),
    value: document.getElementById("contrastValue"),
    unit: "%",
    css: "contrast"
  },
  saturate: {
    input: document.getElementById("saturate"),
    value: document.getElementById("saturateValue"),
    unit: "%",
    css: "saturate"
  },
  grayscale: {
    input: document.getElementById("grayscale"),
    value: document.getElementById("grayscaleValue"),
    unit: "%",
    css: "grayscale"
  },
  sepia: {
    input: document.getElementById("sepia"),
    value: document.getElementById("sepiaValue"),
    unit: "%",
    css: "sepia"
  },
  blur: {
    input: document.getElementById("blur"),
    value: document.getElementById("blurValue"),
    unit: "px",
    css: "blur"
  },
  invert: {
    input: document.getElementById("invert"),
    value: document.getElementById("invertValue"),
    unit: "%",
    css: "invert"
  }
};
 
const defaultValues = {
  brightness: 100,
  contrast: 100,
  saturate: 100,
  grayscale: 0,
  sepia: 0,
  blur: 0,
  invert: 0
};
 
function updateFilters() {
  const filterList = [];
 
  for (const key in filters) {
    const filter = filters[key];
    const inputValue = filter.input.value;
 
    filter.value.textContent = inputValue + filter.unit;
 
    filterList.push(`${filter.css}(${inputValue}${filter.unit})`);
  }
 
  const finalFilter = filterList.join(" ");
 
  preview.style.filter = finalFilter;
  cssCode.textContent = `filter: ${finalFilter};`;
}
 
function resetFilters() {
  for (const key in filters) {
    filters[key].input.value = defaultValues[key];
  }
 
  updateFilters();
}
 
for (const key in filters) {
  filters[key].input.addEventListener("input", updateFilters);
}
 
resetBtn.addEventListener("click", resetFilters);
 
updateFilters();