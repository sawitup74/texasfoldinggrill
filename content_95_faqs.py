_ADD = {
"building-a-texas-coal-bed":[("What's the best charcoal for Texas-style grilling?","Lump charcoal lights fast and burns hot, good for fajitas and steaks; briquettes burn steadier for longer cooks.")],
"burning-splits-down-to-coals":[("How long does wood take to burn down to coals?","Roughly 30 to 45 minutes for small, dry splits.")],
"pork-spare-ribs-on-a-flat-pack-grill":[("When are ribs done?","When a probe slides between the bones easily, usually around 195–203°F. They're safe at 145°F but not yet tender.")],
"beef-short-ribs-on-a-flat-pack-grill":[("What short ribs work on a small grill?","Bone-in chuck short ribs in 2–3 inch pieces.")],
"chopped-beef-sandwiches":[("How long do brisket leftovers keep?","Refrigerate within 2 hours (1 hour above 90°F); use within 3 to 4 days, and reheat to 165°F.")],
"beef-fajitas-skirt-steak":[("How long should fajita meat marinate?","1 to 8 hours in the fridge; longer in lime juice can make it mushy.")],
"texas-football-tailgate-grilling":[("Do stadiums allow charcoal grills?","Many lots do with conditions, some don't. Check the venue's tailgate policy.")],
"lake-weekend-grilling-texas":[("Can I grill on my boat?","Not with charcoal. Carry the grill as cargo and cook on shore.")],
"gulf-coast-beach-grilling":[("Are charcoal grills allowed on Texas beaches?","It depends on the city, county or park. Check local beach rules before you go.")],
"made-in-buna-texas":[("Where is the Slot Grill made?","Slot Grill says Keith makes the grills in Buna, Texas, with U.S.-based partners helping during very high demand.")],
"compact-vs-full-size-slot-grill":[("Which Slot Grill should I get for brisket and ribs?","The Full Size: more room for a cool zone and cast iron.")],
"griddle-plates-for-tex-mex":[("Can I use a griddle and a grate at the same time?","Yes. The two-piece top takes one griddle plate and one grate, or two plates.")],
}
PAGES = [p if p[0] not in _ADD else p[:6]+(p[6]+_ADD[p[0]],) for p in PAGES]
