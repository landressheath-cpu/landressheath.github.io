import os
import re

pubs = [
    {
        "title": "Child Protective Services Workers' Decision Making and Risk Management",
        "date": "2024-01-01",
        "venue": "Walden Dissertations and Doctoral Studies",
        "url": "https://scholarworks.waldenu.edu/dissertations/16143",
        "type": "Dissertation (ScholarWorks)",
        "category": "scholarly",
        "citation": "Landress, Heath Nicholas, \"Child Protective Services Workers' Decision Making and Risk Management\" (2024). Walden Dissertations and Doctoral Studies. 16143."
    },
    {
        "title": "Identifying Symbolic Modeling of Grooming Precursors in Social Media",
        "date": "2026-01-01",
        "venue": "ProQuest Dissertations & Theses @ Walden University",
        "url": "https://www.proquest.com/dissertations-theses/identifying-symbolic-modeling-grooming-precursors/docview/3367605382/se-2",
        "type": "Dissertation",
        "category": "scholarly",
        "citation": "Landress, H. N. (2026). Identifying Symbolic Modeling of Grooming Precursors in Social Media (Order No. 32791504). Available from Dissertations & Theses @ Walden University."
    },
    {
        "title": "Nihilistic Violence Aesthetics in Public Online Communication: A Theoretical Framework for Interpreting Hybridized Violent Signaling",
        "date": "2026-01-02",
        "venue": "Behavioral Sciences of Terrorism and Political Aggression",
        "url": "",
        "type": "Manuscript under review",
        "category": "scholarly",
        "citation": "Landress, H. N. (under review). Nihilistic Violence Aesthetics in Public Online Communication: A Theoretical Framework for Interpreting Hybridized Violent Signaling. Manuscript under review (Behavioral Sciences of Terrorism and Political Aggression)."
    },
    {
        "title": "Surfacing and Ranking the Forces That Shape Frontline Practice: A Step-by-Step Force Field Analysis Within a Quasi-Delphi Design for Assessing Risk Assessment and Decision-Making Among Child Protective Services Workers",
        "date": "2026-01-03",
        "venue": "Journal of Public Child Welfare",
        "url": "",
        "type": "Manuscript under review",
        "category": "scholarly",
        "citation": "Landress, H. N. (under review). Surfacing and Ranking the Forces That Shape Frontline Practice: A Step-by-Step Force Field Analysis Within a Quasi-Delphi Design for Assessing Risk Assessment and Decision-Making Among Child Protective Services Workers. Manuscript under review (Journal of Public Child Welfare)."
    },
    {
        "title": "The Practitioner-Sourced Force Field (PSFF) Framework: A Conceptual Model of Dual-Valence Forces in Child Welfare Decision-Making",
        "date": "2026-01-04",
        "venue": "Journal of Public Child Welfare",
        "url": "",
        "type": "Manuscript under review",
        "category": "scholarly",
        "citation": "Landress, H. N. (under review). The Practitioner-Sourced Force Field (PSFF) Framework: A Conceptual Model of Dual-Valence Forces in Child Welfare Decision-Making. Manuscript under review (Journal of Public Child Welfare)."
    },
    {
        "title": "Using Force Field Analysis to Strengthen Child Welfare Risk Assessment: A Practice Framework for Supervisors and Administrators",
        "date": "2026-01-05",
        "venue": "CWLA",
        "url": "",
        "type": "Manuscript under review",
        "category": "scholarly",
        "citation": "Using Force Field Analysis to Strengthen Child Welfare Risk Assessment: A Practice Framework for Supervisors and Administrators Manuscript under review (CWLA)."
    },
    {
        "title": "The SAFE Milieu Framework: A Conceptual Architecture for Trauma-Informed Administration in Specialized Residential Care",
        "date": "2026-01-06",
        "venue": "Developmental Child Welfare",
        "url": "",
        "type": "Manuscript under review",
        "category": "scholarly",
        "citation": "Landress, H. N. (2026). The SAFE Milieu Framework: A Conceptual Architecture for Trauma-Informed Administration in Specialized Residential Care Manuscript under review (Developmental Child Welfare)."
    },
    {
        "title": "The Youth Online Exploitation–Extremism Interface: A Conceptual Framework for Anti-Trafficking Identification and Digital Child Protection",
        "date": "2026-01-07",
        "venue": "Journal of Human Trafficking",
        "url": "",
        "type": "Manuscript under review (Brief Report)",
        "category": "scholarly",
        "citation": "Landress, H. N. (2026). The Youth Online Exploitation–Extremism Interface: A Conceptual Framework for Anti-Trafficking Identification and Digital Child Protection Manuscript under review (Journal of Human Trafficking) (Brief Report)."
    },
    {
        "title": "Analytically Separable, Empirically Entangled: A Structural Validation of the Youth Online Exploitation–Extremism Interface Framework Using the PERIL Nihilistic Violent Extremism Tracker",
        "date": "2026-01-08",
        "venue": "Journal of Police and Criminal Psychology",
        "url": "",
        "type": "Manuscript under review",
        "category": "scholarly",
        "citation": "Landress, H. N. (2026). Analytically Separable, Empirically Entangled: A Structural Validation of the Youth Online Exploitation–Extremism Interface Framework Using the PERIL Nihilistic Violent Extremism Tracker Manuscript under review (Journal of Police and Criminal Psychology)."
    },
    {
        "title": "Nihilistic Violence Aesthetics in Public Online Communications",
        "date": "2026-01-09",
        "venue": "Journal of Social, Behavioral, and Health Sciences",
        "url": "",
        "type": "Manuscript under review (Comprehensive Literature Review)",
        "category": "scholarly",
        "citation": "Landress, H. N. (2026). Nihilistic Violence Aesthetics in Public Online Communications Manuscript under review (Journal of Social, Behavioral, and Health Sciences) (Comprehensive Literature Review)."
    },
    {
        "title": "Identifying Symbolic Modeling of Grooming Precursors in Social Media",
        "date": "2026-01-10",
        "venue": "Journal of Social, Behavioral, and Health Sciences",
        "url": "",
        "type": "Manuscript under review",
        "category": "scholarly",
        "citation": "Landress, H. N. (2026). Identifying Symbolic Modeling of Grooming Precursors in Social Media Manuscript under review (Journal of Social, Behavioral, and Health Sciences)."
    },
    {
        "title": "Nihilistic Violence Aesthetics in Public Online Communication: A Conceptual Framework for Interpreting Hybridized Violent Signaling A Research-Informed White Paper for Researchers, Practitioners, and Policy Audiences",
        "date": "2026-01-11",
        "venue": "Zenodo",
        "url": "https://doi.org/10.5281/zenodo.20185872",
        "type": "White Paper",
        "category": "nonpeer",
        "citation": "H. N., L. (2026). Nihilistic Violence Aesthetics in Public Online Communication: A Conceptual Framework for Interpreting Hybridized Violent Signaling A Research-Informed White Paper for Researchers, Practitioners, and Policy Audiences. Zenodo. https://doi.org/10.5281/zenodo.20185872"
    },
    {
        "title": "White Paper: The Youth Online Exploitation–Extremism Interface A Conceptual Framework for Anti-Trafficking Identification and Digital Child Protection (Version 1)",
        "date": "2026-01-12",
        "venue": "Zenodo",
        "url": "https://doi.org/10.5281/zenodo.20421646",
        "type": "White Paper",
        "category": "nonpeer",
        "citation": "Landress, H. N. (2026). White Paper: The Youth Online Exploitation–Extremism Interface A Conceptual Framework for Anti-Trafficking Identification and Digital Child Protection (Version 1). Zenodo. https://doi.org/10.5281/zenodo.20421646"
    },
    {
        "title": "Identifying Symbolic Modeling of Grooming Precursors in Social Media (Version 1)",
        "date": "2026-01-13",
        "venue": "Zenodo",
        "url": "https://doi.org/10.5281/zenodo.21513869",
        "type": "White Paper",
        "category": "nonpeer",
        "citation": "Landress, H. N. (2026). Identifying Symbolic Modeling of Grooming Precursors in Social Media (Version 1). Zenodo. https://doi.org/10.5281/zenodo.21513869"
    }
]

os.makedirs("_publications", exist_ok=True)

for i, p in enumerate(pubs):
    title_clean = re.sub(r'[^a-zA-Z0-9]+', '-', p['title'].lower()).strip('-')[:50]
    filename = f"_publications/{p['date']}-{title_clean}.md"
    
    content = f"---\n"
    content += f"title: \"{p['title']}\"\n"
    content += f"collection: publications\n"
    content += f"category: {p['category']}\n"
    content += f"permalink: /publication/{p['date']}-{title_clean}\n"
    content += f"excerpt: '{p['type']}'\n"
    content += f"date: {p['date']}\n"
    content += f"venue: '{p['venue']}'\n"
    if p['url']:
        content += f"paperurl: '{p['url']}'\n"
    
    cit = p['citation'].replace('"', '&quot;')
    content += f"citation: '{cit}'\n"
    content += f"---\n\n"
    
    if p['url']:
        content += f"[Link to publication]({p['url']})\n"
    else:
        content += f"This manuscript is currently {p['type'].lower()}.\n"
        
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

print(f"Generated {len(pubs)} publication files with categories.")
