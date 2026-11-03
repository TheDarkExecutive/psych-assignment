import os
import io
import base64
import json
from PIL import Image

base_dir = r"c:\Users\Azrael\Downloads\Nicoli PPT"
clean_dir = os.path.join(base_dir, "clean_photos")
html_out_path = os.path.join(base_dir, "index.html")

def img_to_b64(path, max_dim=1400, quality=80):
    with Image.open(path) as img:
        img = img.convert("RGB")
        w, h = img.size
        m = max(w, h)
        if m > max_dim:
            scale = max_dim / m
            img = img.resize((int(w * scale), int(h * scale)), Image.Resampling.LANCZOS)
        buf = io.BytesIO()
        img.save(buf, format="JPEG", quality=quality, optimize=True)
        return "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode("utf-8")

def png_to_b64(path, max_dim=800):
    with Image.open(path) as img:
        w, h = img.size
        m = max(w, h)
        if m > max_dim:
            scale = max_dim / m
            img = img.resize((int(w * scale), int(h * scale)), Image.Resampling.LANCZOS)
        buf = io.BytesIO()
        img.save(buf, format="PNG", optimize=True)
        return "data:image/png;base64," + base64.b64encode(buf.getvalue()).decode("utf-8")

print("Encoding logo and villager sprite...")
logo_b64 = png_to_b64(os.path.join(base_dir, "nicoli_logo_clean.png"))
villager_b64 = png_to_b64(os.path.join(base_dir, "villager_rembg.png"))

scenes_meta = [
    {
        "id": "scene_1",
        "title": "Street Approach & Quiet Enclave",
        "zone": "Exterior / Approach",
        "clean_file": "1_-_Path_x_Find_clean.jpg",
        "ai_file": "1 - Path x Find - Game UI.jpg",
        "observation": "Chief! Notice how the residential approach has almost no commercial signage. Visitors must rely on GPS or subtle visual anchors to find Nicoli!",
        "chevrons": [
            {"target": "scene_2", "label": "Walk to Entrance Gate", "x": 50, "y": 74, "angle": 0, "scale": 1.05}
        ]
    },
    {
        "id": "scene_2",
        "title": "Entrance Threshold & Screening Foliage",
        "zone": "Exterior / Gate",
        "clean_file": "2_-_Entrance__x_parking__clean.jpg",
        "ai_file": "2 - Entrance x parking - Game UI.jpg",
        "observation": "Chief! The entrance is obscured by heavy foliage with no lighted signifiers, making wayfinding an intriguing puzzle for first-timers!",
        "chevrons": [
            {"target": "scene_3", "label": "Enter Courtyard", "x": 49, "y": 70, "angle": -8, "scale": 0.95},
            {"target": "scene_1", "label": "Back to Street", "x": 22, "y": 88, "angle": 180, "scale": 0.75}
        ]
    },
    {
        "id": "scene_3",
        "title": "Courtyard Hub & Natural Canopy",
        "zone": "Central Courtyard",
        "clean_file": "3_-_Overview_-_Lighting_x_Back_supporting_x_distanceless_chairs__clean.jpg",
        "ai_file": "3 - Overview - Game UI.jpg",
        "observation": "Chief! This open courtyard acts as our central hub! Dappled foliage naturally divides the space into acoustic, lounge, and dining zones leading into the bakery.",
        "chevrons": [
            {"target": "scene_4", "label": "Enter Pastry Shop", "x": 33, "y": 64, "angle": -25, "scale": 0.8},
            {"target": "scene_3_1", "label": "Inspect Acoustic Niche", "x": 44, "y": 55, "angle": 10, "scale": 0.7},
            {"target": "scene_3_2", "label": "Examine Swing Seating", "x": 82, "y": 68, "angle": 40, "scale": 0.8},
            {"target": "scene_3_3", "label": "Garden Dining Canopy", "x": 65, "y": 72, "angle": 25, "scale": 0.8},
            {"target": "scene_3_4", "label": "Small Events Patio", "x": 16, "y": 75, "angle": -60, "scale": 0.8},
            {"target": "scene_2", "label": "Exit to Front Gate", "x": 50, "y": 92, "angle": 180, "scale": 0.8}
        ]
    },
    {
        "id": "scene_3_1",
        "title": "Acoustic Ambiance & Spatial Sound",
        "zone": "Courtyard / Acoustic Zone",
        "clean_file": "3.1_-_faint_speaker__clean.jpg",
        "ai_file": "3.1 - faint speaker - Game UI.jpg",
        "observation": "Chief! The acoustic speaker is tucked discreetly into this exterior alcove—providing subtle auditory ambiance without overpowering dining conversations!",
        "chevrons": [
            {"target": "scene_3", "label": "Return to Courtyard Hub", "x": 50, "y": 88, "angle": 180, "scale": 0.9}
        ]
    },
    {
        "id": "scene_3_2",
        "title": "Swing Seating & Ergonomic Affordance",
        "zone": "Courtyard / Playful Seating",
        "clean_file": "3.2_funny_looking_chairs__clean.jpg",
        "ai_file": "3.2 funny looking chairs - Game UI.jpg",
        "observation": "Chief! These novelty swing seats create a playful, dynamic affordance, but the rigid suspended frame limits lumbar support for longer dining sessions!",
        "chevrons": [
            {"target": "scene_3_3", "label": "Over to Garden Canopy", "x": 78, "y": 78, "angle": 35, "scale": 0.85},
            {"target": "scene_3", "label": "Return to Courtyard Hub", "x": 32, "y": 88, "angle": 180, "scale": 0.9}
        ]
    },
    {
        "id": "scene_3_3",
        "title": "Frangipani Canopy & Intimate Dining",
        "zone": "Courtyard / Garden Dining",
        "clean_file": "3.3_lighting__clean.jpg",
        "ai_file": "3.3 lighting - Game UI.jpg",
        "observation": "Chief! Dappled sunlight through the canopy creates a romantic natural ambiance, but the hard iron seating trades long-stay comfort for garden aesthetics!",
        "chevrons": [
            {"target": "scene_3_2", "label": "Swing Seating Area", "x": 25, "y": 76, "angle": -55, "scale": 0.85},
            {"target": "scene_3", "label": "Return to Courtyard Hub", "x": 50, "y": 90, "angle": 180, "scale": 0.9}
        ]
    },
    {
        "id": "scene_3_4",
        "title": "Event Sub-Stage & Living Wall",
        "zone": "Courtyard / Event Patio",
        "clean_file": "3.4_-_small_events_area__clean.jpg",
        "ai_file": "3.4 - small events area - Game UI.jpg",
        "observation": "Chief! This covered patio creates an intimate sub-stage framed by living walls—great for small events, though lighting drops noticeably from the sunny courtyard!",
        "chevrons": [
            {"target": "scene_3", "label": "Return to Courtyard Hub", "x": 50, "y": 88, "angle": 180, "scale": 0.9}
        ]
    },
    {
        "id": "scene_4",
        "title": "Pastry Counter & Visual Appeal",
        "zone": "Interior / Order Counter",
        "clean_file": "4_-_pastery_ideas_appeal__clean.jpg",
        "ai_file": "4 - pastery ideas appeal - Game UI.png",
        "observation": "Chief! The indoor pastel-themed counter makes visual search easy and invites you in, but there is no clear sign for where to order or pick up!",
        "chevrons": [
            {"target": "scene_5", "label": "To Indoor Seating Nook", "x": 26, "y": 80, "angle": -60, "scale": 0.9},
            {"target": "scene_3", "label": "Back to Courtyard", "x": 74, "y": 86, "angle": 120, "scale": 0.85}
        ]
    },
    {
        "id": "scene_5",
        "title": "Velvet Booth & Tactile Aesthetics",
        "zone": "Interior / Dining Nook",
        "clean_file": "5_-_aesthetic_inside_pt.1__clean.jpg",
        "ai_file": "5 - aesthetic inside pt.1 - Game UI.jpg",
        "observation": "Chief! The plush pink channel tufting provides tactile warmth and acoustic comfort, while the gallery wall frames an inviting, photo-worthy aesthetic!",
        "chevrons": [
            {"target": "scene_5_1", "label": "To Self-Service Station", "x": 22, "y": 82, "angle": -55, "scale": 0.85},
            {"target": "scene_5_2", "label": "To Reading Shelf Nook", "x": 78, "y": 82, "angle": 55, "scale": 0.85},
            {"target": "scene_4", "label": "Back to Pastry Counter", "x": 50, "y": 92, "angle": 180, "scale": 0.85}
        ]
    },
    {
        "id": "scene_5_2",
        "title": "Third-Place Psychology & Domestic Cues",
        "zone": "Interior / Quiet Niche",
        "clean_file": "5_-_aesthetic_inside_pt.2__clean.jpg",
        "ai_file": "5 - aesthetic inside pt.2 - Game UI.jpg",
        "observation": "Chief! A curated shelf niche provides domestic cues, reinforcing a relaxed third-place dwelling psychology rather than a rushed cafe!",
        "chevrons": [
            {"target": "scene_5", "label": "Back to Dining Nook", "x": 26, "y": 88, "angle": -120, "scale": 0.85},
            {"target": "scene_5_1", "label": "To Self-Service Caddies", "x": 76, "y": 88, "angle": 60, "scale": 0.85}
        ]
    },
    {
        "id": "scene_5_1",
        "title": "Self-Service Station & User Affordance",
        "zone": "Interior / Service Station",
        "clean_file": "5.1_-_wanted_needs_arranged_for_ease__clean.jpg",
        "ai_file": "5.1 - wanted needs arranged for ease - Game UI.jpg",
        "observation": "Chief! Grouping cutlery, napkins, and plates in clear wooden caddies establishes immediate affordance and customer autonomy for self-service ease!",
        "chevrons": [
            {"target": "scene_5", "label": "Return to Dining Nook", "x": 50, "y": 88, "angle": 180, "scale": 0.9}
        ]
    }
]

scenes = []
for i, s in enumerate(scenes_meta):
    print(f"Encoding Scene {i+1}/{len(scenes_meta)}: {s['title']}...")
    clean_path = os.path.join(clean_dir, s["clean_file"])
    ai_path = os.path.join(base_dir, s["ai_file"])

    clean_b64 = img_to_b64(clean_path, max_dim=1300, quality=78) if os.path.exists(clean_path) else ""
    ai_b64 = img_to_b64(ai_path, max_dim=1300, quality=78) if os.path.exists(ai_path) else clean_b64

    scenes.append({
        "id": s["id"],
        "title": s["title"],
        "zone": s["zone"],
        "photo": clean_b64,
        "ai_photo": ai_b64,
        "observation": s["observation"],
        "chevrons": s["chevrons"]
    })

scenes_json = json.dumps(scenes)

html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Nicoli Pasticceria - Journey Mode Walkthrough</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@700;800;900&family=Montserrat:wght@500;600;700;800;900&display=swap" rel="stylesheet">
  <style>
    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      user-select: none;
      -webkit-user-select: none;
    }}

    body {{
      width: 100vw;
      height: 100vh;
      overflow: hidden;
      background-color: #0b0d11;
      font-family: 'Montserrat', sans-serif;
      color: #fff;
    }}

    #viewport {{
      position: relative;
      width: 100vw;
      height: 100vh;
      display: flex;
      align-items: center;
      justify-content: center;
      overflow: hidden;
    }}

    .ambient-backdrop {{
      position: absolute;
      inset: -20px;
      background-size: cover;
      background-position: center;
      filter: blur(48px) brightness(0.25) saturate(1.2);
      transform: scale(1.08);
      z-index: 1;
      transition: background-image 0.6s ease;
      pointer-events: none;
    }}

    .vignette-overlay {{
      position: absolute;
      inset: 0;
      background: radial-gradient(circle at center, transparent 40%, rgba(8, 10, 14, 0.8) 100%);
      z-index: 2;
      pointer-events: none;
    }}

    .stage-wrapper {{
      position: relative;
      z-index: 10;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      max-width: 94vw;
      max-height: 89vh;
      border-radius: 12px;
      box-shadow: 0 20px 50px rgba(0, 0, 0, 0.88), 0 0 0 1.5px rgba(255, 215, 0, 0.28);
      overflow: hidden;
      background: #000;
      transition: transform 0.45s cubic-bezier(0.2, 0.8, 0.2, 1), opacity 0.35s ease;
    }}

    .stage-wrapper.transition-forward {{
      transform: scale(1.04);
      opacity: 0.2;
    }}

    .stage-wrapper.transition-backward {{
      transform: scale(0.96);
      opacity: 0.2;
    }}

    .scene-image {{
      display: block;
      max-width: 94vw;
      max-height: 89vh;
      width: auto;
      height: auto;
      object-fit: contain;
      pointer-events: none;
    }}

    .chevron-layer {{
      position: absolute;
      inset: 0;
      width: 100%;
      height: 100%;
      pointer-events: none;
      z-index: 20;
    }}

    .streetview-chevron {{
      position: absolute;
      pointer-events: auto;
      cursor: pointer;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      transform-origin: center bottom;
      transition: transform 0.22s cubic-bezier(0.34, 1.56, 0.64, 1);
    }}

    .chevron-svg-wrap {{
      width: 82px;
      height: 52px;
      transform: perspective(300px) rotateX(62deg);
      transition: transform 0.22s ease, filter 0.22s ease;
      filter: drop-shadow(0 6px 12px rgba(0, 0, 0, 0.85));
    }}

    .streetview-chevron:hover .chevron-svg-wrap {{
      transform: perspective(300px) rotateX(48deg) scale(1.22);
      filter: drop-shadow(0 14px 22px rgba(255, 255, 255, 0.95)) drop-shadow(0 0 18px rgba(0, 180, 255, 0.9));
    }}

    .chevron-svg {{
      width: 100%;
      height: 100%;
      overflow: visible;
    }}

    .chevron-tooltip {{
      position: absolute;
      bottom: 100%;
      margin-bottom: 6px;
      background: rgba(14, 18, 24, 0.94);
      backdrop-filter: blur(8px);
      -webkit-backdrop-filter: blur(8px);
      border: 1.5px solid rgba(255, 215, 0, 0.7);
      color: #ffffff;
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 0.8px;
      text-transform: uppercase;
      padding: 5px 12px;
      border-radius: 20px;
      white-space: nowrap;
      pointer-events: none;
      opacity: 0;
      transform: translateY(6px);
      transition: opacity 0.2s ease, transform 0.2s ease;
      box-shadow: 0 6px 16px rgba(0,0,0,0.7);
    }}

    .streetview-chevron:hover .chevron-tooltip {{
      opacity: 1;
      transform: translateY(0);
    }}

    #top-bar {{
      position: absolute;
      top: 14px;
      left: 50%;
      transform: translateX(-50%);
      z-index: 50;
      display: flex;
      flex-direction: column;
      align-items: center;
      pointer-events: auto;
    }}

    .journey-badge {{
      display: flex;
      align-items: center;
      gap: 16px;
      background: linear-gradient(180deg, #44474f 0%, #252830 50%, #15161b 100%);
      border: 2.5px solid #b8860b;
      box-shadow: 0 0 0 1.5px #ffd700, 0 10px 28px rgba(0, 0, 0, 0.8), inset 0 2px 0 rgba(255, 255, 255, 0.25);
      border-radius: 14px;
      padding: 8px 24px;
      position: relative;
    }}

    .journey-badge::before, .journey-badge::after {{
      content: '';
      position: absolute;
      top: -4px;
      width: 8px;
      height: 8px;
      background: #ffd700;
      border-radius: 1.5px;
      box-shadow: 0 0 6px rgba(255,215,0,0.9);
    }}
    .journey-badge::before {{ left: -4px; }}
    .journey-badge::after {{ right: -4px; }}

    .badge-logo {{
      height: 44px;
      width: auto;
      object-fit: contain;
      filter: drop-shadow(0 3px 6px rgba(0,0,0,0.7));
    }}

    .badge-titles {{
      display: flex;
      flex-direction: column;
      align-items: center;
      line-height: 1.15;
    }}

    .journey-mode-title {{
      font-size: 21px;
      font-weight: 900;
      letter-spacing: 2px;
      text-transform: uppercase;
      color: #ffd84d;
      text-shadow: 0 2px 0 #8b5a00, 0 4px 8px rgba(0, 0, 0, 0.95);
      font-family: 'Cinzel', 'Montserrat', serif;
    }}

    .nicoli-title {{
      font-size: 13px;
      font-weight: 800;
      letter-spacing: 2.5px;
      text-transform: uppercase;
      color: #f0f0f0;
      text-shadow: 0 1px 3px rgba(0,0,0,0.85);
      margin-top: 2px;
    }}

    .top-left-hud {{
      position: absolute;
      top: 14px;
      left: 18px;
      z-index: 50;
      display: flex;
      align-items: center;
      gap: 12px;
    }}

    .coc-menu-btn {{
      background: linear-gradient(180deg, #3aa0e6 0%, #1c6ba4 50%, #10426b 100%);
      border: 2px solid #85c8f8;
      box-shadow: 0 0 0 1px #092c4b, 0 4px 12px rgba(0, 0, 0, 0.6), inset 0 2px 0 rgba(255, 255, 255, 0.4);
      color: #ffffff;
      padding: 8px 16px;
      border-radius: 10px;
      font-size: 13px;
      font-weight: 900;
      letter-spacing: 1px;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 8px;
      text-shadow: 0 2px 3px rgba(0, 0, 0, 0.8);
      transition: all 0.2s ease;
    }}

    .coc-menu-btn:hover {{
      transform: translateY(-2px);
      filter: brightness(1.15);
      box-shadow: 0 0 14px rgba(58, 160, 230, 0.8), 0 6px 16px rgba(0, 0, 0, 0.7);
    }}

    .menu-icon-svg {{
      width: 16px;
      height: 16px;
      fill: #ffffff;
      filter: drop-shadow(0 1px 2px rgba(0,0,0,0.5));
    }}

    .level-badge {{
      display: flex;
      align-items: center;
      gap: 6px;
      background: rgba(18, 22, 28, 0.88);
      border: 1.5px solid rgba(255, 215, 0, 0.5);
      padding: 6px 12px;
      border-radius: 20px;
      font-size: 11px;
      font-weight: 800;
      color: #ffd700;
      box-shadow: 0 4px 12px rgba(0, 0, 0, 0.5);
      backdrop-filter: blur(6px);
    }}

    .top-right-hud {{
      position: absolute;
      top: 14px;
      right: 18px;
      z-index: 50;
      display: flex;
      flex-direction: column;
      gap: 6px;
      align-items: flex-end;
    }}

    .coc-resource-row {{
      display: flex;
      align-items: center;
      gap: 6px;
    }}

    .coc-meter {{
      position: relative;
      width: 170px;
      height: 22px;
      background: linear-gradient(180deg, #1e2025 0%, #101114 100%);
      border: 1.5px solid #4a4d55;
      border-radius: 5px;
      overflow: hidden;
      box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.9), 0 3px 6px rgba(0, 0, 0, 0.6);
      display: flex;
      align-items: center;
      justify-content: flex-end;
      padding-right: 8px;
    }}

    .meter-fill {{
      position: absolute;
      left: 0;
      top: 0;
      bottom: 0;
      border-radius: 3px;
      transition: width 0.4s ease;
    }}

    .meter-fill.gold {{
      background: linear-gradient(180deg, #ffe066 0%, #f5a623 50%, #b86e00 100%);
      box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.5);
    }}

    .meter-fill.elixir {{
      background: linear-gradient(180deg, #f070f0 0%, #c41ec4 50%, #7b0d7b 100%);
      box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.5);
    }}

    .meter-val {{
      position: relative;
      z-index: 2;
      font-size: 11px;
      font-weight: 900;
      letter-spacing: 0.5px;
      color: #ffffff;
      text-shadow: 0 1px 3px #000, 0 2px 0 #000;
      font-family: 'Montserrat', sans-serif;
    }}

    .res-icon-circle {{
      width: 28px;
      height: 28px;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      position: relative;
      z-index: 3;
      margin-left: -10px;
      box-shadow: 0 3px 8px rgba(0, 0, 0, 0.7);
    }}

    .res-icon-circle.gold {{
      background: radial-gradient(circle at 35% 35%, #fff275 0%, #d49504 70%, #7c4c02 100%);
      border: 1.5px solid #ffea79;
    }}

    .res-icon-circle.elixir {{
      background: radial-gradient(circle at 35% 35%, #ff94ff 0%, #a81ba8 70%, #5e0d5e 100%);
      border: 1.5px solid #ffaeff;
    }}

    .res-icon-circle.gem {{
      background: radial-gradient(circle at 35% 35%, #7bf67b 0%, #159b15 70%, #084c08 100%);
      border: 1.5px solid #a3ffa3;
    }}

    .coc-plus-btn {{
      width: 22px;
      height: 22px;
      background: linear-gradient(180deg, #6fd339 0%, #439719 50%, #26600a 100%);
      border: 1.5px solid #a4f07a;
      box-shadow: 0 2px 4px rgba(0,0,0,0.5), inset 0 1px 0 rgba(255,255,255,0.4);
      border-radius: 5px;
      color: #fff;
      font-weight: 900;
      font-size: 13px;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      text-shadow: 0 1px 2px rgba(0,0,0,0.8);
      transition: all 0.15s ease;
    }}

    .coc-plus-btn:hover {{
      filter: brightness(1.15);
      transform: scale(1.08);
    }}

    #villager-widget {{
      position: absolute;
      bottom: 14px;
      left: 18px;
      z-index: 60;
      display: flex;
      align-items: flex-end;
      gap: 14px;
      pointer-events: auto;
      max-width: 520px;
      transition: transform 0.3s cubic-bezier(0.34, 1.56, 0.64, 1), opacity 0.3s ease;
    }}

    #villager-widget.minimized {{
      transform: translateY(140px);
      opacity: 0;
      pointer-events: none;
    }}

    .villager-avatar-wrap {{
      width: 125px;
      height: 165px;
      flex-shrink: 0;
      position: relative;
      cursor: pointer;
      filter: drop-shadow(0 10px 18px rgba(0, 0, 0, 0.95)) drop-shadow(0 0 10px rgba(255, 215, 0, 0.3));
      transition: transform 0.22s ease, filter 0.22s ease;
    }}

    .villager-avatar-wrap:hover {{
      transform: scale(1.06) translateY(-4px);
      filter: drop-shadow(0 14px 24px rgba(0, 0, 0, 0.95)) drop-shadow(0 0 18px rgba(255, 215, 0, 0.6));
    }}

    .villager-sprite {{
      width: 100%;
      height: 100%;
      object-fit: contain;
      object-position: bottom;
    }}

    .dialogue-card {{
      background: linear-gradient(180deg, #3d4047 0%, #25272e 100%);
      border: 2.5px solid #8e6820;
      box-shadow: 0 0 0 1.5px #deb841, 0 12px 32px rgba(0, 0, 0, 0.85);
      border-radius: 16px;
      padding: 14px 18px;
      position: relative;
      color: #f7f7f7;
      min-width: 280px;
      max-width: 380px;
    }}

    .dialogue-card::before {{
      content: '';
      position: absolute;
      left: -11px;
      bottom: 28px;
      border-top: 10px solid transparent;
      border-bottom: 10px solid transparent;
      border-right: 11px solid #deb841;
    }}
    .dialogue-card::after {{
      content: '';
      position: absolute;
      left: -8px;
      bottom: 28px;
      border-top: 10px solid transparent;
      border-bottom: 10px solid transparent;
      border-right: 10px solid #282a31;
    }}

    .dialogue-header {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 8px;
      gap: 10px;
    }}

    .villager-nametag {{
      background: linear-gradient(180deg, #ffd700 0%, #b8860b 100%);
      color: #2b1d03;
      font-size: 11px;
      font-weight: 900;
      letter-spacing: 1.5px;
      padding: 3px 10px;
      border-radius: 6px;
      border: 1px solid #fff;
      box-shadow: 0 2px 5px rgba(0,0,0,0.55);
      text-transform: uppercase;
      font-family: 'Montserrat', sans-serif;
    }}

    .dialogue-actions {{
      display: flex;
      align-items: center;
      gap: 8px;
    }}

    .dialogue-ai-btn {{
      background: rgba(255, 215, 0, 0.15);
      border: 1px solid #ffd700;
      color: #ffd700;
      font-size: 10.5px;
      font-weight: 800;
      letter-spacing: 0.5px;
      padding: 3px 8px;
      border-radius: 6px;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 4px;
      transition: all 0.2s ease;
    }}

    .dialogue-ai-btn:hover {{
      background: #ffd700;
      color: #1a1a1a;
      box-shadow: 0 0 10px rgba(255, 215, 0, 0.6);
    }}

    .dialogue-ai-btn.active {{
      background: #ffd700;
      color: #1a1a1a;
      box-shadow: 0 0 10px rgba(255, 215, 0, 0.7);
    }}

    .dialogue-close-btn {{
      background: none;
      border: none;
      color: #9ea3ae;
      font-size: 14px;
      cursor: pointer;
      padding: 2px 4px;
      transition: color 0.15s ease;
    }}
    .dialogue-close-btn:hover {{
      color: #ffd700;
    }}

    .dialogue-text {{
      font-size: 13.5px;
      line-height: 1.55;
      font-weight: 500;
      color: #f0f3f9;
    }}

    #guide-reopen-btn {{
      position: absolute;
      bottom: 18px;
      left: 18px;
      z-index: 59;
      background: rgba(26, 29, 36, 0.94);
      border: 2px solid #ffd700;
      border-radius: 50px;
      padding: 6px 14px 6px 8px;
      display: flex;
      align-items: center;
      gap: 10px;
      cursor: pointer;
      box-shadow: 0 8px 20px rgba(0,0,0,0.7);
      transition: all 0.2s ease;
      opacity: 0;
      pointer-events: none;
      transform: translateY(20px);
    }}

    #guide-reopen-btn.visible {{
      opacity: 1;
      pointer-events: auto;
      transform: translateY(0);
    }}

    #guide-reopen-btn:hover {{
      background: rgba(45, 50, 62, 0.98);
      box-shadow: 0 0 14px rgba(255, 215, 0, 0.7);
      transform: translateY(-2px);
    }}

    .guide-mini-avatar {{
      width: 32px;
      height: 32px;
      border-radius: 50%;
      object-fit: cover;
      object-position: top;
      border: 1.5px solid #ffd700;
      background: #333;
    }}

    .guide-btn-label {{
      font-size: 11.5px;
      font-weight: 800;
      color: #ffd700;
      text-transform: uppercase;
      letter-spacing: 0.8px;
    }}

    #bottom-nav {{
      position: absolute;
      bottom: 18px;
      right: 18px;
      z-index: 50;
      display: flex;
      align-items: center;
      gap: 12px;
      background: rgba(18, 20, 26, 0.88);
      border: 1.5px solid rgba(255, 215, 0, 0.45);
      padding: 8px 16px;
      border-radius: 30px;
      backdrop-filter: blur(8px);
      box-shadow: 0 8px 24px rgba(0, 0, 0, 0.6);
    }}

    .nav-arrow-btn {{
      background: rgba(255, 255, 255, 0.1);
      border: 1px solid rgba(255, 255, 255, 0.25);
      color: #fff;
      width: 32px;
      height: 32px;
      border-radius: 50%;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 14px;
      transition: all 0.2s ease;
    }}

    .nav-arrow-btn:hover:not(:disabled) {{
      background: #ffd700;
      color: #111;
      border-color: #ffd700;
      transform: scale(1.1);
    }}

    .nav-arrow-btn:disabled {{
      opacity: 0.3;
      cursor: not-allowed;
    }}

    .scene-dots {{
      display: flex;
      align-items: center;
      gap: 6px;
    }}

    .scene-dot {{
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background: rgba(255, 255, 255, 0.3);
      cursor: pointer;
      transition: all 0.2s ease;
    }}

    .scene-dot.active {{
      width: 20px;
      border-radius: 10px;
      background: #ffd700;
      box-shadow: 0 0 8px rgba(255, 215, 0, 0.8);
    }}

    #menu-modal {{
      position: fixed;
      inset: 0;
      background: rgba(0, 0, 0, 0.86);
      backdrop-filter: blur(12px);
      z-index: 100;
      display: flex;
      align-items: center;
      justify-content: center;
      opacity: 0;
      pointer-events: none;
      transition: opacity 0.3s ease;
    }}

    #menu-modal.open {{
      opacity: 1;
      pointer-events: auto;
    }}

    .menu-card {{
      background: #181b22;
      border: 2.5px solid #deb841;
      border-radius: 18px;
      padding: 24px;
      width: 92%;
      max-width: 880px;
      max-height: 86vh;
      overflow-y: auto;
      box-shadow: 0 20px 50px rgba(0,0,0,0.85);
    }}

    .menu-header {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      border-bottom: 1.5px solid rgba(255, 215, 0, 0.35);
      padding-bottom: 14px;
      margin-bottom: 18px;
    }}

    .menu-title-group {{
      display: flex;
      align-items: center;
      gap: 12px;
    }}

    .menu-title {{
      font-size: 20px;
      font-weight: 900;
      color: #ffd700;
      letter-spacing: 1px;
    }}

    .menu-quick-options {{
      display: flex;
      gap: 10px;
      margin-bottom: 18px;
      flex-wrap: wrap;
    }}

    .menu-opt-btn {{
      background: #252934;
      border: 1.5px solid rgba(255, 215, 0, 0.4);
      color: #f0f0f0;
      padding: 8px 16px;
      border-radius: 8px;
      font-size: 12px;
      font-weight: 700;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 6px;
      transition: all 0.2s ease;
    }}

    .menu-opt-btn:hover {{
      background: #343949;
      border-color: #ffd700;
      color: #ffd700;
    }}

    .menu-opt-btn.active {{
      background: #ffd700;
      color: #111;
      border-color: #fff;
    }}

    .menu-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(210px, 1fr));
      gap: 14px;
    }}

    .menu-node {{
      background: #242732;
      border: 1.5px solid rgba(255, 255, 255, 0.12);
      border-radius: 10px;
      padding: 10px;
      cursor: pointer;
      transition: all 0.2s ease;
      display: flex;
      flex-direction: column;
      gap: 6px;
    }}

    .menu-node:hover {{
      border-color: #ffd700;
      transform: translateY(-2px);
      background: #2e3342;
    }}

    .menu-node.active-node {{
      border: 2px solid #ffd700;
      background: #3a4052;
      box-shadow: 0 0 12px rgba(255, 215, 0, 0.4);
    }}

    .menu-node img {{
      width: 100%;
      height: 105px;
      object-fit: cover;
      border-radius: 6px;
    }}

    .menu-node-title {{
      font-size: 12px;
      font-weight: 700;
      color: #fff;
    }}

    .menu-node-zone {{
      font-size: 10px;
      color: #ffd700;
      font-weight: 700;
      text-transform: uppercase;
    }}
  </style>
</head>
<body>

  <div id="viewport">
    
    <div class="ambient-backdrop" id="ambient-backdrop"></div>
    <div class="vignette-overlay"></div>

    <!-- TOP-LEFT: Clash of Clans Menu Button + Step Indicator -->
    <div class="top-left-hud">
      <button class="coc-menu-btn" id="open-menu-btn" title="Open Journey Menu">
        <svg class="menu-icon-svg" viewBox="0 0 24 24">
          <path d="M3 6h18v2.5H3V6zm0 5.75h18v2.5H3v-2.5zm0 5.75h18V20H3v-2.5z"/>
        </svg>
        <span>MENU</span>
      </button>

      <div class="level-badge" title="Current Step in Walkthrough">
        <span>⭐</span>
        <span id="step-indicator">1 / 11</span>
      </div>
    </div>

    <!-- TOP-CENTER: Enriched Journey Mode & Nicoli Header -->
    <div id="top-bar">
      <div class="journey-badge">
        <img src="{logo_b64}" alt="Nicoli Logo" class="badge-logo" />
        <div class="badge-titles">
          <span class="journey-mode-title">JOURNEY MODE</span>
          <span class="nicoli-title">NICOLI PASTICCERIA</span>
        </div>
      </div>
    </div>

    <!-- TOP-RIGHT: Authentic Clash of Clans Gold, Elixir & Gems Bars -->
    <div class="top-right-hud">
      <div class="coc-resource-row">
        <div class="coc-meter">
          <div class="meter-fill gold" style="width: 82%;"></div>
          <span class="meter-val">2,768,658</span>
        </div>
        <div class="res-icon-circle gold" title="Gold">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="#663c00">
            <ellipse cx="12" cy="7" rx="8" ry="4" fill="#ffe066" stroke="#b86e00" stroke-width="1.5"/>
            <path d="M4 7v6c0 2.2 3.6 4 8 4s8-1.8 8-4V7" fill="#f5a623" stroke="#b86e00" stroke-width="1.5"/>
            <path d="M4 11v6c0 2.2 3.6 4 8 4s8-1.8 8-4v-6" fill="#f5a623" stroke="#b86e00" stroke-width="1.5"/>
          </svg>
        </div>
        <button class="coc-plus-btn" title="Treasury">+</button>
      </div>

      <div class="coc-resource-row">
        <div class="coc-meter">
          <div class="meter-fill elixir" style="width: 68%;"></div>
          <span class="meter-val">1,388,500</span>
        </div>
        <div class="res-icon-circle elixir" title="Elixir">
          <svg width="18" height="18" viewBox="0 0 24 24">
            <path d="M12 2 C8 7 5 12 5 16 C5 20 8 23 12 23 C16 23 19 20 19 16 C19 12 16 7 12 2 Z" fill="#ff70ff" stroke="#7b0d7b" stroke-width="1.5"/>
            <circle cx="10" cy="14" r="2.5" fill="#ffffff" opacity="0.75"/>
          </svg>
        </div>
        <button class="coc-plus-btn" title="Elixir Storage">+</button>
      </div>

      <div class="coc-resource-row">
        <div class="coc-meter" style="width: 120px;">
          <span class="meter-val" style="color: #6fe86f;">1,500</span>
        </div>
        <div class="res-icon-circle gem" title="Gems">
          <svg width="18" height="18" viewBox="0 0 24 24">
            <polygon points="12,2 21,9 18,22 6,22 3,9" fill="#5fe35f" stroke="#084c08" stroke-width="1.5"/>
            <polygon points="12,2 17,9 12,18 7,9" fill="#a4ffa4" opacity="0.8"/>
          </svg>
        </div>
        <button class="coc-plus-btn" title="Get Gems">+</button>
      </div>
    </div>

    <!-- Centered Stage Wrapper (100% visible, original aspect ratio) -->
    <div class="stage-wrapper" id="stage-wrapper">
      <img src="" alt="Nicoli Scene" class="scene-image" id="scene-img" />
      <div class="chevron-layer" id="chevron-layer"></div>
    </div>

    <!-- BOTTOM-LEFT: Bigger Villager Guide with AI View Toggle -->
    <div id="villager-widget">
      <div class="villager-avatar-wrap" id="villager-avatar" title="Villager Guide">
        <img src="{villager_b64}" alt="Villager Guide" class="villager-sprite" />
      </div>
      <div class="dialogue-card">
        <div class="dialogue-header">
          <span class="villager-nametag">VILLAGER</span>
          <div class="dialogue-actions">
            <button class="dialogue-ai-btn" id="ai-toggle-btn" title="Switch between clean photo and AI Concept">
              🎨 <span id="ai-btn-text">AI Concept</span>
            </button>
            <button class="dialogue-close-btn" id="close-guide-btn" title="Minimize Guide">✕</button>
          </div>
        </div>
        <p class="dialogue-text" id="dialogue-content">Loading observation...</p>
      </div>
    </div>

    <div id="guide-reopen-btn">
      <img src="{villager_b64}" alt="Avatar" class="guide-mini-avatar" />
      <span class="guide-btn-label">Tour Guide</span>
    </div>

    <!-- BOTTOM-RIGHT: Navigation Controls -->
    <div id="bottom-nav">
      <button class="nav-arrow-btn" id="prev-btn" title="Previous Slide (←)">◀</button>
      <div class="scene-dots" id="scene-dots"></div>
      <button class="nav-arrow-btn" id="next-btn" title="Next Slide (→)">▶</button>
    </div>

  </div>

  <!-- MENU DRAWER MODAL -->
  <div id="menu-modal">
    <div class="menu-card">
      <div class="menu-header">
        <div class="menu-title-group">
          <span class="menu-title">JOURNEY MENU & CONTROLS</span>
        </div>
        <button class="menu-opt-btn" id="close-menu-btn">✕ Close</button>
      </div>

      <div class="menu-quick-options">
        <button class="menu-opt-btn" id="menu-ai-toggle">
          🎨 <span id="menu-ai-text">Switch to AI Concept View</span>
        </button>
        <button class="menu-opt-btn" id="fs-btn">
          ⛶ Toggle Fullscreen
        </button>
      </div>

      <div style="font-size: 13px; font-weight: 800; color: #ffd700; margin-bottom: 12px; letter-spacing: 1px;">
        SELECT ANY SCENE NODE:
      </div>
      <div class="menu-grid" id="menu-grid"></div>
    </div>
  </div>

  <script>
    const scenes = {scenes_json};

    let currentIdx = 0;
    let showAiConcept = false;

    // Web Audio Synthesizer
    let audioCtx = null;
    function playStepSound() {{
      try {{
        if (!audioCtx) audioCtx = new (window.AudioContext || window.webkitAudioContext)();
        if (audioCtx.state === 'suspended') audioCtx.resume();
        const osc = audioCtx.createOscillator();
        const gain = audioCtx.createGain();
        osc.type = 'sine';
        osc.frequency.setValueAtTime(440, audioCtx.currentTime);
        osc.frequency.exponentialRampToValueAtTime(880, audioCtx.currentTime + 0.08);
        gain.gain.setValueAtTime(0.12, audioCtx.currentTime);
        gain.gain.exponentialRampToValueAtTime(0.001, audioCtx.currentTime + 0.1);
        osc.connect(gain);
        gain.connect(audioCtx.destination);
        osc.start();
        osc.stop(audioCtx.currentTime + 0.1);
      }} catch (err) {{}}
    }}

    const sceneImg = document.getElementById('scene-img');
    const stageWrapper = document.getElementById('stage-wrapper');
    const ambientBackdrop = document.getElementById('ambient-backdrop');
    const chevronLayer = document.getElementById('chevron-layer');
    const dialogueContent = document.getElementById('dialogue-content');
    const stepIndicator = document.getElementById('step-indicator');
    const prevBtn = document.getElementById('prev-btn');
    const nextBtn = document.getElementById('next-btn');
    const sceneDotsContainer = document.getElementById('scene-dots');
    const villagerWidget = document.getElementById('villager-widget');
    const guideReopenBtn = document.getElementById('guide-reopen-btn');
    const closeGuideBtn = document.getElementById('close-guide-btn');
    const aiToggleBtn = document.getElementById('ai-toggle-btn');
    const aiBtnText = document.getElementById('ai-btn-text');
    const menuAiToggle = document.getElementById('menu-ai-toggle');
    const menuAiText = document.getElementById('menu-ai-text');
    const openMenuBtn = document.getElementById('open-menu-btn');
    const closeMenuBtn = document.getElementById('close-menu-btn');
    const menuModal = document.getElementById('menu-modal');
    const menuGrid = document.getElementById('menu-grid');
    const fsBtn = document.getElementById('fs-btn');

    scenes.forEach((s, i) => {{
      const dot = document.createElement('div');
      dot.className = `scene-dot ${{i === 0 ? 'active' : ''}}`;
      dot.title = s.title;
      dot.addEventListener('click', () => navigateTo(i, 'forward'));
      sceneDotsContainer.appendChild(dot);
    }});

    function buildMenuGrid() {{
      menuGrid.innerHTML = '';
      scenes.forEach((s, i) => {{
        const node = document.createElement('div');
        node.className = `menu-node ${{i === currentIdx ? 'active-node' : ''}}`;
        node.innerHTML = `
          <img src="${{s.photo}}" alt="${{s.title}}" />
          <span class="menu-node-zone">${{s.zone}}</span>
          <span class="menu-node-title">${{s.title}}</span>
        `;
        node.addEventListener('click', () => {{
          menuModal.classList.remove('open');
          navigateTo(i, i >= currentIdx ? 'forward' : 'backward');
        }});
        menuGrid.appendChild(node);
      }});
    }}

    function renderScene(idx, direction = 'forward') {{
      const scene = scenes[idx];
      const targetSrc = showAiConcept ? scene.ai_photo : scene.photo;

      stepIndicator.textContent = `${{idx + 1}} / ${{scenes.length}}`;
      dialogueContent.textContent = scene.observation;

      document.querySelectorAll('.scene-dot').forEach((dot, i) => {{
        dot.classList.toggle('active', i === idx);
      }});

      prevBtn.disabled = idx === 0;
      nextBtn.disabled = idx === scenes.length - 1;

      aiToggleBtn.classList.toggle('active', showAiConcept);
      aiBtnText.textContent = showAiConcept ? 'Clean Photo' : 'AI Concept';
      menuAiToggle.classList.toggle('active', showAiConcept);
      menuAiText.textContent = showAiConcept ? 'Switch to Clean Photo' : 'Switch to AI Concept View';

      stageWrapper.classList.add(direction === 'forward' ? 'transition-forward' : 'transition-backward');
      
      setTimeout(() => {{
        sceneImg.src = targetSrc;
        ambientBackdrop.style.backgroundImage = `url('${{scene.photo}}')`;
        stageWrapper.classList.remove('transition-forward', 'transition-backward');
      }}, 120);

      renderChevrons(scene);
    }}

    function renderChevrons(scene) {{
      chevronLayer.innerHTML = '';
      if (showAiConcept) return;

      scene.chevrons.forEach(c => {{
        const chevron = document.createElement('div');
        chevron.className = 'streetview-chevron';
        chevron.style.left = `${{c.x}}%`;
        chevron.style.top = `${{c.y}}%`;
        chevron.style.transform = `translate(-50%, -50%) rotate(${{c.angle}}deg) scale(${{c.scale || 1}})`;

        chevron.innerHTML = `
          <div class="chevron-tooltip" style="transform: rotate(${{-c.angle}}deg);">${{c.label}}</div>
          <div class="chevron-svg-wrap">
            <svg class="chevron-svg" viewBox="0 0 100 64" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M10 52 L50 14 L90 52 L80 58 L50 26 L20 58 Z" fill="rgba(0, 0, 0, 0.45)" />
              <path d="M12 48 L50 10 L88 48 L78 54 L50 22 L22 54 Z" fill="#ffffff" stroke="rgba(255,255,255,0.95)" stroke-width="2" stroke-linejoin="round" />
            </svg>
          </div>
        `;

        chevron.addEventListener('click', (e) => {{
          e.stopPropagation();
          playStepSound();
          const targetIdx = scenes.findIndex(s => s.id === c.target);
          if (targetIdx !== -1) {{
            navigateTo(targetIdx, targetIdx >= currentIdx ? 'forward' : 'backward');
          }}
        }});

        chevronLayer.appendChild(chevron);
      }});
    }}

    function navigateTo(idx, direction = 'forward') {{
      if (idx < 0 || idx >= scenes.length) return;
      currentIdx = idx;
      playStepSound();
      renderScene(currentIdx, direction);
    }}

    prevBtn.addEventListener('click', () => navigateTo(currentIdx - 1, 'backward'));
    nextBtn.addEventListener('click', () => navigateTo(currentIdx + 1, 'forward'));

    window.addEventListener('keydown', (e) => {{
      if (e.key === 'ArrowRight' || e.key === ' ') {{
        e.preventDefault();
        navigateTo(currentIdx + 1, 'forward');
      }} else if (e.key === 'ArrowLeft') {{
        e.preventDefault();
        navigateTo(currentIdx - 1, 'backward');
      }}
    }});

    closeGuideBtn.addEventListener('click', () => {{
      villagerWidget.classList.add('minimized');
      guideReopenBtn.classList.add('visible');
    }});

    guideReopenBtn.addEventListener('click', () => {{
      villagerWidget.classList.remove('minimized');
      guideReopenBtn.classList.remove('visible');
    }});

    function toggleAiConcept() {{
      showAiConcept = !showAiConcept;
      playStepSound();
      renderScene(currentIdx, 'forward');
    }}

    aiToggleBtn.addEventListener('click', toggleAiConcept);
    menuAiToggle.addEventListener('click', () => {{
      toggleAiConcept();
      menuModal.classList.remove('open');
    }});

    openMenuBtn.addEventListener('click', () => {{
      playStepSound();
      buildMenuGrid();
      menuModal.classList.add('open');
    }});

    closeMenuBtn.addEventListener('click', () => menuModal.classList.remove('open'));
    menuModal.addEventListener('click', (e) => {{
      if (e.target === menuModal) menuModal.classList.remove('open');
    }});

    fsBtn.addEventListener('click', () => {{
      if (!document.fullscreenElement) {{
        document.documentElement.requestFullscreen().catch(() => {{}});
      }} else {{
        document.exitFullscreen().catch(() => {{}});
      }}
    }});

    renderScene(0, 'forward');
  </script>
</body>
</html>"""

with open(html_out_path, "w", encoding="utf-8") as f:
    f.write(html_template)

print(f"Successfully generated standalone self-contained index.html!")
print(f"File size: {os.path.getsize(html_out_path) / (1024 * 1024):.2f} MB")
