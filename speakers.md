---
layout: default
permalink: /speakers.html
title: Speakers
nav: true
nav_order: 4
---

## Keynote Speakers

<p style="text-align: center; font-size: 1.2rem; font-style: italic; margin: 2rem 0;">To Be Announced (TBA)</p>

<!--
<div class="speaker-flex">
  {% for speaker in site.data.speakers.keynote %}
  <div class="speaker-card">
    <img src="{{ speaker.image }}" alt="{{ speaker.name }}" class="speaker-img"/>
    <div class="speaker-name"><a href="{{ speaker.url }}" target="_blank" rel="noopener">{{ speaker.name }}</a></div>
    <div class="speaker-designation"><span style="font-weight:600; color:#194e6a;">{{ speaker.designation_title }}</span><br><span style="font-style:italic; color:#333;">{{ speaker.designation_org }}</span><br><span style="color:black">{{ speaker.designation_country }}</span></div>
    <button class="speaker-toggle-btn" onclick="toggleAbstract(this)">Talk Abstract</button>
    <div class="speaker-abstract">
      <strong>{{ speaker.talk_title }}</strong><br>
      {{ speaker.abstract | newline_to_br }}
    </div>
  </div>
  {% endfor %}
</div>
-->

----
## Invited Speakers

<p style="text-align: center; font-size: 1.2rem; font-style: italic; margin: 2rem 0;">To Be Announced (TBA)</p>

<!--
<div class="speaker-flex">
  {% for speaker in site.data.speakers.invited %}
  <div class="speaker-card">
    <img src="{{ speaker.image }}" alt="{{ speaker.name }}" class="speaker-img"/>
    <div class="speaker-name"><a href="{{ speaker.url }}" target="_blank" rel="noopener">{{ speaker.name }}</a></div>
    <div class="speaker-designation"><span style="font-weight:600; color:#194e6a;">{{ speaker.designation_title }}</span><br><span style="font-style:italic; color:#333;">{{ speaker.designation_org }}</span><br><span style="color:black">{{ speaker.designation_country }}</span></div>
    <button class="speaker-toggle-btn" onclick="toggleAbstract(this)">Talk Abstract</button>
    <div class="speaker-abstract">
      <strong>{{ speaker.talk_title }}</strong><br>
      {{ speaker.abstract | newline_to_br }}
    </div>
  </div>
  {% endfor %}
</div>
-->

<script>
function toggleAbstract(btn) {
  var abs = btn.nextElementSibling;
  if (abs.style.display === "block") {
    abs.style.display = "none";
    btn.textContent = "Talk Abstract";
  } else {
    abs.style.display = "block";
    btn.textContent = "Hide Abstract";
  }
}
</script>
