import json

# Data scraped from the output
scraped = {
  "advisors": [
    {
      "name": "Mamta",
      "image": "assets/organizer_images/mamta.jpg",
      "url": "https://mamtanlp.github.io/cv/",
      "role": "Advisor",
      "affiliation": "Research Associate, King's College London"
    },
    {
      "name": "Oana Cocarascu",
      "image": "assets/organizer_images/oana_cocarascu.jpg",
      "url": "https://scholar.google.com/citations?user=TrgGMO0AAAAJ&hl=en",
      "role": "Advisor",
      "affiliation": "Senior Lecturer, King's College London"
    },
    {
      "name": "Hassan Alhuzali",
      "image": "assets/organizer_images/hassan_alhuzali.jpg",
      "url": "https://hasanhuz.github.io/",
      "role": "Advisor",
      "affiliation": "Assistant Professor @ Umm Al-Qura University"
    },
    {
      "name": "Katie Atkinson",
      "image": "assets/organizer_images/katie_atkinson.jpg",
      "url": "http://www.csc.liv.ac.uk/~katie",
      "role": "Advisor",
      "affiliation": "Professor of Computer Science, University of Liverpool"
    }
  ],
  "organizers": [
    {
      "name": "Iryna Gurevych",
      "image": "assets/organizer_images/iryna_gurevych.jpg",
      "url": "https://www.informatik.tu-darmstadt.de/ukp/ukp_home/head_ukp/index.en.jsp",
      "role": "Organizer",
      "affiliation": "Full Professor, TU Darmstadt; Adjunct Professor, MBZUAI, UAE; Affiliated Professor, INSAIT, Bulgaria"
    }
  ]
}

with open('_data/organizers.json', 'r') as f:
    data = json.load(f)

# Append to advisors
data['advisors'].extend(scraped['advisors'])

# Append to main organizers
data['main'].extend(scraped['organizers'])

with open('_data/organizers.json', 'w') as f:
    json.dump(data, f, indent=2)
