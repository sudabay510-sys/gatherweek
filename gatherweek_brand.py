from helpers import L, LM, opt, env_names

Q = [
    {"id": "org", "type": "choice", "prompt": "What kind of community do you coordinate?",
     "options": [opt("worship", "Church, mosque, synagogue, temple, or other faith community"), opt("mutual", "Mutual-aid / neighborhood group"), opt("pta", "PTA / school group"), opt("nonprofit", "Small nonprofit"), opt("club", "Club / league / association")]},
    {"id": "size", "type": "choice", "prompt": "How many people are regularly involved?",
     "options": [opt("small", "Under 50"), opt("mid", "50–200"), opt("large", "200–500"), opt("xl", "500+")]},
    {"id": "gatherings", "type": "choice", "prompt": "How often do you gather?",
     "options": [opt("weekly", "Weekly"), opt("multi", "Several times a week"), opt("monthly", "Monthly"), opt("events", "Around events")]},
    {"id": "roles", "type": "choice", "multi": True, "prompt": "Which volunteer roles do you fill regularly?", "help": "Select all that apply.",
     "options": [opt("greet", "Greeters / welcome"), opt("setup", "Setup & teardown"), opt("food", "Food / hospitality"), opt("kids", "Childcare / youth"), opt("av", "Sound / AV / livestream"), opt("outreach", "Outreach / deliveries")]},
    {"id": "channels", "type": "choice", "multi": True, "prompt": "How do you share announcements?",
     "options": [opt("email", "Email newsletter"), opt("text", "Group text / WhatsApp"), opt("social", "Social media"), opt("print", "Printed bulletin / flyers"), opt("spoken", "Spoken at gatherings")]},
    {"id": "pain", "type": "choice", "prompt": "What breaks most often?",
     "options": [opt("noshow", "Volunteers forget or no-show"), opt("same", "The same few people do everything"), opt("late", "Announcements go out late"), opt("new", "Newcomers don’t get plugged in"), opt("burnout", "Coordinator burnout (maybe you)")]},
    {"id": "hours", "type": "choice", "prompt": "Admin hours you have each week?",
     "options": [opt("1", "About 1"), opt("3", "2–4"), opt("6", "5+")]},
    {"id": "season", "type": "choice", "prompt": "Anything special coming in the next 2 months?",
     "options": [opt("holy", "A holy day / holiday season"), opt("drive", "A drive or service project"), opt("event", "A big event"), opt("none", "Regular rhythm")]},
    {"id": "tone", "type": "choice", "prompt": "How should announcements sound?",
     "options": [opt("warm", "Warm & welcoming"), opt("formal", "Respectful & formal"), opt("brief", "Brief & practical"), opt("joyful", "Joyful & energetic")]},
]


def plan(a):
    pain = a.get("pain", "noshow")
    roles = LM(Q[3]["options"], a.get("roles") or ["greet"])
    fix = {
        "noshow": ["Send a reminder 48 hours before each shift and a short thank-you after.", "Let volunteers swap shifts with one simple ‘swap request’ message."],
        "same": ["Break big jobs into 30-minute ‘micro-roles’ newcomers can say yes to.", "Ask personally — one direct invitation beats ten general appeals."],
        "late": ["Fix one weekly send day and time; draft on the day before.", "Use one template: this week / coming up / how to help."],
        "new": ["Name a welcome buddy for each newcomer for their first 4 weeks.", "Send a 3-message welcome sequence over the first month."],
        "burnout": ["Write down every task you do weekly; hand off two of them this month.", "Protect one week per quarter with no new initiatives."],
    }[pain]
    return {
        "title": f"Gatherweek 4-week plan — {L(Q[0]['options'], a.get('org'))}",
        "summary": f"About {L(Q[1]['options'], a.get('size')).lower()} people, gathering {L(Q[2]['options'], a.get('gatherings')).lower()}. Roles: {roles}. Channels: {LM(Q[4]['options'], a.get('channels') or ['email'])}. Tone: {L(Q[8]['options'], a.get('tone')).lower()}. A coordination plan — no attendance or fundraising promises.",
        "preview_sections": [
            {"title": "Start with your biggest break point", "bullets": fix},
            {"title": "Weekly announcement rhythm (unlocked)", "bullets": ["Day 1: collect updates (one shared form or thread).", "Day 2: draft using this week / coming up / how to help.", "Day 3: send on every channel you use; keep the spoken version under 60 seconds.", "Day 7: thank volunteers by name (with permission)."]},
            {"title": "Respect & privacy", "body": "Get consent before sharing names, photos, or prayer/support requests. Keep member contact lists private and follow your organization’s policies."},
        ],
        "locked_sections": [
            {"title": "4-week announcement calendar", "teaser": "Dated drafts for each week in your tone."},
            {"title": "Volunteer shift templates", "teaser": "Sign-up, reminder, swap, and thank-you messages."},
            {"title": "Newcomer onboarding checklist", "teaser": "From first visit to first volunteer role."},
            {"title": "Seasonal & event-week playbooks", "teaser": "Holy days, drives, and big events."},
        ],
    }


BRAND = {
    "name": "Gatherweek", "slug": "gatherweek", "port": 5114,
    "tagline": "A weekly volunteer and announcements plan for small communities.",
    "eyebrow": "For faith communities, nonprofits, PTAs & groups",
    "hero_title": "Fewer last-minute asks. More people sharing the load.",
    "hero_lede": "Gatherweek asks about your community, volunteer roles, and channels, then builds a weekly announcement rhythm and volunteer templates that respect everyone’s time.",
    "cta_primary": "Build our weekly plan", "cta_short": "Start quiz",
    "cta_band_title": "Coordinators deserve a rest too.",
    "cta_band_text": "A rhythm that keeps people informed and invites new helpers in.",
    "honesty_line": "Coordination help only. No attendance, donation, or fundraising promises.",
    "audience_line": "Volunteer coordinators and admins at faith communities, mutual-aid groups, PTAs, and small nonprofits.",
    "personas": [
        {"title": "Volunteer coordinator", "text": "You fill the schedule — often by texting the same five people."},
        {"title": "Part-time admin", "text": "The bulletin, the email, the slides — all on you."},
        {"title": "New group organizer", "text": "Starting a group and want good habits from day one."},
    ],
    "journey": [
        {"stage": "Collect", "pain": "Updates arrive at the last minute.", "fix": "One weekly collection day and form."},
        {"stage": "Announce", "pain": "Different message on every channel.", "fix": "One template, sent everywhere."},
        {"stage": "Staff", "pain": "No-shows and the same few helpers.", "fix": "Micro-roles, reminders, and swaps."},
        {"stage": "Welcome", "pain": "Newcomers drift away.", "fix": "A buddy and a 3-message welcome sequence."},
    ],
    "how_steps": [
        {"title": "Quiz your community", "text": "Size, gatherings, roles, channels, and break points."},
        {"title": "Preview your plan", "text": "Your biggest fix and weekly rhythm unlocked."},
        {"title": "Start your plan", "text": "Enter your email, then complete checkout on Gumroad."},
    ],
    "features": [
        {"title": "Announcement calendar", "text": "4 weeks of drafts in your tone."},
        {"title": "Volunteer templates", "text": "Sign-up, reminder, swap, thank-you."},
        {"title": "Newcomer onboarding", "text": "From first visit to first role."},
        {"title": "Seasonal playbooks", "text": "Subscription: holy days, drives, and events."},
    ],
    "sample_peek": ["48-hour shift reminders", "This week / coming up / how to help", "30-minute micro-roles", "Welcome buddy for newcomers"],
    "trust_points": [
        {"title": "Respectful of every tradition", "text": "Neutral templates you adapt to your community."},
        {"title": "Privacy first", "text": "Consent before sharing names, photos, or requests."},
        {"title": "No political fundraising", "text": "We don’t write political or fundraising-promise copy."},
    ],
    "faq": [
        {"q": "How does billing work?", "a": "Choose Monthly, Quarterly or Yearly, save your email, then complete payment on Gumroad. Renews automatically. Cancel anytime from your Gumroad library."},
        {"q": "Is this church-management software?", "a": "No. Gatherweek is a planning and template tool — no member database or giving features."},
        {"q": "Will it increase attendance or donations?", "a": "We don’t promise that. It helps you communicate clearly and share volunteer work."},
        {"q": "Does it fit non-religious groups?", "a": "Yes — PTAs, mutual-aid groups, clubs, and nonprofits all work."},
    ],
    "pricing": [
        {"id": "monthly", "name": "Monthly", "price": "$15", "period": "/ month",
         "intro": "$15", "renewal": "$15 / month", "renewal_note": "Renews automatically. Cancel anytime from your Gumroad library.",
         "includes": ["Announcement calendar", "Volunteer templates", "Weekly rhythm"]},
        {"id": "quarterly", "name": "Quarterly", "price": "$39", "period": "every 3 months",
         "intro": "$39", "renewal": "$39 every 3 months", "renewal_note": "Renews automatically. Cancel anytime from your Gumroad library.", "featured": True,
         "includes": ["Everything in 4-week", "Newcomer onboarding", "Seasonal playbooks"]},
        {"id": "yearly", "name": "Yearly", "price": "$129", "period": "/ year",
         "intro": "$129", "renewal": "$129 / year", "renewal_note": "Renews automatically. Cancel anytime from your Gumroad library.",
         "includes": ["Everything in 12-week", "All seasonal playbooks", "Up to 3 coordinators (planned)"]},
    ],
    "checkout_url": "https://solvfix.gumroad.com/l/anotdg",
    "disclaimer_short": "Coordination education only. No attendance, donation, or fundraising guarantees. Follow your organization’s policies.",
    "disclaimer_long": "Gatherweek provides general volunteer-coordination and communications templates. It is not affiliated with any religious body or organization, does not guarantee attendance, volunteer sign-ups, or donations, and is not legal, tax, or fundraising-compliance advice. Get consent before sharing personal information and follow your organization’s safeguarding and privacy policies. Payments are processed by Gumroad, not on this site.",
    "font_url": "https://fonts.googleapis.com/css2?family=Literata:opsz,wght@7..72,500;7..72,700&family=Source+Sans+3:wght@400;600;700&display=swap",
    "fonts": ("Libre Baskerville", "Nunito Sans"),
    "questions": Q, "generate_plan": plan,
    "voice": "Warm, respectful, inclusive. Speaks to every tradition without assuming one.",
    "palette": {"Background (parchment)": "#F8F6F0", "Alt": "#EFEBDF", "Card": "#FFFFFF", "Ink": "#1E2A3A", "Muted": "#5B6474", "Accent (deep teal)": "#14706B", "Accent hover": "#0F5753", "Highlight (gold)": "#D4A73A"},
    "logo_svg": '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" fill="none"><rect width="64" height="64" rx="16" fill="#14706B"/><circle cx="32" cy="22" r="5" fill="#D4A73A"/><circle cx="19" cy="30" r="4" fill="#F8F6F0"/><circle cx="45" cy="30" r="4" fill="#F8F6F0"/><path d="M14 46c2-6 7-9 12-9M50 46c-2-6-7-9-12-9M22 48c1.5-7 5.5-11 10-11s8.5 4 10 11" stroke="#F8F6F0" stroke-width="3.5" stroke-linecap="round"/></svg>',
    "css_vars": """
  --bg:#F8F6F0;--bg-alt:#EFEBDF;--card:#FFFFFF;--ink:#1E2A3A;--muted:#5B6474;--line:#E0DACB;
  --accent:#14706B;--accent-2:#0F5753;--on-accent:#FFFFFF;--hi:#D4A73A;--radius:14px;
  --font-display:'Libre Baskerville', Georgia, serif;--font-body:'Nunito Sans', system-ui, sans-serif;
  --shadow-card:0 16px 36px rgba(30,42,58,.08);--shadow-btn:0 8px 18px rgba(20,112,107,.25);
  --cta-band-bg:#14706B;--cta-band-ink:#F8F6F0;--cta-band-btn:#D4A73A;--cta-band-btn-ink:#1E2A3A;--tracking:-0.01em;
""",
    "personality": "background:radial-gradient(900px 400px at 50% -20%, #F1E3B9 0%, transparent 60%), var(--bg);",
    "extra_css": "h1{font-size:clamp(1.9rem,3.6vw,3rem)}.journey-card{border-bottom:4px solid var(--hi)}",
    "dos": ["Use neutral language that fits any faith or secular group.", "Emphasize consent and privacy."],
    "donts": ["Assume a specific religion or use political messaging.", "Promise attendance, donations, or fundraising results."],
}
BRAND.update(env_names("gatherweek"))
