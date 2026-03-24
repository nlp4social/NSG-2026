---
layout: default
permalink: /organizers.html
title: Organizers
nav: true
nav_order: 6
---

<h2 style="text-align: center;">Advisors</h2>

<div class="single-card-flex">
  {% for advisor in site.data.organizers.advisors %}
  <div class="organizer-card">
    <img src="{{ advisor.image }}" alt="{{ advisor.name }}" class="organizer-img"/>
    <div style="margin-top: 8px;"><a href="{{ advisor.url }}">{{ advisor.name }}</a></div>
    <div style="font-size: 0.95em; color: #555;">{{ advisor.role }}<br>{{ advisor.affiliation }}</div>
  </div>
  {% endfor %}
</div>

---

<h2 style="text-align: center;">Organizers</h2>

<div class="organizer-flex">
  {% for organizer in site.data.organizers.main %}
  <div class="organizer-card">
    <img src="{{ organizer.image }}" alt="{{ organizer.name }}" class="organizer-img"/>
    <div style="margin-top: 8px;"><a href="{{ organizer.url }}">{{ organizer.name }}</a></div>
    <div style="font-size: 0.95em; color: #555;">{{ organizer.role }}<br>{{ organizer.affiliation }}</div>
  </div>
  {% endfor %}
</div>

---

<h2 style="text-align: center;">Student Volunteers</h2>

<div class="single-card-flex">
  {% for volunteer in site.data.organizers.volunteers %}
  <div class="organizer-card">
    <img src="{{ volunteer.image }}" alt="{{ volunteer.name }}" class="volunteer-img"/>
    <div style="margin-top: 8px;"><a href="{{ volunteer.url }}">{{ volunteer.name }}</a></div>
    <div style="font-size: 0.95em; color: #555;">{{ volunteer.role }}<br>{{ volunteer.affiliation }}</div>
  </div>
  {% endfor %}
</div>
