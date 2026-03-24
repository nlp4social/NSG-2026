---
layout: default
permalink: /programme.html
title: Schedule
nav: true
nav_order: 5
---

## Schedule

{% for day in site.data.programme %}
### **{{ day.date }}**

<table class="schedule-table">
  <thead>
    <tr>
      <th style="text-align:center;">Time (BST)</th>
      <th style="text-align:center;">Session</th>
    </tr>
  </thead>
  <tbody>
    {% for session in day.sessions %}
    <tr>
      <td>{{ session.time }}</td>
      <td>{{ session.description }}</td>
    </tr>
    {% endfor %}
  </tbody>
</table>

---

{% endfor %}

<!-- [back](./) -->
