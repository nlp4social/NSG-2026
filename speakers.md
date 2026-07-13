---
layout: default
permalink: /speakers.html
title: Speakers
nav: true
nav_order: 4
---

## Keynote Speakers

<div class="single-card-flex">
  <div class="speaker-card" style="cursor: pointer; padding: 2rem; display: flex; flex-direction: row; align-items: center; max-width: 550px;" onclick="toggleZhijing(this)">
    <div style="display: flex; align-items: center; gap: 1.5rem; text-align: left; width: 100%;">
      <img src="assets/speaker_images/milind_tambe.jpg" alt="Zhijing Jin" class="speaker-img" style="width: 110px; height: 110px; flex-shrink: 0; margin: 0;"/>
      <div>
        <div class="speaker-name" style="font-size: 1.4rem; margin-top: 0;">
          <a href="https://zhijing-jin.com/home/" target="_blank" rel="noopener" style="text-decoration: none;" onclick="event.stopPropagation();">Milind Tambe</a>
        </div>
        <div class="speaker-designation" style="margin-top: 0.5rem; font-size: 1rem;">
          <span style="font-weight:600; color:#194e6a;">Professor</span><br>
          <span style="font-style:italic; color:#333;">Harvard University</span> <br>
           <span style="font-style:italic; color:#333;">Director for “AI for Social Good” at Google Research</span>
        </div>
      </div>
    </div>
  </div>
    <div class="speaker-card" style="cursor: pointer; padding: 2rem; display: flex; flex-direction: row; align-items: center; max-width: 550px;" onclick="toggleLucie(this)">
    <div style="display: flex; align-items: center; gap: 1.5rem; text-align: left; width: 100%;">
      <img src="assets/speaker_images/lucie.jpg" alt="Lucie Flek" class="speaker-img" style="width: 110px; height: 110px; flex-shrink: 0; margin: 0;"/>
      <div>
        <div class="speaker-name" style="font-size: 1.4rem; margin-top: 0;">
          <a href="https://zhijing-jin.com/home/" target="_blank" rel="noopener" style="text-decoration: none;" onclick="event.stopPropagation();">Lucie Flek</a>
        </div>
        <div class="speaker-designation" style="margin-top: 0.5rem; font-size: 1rem;">
          <span style="font-weight:600; color:#194e6a;">Professor</span><br>
          <span style="font-style:italic; color:#333;">University of Bonn</span>
        </div>
      </div>
    </div>
  </div>
  <div class="speaker-card" style="cursor: pointer; padding: 2rem; display: flex; flex-direction: row; align-items: center; max-width: 550px;" onclick="toggleZhijing(this)">
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
  </div>
  </div>
    


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

<!--<script>
function toggleZhijing(card) {
  var abs = card.querySelector('.zhijing-abstract');
  if (abs.style.display === "block") {
    abs.style.display = "none";
  } else {
    abs.style.display = "block";
  }
}

function toggleLucie(card) {
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
</script>-->
