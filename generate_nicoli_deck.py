import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE
from PIL import Image

def build_nicoli_deck():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # Color Palette: Modern Minimal Editorial Architectural Case Study
    COLOR_BG = RGBColor(250, 249, 246)         # Soft warm off-white #FAF9F6
    COLOR_CARD = RGBColor(255, 255, 255)       # Pure white
    COLOR_CARD_BORDER = RGBColor(226, 229, 234)# Crisp light gray #E2E5EA
    COLOR_TEXT_MAIN = RGBColor(26, 29, 34)     # Deep charcoal #1A1D22
    COLOR_TEXT_MUTED = RGBColor(98, 104, 115)  # Neutral slate #626873
    COLOR_ACCENT = RGBColor(184, 134, 11)      # Refined Gold #B8860B
    COLOR_ACCENT_BG = RGBColor(253, 248, 235)  # Light gold tint #FDF8EB
    COLOR_DIVIDER = RGBColor(218, 222, 229)    # Border line

    base_dir = r"c:\Users\Azrael\Downloads\Nicoli PPT"
    clean_photos_dir = os.path.join(base_dir, "clean_photos")
    logo_path = os.path.join(base_dir, "nicoli_logo_clean.png")

    def set_slide_background(slide):
        bg_shape = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
        bg_shape.fill.solid()
        bg_shape.fill.fore_color.rgb = COLOR_BG
        bg_shape.line.fill.background()

    # -------------------------------------------------------------
    # SLIDE 1: TITLE SLIDE
    # -------------------------------------------------------------
    s1 = prs.slides.add_slide(blank_layout)
    set_slide_background(s1)

    # Main Card
    card = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.2), Inches(1.0), Inches(10.933), Inches(5.5))
    card.fill.solid()
    card.fill.fore_color.rgb = COLOR_CARD
    card.line.color.rgb = COLOR_CARD_BORDER
    card.line.width = Pt(1.5)

    # Logo if available
    if os.path.exists(logo_path):
        s1.shapes.add_picture(logo_path, Inches(1.8), Inches(1.6), height=Inches(1.2))

    # Title text box
    tb = s1.shapes.add_textbox(Inches(1.8), Inches(2.9), Inches(9.5), Inches(3.2))
    tf = tb.text_frame
    tf.word_wrap = True

    p0 = tf.paragraphs[0]
    p0.text = "SPATIAL ARCHITECTURE & ENVIRONMENTAL PSYCHOLOGY"
    p0.font.size = Pt(12)
    p0.font.bold = True
    p0.font.color.rgb = COLOR_ACCENT
    p0.font.name = "Arial"
    p0.space_after = Pt(12)

    p1 = tf.add_paragraph()
    p1.text = "NICOLI PASTICCERIA"
    p1.font.size = Pt(40)
    p1.font.bold = True
    p1.font.color.rgb = COLOR_TEXT_MAIN
    p1.font.name = "Arial"
    p1.space_after = Pt(8)

    p2 = tf.add_paragraph()
    p2.text = "A Holistic Study of Customer Journey, Wayfinding Friction, Sensory Zoning, and Dwell-Time Affordance"
    p2.font.size = Pt(16)
    p2.font.color.rgb = COLOR_TEXT_MUTED
    p2.font.name = "Calibri"
    p2.space_after = Pt(28)

    p3 = tf.add_paragraph()
    p3.text = "LIB1020 Design Case Study  •  Architectural Space Planning & Behavioral Analysis"
    p3.font.size = Pt(12)
    p3.font.color.rgb = COLOR_TEXT_MAIN
    p3.font.bold = True
    p3.font.name = "Calibri"

    # -------------------------------------------------------------
    # SLIDE 2: JOURNEY FRAMEWORK
    # -------------------------------------------------------------
    s2 = prs.slides.add_slide(blank_layout)
    set_slide_background(s2)

    # Header
    tb_h = s2.shapes.add_textbox(Inches(0.8), Inches(0.6), Inches(11.7), Inches(1.0))
    tf_h = tb_h.text_frame
    tf_h.word_wrap = True
    p = tf_h.paragraphs[0]
    p.text = "THE SPATIAL EXPERIENCE FRAMEWORK"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = COLOR_ACCENT
    p = tf_h.add_paragraph()
    p.text = "Mapping Customer Journey Across Five Experiential Thresholds"
    p.font.size = Pt(24)
    p.font.bold = True
    p.font.color.rgb = COLOR_TEXT_MAIN

    # 5 Phase Cards
    phases = [
        ("PHASE 01", "Street Approach", "Residential enclave, minimal signage, GPS-dependent discovery.", "1 - Path x Find"),
        ("PHASE 02", "Threshold Gate", "Dense foliage veil, psychological filtering, entrance obscurity.", "2 - Entrance Gate"),
        ("PHASE 03", "Courtyard Hub", "Prospect & refuge, dappled daylight, acoustic & seating nodes.", "3 - Central Hub"),
        ("PHASE 04", "Pastry Sanctuary", "High visual saliency, vitrine merchandising, ordering flow.", "4 - Bakery Counter"),
        ("PHASE 05", "Third-Place Dwell", "Tactile velvet booths, domestic shelving, user autonomy.", "5 - Interior Seating")
    ]

    card_w = Inches(2.2)
    card_gap = Inches(0.18)
    start_left = Inches(0.8)

    for i, (tag, title, desc, ref) in enumerate(phases):
        c_left = start_left + i * (card_w + card_gap)
        c_shape = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, c_left, Inches(1.8), card_w, Inches(4.8))
        c_shape.fill.solid()
        c_shape.fill.fore_color.rgb = COLOR_CARD
        c_shape.line.color.rgb = COLOR_CARD_BORDER
        c_shape.line.width = Pt(1.5)

        tb_c = s2.shapes.add_textbox(c_left + Inches(0.15), Inches(2.0), card_w - Inches(0.3), Inches(4.3))
        tf_c = tb_c.text_frame
        tf_c.word_wrap = True

        p = tf_c.paragraphs[0]
        p.text = tag
        p.font.size = Pt(10)
        p.font.bold = True
        p.font.color.rgb = COLOR_ACCENT

        p = tf_c.add_paragraph()
        p.text = title
        p.font.size = Pt(16)
        p.font.bold = True
        p.font.color.rgb = COLOR_TEXT_MAIN
        p.space_after = Pt(14)

        p = tf_c.add_paragraph()
        p.text = desc
        p.font.size = Pt(12)
        p.font.color.rgb = COLOR_TEXT_MUTED
        p.space_after = Pt(20)

        p = tf_c.add_paragraph()
        p.text = f"Anchor: {ref}"
        p.font.size = Pt(10.5)
        p.font.bold = True
        p.font.color.rgb = COLOR_TEXT_MAIN

    # -------------------------------------------------------------
    # DETAILED SLIDES BUILDER
    # -------------------------------------------------------------
    slides_data = [
        {
            "tag": "ZONE 01 // ARRIVAL & APPROACH",
            "title": "Street Approach & Signage Legibility",
            "subtitle": "Navigating Residential Fabric without Commercial Markers",
            "img": "1_-_Path_x_Find_clean.jpg",
            "is_landscape": False,
            "obs": "Quiet residential lane lined with mature neem trees, parked vehicles, and low-scale residential gates. Total absence of commercial pylon signs, roadside billboards, or elevated illuminated brand markers.",
            "psych": "High reliance on external digital wayfinding (GPS). Creates an intriguing 'speakeasy' discovery effect for deliberate visitors, but imposes noticeable cognitive friction and doubt for first-timers.",
            "critique": "Context-sensitive environmental cues—such as refined sidewalk pavers, branded planters, or low bollards—would reassure pedestrians without disrupting neighborhood residential harmony."
        },
        {
            "tag": "ZONE 02 // THRESHOLD TRANSITION",
            "title": "Entrance Threshold & Foliage Screening",
            "subtitle": "Boundary Transition and Sensory Filtering at the Gate",
            "img": "2_-_Entrance__x_parking__clean.jpg",
            "is_landscape": False,
            "obs": "Earth-toned brick pillars with metallic serif 'NICOLI' lettering, weathered wooden split gates, and dense overhead tree canopy casting a deep shadow over the entrance threshold.",
            "psych": "The dense vegetation functions as a sensory airlock, shielding visitors from vehicular street noise. However, deep shadows obscure interior sightlines, triggering approach hesitation.",
            "critique": "Implement warm, low-glare ground uplighting on the brick pillar and entrance path to establish an unmistakable visual beacon during overcast afternoons and twilight hours."
        },
        {
            "tag": "ZONE 03 // CENTRAL COURTYARD HUB",
            "title": "Courtyard Hub & Spatial Circulation",
            "subtitle": "Multi-Zonal Organization and Biophilic Orientation",
            "img": "3_-_Overview_-_Lighting_x_Back_supporting_x_distanceless_chairs__clean.jpg",
            "is_landscape": True,
            "obs": "Sprawling frangipani canopy casting dappled shade across flagstones; stone-filled gabion wall separates outdoor dining from circulation. Direct sightlines connect the bakery door, swing seating, covered patio, and garden tables.",
            "psych": "Acts as the primary orientation node ('Prospect and Refuge'). Visitors pause at the center to survey multiple micro-climates and seating modalities before committing to a table.",
            "critique": "The hub-and-spoke circulation is naturally intuitive; subtle paving color shifts could delineate the primary path to the pastry shop without needing intrusive directional signage."
        },
        {
            "tag": "ZONE 03.1 // ACOUSTIC ENVIRONMENT",
            "title": "Auditory Ambiance & Acoustic Concealment",
            "subtitle": "Balancing Environmental Noise with Dispersed Sound",
            "img": "3.1_-_faint_speaker__clean.jpg",
            "is_landscape": False,
            "obs": "Compact audio speaker housed discreetly within a recessed exterior wall alcove above the doorway, color-matched to the beige stucco and natural stone trim.",
            "psych": "Generates a diffuse acoustic floor that softens street murmur while safeguarding conversation privacy. Concealed hardware maintains the authentic illusion of an organic domestic garden.",
            "critique": "Sound concealment prevents visual clutter and acoustic fatigue; decibel levels should dynamically calibrate between serene afternoon tea and bustling weekend gatherings."
        },
        {
            "tag": "ZONE 03.2 // SEATING ERGONOMICS",
            "title": "Swing Seating: Playful Affordance vs. Posture",
            "subtitle": "High-Novelty Magnet vs. Long-Stay Ergonomic Limits",
            "img": "3.2_funny_looking_chairs__clean.jpg",
            "is_landscape": False,
            "obs": "Heavy structural steel box-frame suspending timber swing bench seats around an integrated stone table over rough-cut flagstone paving.",
            "psych": "High visual affordance: immediately invites touch, playful interaction, and photography. However, lack of lumbar support and a fixed swing radius discourage long-dwell dining or laptop work.",
            "critique": "Functions brilliantly as a social focal point and photo magnet; must be strategically balanced with ergonomically cushioned banquettes elsewhere in the floor plan."
        },
        {
            "tag": "ZONE 03.3 // LIGHTING & ATMOSPHERE",
            "title": "Dappled Daylight & Garden Dining",
            "subtitle": "Biophilic Lighting and Material Valence",
            "img": "3.3_lighting__clean.jpg",
            "is_landscape": False,
            "obs": "Ornate white wrought-iron garden chairs and filigree table beneath the leafy canopy, adjacent to an earthy terracotta raised planter box.",
            "psych": "Dappled sunlight filtering through natural leaves ('komorebi') triggers parasympathetic calming. The delicate white filigree stands out crisp and romantic against dark organic foliage.",
            "critique": "Hard unpadded iron creates physical pressure points after 25+ minutes; weather-resistant seat cushions would bridge the gap between visual romance and physical comfort."
        },
        {
            "tag": "ZONE 03.4 // SPATIAL FLEXIBILITY",
            "title": "Covered Event Sub-Stage & Living Wall",
            "subtitle": "Transitional Micro-Climates and Programmatic Adaptability",
            "img": "3.4_-_small_events_area__clean.jpg",
            "is_landscape": False,
            "obs": "Deep sheltered patio framed by white structural columns, geometric wire pendant lights, smooth concrete flooring, and an artificial vertical hedge wall.",
            "psych": "High psychological refuge: overhead roof provides intimacy and shade. The vertical green wall acts as an acoustic baffle and clean focal backdrop for private gatherings or performances.",
            "critique": "The transition from sunny courtyard to deep patio causes a steep drop in illumination; warm accent track lighting along ceiling beams is vital to avoid a sunken, shadowy feel."
        },
        {
            "tag": "ZONE 04 // INTERIOR ORDERING COUNTER",
            "title": "Pastry Showcase & Merchandising Saliency",
            "subtitle": "Visual Appetite Cues vs. Queueing Flow Ambiguity",
            "img": "4_-_pastery_ideas_appeal__clean.jpg",
            "is_landscape": False,
            "obs": "L-shaped marble-clad counter with illuminated glass vitrines displaying artisanal pastries, central brass 'N' monogram, and POS terminal against soft pastel walls.",
            "psych": "High visual saliency: brilliantly lit pastries act as irresistible appetite anchors. However, the counter provides no visual indicators for where the queue starts versus where orders are collected.",
            "critique": "Incorporate subtle architectural cues—such as a specific pendant light drop or floor inlay pattern—to guide intuitive ordering progression without tacky rope barriers."
        },
        {
            "tag": "ZONE 05.1 // TACTILE COMFORT & BOOTH",
            "title": "Velvet Booth & Tactile Aesthetics",
            "subtitle": "Acoustic Dampening and Photo-Ready Domestic Charm",
            "img": "5_-_aesthetic_inside_pt.1__clean.jpg",
            "is_landscape": False,
            "obs": "Dusty-rose vertical channel-tufted upholstered wall banquette, white turned-leg table, and a curated culinary typographical gallery wall.",
            "psych": "Velvet tufting absorbs acoustic reverberation and offers rich tactile warmth. High-back banquettes satisfy instinctual desires for territory and psychological refuge.",
            "critique": "Vertical upholstery successfully doubles as artistic accent and sound dampener, creating the most emotionally comforting, high-demand seating zone in the cafe."
        },
        {
            "tag": "ZONE 05.2 // THIRD-PLACE PSYCHOLOGY",
            "title": "Domestic Cues & 'Third Place' Sanctuary",
            "subtitle": "Fostering Belonging Through Residential Joinery",
            "img": "5_-_aesthetic_inside_pt.2__clean.jpg",
            "is_landscape": False,
            "obs": "White built-in cabinetry featuring an open wooden crate bookshelf with real books, a potted houseplant, and a framed chalkboard coffee quote.",
            "psych": "Directly embodies Ray Oldenburg's 'Third Place' theory: domestic architectural elements signal that leisurely dwelling, reading, and unhurried contemplation are welcomed.",
            "critique": "Residential styling humanizes commercial hospitality, building customer attachment and encouraging repeat visits over rapid transactional turnover."
        },
        {
            "tag": "ZONE 05.3 // SELF-SERVICE & AUTONOMY",
            "title": "Tableware Station & Customer Agency",
            "subtitle": "Perceived Affordance and Frictionless Self-Service",
            "img": "5.1_-_wanted_needs_arranged_for_ease__clean.jpg",
            "is_landscape": False,
            "obs": "Solid timber side table arranged with rustic wooden crates containing condiment packets, tall pepper grinders, stainless steel cutlery, and stacked plates.",
            "psych": "Immediate perceived affordance: necessities are categorized, exposed, and reachable. Empowers patrons with agency, avoiding awkward delays waiting for busy servers.",
            "critique": "Natural wood caddies reinforce handcrafted culinary values; keeping the station in plain sight from all indoor tables ensures frictionless customer autonomy."
        }
    ]

    for item in slides_data:
        slide = prs.slides.add_slide(blank_layout)
        set_slide_background(slide)

        img_file = os.path.join(clean_photos_dir, item["img"])
        is_landscape = item["is_landscape"]

        # Image placement
        if os.path.exists(img_file):
            with Image.open(img_file) as im:
                ow, oh = im.size

            if is_landscape:
                target_w = Inches(5.8)
                target_h = target_w * (oh / ow)
                img_top = Inches(1.6)
                img_left = Inches(0.8)
            else:
                target_h = Inches(6.1)
                target_w = target_h * (ow / oh)
                img_top = Inches(0.7)
                img_left = Inches(0.8)

            slide.shapes.add_picture(img_file, img_left, img_top, width=target_w, height=target_h)

            # Image frame / border accent
            border_rect = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, img_left, img_top, target_w, target_h)
            border_rect.fill.background()
            border_rect.line.color.rgb = COLOR_CARD_BORDER
            border_rect.line.width = Pt(1.5)

            content_left = img_left + target_w + Inches(0.45)
            content_width = Inches(13.333) - content_left - Inches(0.8)
        else:
            content_left = Inches(0.8)
            content_width = Inches(11.733)

        # Content Column
        content_top = Inches(0.7)
        content_height = Inches(6.1)

        # Header box
        header_tb = slide.shapes.add_textbox(content_left, content_top, content_width, Inches(1.2))
        htf = header_tb.text_frame
        htf.word_wrap = True

        hp0 = htf.paragraphs[0]
        hp0.text = item["tag"]
        hp0.font.size = Pt(10.5)
        hp0.font.bold = True
        hp0.font.color.rgb = COLOR_ACCENT
        hp0.font.name = "Arial"

        hp1 = htf.add_paragraph()
        hp1.text = item["title"]
        hp1.font.size = Pt(22)
        hp1.font.bold = True
        hp1.font.color.rgb = COLOR_TEXT_MAIN
        hp1.font.name = "Arial"

        hp2 = htf.add_paragraph()
        hp2.text = item["subtitle"]
        hp2.font.size = Pt(12)
        hp2.font.color.rgb = COLOR_TEXT_MUTED
        hp2.font.name = "Calibri"

        # Three Structured Analysis Cards
        blocks = [
            ("PHYSICAL & SPATIAL OBSERVATION", item["obs"]),
            ("ENVIRONMENTAL PSYCHOLOGY & WAYFINDING", item["psych"]),
            ("DESIGN CRITIQUE & RECOMMENDATION", item["critique"])
        ]

        card_y = content_top + Inches(1.4)
        card_h = Inches(1.42)
        gap = Inches(0.14)

        for b_title, b_text in blocks:
            b_card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, content_left, card_y, content_width, card_h)
            b_card.fill.solid()
            b_card.fill.fore_color.rgb = COLOR_CARD
            b_card.line.color.rgb = COLOR_CARD_BORDER
            b_card.line.width = Pt(1)

            tb_b = slide.shapes.add_textbox(content_left + Inches(0.2), card_y + Inches(0.12), content_width - Inches(0.4), card_h - Inches(0.24))
            btf = tb_b.text_frame
            btf.word_wrap = True

            bp0 = btf.paragraphs[0]
            bp0.text = b_title
            bp0.font.size = Pt(9.5)
            bp0.font.bold = True
            bp0.font.color.rgb = COLOR_ACCENT
            bp0.font.name = "Arial"
            bp0.space_after = Pt(4)

            bp1 = btf.add_paragraph()
            bp1.text = b_text
            bp1.font.size = Pt(11.5)
            bp1.font.color.rgb = COLOR_TEXT_MAIN
            bp1.font.name = "Calibri"

            card_y += card_h + gap

    # -------------------------------------------------------------
    # SLIDE 14: SPATIAL SYNTHESIS MATRIX
    # -------------------------------------------------------------
    s14 = prs.slides.add_slide(blank_layout)
    set_slide_background(s14)

    tb_h = s14.shapes.add_textbox(Inches(0.8), Inches(0.6), Inches(11.7), Inches(1.0))
    tf_h = tb_h.text_frame
    tf_h.word_wrap = True
    p = tf_h.paragraphs[0]
    p.text = "SPATIAL SYNTHESIS & BEHAVIORAL MATRIX"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = COLOR_ACCENT
    p = tf_h.add_paragraph()
    p.text = "Environmental Cues Across Spatial Zones at Nicoli"
    p.font.size = Pt(24)
    p.font.bold = True
    p.font.color.rgb = COLOR_TEXT_MAIN

    # Matrix Table
    rows, cols = 7, 5
    table_shape = s14.shapes.add_table(rows, cols, Inches(0.8), Inches(1.8), Inches(11.733), Inches(4.8))
    table = table_shape.table

    table.columns[0].width = Inches(2.2) # Zone
    table.columns[1].width = Inches(2.3) # Lighting
    table.columns[2].width = Inches(2.2) # Acoustic Level
    table.columns[3].width = Inches(1.8) # Avg Dwell
    table.columns[4].width = Inches(3.233) # Psychological Driver

    headers = ["Spatial Zone", "Lighting Environment", "Acoustic Level", "Dwell Time", "Dominant Psychological Driver"]
    for col_idx, h_text in enumerate(headers):
        cell = table.cell(0, col_idx)
        cell.fill.solid()
        cell.fill.fore_color.rgb = COLOR_CARD_BORDER
        p = cell.text_frame.paragraphs[0]
        p.text = h_text
        p.font.bold = True
        p.font.size = Pt(11)
        p.font.color.rgb = COLOR_TEXT_MAIN

    data_matrix = [
        ("Street Approach", "Full Daylight / Sun", "Urban Ambient / Low", "2 - 3 mins", "Anticipation & Exploration"),
        ("Entrance Threshold", "Deep Canopy Shade", "Sensory Airlock Filter", "1 - 2 mins", "Boundary Crossing / Discovery"),
        ("Courtyard Hub", "Dappled Foliage Shade", "Diffuse Background Music", "30 - 60 mins", "Prospect & Refuge Dynamic"),
        ("Covered Patio", "Sheltered Sub-ambient", "Baffled Green Wall", "20 - 45 mins", "Spatial Intimacy / Event Focus"),
        ("Pastry Counter", "High-Lumen Showcase", "Active Transactional", "3 - 5 mins", "Visual Saliency / Appetite"),
        ("Dining Banquette", "Warm Diffuse Lighting", "Upholstery Absorbed", "45 - 90 mins", "Tactile Warmth & Sanctuary")
    ]

    for row_idx, row_data in enumerate(data_matrix, start=1):
        for col_idx, text_val in enumerate(row_data):
            cell = table.cell(row_idx, col_idx)
            cell.fill.solid()
            cell.fill.fore_color.rgb = COLOR_CARD if row_idx % 2 == 1 else COLOR_BG
            p = cell.text_frame.paragraphs[0]
            p.text = text_val
            p.font.size = Pt(11)
            p.font.color.rgb = COLOR_TEXT_MAIN

    # -------------------------------------------------------------
    # SLIDE 15: STRATEGIC DESIGN RECOMMENDATIONS
    # -------------------------------------------------------------
    s15 = prs.slides.add_slide(blank_layout)
    set_slide_background(s15)

    tb_h = s15.shapes.add_textbox(Inches(0.8), Inches(0.6), Inches(11.7), Inches(1.0))
    tf_h = tb_h.text_frame
    tf_h.word_wrap = True
    p = tf_h.paragraphs[0]
    p.text = "ARCHITECTURAL TAKEAWAYS"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = COLOR_ACCENT
    p = tf_h.add_paragraph()
    p.text = "Four Design Principles for Experiential Hospitality Spaces"
    p.font.size = Pt(24)
    p.font.bold = True
    p.font.color.rgb = COLOR_TEXT_MAIN

    recs = [
        ("01", "Threshold Legibility", "Balance the intrigue of foliage and mystery with illuminated low-glare twilight signifiers to prevent first-timer friction."),
        ("02", "Ergonomic Diversity", "Pair high-novelty magnets (like swing seating) with supportive, upholstered banquettes to cater across dwell times."),
        ("03", "Intuitive Wayfinding", "Delineate ordering, queuing, and circulation zones through architectural shifts in flooring and lighting rather than clunky signage."),
        ("04", "Sensory 'Third Place'", "Seamlessly integrate residential cues, biophilia, acoustic baffling, and customer autonomy to transform a cafe into a living sanctuary.")
    ]

    r_w = Inches(5.6)
    r_h = Inches(2.2)

    positions = [
        (Inches(0.8), Inches(1.9)),
        (Inches(6.8), Inches(1.9)),
        (Inches(0.8), Inches(4.4)),
        (Inches(6.8), Inches(4.4))
    ]

    for (num, title, body), (rx, ry) in zip(recs, positions):
        r_card = s15.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, rx, ry, r_w, r_h)
        r_card.fill.solid()
        r_card.fill.fore_color.rgb = COLOR_CARD
        r_card.line.color.rgb = COLOR_CARD_BORDER
        r_card.line.width = Pt(1.5)

        tb_r = s15.shapes.add_textbox(rx + Inches(0.3), ry + Inches(0.2), r_w - Inches(0.6), r_h - Inches(0.4))
        rtf = tb_r.text_frame
        rtf.word_wrap = True

        p = rtf.paragraphs[0]
        p.text = num
        p.font.size = Pt(22)
        p.font.bold = True
        p.font.color.rgb = COLOR_ACCENT
        p.space_after = Pt(4)

        p = rtf.add_paragraph()
        p.text = title
        p.font.size = Pt(15)
        p.font.bold = True
        p.font.color.rgb = COLOR_TEXT_MAIN
        p.space_after = Pt(8)

        p = rtf.add_paragraph()
        p.text = body
        p.font.size = Pt(11.5)
        p.font.color.rgb = COLOR_TEXT_MUTED

    # Save output
    output_pptx = os.path.join(base_dir, "Nicoli_Pasticceria_Spatial_Analysis.pptx")
    prs.save(output_pptx)
    print(f"Presentation successfully created: {output_pptx}")
    print(f"Total Slides: {len(prs.slides)}")

if __name__ == "__main__":
    build_nicoli_deck()
