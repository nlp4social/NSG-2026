---
layout: default
permalink: /speakers.html
title: Speakers
nav: true
nav_order: 4
---

## Keynote Speakers

<div class="single-card-flex">
  <div class="speaker-card" style="cursor: pointer; padding: 2rem; display: flex; flex-direction: column; align-items: center; max-width: 550px;" onclick="toggleZhijing(this)">
    <div style="display: flex; align-items: center; gap: 1.5rem; text-align: left; width: 100%;">
      <img src="assets/speaker_images/ZhijingJin.webp" alt="Zhijing Jin" class="speaker-img" style="width: 110px; height: 110px; flex-shrink: 0; margin: 0;"/>
      <div>
        <div class="speaker-name" style="font-size: 1.4rem; margin-top: 0;">
          <a href="https://zhijing-jin.com/home/" target="_blank" rel="noopener" style="text-decoration: none;" onclick="event.stopPropagation();">Zhijing Jin</a>
        </div>
        <div class="speaker-designation" style="margin-top: 0.5rem; font-size: 1rem;">
          <span style="font-weight:600; color:#194e6a;">Assistant Professor</span><br>
          <span style="font-style:italic; color:#333;">University of Toronto</span>
        </div>
      </div>
    </div>
    
    <div class="zhijing-abstract speaker-abstract" style="text-align: left; display: none; margin-top: 1.5rem; width: 100%; cursor: default;" onclick="event.stopPropagation();">
      <strong>About</strong><br>
      An incoming Assistant Professor at University of Toronto and Research Scientist at the Max Planck Institute with Bernhard Schölkopf, they are the founder of EuroSafeAI and hold affiliations with Center for Human-Compatible AI (CHAI), the Vector Institute, the Schwartz Reisman Institute for Technology and Society, and ELLIS.<br><br>
      Their research focuses on Large Language Models, Causal Inference, and Responsible AI, with contributions to causal reasoning, multi-agent systems, interpretability, and AI safety. They are a recipient of the ELLIS PhD Award, multiple Rising Star recognitions, and Best Paper Awards at NeurIPS 2024 Workshops, with work featured in WIRED and MIT News.<br><br>
      <strong>Links</strong><br>
      <div style="display: flex; flex-wrap: wrap; gap: 12px; margin-top: 0.5rem;">
        <a href="https://zhijing-jin.com/home/" target="_blank" rel="noopener" style="font-weight: 500;">Website</a> &bull;
        <a href="https://x.com/ZhijingJin" target="_blank" rel="noopener" style="font-weight: 500;">𝕏 (Twitter)</a> &bull;
        <a href="https://scholar.google.com/citations?user=Mdr6wjUAAAAJ" target="_blank" rel="noopener" style="font-weight: 500;">Google Scholar</a> &bull;
        <a href="https://bsky.app/profile/zhijingjin.bsky.social" target="_blank" rel="noopener" style="font-weight: 500;">BlueSky</a>
      </div>
    </div>
  </div>
</div>

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
function toggleZhijing(card) {
  var abs = card.querySelector('.zhijing-abstract');
  if (abs.style.display === "block") {
    abs.style.display = "none";
  } else {
    abs.style.display = "block";
  }
}

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
