---
layout: default
permalink: /papers.html
title: Accepted Papers
nav: true
nav_order: 3
---

## List of Accepted Papers

<p style="text-align: center; font-size: 1.2rem; font-style: italic; margin: 2rem 0;">To Be Announced (TBA)</p>

<!--
<div class="paper-list-flex">
  {% for paper in site.data.papers %}
  <div class="paper-card">
    <div class="paper-title">{{ paper.title }}</div>
    <div class="paper-authors">{{ paper.authors }}</div>
    <button class="paper-toggle-btn" onclick="togglePaperDetails(this)">Show Details</button>
    <div class="paper-details">
      <strong>Abstract:</strong> {{ paper.abstract }}
    </div>
  </div>
  {% endfor %}
</div>
-->

<script>
function togglePaperDetails(btn) {
  var details = btn.nextElementSibling;
  if (details.style.display === "block") {
    details.style.display = "none";
    btn.textContent = "Show Details";
  } else {
    details.style.display = "block";
    btn.textContent = "Hide Details";
  }
}
</script>
